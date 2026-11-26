"""Append data/install-prompt.js to apps/<id>/index.html in its own <script> (idempotent).
Usage: python3 data/apply_install_prompt.py id [id ...]"""
import sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
JS = (ROOT / "data/install-prompt.js").read_text().strip()
A, B = "/*INSTALL_PROMPT*/", "/*END_INSTALL_PROMPT*/"
for id_ in sys.argv[1:]:
    f = ROOT / "apps" / id_ / "index.html"; s = f.read_text()
    if A in s:
        a = s.index(A); b = s.index(B) + len(B)
        s = s[:a] + JS + s[b:]
    else:
        s = s.rstrip() + "\n<script>\n" + JS + "\n</script>\n"
    f.write_text(s)
    print(id_, "ok")
