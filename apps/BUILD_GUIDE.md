# Building a Claude AppStore app

Slogan: **Stop paying for apps.** Every app here must be good enough that a person can cancel the paid app it replaces. Build the best software you can, not a demo.

## 1. Research what people pay for (do this first)

- Look up the paid product(s) you replace (WebSearch, mode "standard"; official feature/pricing pages and help docs). List the features people actually pay for and the everyday workflow.
- Implement every feature that is possible inside an artifact. For each one you can't do, write down why.
- **Zero migration cost.** A person switching must keep working with their own data on day one:
  - Open the file formats they already have (drag and drop, file picker, paste). Export back to the same formats.
  - Keep the keyboard shortcuts and terms they know from the paid app where it makes sense.
  - Paste from clipboard everywhere it makes sense (the `paste` event works; `navigator.clipboard.readText` does not).
- Write the research in your report (short): features of the paid app, which ones you shipped, import/export formats.

## 2. Design: borrow from Mobbin

Local Mobbin database (top-rated web and iOS apps, real screens):
- Metadata: `~/Desktop/Mobbin研究/data/meta/web/NNNN_<slug>.json` and `.../meta/ios/...`. Each has `app`, `screens[]` (with `screenPatterns`, `screenElements`, `ocr` text) and `flows[]` (named flows with ordered screen ids).
- Screenshots: `~/Library/Mobile Documents/com~apple~CloudDocs/Mobbin图库/web/NNNN_<slug>/NNNN_<screenId>.webp` (the NNNN index matches the order of `screens` in the meta). Files may be iCloud placeholders; reading one with the Read tool can take a few seconds while it downloads. Look at 5-15 relevant screens, not hundreds.
- Useful entries: Grammarly 0094, Gamma 0098 and 0235, Pitch 0100, Notion 0032, Craft 0042, Coda 0179, Airtable 0315, Rows 0450, Miro 0341, Claude 0362, Perplexity 0082, Adobe 0379, Canva 0247, Linear 0005, Tana 0468. `ls` the folder for more.
- Take layout, hierarchy, interaction patterns and polish from the best ones. Do not copy logos, brand names or exact visual identity.
- Mac-native feel: system font stack (`-apple-system, BlinkMacSystemFont, "SF Pro Text", "Inter", "Segoe UI", system-ui, sans-serif`), restrained color, real empty states, keyboard-first.

## 3. Technical contract (artifact runtime)

The page is published as a Claude artifact and installed as a desktop app. Read `apps/_ref/*.d.ts` (sample, desktop, downloads, tts, claude) before writing code. Look at `apps/translator/index.html` for a working example of every pattern below.

**File shape**
- One file `apps/<id>/index.html`, no `<!doctype>`, `<html>`, `<head>` or `<body>` tags (the platform wraps it). Start with `<title>Functional Name</title>`, then `<meta name="claude:viewport-fit-sides" content="cover">`, then the manifest tag if needed, then `<style>`.
- The `<title>` is the installed app's name. Use the functional name you were given.
- Include `[hidden]{display:none!important}`.
- Colors as tokens on `:root`, dark values under `@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){...;color-scheme:dark}}` and again under `:root[data-theme="dark"]{...}`. `body` sets an explicit background.
- Works at 400px wide with no horizontal page scroll. Side gutter `padding-left:max(16px,env(safe-area-inset-left,0px))` and the right equivalent.

**Network (CSP-enforced)**
- Scripts only from `https://cdnjs.cloudflare.com`, `https://cdn.jsdelivr.net/npm/`, `https://unpkg.com`, pinned to an exact version at least a few months old (e.g. `xlsx@0.18.5`). Use UMD builds that set a global, loaded with `<script src>` before your inline script.
- Fonts only from Google Fonts. Nothing else loads: no `fetch` to other hosts, no external images, no iframes. Libraries that fetch workers or WASM at runtime will fail; pick ones that don't, or load the worker script itself with a `<script>` tag so the library falls back to the main thread.
- No `alert/confirm/prompt`, no `window.print()`, no `<a download>`.

**Capabilities** (always via `const x = window.claude?.use ? await window.claude.use("name").catch(()=>null) : null;`, design for `null`)
- `sample`: ask Claude. Call only from a user action. Use `onText` to stream, an `AbortController` per call for Stop, `cache:false` for anything that should be fresh, `sample.json` for structured output (say the exact JSON shape in the prompt). `modelTier:"quick"` for fast small edits, `"default"` for real work, `"complex"` only when it clearly needs it. Inputs ≤ 256 KiB: chunk long documents. Map error codes to friendly text (`rate_limited`, `not_granted` → hide AI UI, `refused`, `prompt_too_large`, `session_expired`). Never retry in a loop. Images need `capabilities: {sample:{images:true}}`.
- `downloads`: `await downloads.save({filename, data})` from a click. Allowed extensions include `txt json md csv docx pptx xlsx pdf html svg png jpg zip`. Handle `declined`.
- `desktop`: when `desktop?.tray` exists the page runs as the installed app: set a Dock icon with `desktop.app.dock.setIcon(canvasPngDataUrl)` and window options with `desktop.window.setOptions({...})` (always the same options, or the page reloads forever). Otherwise, if `await desktop?.install.state()==="available"`, show an "Install as app" button that calls `desktop.install.request()`. Optional permissions (`overlay`, `shortcuts`, `notifications`, `menu-bar`) must be listed in `<script type="application/json" id="claude-artifacts-manifest">{"permissions":[...]}</script>` and requested from a click. Never use `full-access`.
- `tts`: read text aloud if useful.
- Storage: `localStorage` (wrapped in try/catch) for the person's recent documents and settings. It lives only on their computer. Keep a "Recent" list so reopening the app feels like a real app.

**Writing**
- English UI copy, plain and specific. Label buttons by what they do. Errors say what happened and what to do.
- Every AI action that changes the person's content needs Undo, or must show the change for review (accept/reject) first.

## 4. Test before you report

- `node -e` syntax check of every inline script.
- Open the file in the Claude_Browser preview (`preview_start` with `url: file:///...`) and click through the non-AI paths with real files: create sample .docx/.xlsx/.pptx/.pdf/.xmind/.csv files yourself (python3 is available; check what libraries exist before relying on them, or generate the sample with the same JS library in the page).
- For AI paths, make a test copy in your scratch folder with a stub injected before the app script, e.g. `<script>window.claude={use:async n=>n==="sample"?Object.assign(async(p,o)=>{const t="...";o?.onText?.({text:t,delta:t});return {text:t,truncated:false}},{json:async()=>({...}),limits:async()=>({maxPromptBytes:262144})}):null}</script>`, and check the UI renders stubbed answers correctly. Never ship the stub.
- Check light and dark (`resize_window` with `colorScheme`) and 400px width. Close every browser tab you open.

## 5. Rules

- Write only inside `apps/<your id>/` and your own private scratch folder. Don't commit, don't publish, don't edit other apps, the store, or shared files.
- Never delete directories. Don't log in anywhere or post anything.
- Report back: path, the capabilities object to publish with, one icon word, one-sentence artifact description, store entry (`name`, `subtitle` ≤ 6 words, `category` from play/learn/work/life, `desc` 2-3 sentences, `perms` list), the paid app(s) it replaces, features shipped vs. not possible, import/export formats, what you tested and what you could not.
