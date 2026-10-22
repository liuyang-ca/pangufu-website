#!/usr/bin/env python3
"""Generate the citizenship practice-test pages from the app's question files.

Standard library only. Writes the chapter pages whole, replaces the marked block of
the hand-written main page, and rewrites sitemap.xml. Re-run it whenever the app's
free-chapter questions change:

    python3 tools/make_citizenship_pages.py

Plan: docs/plan-seo-practice-pages.md (Decisions 1-5, Phase 2).
"""
import argparse
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
APP_RESOURCES = ROOT.parent / "citizencoach/CitizenCoachKit/Sources/CitizenCoachKit/Resources"
SITE = "https://pangufu.ca"
START = "<!-- generated:questions:start -->"
END = "<!-- generated:questions:end -->"

# Fixed so the page does not reshuffle on every run; spread over the three free chapters.
SAMPLES = [
    "rights-rights-01", "rights-equality-01", "rights-oath-04",
    "who-we-are-introduction-01", "who-we-are-aboriginal-05", "who-we-are-diversity-04",
    "history-new-france-02", "history-confederation-06",
    "history-first-world-war-02", "history-second-world-war-06",
]

COPY_EN = {
    "chapter_title": "{title}: {count} Citizenship Test Practice Questions | PANGUFU",
    "chapter_description": (
        "{count} free citizenship test practice questions on {title}, with answers and "
        "explanations. No account. Independent practice."
    ),
    "chapter_h1": "{title}: Citizenship Test Practice Questions",
    "chapter_eyebrow": "Free chapter {number}",
    "chapter_intro": (
        "{count} free practice questions on this chapter of the study guide. Pick an answer "
        "in your head, then open “Show answer” to check it and read the explanation."
    ),
    "guide_link": "Read this chapter in Discover Canada",
    "show_answer": "Show answer",
    "answer": "Answer:",
    "take_test": "Take the timed 20-question practice test",
    "more_h2": "More practice by chapter",
    "questions_n": "{count} questions",
    "sample_h2": "Sample questions",
    "sample_intro": "Try these ten with no timer. Open “Show answer” to check each one.",
    "chapters_h2": "Practice by chapter",
    "chapters_intro": "Every question in each free chapter, with answers and explanations.",
    "quiz_h2": "Timed practice test",
    "quiz_intro": (
        "20 random questions from the three free chapters, one at a time, in 45 minutes. "
        "You need 15 correct to pass, like the real test."
    ),
    "quiz_noscript": "The timed test needs JavaScript. The sample questions and chapter pages work without it.",
    "quiz_start": "Start practice test",
    "quiz_time": "Time left:",
    "quiz": {
        "progress": "Question {n} of {total}",
        "next": "Next question",
        "finish": "See my score",
        "score": "You scored {score} of {total}",
        "pass": "Pass. The real test needs 15 correct answers out of 20.",
        "fail": "Not a pass yet. The real test needs 15 correct answers out of 20.",
        "timeUp": "Time is up. Unanswered questions count as wrong.",
        "review": "Questions to review",
        "notCorrect": "Not correct",
        "yours": "Your answer:",
        "noAnswer": "No answer",
        "right": "Right answer:",
        "appNote": (
            "This test used 3 of 11 chapters. The app covers all 11 chapters and your "
            "province, in English and French, with audio."
        ),
        "soon": "Coming soon to the App Store",
        "again": "Try another test",
    },
}


