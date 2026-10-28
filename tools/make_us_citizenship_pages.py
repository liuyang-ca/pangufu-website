#!/usr/bin/env python3
"""Generate the US citizenship practice-test pages from the US Citizen Test Coach question file.

Standard library only. Writes the section pages whole, replaces the marked block of the
hand-written main page, and updates the language's URLs in sitemap.xml:

    python3 tools/make_us_citizenship_pages.py

Plan: docs/plan-us-practice-pages.md (Decisions 1-8). Spanish is `--lang es`, read from
questions-es.json; the pages of the two languages link each other with hreflang and a visible switch.
"""
import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from make_citizenship_pages import (  # noqa: E402
    END, QUIZ_JS, ROOT, SITE, START, esc, replace_block, script_json, seo_head, update_sitemap)

APP_RESOURCES = ROOT.parent / "uscitizencoach/USCitizenCoachKit/Sources/USCitizenCoachKit/Resources"

# Grouped as the official list is (Decision 2). Every unit must appear once.
UNITS = {
    "government": ["gov-principles", "gov-system", "gov-rights"],
    "history": ["history-colonial", "history-1800s", "history-recent"],
    "symbols-holidays": ["symbols", "holidays"],
}

# Fixed so the page does not reshuffle on every run; 4 government, 4 history, 2 symbols and holidays.
SAMPLES = ["q001", "q010", "q021", "q052", "q078", "q092", "q102", "q113", "q123", "q126"]

COPY_EN = {
    "section_title": "{title}: {count} US Citizenship Test Questions",
    "section_description": (
        "{count} free US citizenship test practice questions on {title}, with every accepted "
        "answer and an explanation. No account. Independent practice."
    ),
    "section_h1": "{title}: US Citizenship Test Practice Questions",
    "section_eyebrow": "Free section",
    "section_intro": (
        "{count} practice questions from this part of the 2025 civics test. Answer out loud, "
        "then open “Show answer” to check it and read the explanation."
    ),
    "left_out": (
        "Eight questions are not listed because the answer depends on where you live or who "
        "holds office now: your senator, representative, governor and state capital, and the "
        "current Speaker of the House, President, Vice President and Chief Justice. The app asks "
        "for your state and shows the current officeholders."
    ),
    "show_answer": "Show answer",
    "answer": "Answer:",
    "accepted": "Accepted answers:",
    "give_n": "Give {count} of these.",
    "take_test": "Take the 20-question practice test",
    "more_h2": "More practice by section",
    "questions_n": "{count} questions",
    "sample_h2": "Sample questions",
    "sample_intro": "Try these ten out loud first. Open “Show answer” to check each one.",
    "sections_h2": "Practice by section",
    "sections_intro": "Every question in each section, with all accepted answers and explanations.",
    "quiz_h2": "Practice test",
    "quiz_intro": (
        "Start with a quick 5-question quiz, or take the full test: 20 random questions from the "
        "bank. You need 12 correct to pass, like the real test. There is no timer, as in the "
        "real interview."
    ),
    "quiz_noscript": "The practice test requires JavaScript. The sample questions and section pages work without it.",
    "quiz_quick": "Start quick quiz: 5 questions",
    "quiz_full": "Start full test: 20 questions",
    "quiz": {
        "progress": "Question {n} of {total}",
        "next": "Next question",
        "finish": "See my score",
        "score": "You scored {score} of {total}",
        "pass": "Pass. The real test needs 12 correct answers out of 20.",
        "fail": "Not a pass yet. The real test needs 12 correct answers out of 20.",
        "timeUp": "",
        "quickDone": "That was a quick quiz. The full test has 20 questions and needs 12 correct answers, like the real one.",
        "fullTest": "Take the full 20-question test",
        "review": "Questions to review",
        "notCorrect": "Not correct",
        "yours": "Your answer:",
        "noAnswer": "No answer",
        "right": "Right answer:",
        "passMark": 12,
        "minutes": 0,
        "and": "and",
        "serial": True,
        "appNote": (
            "The app covers all 128 questions, your state and current officeholders, a spoken "
            "mock interview and reading and writing practice."
        ),
        "soon": "Coming soon to the App Store",
        "again": "Try another",
    },
}

