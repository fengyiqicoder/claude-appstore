#!/usr/bin/env python3
"""Build Claude AppStore from data/apps.json.

Outputs:
  docs/index.html      the website (GitHub Pages, claudeappstore.000ooo.ooo)
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
import urllib.parse
ICONS = {f.stem: f.read_text() for f in sorted((ROOT / "data/icons").glob("*.svg"))}
i0, i1 = page.index("/*ICONS*/"), page.index("/*ENDICONS*/") + len("/*ENDICONS*/")
page = page[:i0] + json.dumps(ICONS, ensure_ascii=False).replace("</", "<\\/") + page[i1:]
ZH = json.loads((ROOT / "data/zh.json").read_text()) if (ROOT / "data/zh.json").exists() else {}
z0, z1 = page.index("/*ZH_DATA*/"), page.index("/*END_ZH*/") + len("/*END_ZH*/")
page = page[:z0] + json.dumps(ZH, ensure_ascii=False).replace("</", "<\\/") + page[z1:]
FAVICON = "data:image/svg+xml," + urllib.parse.quote(ICONS.get("store", ""), safe=":/=,;'")

art_url = (ROOT / "data/artifact_url.txt").read_text().strip() if (ROOT / "data/artifact_url.txt").exists() else ""
page = page.replace("/*STORE_ARTIFACT*/", art_url)
(ROOT / "artifact").mkdir(exist_ok=True)
(ROOT / "artifact/store.html").write_text(page)
site_page = page.replace("const SITE = /*SITE*/false;", "const SITE = true;")

STORE = "https://claudeappstore.000ooo.ooo"
ALT = f'<link rel="alternate" hreflang="en" href="{STORE}/"><link rel="alternate" hreflang="zh-CN" href="{STORE}/zh/"><link rel="alternate" hreflang="x-default" href="{STORE}/">'
def site_head(lang):
    zh = lang == "zh"
    title = "Claude AppStore：别再为 App 付费了" if zh else "Claude AppStore: Stop paying for apps"
    desc = ("Word、Excel、PowerPoint、Acrobat、Grammarly、Xmind、Canva、Notion 等软件的免费 AI 替代，跑在你已有的 Claude 套餐上，装到 Mac 或 Windows 就能用。" if zh
            else "Free AI alternatives to Word, Excel, PowerPoint, Acrobat, Grammarly, Xmind, Canva and more. They run on the Claude plan you already have and install on your Mac or Windows.")
    # Chinese browsers landing on the English page go to /zh/ unless they chose English
    redirect = "" if zh else """<script>try{if(/^zh/i.test(navigator.language||"")&&!/[?&]lang=en/.test(location.search)&&localStorage.getItem("lang")!=="en")location.replace("zh/"+location.hash)}catch(e){}</script>"""
    return f"""<!doctype html>
<html lang="{'zh-CN' if zh else 'en'}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<link rel="canonical" href="{STORE}/{'zh/' if zh else ''}">
{ALT}{redirect}
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<link rel="icon" href="{FAVICON}">
<style>:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px);height:100%}}[hidden]{{display:none!important}}</style>
</head><body>
"""
(ROOT / "docs").mkdir(exist_ok=True)
(ROOT / "docs/zh").mkdir(exist_ok=True)
(ROOT / "docs/index.html").write_text(site_head("en") + site_page.replace("/*LANG*/null", '"en"') + "\n</body></html>\n")
(ROOT / "docs/zh/index.html").write_text(site_head("zh") + site_page.replace("/*LANG*/null", '"zh"') + "\n</body></html>\n")
(ROOT / "docs/CNAME").write_text("claudeappstore.000ooo.ooo\n")

# README
CATS = [("play", "Play"), ("learn", "Learn"), ("work", "Work"), ("life", "Life")]
def entry(a):
    name = f"[{a['name']}]({a['artifact']})" if a["artifact"] else a["name"]
    lang = f" {a['lang']}." if a["lang"] else ""
    if a.get("soon"):
        return f"- **{a['name']}** - {a['subtitle']}. Planned, not available yet."
    if a.get("maker"):
        return f"- **{name}** - {a['desc']} ([source]({a['post']}), made by this repo)"
    site = "Hacker News" if "news.ycombinator.com" in a["post"] else "Reddit" if "reddit.com" in a["post"] else "X"
    prof = {"Hacker News": "https://news.ycombinator.com/user?id=", "Reddit": "https://www.reddit.com/user/"}.get(site, "https://x.com/") + a["author"]
    return f"- **{name}** - {a['desc']}{lang} ([post]({a['post']}) by [@{a['author']}]({a.get('authorUrl', prof)}))"
def links(items):
    return "\n".join(f"- [{x['title']}]({x['url']}) - {x['note']}" for x in items)

parts = [f"""# Claude AppStore [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> **Stop paying for apps.** Free AI apps that run on the Claude plan you already have and install on your Mac or Windows: our own Claude-powered tools, plus the best artifacts the community has shared.

**Browse the store: [claudeappstore.000ooo.ooo]({STORE})**, or install the store itself as an app: [open it in Claude](ARTIFACT_URL) and choose *Install as app*.

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