# Canadian French, written without a French speaker's review (plan, Risks).
COPY_FR = {
    "chapter_title": "{title}\u00a0: {count} questions d’examen de citoyenneté | PANGUFU",
    "chapter_description": (
        "{count} questions de pratique gratuites sur «\u00a0{title}\u00a0» pour l’examen de "
        "citoyenneté, avec réponses et explications. Sans compte. Pratique indépendante."
    ),
    "chapter_h1": "{title}\u00a0: questions de pratique",
    "chapter_eyebrow": "Chapitre gratuit {number}",
    "chapter_intro": (
        "{count} questions de pratique gratuites sur ce chapitre du guide d’étude. Choisissez une "
        "réponse dans votre tête, puis ouvrez «\u00a0Afficher la réponse\u00a0» pour la vérifier "
        "et lire l’explication."
    ),
    "guide_link": "Lire ce chapitre dans Découvrir le Canada",
    "show_answer": "Afficher la réponse",
    "answer": "Réponse\u00a0:",
    "take_test": "Faire le test chronométré de 20 questions",
    "more_h2": "Plus de pratique par chapitre",
    "questions_n": "{count} questions",
    "sample_h2": "Exemples de questions",
    "sample_intro": (
        "Essayez ces dix questions sans chronomètre. Ouvrez «\u00a0Afficher la réponse\u00a0» "
        "pour vérifier chacune."
    ),
    "chapters_h2": "Pratique par chapitre",
    "chapters_intro": "Toutes les questions de chaque chapitre gratuit, avec réponses et explications.",
    "quiz_h2": "Test pratique chronométré",
    "quiz_intro": (
        "20 questions tirées au hasard dans les trois chapitres gratuits, une à la fois, en "
        "45 minutes. Il faut 15 bonnes réponses pour réussir, comme à l’examen réel."
    ),
    "quiz_noscript": (
        "Le test chronométré demande JavaScript. Les exemples de questions et les pages par "
        "chapitre fonctionnent sans."
    ),
    "quiz_start": "Commencer le test pratique",
    "quiz_time": "Temps restant\u00a0:",
    "quiz": {
        "progress": "Question {n} sur {total}",
        "next": "Question suivante",
        "finish": "Voir mon résultat",
        "score": "Vous avez obtenu {score} sur {total}",
        "pass": "Réussi. L’examen réel exige 15 bonnes réponses sur 20.",
        "fail": "Pas encore réussi. L’examen réel exige 15 bonnes réponses sur 20.",
        "timeUp": "Le temps est écoulé. Les questions sans réponse comptent comme fausses.",
        "review": "Questions à revoir",
        "notCorrect": "Incorrect",
        "yours": "Votre réponse\u00a0:",
        "noAnswer": "Aucune réponse",
        "right": "Bonne réponse\u00a0:",
        "appNote": (
            "Ce test couvrait 3 chapitres sur 11. L’application couvre les 11 chapitres et votre "
            "province, en français et en anglais, avec audio."
        ),
        "soon": "Bientôt sur l’App Store",
        "again": "Faire un autre test",
    },
}

# Add a language by adding an entry. Each language's hand-written main page must carry the
# hreflang alternates and the .nav-lang switch (see localize_head).
LANGS = {
    "en": {
        "questions": "questions-en.json",
        "sections": "sections-en.json",
        "out": "canada-citizenship-test",
        "slugs": {"rights": "rights", "who-we-are": "who-we-are", "history": "history"},
        "samples": SAMPLES,
        "copy": COPY_EN,
    },
    "fr": {
        "questions": "questions-fr.json",
        "sections": "sections-fr.json",
        "out": "fr/examen-citoyennete-canadienne",
        "slugs": {"rights": "droits", "who-we-are": "qui-nous-sommes", "history": "histoire"},
        "samples": SAMPLES,
        "copy": COPY_FR,
    },
}