COPY_ES = {
    "section_title": "{title}: {count} preguntas de ciudadanía",
    "section_description": (
        "{count} preguntas de práctica del examen de ciudadanía de EE. UU. sobre {topic}, "
        "con respuestas y explicaciones. Gratis y sin cuenta."
    ),
    "section_h1": "{title}: preguntas de práctica del examen de ciudadanía de EE. UU.",
    "section_eyebrow": "Sección gratis",
    "section_intro": (
        "{count} preguntas de práctica de esta parte del examen de educación cívica de 2025. "
        "Responda en voz alta y luego abra “Ver respuesta” para comprobarla y leer la explicación."
    ),
    "left_out": (
        "Ocho preguntas no aparecen porque la respuesta depende de dónde vive usted o de quién "
        "ocupa el cargo ahora: su senador, su representante, su gobernador y la capital de su "
        "estado, y el actual Presidente de la Cámara de Representantes, el Presidente, el "
        "Vicepresidente y el presidente de la Corte Suprema. La app le pregunta su estado y "
        "muestra a los funcionarios actuales."
    ),
    "show_answer": "Ver respuesta",
    "answer": "Respuesta:",
    "accepted": "Respuestas aceptadas:",
    "give_n": "Dé {count} de estas.",
    "take_test": "Haga el examen de práctica de 20 preguntas",
    "more_h2": "Más práctica por sección",
    "questions_n": "{count} preguntas",
    "sample_h2": "Preguntas de muestra",
    "sample_intro": "Responda primero estas diez en voz alta. Abra “Ver respuesta” para comprobar cada una.",
    "sections_h2": "Practique por sección",
    "sections_intro": "Todas las preguntas de cada sección, con todas las respuestas aceptadas y explicaciones.",
    "quiz_h2": "Examen de práctica",
    "quiz_intro": (
        "Empiece con un cuestionario rápido de 5 preguntas o haga el examen completo: 20 preguntas "
        "al azar del banco. Necesita 12 respuestas correctas para aprobar, como en el examen real. "
        "No hay cronómetro, como en la entrevista real."
    ),
    "quiz_noscript": "El examen de práctica necesita JavaScript. Las preguntas de muestra y las páginas por sección funcionan sin él.",
    "quiz_quick": "Empiece el cuestionario rápido: 5 preguntas",
    "quiz_full": "Empiece el examen completo: 20 preguntas",
    "quiz": {
        "progress": "Pregunta {n} de {total}",
        "next": "Siguiente pregunta",
        "finish": "Ver mi puntaje",
        "score": "Obtuvo {score} de {total}",
        "pass": "Aprobado. El examen real requiere 12 respuestas correctas de 20.",
        "fail": "Todavía no aprueba. El examen real requiere 12 respuestas correctas de 20.",
        "timeUp": "",
        "quickDone": "Fue un cuestionario rápido. El examen completo tiene 20 preguntas y requiere 12 respuestas correctas, como el real.",
        "fullTest": "Haga el examen completo de 20 preguntas",
        "review": "Preguntas para repasar",
        "notCorrect": "Incorrecta",
        "yours": "Su respuesta:",
        "noAnswer": "Sin respuesta",
        "right": "Respuesta correcta:",
        "passMark": 12,
        "minutes": 0,
        "and": "y",
        "serial": False,
        "appNote": (
            "La app cubre las 128 preguntas, su estado y los funcionarios actuales, una entrevista "
            "de práctica hablada y práctica de lectura y escritura."
        ),
        "soon": "Próximamente en la App Store",
        "again": "Probar con otras",
    },
}

LANGS = {
    "en": {
        "questions": "questions-en.json",
        "out": "us-citizenship-test",
        "sections": {"government": ("government", "American Government"),
                     "history": ("history", "American History"),
                     "symbols-holidays": ("symbols-holidays", "Symbols and Holidays")},
        "samples": SAMPLES,
        "copy": COPY_EN,
        "switch_to": "es",
    },
    "es": {
        "questions": "questions-es.json",
        "out": "es/examen-ciudadania-estados-unidos",
        "sections": {"government": ("gobierno", "Gobierno estadounidense"),
                     "history": ("historia", "Historia estadounidense"),
                     "symbols-holidays": ("simbolos-feriados", "Símbolos y días feriados")},
        "topics": {"government": "el gobierno estadounidense", "history": "la historia estadounidense",
                   "symbols-holidays": "los símbolos y días feriados"},
        "samples": SAMPLES,
        "copy": COPY_ES,
        "switch_to": "en",
    },
}


def load_questions(cfg, path):
    """Return (sections, questions): every question except `local` and `current`, in file order."""
    unit_to_section = {u: sid for sid, units in UNITS.items() for u in units}
    sections = [{"id": sid, "slug": slug, "title": title} for sid, (slug, title) in cfg["sections"].items()]
    questions, dropped = [], {sid: 0 for sid in UNITS}
    for q in json.loads(Path(path).read_text(encoding="utf-8")):
        if q["unit"] not in unit_to_section:
            raise SystemExit(f"{q['id']}: unit {q['unit']!r} is not in any section")
        sid = unit_to_section[q["unit"]]
        if q.get("local") or q.get("current"):
            dropped[sid] += 1
        else:
            questions.append({**q, "section": sid})
    for s in sections:
        s["dropped"] = dropped[s["id"]]
    return sections, questions


