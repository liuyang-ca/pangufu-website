import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import make_citizenship_pages as ca  # noqa: E402
import make_us_citizenship_pages as gen  # noqa: E402

REPO = gen.ROOT
SITE = gen.SITE
CFG = gen.LANGS["en"]


def q(qid, unit, prompt, answers, required=1, **extra):
    return {"id": qid, "unit": unit, "prompt": prompt, "required": required,
            "answers": [{"text": a, "aliases": []} for a in answers],
            "choices": ["w1", "w2", "w3"], "explanation": f"Because {qid} <i>says</i>.", **extra}


QUESTIONS = [
    q("q001", "gov-principles", "Form of government?", ["Republic"]),
    q("q002", "gov-system", "Tricky </script><script>alert(1)</script>?", ["A & B", "C"]),
    q("q003", "gov-system", "Your senator?", ["Local name"], local="senator"),
    q("q004", "gov-system", "The President?", ["Current name"], current="president"),
    q("q005", "gov-rights", "Three rights?", ["Speech", "Press", "Worship", "Assembly"], required=3),
    q("q006", "history-colonial", "Who wrote it?", ["Jefferson"]),
    q("q007", "history-recent", "Which war?", ["Korea", "Vietnam"]),
    q("q008", "symbols", "Capital?", ["Washington, D.C."]),
    q("q009", "holidays", "Memorial Day?", ["Honors the fallen"]),
]
SAMPLES = ["q001", "q002", "q005", "q006", "q008"]
CFG_FIXTURE = {**CFG, "samples": SAMPLES}
HAS_NODE = shutil.which("node") is not None

def head_tag(page, pattern):
    return re.search(pattern, page).group(1)


def check_share_tags(test, page, url):
    """og:title/description/url must equal the page's title, meta description and canonical; breadcrumbs end here."""
    test.assertEqual(head_tag(page, r'og:title" content="([^"]*)"'), head_tag(page, r"<title>(.*?)</title>"))
    test.assertEqual(head_tag(page, r'og:description" content="([^"]*)"'), head_tag(page, r'name="description" content="([^"]*)"'))
    test.assertEqual(head_tag(page, r'og:url" content="([^"]*)"'), url)
    test.assertEqual(head_tag(page, r'rel="canonical" href="([^"]*)"'), url)
    test.assertEqual(page.count("twitter:card"), 1)
    crumbs = json.loads(head_tag(page, r'ld\+json">(.*?)</script>'))["itemListElement"]
    test.assertEqual([c["position"] for c in crumbs], [1, 2, 3])
    test.assertEqual(crumbs[-1]["item"], url)


class GeneratorTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp)
        self.root = self.tmp / "site"
        (self.root / CFG["out"]).mkdir(parents=True)
        shutil.copy(REPO / CFG["out"] / "index.html", self.root / CFG["out"] / "index.html")
        shutil.copy(REPO / "sitemap.xml", self.root / "sitemap.xml")
        self.qpath = self.tmp / "q.json"
        self.qpath.write_text(json.dumps(QUESTIONS), encoding="utf-8")

    def run_gen(self):
        urls = gen.generate(CFG_FIXTURE, self.root, self.qpath)
        ca.update_sitemap(self.root / "sitemap.xml", urls)
        return urls

    def read(self, *parts):
        return self.root.joinpath(CFG["out"], *parts).read_text(encoding="utf-8")

    def quiz_data(self):
        data = self.read("index.html").split('id="question-data">')[1].split("</script>")[0]
        return json.loads(data)

    def test_local_and_current_questions_never_appear(self):
        self.run_gen()
        text = self.read("index.html") + "".join(self.read(s, "index.html") for s in ("government", "history", "symbols-holidays"))
        for leaked in ("Local name", "Current name", "Your senator", "q003", "q004"):
            self.assertNotIn(leaked, text)
        self.assertEqual([x["id"] for x in self.quiz_data()],
                         ["q001", "q002", "q005", "q006", "q007", "q008", "q009"])

    def test_each_section_page_holds_exactly_its_units(self):
        self.run_gen()
        for slug, ids in (("government", ["q001", "q002", "q005"]),
                          ("history", ["q006", "q007"]), ("symbols-holidays", ["q008", "q009"])):
            page = self.read(slug, "index.html")
            for n in range(1, 10):
                self.assertEqual(f'id="q00{n}"' in page, f"q00{n}" in ids, (slug, n))
        self.assertIn("Eight questions are not listed", self.read("government", "index.html"))
        self.assertNotIn("Eight questions are not listed", self.read("history", "index.html").split("<main>")[1].split('id="more-title"')[0])

    def test_every_accepted_answer_and_the_give_n_note_survive(self):
        self.run_gen()
        gov = self.read("government", "index.html")
        for text in ("Speech", "Press", "Worship", "Assembly", "A &amp; B", "Give 3 of these."):
            self.assertIn(text, gov)
        self.assertIn("<strong>Answer:</strong> Republic", gov)
        self.assertNotIn("Give 1 of these", gov)
        accepted = {x["id"]: x["accepted"] for x in self.quiz_data()}
        self.assertEqual(accepted["q005"], ["Speech", "Press", "Worship", "Assembly"])
        self.assertEqual(next(x for x in self.quiz_data() if x["id"] == "q005")["required"], 3)

    def test_question_text_cannot_break_out_of_the_page(self):
        self.run_gen()
        block = self.read("index.html").split('<script type="application/json"')[1].split("</script>")[0]
        self.assertNotIn("<", block)
        self.assertNotIn("<script>alert", self.read("government", "index.html"))

    def test_only_marked_block_of_main_page_changes(self):
        cut = lambda t: (t[: t.index(gen.START)], t[t.index(gen.END):])  # noqa: E731
        before = (REPO / CFG["out"] / "index.html").read_text(encoding="utf-8")
        self.run_gen()
        self.assertEqual(cut(before), cut(self.read("index.html")))
        self.assertNotEqual(before, self.read("index.html"))

    def test_section_pages_have_unique_head_and_one_h1(self):
        self.run_gen()
        titles = set()
        for slug in ("government", "history", "symbols-holidays"):
            page = self.read(slug, "index.html")
            self.assertEqual(page.count("<h1"), 1)
            self.assertIn(f'<link rel="canonical" href="{SITE}/{CFG["out"]}/{slug}/">', page)
            titles.add(page.split("<title>")[1].split("</title>")[0])
        self.assertEqual(len(titles), 3)

    def test_quiz_has_no_timer_and_pass_mark_12(self):
        self.run_gen()
        main = self.read("index.html")
        self.assertIn('"passMark":12,"minutes":0', main)
        self.assertNotIn('id="quiz-clock"', main.split("<script")[0])
        self.assertNotIn("Time left", main)
        self.assertIn("Coming soon to the App Store", main)

    def test_section_share_tags_match_title_and_description(self):
        self.run_gen()
        for slug in ("government", "history", "symbols-holidays"):
            check_share_tags(self, self.read(slug, "index.html"), f'{SITE}/{CFG["out"]}/{slug}/')

    def test_hand_written_pages_share_tags_match_and_image_exists(self):
        for rel in ("index.html", "blackjack-video-poker-coach/index.html", "canada-citizenship-test/index.html",
                    "fr/examen-citoyennete-canadienne/index.html", "us-citizenship-test/index.html",
                    "es/examen-ciudadania-estados-unidos/index.html"):
            page = (REPO / rel).read_text(encoding="utf-8")
            self.assertEqual(head_tag(page, r'og:title" content="([^"]*)"'), head_tag(page, r"<title>(.*?)</title>"), rel)
            self.assertEqual(head_tag(page, r'og:description" content="([^"]*)"'),
                             head_tag(page, r'name="description" content="([^"]*)"'), rel)
            self.assertEqual(head_tag(page, r'og:url" content="([^"]*)"'), head_tag(page, r'rel="canonical" href="([^"]*)"'), rel)
            image = head_tag(page, r'og:image" content="https://pangufu.ca/([^"]*)"')
            self.assertTrue((REPO / image).is_file(), image)

    def test_output_is_stable_across_runs(self):
        self.run_gen()
        first = {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        self.run_gen()
        self.assertEqual(first, {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()})

    def test_canadian_sitemap_entries_survive_and_us_urls_listed_once(self):
        self.run_gen()
        self.run_gen()
        sitemap = (self.root / "sitemap.xml").read_text(encoding="utf-8")
        for url in ("https://pangufu.ca/", f"{SITE}/canada-citizenship-test/", f"{SITE}/canada-citizenship-test/history/",
                    f"{SITE}/{CFG['out']}/", f"{SITE}/{CFG['out']}/government/", f"{SITE}/{CFG['out']}/symbols-holidays/"):
            self.assertEqual(sitemap.count(f"<loc>{url}</loc>"), 1, url)

    def test_spanish_run_links_both_languages_and_keeps_every_other_sitemap_entry(self):
        es = gen.LANGS["es"]
        (self.root / es["out"]).mkdir(parents=True)
        shutil.copy(REPO / es["out"] / "index.html", self.root / es["out"] / "index.html")
        urls_en = gen.generate(CFG_FIXTURE, self.root, self.qpath)
        urls_es = gen.generate({**es, "samples": SAMPLES}, self.root, self.qpath)
        ca.update_sitemap(self.root / "sitemap.xml", urls_en)
        ca.update_sitemap(self.root / "sitemap.xml", urls_es)
        sitemap = (self.root / "sitemap.xml").read_text(encoding="utf-8")
        for url in ["https://pangufu.ca/", f"{SITE}/canada-citizenship-test/history/", *urls_en, *urls_es]:
            self.assertEqual(sitemap.count(f"<loc>{url}</loc>"), 1, url)
        for slug_en, slug_es in (("", ""), ("government/", "gobierno/"), ("symbols-holidays/", "simbolos-feriados/")):
            en_url, es_url = f"{SITE}/{CFG['out']}/{slug_en}", f"{SITE}/{es['out']}/{slug_es}"
            en_page = (self.root / CFG["out"] / slug_en / "index.html").read_text(encoding="utf-8")
            es_page = (self.root / es["out"] / slug_es / "index.html").read_text(encoding="utf-8")
            for page, own in ((en_page, en_url), (es_page, es_url)):
                self.assertIn(f'<link rel="alternate" hreflang="en-US" href="{en_url}">', page)
                self.assertIn(f'<link rel="alternate" hreflang="es-US" href="{es_url}">', page)
                self.assertIn(f'<link rel="alternate" hreflang="x-default" href="{en_url}">', page)
                self.assertIn(f'<link rel="canonical" href="{own}">', page)
            self.assertIn(f'hreflang="es-US" href="{es_url.removeprefix(SITE)}">Español', en_page)
            self.assertIn(f'hreflang="en-US" href="{en_url.removeprefix(SITE)}">English', es_page)
        self.assertIn('"and":"y","serial":false', (self.root / es["out"] / "index.html").read_text(encoding="utf-8"))

    def test_unknown_unit_stops_the_run(self):
        self.qpath.write_text(json.dumps([q("q900", "new-unit", "?", ["x"])]), encoding="utf-8")
        with self.assertRaises(SystemExit):
            self.run_gen()

    @unittest.skipUnless((gen.APP_RESOURCES / "questions-en.json").exists(), "app repo not checked out")
    def test_real_data_gives_120_questions_in_64_46_10(self):
        sections, questions = gen.load_questions(CFG, gen.APP_RESOURCES / CFG["questions"])
        self.assertEqual(len(questions), 120)
        self.assertEqual([sum(x["section"] == s["id"] for x in questions) for s in sections], [64, 46, 10])
        self.assertEqual([s["dropped"] for s in sections], [8, 0, 0])
        self.assertTrue(set(CFG["samples"]) <= {x["id"] for x in questions})
        self.assertTrue(all(len(x["answers"]) >= x["required"] and len(x["choices"]) == 3 for x in questions))


def run_build(accepted, required, language_cfg):
    """Run the shipped quiz script's build() in node, 300 times; return the right options."""
    js = ca.QUIZ_JS
    funcs = js[js.index("function shuffle"): js.index("function fill")]
    prog = (f"var T = {json.dumps(language_cfg)};{funcs}"
            f"var q = {{prompt:'p', explanation:'e', accepted:{json.dumps(accepted)}, required:{required}, choices:['w1','w2','w3']}};"
            "var out = []; for (var i = 0; i < 300; i++) { var b = build(q); out.push([b.choices.length, b.choices[b.answer]]); }"
            "console.log(JSON.stringify(out));")
    return json.loads(subprocess.run(["node", "-e", prog], capture_output=True, text=True, check=True, timeout=30).stdout)


@unittest.skipUnless(HAS_NODE, "node not installed")
class QuizRuleTest(unittest.TestCase):
    def test_right_option_joins_required_answers_in_bank_order_as_the_app_does(self):
        words = ["A", "B", "C", "D"]
        for required, expected in ((1, set(words)),
                                   (2, {"A and B", "A and C", "A and D", "B and C", "B and D", "C and D"}),
                                   (3, {"A, B, and C", "A, B, and D", "A, C, and D", "B, C, and D"})):
            rights = run_build(words, required, {"and": "and", "serial": True})
            self.assertEqual({r for n, r in rights}, expected, required)
            self.assertTrue(all(n == 4 for n, _ in rights))

    def test_spanish_join_has_no_serial_comma(self):
        rights = {r for _, r in run_build(["A", "B", "C"], 3, {"and": "y", "serial": False})}
        self.assertEqual(rights, {"A, B y C"})

    def test_canadian_questions_pass_through(self):
        js = ca.QUIZ_JS
        funcs = js[js.index("function shuffle"): js.index("function fill")]
        prog = (f"var T = {{}};{funcs}var q = {{prompt:'p', choices:['x','y'], answer:1}};"
                "console.log(build(q) === q);")
        self.assertEqual(subprocess.run(["node", "-e", prog], capture_output=True, text=True, check=True).stdout.strip(), "true")


if __name__ == "__main__":
    unittest.main()
