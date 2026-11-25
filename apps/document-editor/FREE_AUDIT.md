# Free-tier audit: Word for the web / Google Docs vs AI Document Editor

Goal: someone leaving the free Word for the web (or Google Docs) never hits "my free tool did this and this one can't".
Sources: Microsoft Support — "Word features comparison: Word for the web vs desktop", "Differences between using a document in the browser and in Word", "Insert a table of contents", "Add page numbers / Page X of Y in Word for the web", "Insert a header or footer", "Create equations in Word for the web", "Use styles in Word for the web", "Can I use Track Changes in Word for the web?" (support.microsoft.com, checked 2026-11-26).

Status: **have** = already in the app before this round · **added** = built this round · **impossible** = can't be done inside an artifact (reason given) · **not built** = possible but left out (reason given).

## Page & layout
| Feature | Status | Notes |
|---|---|---|
| Print layout with real pages (page breaks, gaps, page count) | added | View → Print layout (default) / Web layout. Paragraphs split across pages at a line, table rows break between pages, headings/lists/images move whole. Status bar shows "Page X of N". Print layout needs ≥760 px window; narrower falls back to web layout. |
| Page size (Letter, Legal, A4, A5, B5, Executive, Tabloid, custom) | added | Layout → Size, Page setup… Round-trips `w:pgSz`. |
| Orientation | added | Layout → Orientation. Writes `w:orient="landscape"`. |
| Margins (presets + custom), header/footer distance | added | Layout → Margins / Page setup… Round-trips `w:pgMar`. |
| Page break | have | ⌘Enter. |
| Section breaks (next page, continuous) | added | Layout → Breaks. Exported as paragraph-level `w:sectPr`; imported back as section-break markers. |
| Per-section page setup | added (round 3) | With section breaks, Margins / Orientation / Size / Page setup apply to the section the cursor is in (Page setup can also apply to the whole document). Pages of different sizes show side by side in print layout and PDF; each section gets its own `w:pgSz`/`w:pgMar` in .docx, and Word files with mixed sections open that way. |
| Columns (1/2/3) | added | Layout → Columns, applies to the selection or the whole document. Exported as continuous sections with `w:cols`, imported back. Column blocks longer than a page now break at the page end and continue on the next page (round 3). |
| Zoom, page width | have / added | View → Zoom, new "Page width" option. |
| Ruler, indents, tab stops | added (round 3) | View → Ruler (on by default in print layout). Drag first-line, hanging/left and right indent markers; click to add left / center / right tab stops (type button on the ruler's left), drag to move, drag off to remove. Default stops every 0.5″ like Word. Saved as `w:ind` and `w:tabs`; Word files' indents and tab stops open the same way. |
| Watermark, page color, page borders | not built | Not offered in Word for the web either. |

## Headers, footers, page numbers
| Feature | Status | Notes |
|---|---|---|
| Edit header and footer | added | Insert → Header & footer, or double-click the top/bottom margin of any page. Left/center/right alignment; a Tab splits a line into left · center · right. |
| Page numbers, Page X of Y | added | Insert → Page numbers (bottom/top, left/center/right, Page X of Y, remove). Real PAGE / NUMPAGES fields in .docx. |
| Different first page | added | `w:titlePg` + first-page header/footer parts. |
| Keep the Word file's own headers (logos, tables) | added | If you don't edit them, the original header/footer parts are kept as they were. Imported text (with page fields and alignment) is shown on every page. |
| Different odd/even pages | added (round 3) | Header & footer dialog → Different odd & even pages. Shown per page on screen and in PDF; saved as `even` header/footer parts plus `w:evenAndOddHeaders` in settings.xml, and read back from Word files. |

## Text formatting & styles
| Feature | Status | Notes |
|---|---|---|
| Bold, italic, underline, strikethrough | have | Word shortcuts. |
| Subscript / superscript | added | ⌘= / ⌘⇧=. |
| Font family, font size, grow/shrink | added | Home ribbon, ⌘⇧> / ⌘⇧<. Exported as run fonts/sizes. |
| Font color, highlight | have | |
| Change case (Sentence, lower, UPPER, Capitalize, tOGGLE) | added | Home → Aa. |
| Clear formatting | have | ⌘\ |
| Format painter | added | Home → 🖌, Esc cancels. |
| Styles gallery | added | Normal, Title, Subtitle, Heading 1–6, Quote, Code. Title/Subtitle map to Word's styles. |
| Paragraph alignment incl. justify | have / added | Justify button added (⌘J). |
| Line spacing, space before/after | added | Home → ↕. Exported as `w:spacing`; direct spacing from Word files imported. |
| Indent / outdent | have | |

## Lists
| Feature | Status | Notes |
|---|---|---|
| Bulleted, numbered lists | have | Autoformat "- " / "1. ". |
| Bullet styles (●, ◦, ▪) | added | Exported with matching bullet characters. |
| Numbering formats (1., a., A., i., I.) | added | |
| Multilevel list (1. → a. → i.) | added | Tab / ⇧Tab to change level. |
| Restart / set numbering value | added | |
| Checklist (Google Docs) | added | Click the box to tick. Exported to Word as ☐ / ☒ paragraphs (Word has no checklist list type). |

## Insert
| Feature | Status | Notes |
|---|---|---|
| Tables (insert, rows/cols, header row) | have | |
| Merge / split cells, cell shading | added | Table menu. Round-trips gridSpan / vMerge / shading. |
| Pictures (insert, paste, drag, resize) | have | Plus a drag handle on the corner. |
| Picture wrap (in line, square left/right) | added | Exported as `wp:anchor` with square wrap; anchored pictures in Word files open as wrapped. |
| Alt text | added | Picture bar → Alt text (kept in .docx `descr`). |
| Shapes | added | 12 shapes with fill, outline, text. Inserted as pictures (PNG in .docx), so they look the same everywhere but aren't editable Word shapes. |
| Text box | added | A bordered box in the text flow; exported as a bordered paragraph group, imported back as a box. Floating/positioned text boxes are not supported. |
| Equations | added | LaTeX input with live preview and templates (KaTeX → MathML on screen). Exported as real Word equations (OMML) — fractions, scripts, roots, sums/integrals, accents, matrices, limits. Word equations import back as editable LaTeX. |
| Symbols | added | Insert → Symbol, with recently used. |
| Links, bookmarks-as-anchors | have | ⌘K. |
| Footnotes | have / improved (round 3) | In print layout and PDF each footnote sits at the bottom of the page its number lands on, under a separator; the page's text area shrinks to make room, and short paragraphs move with their footnotes. Click a note to edit it. Web layout lists them at the end. Real footnotes in .docx. Endnotes from Word open as footnotes. |
| Comments | have | |
| Comment replies | added | Reply thread per comment. Round-trips via `commentsExtended.xml` (paraIdParent). |
| Date, horizontal line | added | |
| Table of contents | added | Insert → Contents or References → Table of contents. Built from Heading 1–3 with page numbers from the page layout; click for Go to / Update / Remove. Exported as a real Word TOC field (sdt + bookmarks + hyperlinks), so Word's "Update table" works. Word TOCs import as an updatable table. |

## Review
| Feature | Status | Notes |
|---|---|---|
| Track changes (own edits), accept/reject, round-trip | have | Plus Previous / Next / Accept all / Reject all on the Review tab. |
| Find & replace | have | |
| Match case, whole words, wildcards (regex with $1) | added | |
| Spell check | have / added | Browser spell check with right-click suggestions; on/off toggle added. Grammar is Claude's Proofread. |
| Word count dialog | added | Pages, words, characters with/without spaces, paragraphs, footnotes, reading time; click the word count or ⌘⇧G. |
| Accessibility checker | added | Missing alt text, skipped heading levels, tables without headers, vague link text, low-contrast text. |
| Read aloud | added | `tts` capability: reads from the cursor (or the selection), highlights the paragraph being read. Hidden when not available. |
| Dictate | added | `dictation` capability: Home → Dictate, live partial text, works with Track changes. Hidden when not available. |
| Translate, rewrite, summarize (Copilot / Editor) | have | Claude features. |

## View, files, history
| Feature | Status | Notes |
|---|---|---|
| Navigation pane (headings) | have | |
| Focus mode | added | View → Focus, Esc to leave. |
| Open .docx / .pdf / .md / .txt / .html, paste from Word/Docs | have | |
| Save .docx / .pdf / .md / .html / .txt | have | PDF uses the same page layout (sizes per section, margins, headers, footers, footnotes, page numbers). Round 3: every page has an invisible text layer placed over the words, so PDF text can be selected, copied and searched in any script (checked with Chinese, Japanese, Korean). It uses a small font built in the browser with one empty glyph per character used, so no font download is needed. |
| Autosave & recent documents | have | On this computer (IndexedDB). |
| Version history | added | Autosaved every 10 minutes of editing, plus named versions; preview and restore (current text is saved as a version first). Kept on this computer, last 80 per document. |
| Print | impossible | `window.print()` is blocked in artifacts. ⌘P offers PDF export to print from. |
| Real-time co-authoring, sharing, @mentions | impossible | No shared editing channel to other people's sessions from this app; documents live on one computer. |
| Cloud save / OneDrive / sync across devices | impossible | Storage is local to the browser; no third-party network calls allowed. |
| Templates gallery | added (round 3) | New ▾ → Résumé, Cover letter, Report (title page, contents, header, Page X of Y), Meeting notes (details table, agenda, action-item checklist). Real styled documents with page setup; "Draft with Claude" covers anything else. |
| Mail merge, citations/bibliography, index, cross-references, captions | not built | Desktop-only in Word (not in the free web version). |
| Password-protected / IRM files | impossible | Encrypted .docx can't be opened without Office's crypto; same limit as Word for the web. |
| Old .doc files | impossible | Binary format; app asks to save as .docx first. |
