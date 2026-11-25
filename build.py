#!/usr/bin/env python3
"""Build Claude AppStore from data/apps.json.

Outputs:
  docs/index.html      the website (GitHub Pages, appstore.000ooo.ooo)
  artifact/store.html  the same page without a document skeleton, published as a Claude artifact
  README.md            the list on GitHub
"""
import json, datetime, pathlib

ROOT = pathlib.Path(__file__).resolve().parent
data = json.loads((ROOT / "data/apps.json").read_text())
today = datetime.date.today().isoformat()

tpl = (ROOT / "site/template.html").read_text()
start, end = tpl.index("/*APPS_DATA*/"), tpl.index("/*END*/") + len("/*END*/")
page = tpl[:start] + json.dumps(data, ensure_ascii=False) + tpl[end:]
page = page.replace("/*UPDATED*/", today)

(ROOT / "artifact").mkdir(exist_ok=True)
(ROOT / "artifact/store.html").write_text(page)

STORE = "https://appstore.000ooo.ooo"
head = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<link rel="canonical" href="{STORE}/">
<meta property="og:title" content="Claude AppStore">
<meta property="og:description" content="A community catalog of Claude artifacts you can install as Mac and Windows apps.">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Crect x='1' y='1' width='22' height='22' rx='5.5' fill='%230a6cdf'/%3E%3Cpath d='M7 7h4v4H7zM13 7h4v4h-4zM7 13h4v4H7z' fill='%23fff'/%3E%3Ccircle cx='15' cy='15' r='2.3' fill='%23fff'/%3E%3C/svg%3E">
<style>:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px);height:100%}}[hidden]{{display:none!important}}</style>
</head><body>
"""
(ROOT / "docs").mkdir(exist_ok=True)
(ROOT / "docs/index.html").write_text(head + page + "\n</body></html>\n")
(ROOT / "docs/CNAME").write_text("appstore.000ooo.ooo\n")

# README
CATS = [("play", "Play"), ("learn", "Learn"), ("work", "Work"), ("life", "Life")]
def entry(a):
    name = f"[{a['name']}]({a['artifact']})" if a["artifact"] else a["name"]
    lang = f" {a['lang']}." if a["lang"] else ""
    return f"- **{name}** - {a['desc']}{lang} ([post]({a['post']}) by [@{a['author']}](https://x.com/{a['author']}))"
def links(items):
    return "\n".join(f"- [{x['title']}]({x['url']}) - {x['note']}" for x in items)

parts = [f"""# Claude AppStore [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Claude artifacts you can install as desktop apps on Mac and Windows, plus the docs, prompts and teardowns that explain how they work.

**Browse the store: [appstore.000ooo.ooo]({STORE})**, or install the store itself as an app: [open it in Claude](ARTIFACT_URL) and choose *Install as app*.

On November 24, 2026, Anthropic shipped **Install as app** (beta) in Claude for Mac and Windows: ask Claude to build an artifact, pick *Install as app*, and it gets its own icon and window. Installed apps can use Claude and your connectors, and, if you allow it, send notifications, add a menu bar item, or read files. ([announcement](https://x.com/ClaudeDevs/status/2125315491522650299))

Every entry links to the creator's own post. Entries with a linked name are public artifacts you can open in Claude Desktop and install. This is a community list, not affiliated with Anthropic.

## Contents

- [Official](#official)
""" + "".join(f"- [{n}](#{k})\n" for k, n in CATS if any(a["category"] == k for a in data["apps"])) + """- [Prompts and ideas](#prompts-and-ideas)
- [How it works](#how-it-works)
- [Good to know](#good-to-know)
- [Contributing](#contributing)

## Official

""" + links(data["official"])]
for k, n in CATS:
    apps = [a for a in data["apps"] if a["category"] == k]
    if apps:
        parts.append(f"## {n}\n\n" + "\n".join(entry(a) for a in apps))
parts.append("## Prompts and ideas\n\n" + links(data["prompts"]))
parts.append("## How it works\n\n" + links(data["guides"]))
parts.append("""## Good to know

From the [help center guide](https://support.claude.com/en/articles/18516354-install-an-artifact-as-an-app):

- Needs Claude for Mac or Windows 6.28899.0 or later. Beta on Free, Pro, Max, Ultra, Team and Enterprise; Enterprise owners must turn it on.
- You must be online and signed in to Claude Desktop to open an installed app, and its requests to Claude count toward your plan's usage limits.
- Editing the artifact updates the installed app. Apps ask before using notifications, keyboard shortcuts, floating windows, files or full computer access.
- Docs, Slides and Sheets artifacts can't be installed. "Add to Dock" or browser shortcuts are just shortcuts, without these desktop features.

## Contributing

Built an artifact app? [Open an issue](../../issues/new) with a link to your post on X (or another public post) showing the app, and the artifact link if it's public. Entries are credited to the person who made the app.

## License

[CC0](LICENSE)
""")
readme = "\n\n".join(parts)
art = (ROOT / "data/artifact_url.txt")
readme = readme.replace("ARTIFACT_URL", art.read_text().strip() if art.exists() else STORE)
(ROOT / "README.md").write_text(readme)
print(f"built: {len(data['apps'])} apps, {today}")