def question_html(n, q, copy):
    """One question as a fieldset with every accepted answer behind <details>, readable without JavaScript."""
    answers = [a["text"] for a in q["answers"]]
    if q["required"] == 1 and len(answers) == 1:
        shown = f'    <p class="answer"><strong>{esc(copy["answer"])}</strong> {esc(answers[0])}</p>\n'
    else:
        give = f' {esc(copy["give_n"].format(count=q["required"]))}' if q["required"] > 1 else ""
        items = "".join(f"<li>{esc(a)}</li>" for a in answers)
        shown = (f'    <p class="answer"><strong>{esc(copy["accepted"])}</strong>{give}</p>\n'
                 f"    <ul>{items}</ul>\n")
    return (
        f'<fieldset class="question" id="{esc(q["id"])}">\n'
        f"  <legend>{n}. {esc(q['prompt'])}</legend>\n"
        f"  <details>\n"
        f"    <summary>{esc(copy['show_answer'])}</summary>\n"
        f"{shown}"
        f"    <p>{esc(q['explanation'])}</p>\n"
        f"  </details>\n"
        f"</fieldset>"
    )


def page_url(cfg, section=None):
    return f"{SITE}/{cfg['out']}/" + (f"{section['slug']}/" if section else "")


def localize_head(head, cfg, section_id=None):
    """Point the copied head's hreflang alternates and language switch at this page's pair.

    Section pages copy the main page's head, so without this they would link to the main pages.
    """
    def url(c):
        slug = c["sections"][section_id][0] + "/" if section_id else ""
        return f"{SITE}/{c['out']}/{slug}"

    en, es = url(LANGS["en"]), url(LANGS["es"])
    target = {"en-US": en, "es-US": es, "x-default": en}
    if head.count('rel="alternate"') != 3 or head.count('class="nav-lang"') != 1:
        raise SystemExit("main page head needs 3 hreflang alternates and one .nav-lang link")
    head = re.sub(r'(<link rel="alternate" hreflang="([^"]+)" href=")[^"]*(">)',
                  lambda m: m.group(1) + target[m.group(2)] + m.group(3), head)
    other = url(LANGS[cfg["switch_to"]])
    return re.sub(r'(<a class="nav-lang"[^>]* href=")[^"]*(")',
                  lambda m: m.group(1) + other.removeprefix(SITE) + m.group(2), head)


def section_links(cfg, sections, counts, skip=None):
    copy = cfg["copy"]
    items = "".join(
        f'<li><a href="/{cfg["out"]}/{s["slug"]}/">{esc(s["title"])}</a> '
        f'({esc(copy["questions_n"].format(count=counts[s["id"]]))})</li>'
        for s in sections if s["id"] != skip
    )
    return f'<ul class="feature-points">{items}</ul>'


def main_block(cfg, sections, questions):
    copy = cfg["copy"]
    by_id = {q["id"]: q for q in questions}
    counts = {s["id"]: sum(q["section"] == s["id"] for q in questions) for s in sections}
    samples = "\n".join(question_html(i, by_id[sid], copy) for i, sid in enumerate(cfg["samples"], 1))
    data = [{"id": q["id"], "prompt": q["prompt"], "accepted": [a["text"] for a in q["answers"]],
             "required": q["required"], "choices": q["choices"], "explanation": q["explanation"]}
            for q in questions]
    text = f"var T = {script_json(copy['quiz'])};{QUIZ_JS}"
    return f"""<section class="prose" id="quiz" aria-labelledby="quiz-title">
  <h2 id="quiz-title">{esc(copy['quiz_h2'])}</h2>
  <p>{esc(copy['quiz_intro'])}</p>
  <noscript><p>{esc(copy['quiz_noscript'])}</p></noscript>
  <div id="quiz-app" hidden>
    <div id="quiz-start" class="quiz-actions">
      <button type="button" class="button primary" id="quiz-quick-btn">{esc(copy['quiz_quick'])}</button>
      <button type="button" class="button secondary" id="quiz-full-btn">{esc(copy['quiz_full'])}</button>
    </div>
    <div id="quiz-run" hidden>
      <p class="quiz-timer"><span id="quiz-progress"></span></p>
      <form id="quiz-form"></form>
    </div>
    <div id="quiz-result"></div>
  </div>
</section>
<section class="prose" aria-labelledby="sample-title">
  <h2 id="sample-title">{esc(copy['sample_h2'])}</h2>
  <p>{esc(copy['sample_intro'])}</p>
{samples}
</section>
<section class="prose" aria-labelledby="sections-title">
  <h2 id="sections-title">{esc(copy['sections_h2'])}</h2>
  <p>{esc(copy['sections_intro'])}</p>
  {section_links(cfg, sections, counts)}
  <p>{esc(copy['left_out'])}</p>
</section>
<script type="application/json" id="question-data">{script_json(data)}</script>
<script>{text}</script>"""


