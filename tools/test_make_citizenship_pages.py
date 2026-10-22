import html
import json
import re
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import make_citizenship_pages as gen  # noqa: E402

REPO = gen.ROOT
SITE = gen.SITE
CFG = gen.LANGS["en"]
CFG_FR = gen.LANGS["fr"]


def q(qid, chapter, prompt, choices, answer, explanation, **extra):
    return {"id": qid, "chapter": chapter, "section": chapter, "kind": "multipleChoice",
            "prompt": prompt, "choices": choices, "answer": answer,
            "explanation": explanation, **extra}


QUESTIONS = [
    q("rights-1", "rights", "Free one?", ["No", "Yes <b>"], 1, "Because <i>reasons</i>."),
    q("who-we-are-1", "who-we-are", "Free two?", ["A", "B", "C"], 2, "Third wins."),
    q("history-1", "history", "Tricky </script><script>alert(1)</script>?", ["x", "y"], 0, "Escaped & safe."),
    q("history-2", "history", "Who is the prime minister?", ["P", "Q"], 0, "Stale soon.", current=True),
    q("modern-canada-1", "modern-canada", "Paid chapter question?", ["m", "n"], 1, "Only in the app."),
]
SECTIONS = [{"id": i, "number": n, "title": t, "guideURL": f"https://example.test/{i}"}
            for n, (i, t) in enumerate([("rights", "Rights"), ("who-we-are", "Who We Are"),
                                        ("history", "History"), ("modern-canada", "Modern Canada")], 1)]
SAMPLES = ["rights-1", "who-we-are-1", "history-1"]
CFG_FIXTURE = {**CFG, "samples": SAMPLES}
CFG_FR_FIXTURE = {**CFG_FR, "samples": SAMPLES}


class GeneratorTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp)
        self.root = self.tmp / "site"
        for c in (CFG, CFG_FR):
            (self.root / c["out"]).mkdir(parents=True)
            shutil.copy(REPO / c["out"] / "index.html", self.root / c["out"] / "index.html")
        shutil.copy(REPO / "sitemap.xml", self.root / "sitemap.xml")
        self.qpath, self.spath = self.tmp / "q.json", self.tmp / "s.json"
        self.qpath.write_text(json.dumps(QUESTIONS), encoding="utf-8")
        self.spath.write_text(json.dumps(SECTIONS), encoding="utf-8")

    def run_gen(self, lang="en", cfg=CFG_FIXTURE):
        urls = gen.generate(lang, cfg, self.root, self.qpath, self.spath)
        gen.update_sitemap(self.root / "sitemap.xml", urls)
        return urls

    def run_both(self):
        return self.run_gen("en", CFG_FIXTURE) + self.run_gen("fr", CFG_FR_FIXTURE)

    def read(self, *parts, cfg=CFG):
        return self.root.joinpath(cfg["out"], *parts).read_text(encoding="utf-8")

    def test_only_free_non_current_questions(self):
        self.run_gen()
        text = self.read("index.html") + "".join(self.read(s, "index.html") for s in CFG["slugs"])
        self.assertNotIn("Paid chapter question", text)
        self.assertNotIn("prime minister", text)
        data = self.read("index.html").split('id="question-data">')[1].split("</script>")[0]
        self.assertEqual([x["id"] for x in json.loads(data)], ["rights-1", "who-we-are-1", "history-1"])

    def test_right_answer_and_explanation_survive_in_chapter_and_quiz_data(self):
        self.run_gen()
        data = self.read("index.html").split('id="question-data">')[1].split("</script>")[0]
        quiz = {x["id"]: x for x in json.loads(data)}
        for item in QUESTIONS[:3]:
            page = self.read(item["chapter"], "index.html")
            right = html.escape(item["choices"][item["answer"]])
            self.assertIn(f"{chr(65 + item['answer'])}. {right}", page)
            self.assertIn(html.escape(item["explanation"]), page)
            self.assertEqual(quiz[item["id"]]["choices"][quiz[item["id"]]["answer"]], item["choices"][item["answer"]])

    def test_question_text_cannot_break_out_of_the_page(self):
        self.run_gen()
        main = self.read("index.html")
        block = main.split("<script type=\"application/json\"")[1].split("</script>")[0]
        self.assertNotIn("<", block)
        self.assertEqual(self.read("history", "index.html").count("<script>alert"), 0)

    def test_only_marked_block_of_main_page_changes(self):
        cut = lambda t: (t[: t.index(gen.START)], t[t.index(gen.END):])  # noqa: E731
        self.run_both()
        for cfg in (CFG, CFG_FR):
            before = (REPO / cfg["out"] / "index.html").read_text(encoding="utf-8")
            after = self.read("index.html", cfg=cfg)
            self.assertEqual(cut(before), cut(after))
            self.assertNotEqual(before, after)

    def test_chapter_pages_have_unique_head_and_one_h1(self):
        self.run_gen()
        titles = set()
        for slug in CFG["slugs"]:
            page = self.read(slug, "index.html")
            self.assertEqual(page.count("<h1"), 1)
            self.assertIn(f'<link rel="canonical" href="https://pangufu.ca/{CFG["out"]}/{slug}/">', page)
            titles.add(page.split("<title>")[1].split("</title>")[0])
        self.assertEqual(len(titles), 3)

    def test_output_is_stable_across_runs(self):
        self.run_gen()
        first = {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        self.run_gen()
        self.assertEqual(first, {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()})

    def test_sitemap_keeps_hand_written_urls_and_lists_chapters(self):
        self.run_gen()
        sitemap = (self.root / "sitemap.xml").read_text(encoding="utf-8")
        for url in ("https://pangufu.ca/", "https://pangufu.ca/purrcade/privacy.html",
                    f"https://pangufu.ca/{CFG['out']}/", f"https://pangufu.ca/{CFG['out']}/history/"):
            self.assertEqual(sitemap.count(f"<loc>{url}</loc>"), 1, url)

    def alternates(self, page):
        return dict(re.findall(r'<link rel="alternate" hreflang="([^"]+)" href="([^"]+)">', page))

    def test_every_page_pairs_with_its_translation_both_ways(self):
        self.run_both()
        pairs = [("", None)] + [(CFG["slugs"][c], c) for c in CFG["slugs"]]
        for _, cid in pairs:
            en_url, fr_url = gen.page_url("en", cid), gen.page_url("fr", cid)
            en_path = (CFG["slugs"][cid] if cid else "", "index.html")
            fr_path = (CFG_FR["slugs"][cid] if cid else "", "index.html")
            for page, lang, own, other in ((self.read(*en_path), "en", en_url, fr_url),
                                           (self.read(*fr_path, cfg=CFG_FR), "fr", fr_url, en_url)):
                self.assertEqual(self.alternates(page), {"en-CA": en_url, "fr-CA": fr_url, "x-default": en_url}, own)
                self.assertIn(f'<link rel="canonical" href="{own}">', page)
                switch = re.search(r'<a class="nav-lang"[^>]*href="([^"]+)"', page).group(1)
                self.assertEqual(SITE + switch, other, own)
                self.assertIn('lang="fr-CA"' if lang == "fr" else 'lang="en-CA"', page.split("<body")[0])

    def test_french_pages_use_french_copy_and_slugs(self):
        urls = self.run_gen("fr", CFG_FR_FIXTURE)
        self.assertEqual([u.removeprefix(SITE) for u in urls], [
            "/fr/examen-citoyennete-canadienne/", "/fr/examen-citoyennete-canadienne/droits/",
            "/fr/examen-citoyennete-canadienne/qui-nous-sommes/", "/fr/examen-citoyennete-canadienne/histoire/"])
        page = self.read("droits", "index.html", cfg=CFG_FR)
        self.assertIn("Afficher la réponse", page)
        self.assertIn("Réponse\u00a0:</strong> B. Yes &lt;b&gt;", page)
        self.assertEqual(page.count("<h1"), 1)
        self.assertNotIn("Show answer", page)
        self.assertIn('"progress":"Question {n} sur {total}"', self.read("index.html", cfg=CFG_FR))

    def test_sitemap_lists_french_pages_once(self):
        self.run_both()
        sitemap = (self.root / "sitemap.xml").read_text(encoding="utf-8")
        for u in (gen.page_url("fr"), gen.page_url("fr", "history"), gen.page_url("en", "history")):
            self.assertEqual(sitemap.count(f"<loc>{u}</loc>"), 1, u)

    @unittest.skipUnless((gen.APP_RESOURCES / "questions-en.json").exists(), "app repo not checked out")
    def test_real_data_gives_the_same_167_free_questions_in_both_languages(self):
        ids = {}
        for lang in ("en", "fr"):
            cfg = gen.LANGS[lang]
            _, questions = gen.load_questions(cfg, gen.APP_RESOURCES / cfg["questions"], gen.APP_RESOURCES / cfg["sections"])
            self.assertEqual(len(questions), 167, lang)
            self.assertFalse(any(x.get("current") for x in questions))
            self.assertTrue(set(cfg["samples"]) <= {x["id"] for x in questions})
            ids[lang] = [x["id"] for x in questions]
        self.assertEqual(ids["en"], ids["fr"])
        en = {x["id"]: x["answer"] for x in json.loads((gen.APP_RESOURCES / "questions-en.json").read_text(encoding="utf-8"))}
        fr = {x["id"]: x["answer"] for x in json.loads((gen.APP_RESOURCES / "questions-fr.json").read_text(encoding="utf-8"))}
        self.assertTrue(all(en[i] == fr[i] for i in ids["en"]))


if __name__ == "__main__":
    unittest.main()
