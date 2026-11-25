# Free-tier audit: Grammarly Free, QuillBot Free, LanguageTool Free

Goal: someone who switches from a free plan never hits "my free tool did this and this one can't".
Researched 2026-11-26 (WebSearch, standard mode; official plan/help pages plus reviews).

Status: `have` = already in the app before this round · `added` = built this round · `impossible (reason)`.

## Grammarly Free

| Feature | Status | Notes |
|---|---|---|
| Spelling, grammar, punctuation checks | have | Claude check plus built-in offline rules |
| Conciseness suggestions | have | Wordy-phrase rules plus AI clarity category |
| Tone detector | have | Tone bars in Review; Adjust tone opens Rewrite |
| Works in every app (extension and desktop app) | added (partial) | **Quick fix**: global shortcut (default ⌥⇧G, 4 choices) plus a menu bar item open a compact Quick fix window. Paste with ⌘V and it is fixed at once. ⌘↵ copies the result and hides the window, then you paste with ⌘V in your app. Modes: Fix grammar, Clearer, Shorter, Formal, Friendly, Paraphrase, Translate. Optional float-on-top. In a browser it is a panel (⌘⇧K). **Impossible:** inline underlines inside other apps, and reading or replacing their text without copy and paste. The artifact can't inject into other apps, and `clipboard.readText` is refused. |
| Generative AI prompts (100/month) | have | Write tab, no monthly cap beyond the person's Claude usage |
| AI agents: Reader reactions, AI grader, Expert review, Paraphraser, Humanizer | have | Write ideas plus the Paraphrase modes (including Humanize) |
| AI agent: Citation finder | added | Write → "Find claims to cite" lists claims that need sources and suggests real sources to verify |
| Citation generator (APA, MLA, Chicago) | added | Cite tab: APA 7, MLA 9, Chicago (author-date), Harvard. Paste a URL, DOI, ISBN or title. Claude fills the fields from what it knows (no web access) and highlights the guessed fields with "check this". Manual entry works offline. Six source types. Insert the in-text citation at the cursor, insert or update the reference list at the end, copy with italics, download .txt. The list is saved per document. |
| Synonyms on double-click | added | Double-click a word to get synonyms that fit the sentence. Pick one to replace it (undo works). |
| AI detector | added | Write → "AI writing check", an estimate with clear caveats (Pro-only at Grammarly) |
| Plagiarism checker | impossible | Needs a search over a web or paper index. The artifact can't fetch other hosts (CSP), and Claude can't search the web through `sample`. It is Pro-only at Grammarly and premium at QuillBot. |
| Personal dictionary | have | Add from a card, import or export .txt |
| Language variants (US/UK/CA/AU/IN) | have, extended | Added New Zealand and South Africa, plus a footer language picker |

## QuillBot Free

| Feature | Status | Notes |
|---|---|---|
| Paraphraser: Standard and Fluency (125 words) | have | Plus Formal, Academic, Simple, Creative, Shorten, Expand and Humanize, 3 versions, no word cap |
| Summarizer (key sentences or paragraph, length) | added | Write → Summarize: Key points, Paragraph or One sentence. Short, Medium or Long. |
| Citation generator | added | See above |
| AI detector | added | See above |
| Translator | added | Write → Translate (45 languages) for the selection or the whole document; also a Quick fix mode |
| Grammar checker | have | |
| Word counter | have | Footer counter cycles through words, characters, time and more. Performance adds readability, vocabulary and a new "Most used words" list. |
| Plagiarism checker | impossible | Same reason as above (premium at QuillBot anyway) |
| Co-writer / Flow | have | Editor with Write with AI |

## LanguageTool Free

| Feature | Status | Notes |
|---|---|---|
| 25-30+ languages and dialects | added | 45 choices: English (7 dialects), German (DE/AT/CH), French (FR/CA), Spanish (ES/LatAm), Portuguese (BR/PT), Italian, Dutch, Catalan, Polish, Czech, Slovak, Romanian, Hungarian, Swedish, Danish, Norwegian, Finnish, Greek, Russian, Ukrainian, Turkish, Arabic, Hebrew, Persian, Hindi, Indonesian, Vietnamese, Thai, Chinese (Simplified/Traditional), Japanese, Korean, Irish, Esperanto, and "Detect language". Picker in the footer and in Goals. Claude checks in that language. The built-in offline rules are English-only, so without Claude a non-English document falls back to the system spell checker in that language (the editor's `lang` is set). |
| Personal dictionary | have | |
| Sentence rephrasing (3/day) | have | Rewrite tab, no daily cap |
| No sign-up, text not stored | have | Documents stay in localStorage on the person's computer |
| Works in browsers and apps | added (partial) | Quick fix, see Grammarly row |

## Shared basics asked for in this round

| Feature | Status | Notes |
|---|---|---|
| Document stats and readability | have | Flesch score, grade level, sentence and word length, reading and speaking time; added most-used words |
| Open and save .docx, .txt, .md | have | Also opens .odt, .rtf and .html. Exports .docx, .md, .txt and a PDF report. A dropped file goes into Quick fix when that is open. |
| Dictation | added | `dictation` capability, footer mic (⌘⇧E). Inserts at the cursor with spacing and capitals, in the chosen language. If that language isn't served, the next press falls back to the default language. |
| Read aloud | added | `tts` capability, footer speaker (⌘⇧U). Reads the selection, or from the cursor's paragraph to the end, and highlights the paragraph being read. Stop button. |
| Global shortcut, menu bar item, overlay | added | "Use in any app…" dialog shows each permission's state, asks only from a click, offers Open permissions when one is denied, and has a shortcut picker. Shortcut and menu bar item are set again on every load. |

## Still impossible

- **Inline checking inside other apps** (Grammarly's extension and desktop overlay): an installed artifact can't see or change other apps' text fields. Quick fix (shortcut, then paste, fix, copy back) is the closest equivalent.
- **Plagiarism checking against the web**: no network access to a search index.
- **Live citation lookup** (fetching a page's metadata or resolving a DOI or ISBN online): no network. Claude fills fields from memory, and guessed fields are flagged for the person to verify.