QUIZ_JS = r"""
var all = JSON.parse(document.getElementById('question-data').textContent);
var N = 20, PASS = 15, MINUTES = 45;
var startBox = document.getElementById('quiz-start');
var runBox = document.getElementById('quiz-run');
var form = document.getElementById('quiz-form');
var out = document.getElementById('quiz-result');
var progress = document.getElementById('quiz-progress');
var timeEl = document.getElementById('quiz-time');
var run, idx, picks, endAt, tick;

function el(tag, text, cls) {
  var e = document.createElement(tag);
  if (text) e.textContent = text;
  if (cls) e.className = cls;
  return e;
}
function clear(n) { while (n.firstChild) n.removeChild(n.firstChild); }
function shuffle(a) {
  a = a.slice();
  for (var i = a.length - 1; i > 0; i--) {
    var j = Math.floor(Math.random() * (i + 1)), t = a[i];
    a[i] = a[j]; a[j] = t;
  }
  return a;
}
function fill(s, o) { return s.replace(/\{(\w+)\}/g, function (m, k) { return o[k]; }); }

function show() {
  var q = run[idx];
  clear(form);
  var fs = el('fieldset', '', 'question');
  fs.tabIndex = -1;
  fs.appendChild(el('legend', q.prompt));
  q.choices.forEach(function (c, i) {
    var lab = el('label', '', 'choice'), r = document.createElement('input');
    r.type = 'radio'; r.name = 'choice'; r.value = i;
    // The native "select one" message stops an empty answer.
    r.required = true;
    lab.appendChild(r);
    lab.appendChild(el('span', c));
    fs.appendChild(lab);
  });
  form.appendChild(fs);
  form.appendChild(el('button', idx === run.length - 1 ? T.finish : T.next, 'button primary'));
  progress.textContent = fill(T.progress, { n: idx + 1, total: run.length });
  fs.focus();
}

function update() {
  var left = Math.max(0, Math.round((endAt - Date.now()) / 1000));
  timeEl.textContent = Math.floor(left / 60) + ':' + ('0' + (left % 60)).slice(-2);
  if (left === 0) finish(true);
}

function start() {
  run = shuffle(all).slice(0, N);
  idx = 0; picks = [];
  clear(out);
  startBox.hidden = true;
  runBox.hidden = false;
  endAt = Date.now() + MINUTES * 60000;
  clearInterval(tick);
  tick = setInterval(update, 1000);
  update();
  show();
}

function finish(timedOut) {
  clearInterval(tick);
  runBox.hidden = true;
  var score = 0, wrong = [];
  run.forEach(function (q, i) { if (picks[i] === q.answer) score++; else wrong.push(i); });
  clear(out);
  var h = el('h3', fill(T.score, { score: score, total: run.length }));
  h.tabIndex = -1;
  out.appendChild(h);
  out.appendChild(el('p', score >= PASS ? T.pass : T.fail, 'verdict'));
  if (timedOut) out.appendChild(el('p', T.timeUp));
  if (wrong.length) {
    out.appendChild(el('h4', T.review));
    wrong.forEach(function (i) {
      var q = run[i], box = el('div', '', 'review');
      box.appendChild(el('p', q.prompt, 'review-prompt'));
      box.appendChild(el('p', T.notCorrect, 'review-flag'));
      box.appendChild(el('p', T.yours + ' ' + (picks[i] === undefined ? T.noAnswer : q.choices[picks[i]])));
      box.appendChild(el('p', T.right + ' ' + q.choices[q.answer]));
      box.appendChild(el('p', q.explanation));
      out.appendChild(box);
    });
  }
  out.appendChild(el('p', T.appNote, 'app-note'));
  var soon = el('p', '', 'status');
  soon.appendChild(el('span'));
  soon.appendChild(document.createTextNode(T.soon));
  out.appendChild(soon);
  var again = el('button', T.again, 'button primary');
  again.type = 'button';
  again.addEventListener('click', start);
  out.appendChild(again);
  h.focus();
}

form.addEventListener('submit', function (e) {
  e.preventDefault();
  picks[idx] = +form.querySelector('input:checked').value;
  if (++idx < run.length) show(); else finish(false);
});
document.getElementById('quiz-start-btn').addEventListener('click', start);
document.getElementById('quiz-app').hidden = false;
"""


def esc(s):
    return html.escape(s, quote=True)


def script_json(obj):
    # "<" as < keeps "</script>" and "<!--" inside question text from ending the block.
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")


def load_questions(cfg, questions_path, sections_path):
    """Return (chapters, questions): free-chapter, non-current questions in file order."""
    sections = {c["id"]: c for c in json.loads(Path(sections_path).read_text(encoding="utf-8"))}
    chapters = []
    for cid, slug in cfg["slugs"].items():
        c = sections[cid]
        chapters.append({"id": cid, "slug": slug, "title": c["title"],
                         "number": c["number"], "guide": c["guideURL"]})
    free = set(cfg["slugs"])
    questions = [q for q in json.loads(Path(questions_path).read_text(encoding="utf-8"))
                 if q["chapter"] in free and not q.get("current")]
    return chapters, questions


def question_html(n, q, copy):
    """One question as a fieldset with the answer behind <details>, readable without JavaScript."""
    choices = "".join(f"<li>{esc(c)}</li>" for c in q["choices"])
    letter = chr(ord("A") + q["answer"])
    return (
        f'<fieldset class="question" id="{esc(q["id"])}">\n'
        f"  <legend>{n}. {esc(q['prompt'])}</legend>\n"
        f'  <ol class="choices" type="A">{choices}</ol>\n'
        f"  <details>\n"
        f"    <summary>{esc(copy['show_answer'])}</summary>\n"
        f'    <p class="answer"><strong>{esc(copy["answer"])}</strong> {letter}. {esc(q["choices"][q["answer"]])}</p>\n'
        f"    <p>{esc(q['explanation'])}</p>\n"
        f"  </details>\n"
        f"</fieldset>"
    )


