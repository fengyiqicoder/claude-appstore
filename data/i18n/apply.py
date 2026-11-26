"""Inject data/i18n/runtime.js with data/i18n/<id>.json into apps/<id>/index.html (idempotent).

<id>.json:
  {"dict": {"English UI text": "中文"},
   "patterns": [["(\\d+) words", "$1 个词"]],      # JS regex source (anchored), JS replacement
   "skip": ".grid, #doc"}                            # extra selectors holding user content
The runtime goes right after the first <script> tag so it runs before the app's own code.
Usage: python3 data/i18n/apply.py id [id ...]
"""
import sys, json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parents[2]
RT = (ROOT / "data/i18n/runtime.js").read_text()


def js(o):
    return json.dumps(o, ensure_ascii=False).replace("</", "<\\/")


for id_ in sys.argv[1:]:
    f = ROOT / "apps" / id_ / "index.html"
    s = f.read_text()
    d = json.loads((ROOT / "data/i18n" / f"{id_}.json").read_text())
    skip = d.get("skip", "").strip()
    rt = (RT.replace("/*I18N_DICT*/{}/*END_I18N_DICT*/", js(d.get("dict", {})))
            .replace("/*I18N_PATTERNS*/[]/*END_I18N_PATTERNS*/", js(d.get("patterns", [])))
            .replace('/*I18N_SKIP*/""/*END_I18N_SKIP*/', js(("," + skip) if skip else ""))).strip()
    if "/*I18N_RUNTIME*/" in s:
        a = s.index("/*I18N_RUNTIME*/")
        b = s.index("/*END_I18N_RUNTIME*/") + len("/*END_I18N_RUNTIME*/")
        s = s[:a] + rt + s[b:]
    else:
        m = re.search(r"<script>", s)
        if not m:
            raise SystemExit(f"{id_}: no inline <script>")
        s = s[:m.end()] + "\n" + rt + "\n" + s[m.end():]
    f.write_text(s)
    print(id_, "dict", len(d.get("dict", {})), "patterns", len(d.get("patterns", [])))