def section_page(cfg, main_text, sections, questions, sec):
    copy = cfg["copy"]
    qs = [q for q in questions if q["section"] == sec["id"]]
    counts = {s["id"]: sum(q["section"] == s["id"] for q in questions) for s in sections}
    fmt = {"title": sec["title"], "count": len(qs), "topic": cfg.get("topics", {}).get(sec["id"], "")}

    # The shell comes from the hand-written main page so the two cannot drift apart.
    head = main_text[: main_text.index("<main>") + len("<main>")]
    notice = re.search(r'\n\s*<section class="notice-section">.*?</section>', main_text, re.S).group(0)
    tail = main_text[re.search(r'\n    <section class="(?:apps-section|support)\b', main_text).start():]
    head = re.sub(r"<title>.*?</title>", lambda m: f"<title>{esc(copy['section_title'].format(**fmt))}</title>", head)
    head = re.sub(r'<meta name="description" content="[^"]*">',
                  lambda m: f'<meta name="description" content="{esc(copy["section_description"].format(**fmt))}">', head)
    head = re.sub(r'<link rel="canonical" href="[^"]*">',
                  lambda m: f'<link rel="canonical" href="{page_url(cfg, sec)}">', head)
    head = localize_head(head, cfg, sec["id"])
    head = seo_head(head, main_text, esc(copy["section_title"].format(**fmt)),
                    esc(copy["section_description"].format(**fmt)), page_url(cfg, sec), sec["title"])

    body = "\n".join(question_html(i, q, copy) for i, q in enumerate(qs, 1))
    left_out = f"\n      <p>{esc(copy['left_out'])}</p>" if sec["dropped"] else ""
    return f"""{head}
    <section class="page-intro wrap" aria-labelledby="page-title">
      <p class="eyebrow">{esc(copy['section_eyebrow'])}</p>
      <h1 id="page-title">{esc(copy['section_h1'].format(**fmt))}</h1>
      <p class="intro-text">{esc(copy['section_intro'].format(**fmt))}</p>
    </section>{notice}

    <div class="wrap">
      <section class="prose" aria-label="{esc(sec['title'])}">
{body}{left_out}
      </section>
      <section class="prose" aria-labelledby="more-title">
        <h2 id="more-title">{esc(copy['more_h2'])}</h2>
        <p><a href="/{cfg['out']}/#quiz">{esc(copy['take_test'])}</a></p>
        {section_links(cfg, sections, counts, skip=sec['id'])}
      </section>
    </div>
{tail}"""


def generate(cfg, root, questions_path):
    """Write one language's pages under root; return its published URLs."""
    out = Path(root) / cfg["out"]
    main_path = out / "index.html"
    main_text = main_path.read_text(encoding="utf-8")
    sections, questions = load_questions(cfg, questions_path)
    missing = set(cfg["samples"]) - {q["id"] for q in questions}
    if missing:
        raise SystemExit(f"sample ids not in the question list: {sorted(missing)}")

    for sec in sections:
        page = out / sec["slug"] / "index.html"
        page.parent.mkdir(parents=True, exist_ok=True)
        page.write_text(section_page(cfg, main_text, sections, questions, sec), encoding="utf-8")

    block = "\n" + main_block(cfg, sections, questions) + "\n      "
    main_path.write_text(replace_block(main_text, block, main_path), encoding="utf-8")
    return [page_url(cfg)] + [page_url(cfg, s) for s in sections]


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--lang", default="en", choices=sorted(LANGS))
    ap.add_argument("--root", default=ROOT, help="site root to write into (default: this repo)")
    ap.add_argument("--resources", default=APP_RESOURCES, help="folder holding the app's questions-*.json")
    args = ap.parse_args()
    cfg = LANGS[args.lang]
    urls = generate(cfg, args.root, Path(args.resources) / cfg["questions"])
    update_sitemap(Path(args.root) / "sitemap.xml", urls)
    print("\n".join(urls))


if __name__ == "__main__":
    main()