def page_url(lang, chapter_id=None):
    """Public URL of a language's main page, or of one of its chapter pages."""
    cfg = LANGS[lang]
    slug = f"{cfg['slugs'][chapter_id]}/" if chapter_id else ""
    return f"{SITE}/{cfg['out']}/{slug}"


def localize_head(head, lang, chapter_id=None):
    """Point the copied head's hreflang alternates and language switch at this page's pair.

    The chapter pages copy the main page's head, so without this they would link to the
    main pages instead of their own translation.
    """
    en, fr = page_url("en", chapter_id), page_url("fr", chapter_id)
    target = {"en-CA": en, "fr-CA": fr, "x-default": en}
    if head.count('rel="alternate"') != 3 or head.count('class="nav-lang"') != 1:
        raise SystemExit("main page head needs 3 hreflang alternates and one .nav-lang link")
    head = re.sub(r'(<link rel="alternate" hreflang="([^"]+)" href=")[^"]*(">)',
                  lambda m: m.group(1) + target[m.group(2)] + m.group(3), head)
    other = fr if lang == "en" else en
    return re.sub(r'(<a class="nav-lang"[^>]* href=")[^"]*(")',
                  lambda m: m.group(1) + other.removeprefix(SITE) + m.group(2), head)


def chapter_links(cfg, chapters, counts, copy, skip=None):
    items = "".join(
        f'<li><a href="/{cfg["out"]}/{c["slug"]}/">{esc(c["title"])}</a> '
        f'({esc(copy["questions_n"].format(count=counts[c["id"]]))})</li>'
        for c in chapters if c["id"] != skip
    )
    return f'<ul class="feature-points">{items}</ul>'


def main_block(cfg, chapters, questions):
    copy = cfg["copy"]
    by_id = {q["id"]: q for q in questions}
    counts = {c["id"]: sum(q["chapter"] == c["id"] for q in questions) for c in chapters}
    samples = "\n".join(question_html(i, by_id[sid], copy) for i, sid in enumerate(cfg["samples"], 1))
    data = [{"id": q["id"], "prompt": q["prompt"], "choices": q["choices"],
             "answer": q["answer"], "explanation": q["explanation"]} for q in questions]
    text = f"var T = {script_json(copy['quiz'])};{QUIZ_JS}"
    return f"""<section class="prose" id="quiz" aria-labelledby="quiz-title">
  <h2 id="quiz-title">{esc(copy['quiz_h2'])}</h2>
  <p>{esc(copy['quiz_intro'])}</p>
  <noscript><p>{esc(copy['quiz_noscript'])}</p></noscript>
  <div id="quiz-app" hidden>
    <div id="quiz-start"><button type="button" class="button primary" id="quiz-start-btn">{esc(copy['quiz_start'])}</button></div>
    <div id="quiz-run" hidden>
      <p class="quiz-timer"><span id="quiz-progress"></span> &middot; {esc(copy['quiz_time'])} <span id="quiz-time">45:00</span></p>
      <form id="quiz-form"></form>
    </div>
    <div id="quiz-result" aria-live="polite"></div>
  </div>
</section>
<section class="prose" aria-labelledby="sample-title">
  <h2 id="sample-title">{esc(copy['sample_h2'])}</h2>
  <p>{esc(copy['sample_intro'])}</p>
{samples}
</section>
<section class="prose" aria-labelledby="chapters-title">
  <h2 id="chapters-title">{esc(copy['chapters_h2'])}</h2>
  <p>{esc(copy['chapters_intro'])}</p>
  {chapter_links(cfg, chapters, counts, copy)}
</section>
<script type="application/json" id="question-data">{script_json(data)}</script>
<script>{text}</script>"""


def chapter_page(cfg, lang, main_text, chapters, questions, ch):
    copy = cfg["copy"]
    qs = [q for q in questions if q["chapter"] == ch["id"]]
    counts = {c["id"]: sum(q["chapter"] == c["id"] for q in questions) for c in chapters}
    fmt = {"title": ch["title"], "count": len(qs), "number": ch["number"]}
    url = f"{SITE}/{cfg['out']}/{ch['slug']}/"

    # The shell comes from the hand-written main page so the two cannot drift apart.
    head = main_text[: main_text.index("<main>") + len("<main>")]
    notice = re.search(r'\n\s*<section class="notice-section">.*?</section>', main_text, re.S).group(0)
    tail = main_text[main_text.index('\n    <section class="apps-section"'):]
    head = re.sub(r"<title>.*?</title>", lambda m: f"<title>{esc(copy['chapter_title'].format(**fmt))}</title>", head)
    head = re.sub(r'<meta name="description" content="[^"]*">',
                  lambda m: f'<meta name="description" content="{esc(copy["chapter_description"].format(**fmt))}">', head)
    head = re.sub(r'<link rel="canonical" href="[^"]*">', lambda m: f'<link rel="canonical" href="{url}">', head)
    head = localize_head(head, lang, ch["id"])

    body = "\n".join(question_html(i, q, copy) for i, q in enumerate(qs, 1))
    return f"""{head}
    <section class="page-intro wrap" aria-labelledby="page-title">
      <p class="eyebrow">{esc(copy['chapter_eyebrow'].format(**fmt))}</p>
      <h1 id="page-title">{esc(copy['chapter_h1'].format(**fmt))}</h1>
      <p class="intro-text">{esc(copy['chapter_intro'].format(**fmt))}</p>
      <p><a class="text-link" href="{esc(ch['guide'])}" rel="noopener">{esc(copy['guide_link'])} <span aria-hidden="true">&#8599;</span></a></p>
    </section>{notice}

    <div class="wrap">
      <section class="prose" aria-label="{esc(ch['title'])}">
{body}
      </section>
      <section class="prose" aria-labelledby="more-title">
        <h2 id="more-title">{esc(copy['more_h2'])}</h2>
        <p><a href="/{cfg['out']}/#quiz">{esc(copy['take_test'])}</a></p>
        {chapter_links(cfg, chapters, counts, copy, skip=ch['id'])}
      </section>
    </div>
{tail}"""


def update_sitemap(path, generated):
    """Keep the hand-written URLs, replace the generated ones with the published list."""
    old = re.findall(r"<loc>([^<]+)</loc>", path.read_text(encoding="utf-8"))
    # generated[0] is the language's main page; everything under it is ours, so stale chapters drop out.
    urls = [u for u in old if u in generated or not u.startswith(generated[0])]
    for i, u in enumerate(generated):
        if u not in urls:
            after = urls.index(generated[i - 1]) + 1 if i and generated[i - 1] in urls else len(urls)
            urls.insert(after, u)
    rows = "".join(f"  <url><loc>{u}</loc></url>\n" for u in urls)
    path.write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + rows + "</urlset>\n",
        encoding="utf-8",
    )


def generate(lang, cfg, root, questions_path, sections_path):
    """Write one language's pages under root; return its published URLs."""
    root = Path(root)
    chapters, questions = load_questions(cfg, questions_path, sections_path)
    out = root / cfg["out"]
    main_path = out / "index.html"
    main_text = main_path.read_text(encoding="utf-8")

    for ch in chapters:
        page = out / ch["slug"] / "index.html"
        page.parent.mkdir(parents=True, exist_ok=True)
        page.write_text(chapter_page(cfg, lang, main_text, chapters, questions, ch), encoding="utf-8")

    block = "\n" + main_block(cfg, chapters, questions) + "\n      "
    if main_text.count(START) != 1 or main_text.count(END) != 1:
        raise SystemExit(f"{main_path}: expected exactly one {START} / {END} pair")
    new_main = re.sub(re.escape(START) + ".*?" + re.escape(END),
                      lambda m: START + block + END, main_text, flags=re.S)
    main_path.write_text(new_main, encoding="utf-8")

    return [page_url(lang)] + [page_url(lang, c["id"]) for c in chapters]


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--lang", default="en", choices=sorted(LANGS))
    ap.add_argument("--root", default=ROOT, help="site root to write into (default: this repo)")
    ap.add_argument("--resources", default=APP_RESOURCES, help="folder holding the app's questions-*.json and sections-*.json")
    args = ap.parse_args()
    cfg = LANGS[args.lang]
    res = Path(args.resources)
    urls = generate(args.lang, cfg, args.root, res / cfg["questions"], res / cfg["sections"])
    update_sitemap(Path(args.root) / "sitemap.xml", urls)
    print("\n".join(urls))


if __name__ == "__main__":
    main()
