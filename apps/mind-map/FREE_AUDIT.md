# Mind Map: free-tier parity audit (rounds 2 and 3, 2026-11-26)

Goal: anyone leaving the **free** plan of Xmind, MindNode, MindMeister or Miro's mind map never hits "my free tool did this and this one can't".

Sources: xmind.com/pricing (Free vs Pro vs Premium table), xmind.com/blog/shortcuts-in-xmind-that-improve-mapping-efficiency, xmind.com/features and /structure, mindnode.com/download and mindnode.com/article/payment-model, MindMeister pricing listings (Capterra / Software Advice; official page not fetchable), miro.com/mind-map.

What the free tiers contain, in short:
- **Xmind Free**: unlimited topics and maps, all structures, Zone, templates, relationship / boundary / summary, marker / label / notes, colored branches (limited), Pitch mode (5 slides), 3-day version history, 3 sheets per collaborative map, PNG export of one map at a time with a watermark. Attachments, equations, topic links, tasks, SVG / Markdown / OPML / Word / Excel export are paid.
- **MindNode Free**: create nodes, titles, reorder, fold, import and export all supported formats. Outline, notes, connections, stickers, tags, focus and styling are Plus.
- **MindMeister Basic**: 3 maps, real-time sharing, colors and text styles, icons; export only as text (some listings also say image / PDF).
- **Miro Free**: 3 editable boards, mind map with auto layout (both sides, left, right, top-down), add child / sibling, colors, collapse, templates, AI credits, export the board as image, real-time collaboration.

Status: `have` = already in the app before this round; `added` = built this round; `impossible (reason)`.

## Structures
| Feature | Status |
|---|---|
| Mind map (balanced, both sides) | have |
| Logic chart right / left | have |
| Brace map | **added** (curly braces per level; imports and exports `org.xmind.ui.brace.right`) |
| Org chart down | have |
| Org chart up | **added** |
| Tree chart | have |
| Tree table (nested cells, Xmind) | **added** |
| Timeline horizontal | have |
| Timeline vertical | **added** (items alternate left and right of the axis) |
| Fishbone right-headed | have |
| Fishbone left-headed | **added** |
| Matrix (Xmind, by row and by column) | **added (round 3)**: main topics are rows (or columns), column names are edited in the Map tab, each subtopic's column is picked in the Topic tab and stored as its first label, the way Xmind does it. Round-trips as `org.xmind.ui.spreadsheet` / `org.xmind.ui.spreadsheet.column` with the `columns` extension, in both content.json and content.xml. |
| Mixing structures per branch (Xmind) | **added (round 3)**: any topic can lay out its own subtopics as Logic, Logic left, Brace, Org chart, Org up or Tree (inspector › Branch structure), nested as deep as you like; focusing on such a branch uses its structure. Round-trips as the topic's own `structureClass` / `structure-class`. Not applied inside Tree table and Matrix, whose cells are fixed grids. |
| Miro layouts (both sides / right / left / top-down) | have (Map, Logic, Logic left, Org chart) |

## Topics and content
| Feature | Status |
|---|---|
| Add subtopic / sibling / parent, edit inline, multi-line | have |
| Floating topics (Xmind, MindNode, Miro free-standing nodes) | **added**: double-click empty canvas; drag to move; drop on a topic to attach; drag a topic into empty space (or hold Option) to detach; "Detach as floating topic" menu; round-trips as Xmind detached topics with position |
| Zone (Xmind group of floating topics) | **added (round 3)**: select floating topics › Group into zone; zones have a label and color, drag the zone to move its topics together, Ungroup keeps the topics, and Export zone as PNG saves just that region. Xmind's own file format for zones isn't public, so zones are stored in the sheet under a `mindmap:zones` key (content.json) and a `mindmap.zones` extension (content.xml): they round-trip through this app, and Xmind keeps the topics as plain floating topics. |
| Callouts | **added** (Alt+Enter, inspector field; Xmind `callout` children in both formats) |
| Numbering of subtopics (1., a., A., i., I., 1.1 nested) | **added** (Xmind `numbering`, stored in content.json) |
| Relationships (curved arrows, labels, arrow ends, dashed / solid, bend) | have |
| Boundaries with labels | have |
| Summaries | have |
| Markers / icons (priority, progress, flags, stars, faces, symbols) | have |
| Emoji icons | **added** (48-emoji picker, "Add as icon") |
| Stickers (Xmind sticker library, MindNode stickers) | **added** as large emoji stickers rendered to images, so they export to every format. Xmind's own illustrated sticker artwork is its property and is not copied. |
| Images in topics (picker, paste, drop) | have; Cmd+Shift+I shortcut **added** |
| Notes | have |
| Links (web) | have |
| Labels | have |
| Task checkboxes with progress counts | have |
| Branch color, fill, shape, bold, italic, size | have |
| Copy style / paste style (Xmind format painter) | **added** (Option+Cmd+C / Option+Cmd+V, context menu) |
| Themes, rainbow branches, line styles, spacing | have |
| Templates (Xmind, MindMeister, Miro) | **added**: 12 templates (brainstorm, project plan, meeting notes, SWOT, weekly planner, book notes, decision, root-cause fishbone, roadmap timeline, org chart, study guide brace, comparison tree table) |

## Working with the map
| Feature | Status |
|---|---|
| Outline view | have; now also lists floating topics |
| Fold / unfold, fold to level | have |
| Focus on a branch (drill down / up) | have; F6 / Shift+F6 **added** (Xmind 8 keys) |
| Zen mode | have; Option+Cmd+F **added** (Xmind's key), Cmd+. kept |
| Pitch / presentation mode | have; **added** "Every branch" mode that steps into sub-branches, and floating topics as slides; no 5-slide cap |
| Drag to reorder / reparent | have |
| Multi-select | have (Shift / Cmd click, Cmd+A); **added** Shift+drag box selection |
| Undo / redo | have |
| Version history (Xmind Free keeps 3 days) | **added**: a version every few minutes while editing (last 40), restore with undo, or open an old version as a copy |
| Sheets (several maps in one .xmind file) | **added**: sheet tabs under the canvas for maps from one file, "+" adds a sheet, Cmd+S saves all sheets back into one .xmind |
| Find in topics, notes, labels, callouts | have (callouts **added** to search) |
| Zoom, fit, 100% | have |

## Keyboard (Xmind Mac keys)
Tab, Enter, Shift+Enter, Cmd+Enter (parent), Space / F2, arrows, Option+arrows, Delete, Cmd+/ fold, Cmd+Shift+L relationship, Cmd+Shift+B boundary, Cmd+] summary, Cmd+Shift+N note, Cmd+K link, Cmd+B / Cmd+I, Cmd+= / Cmd+- / Cmd+0 zoom, Cmd+F find, Cmd+Z / Shift+Cmd+Z: **have**.
**Added**: Cmd+S save to the original file, Shift+Cmd+S export, Cmd+O open, Cmd+N new map, Option+Cmd+C / V style, Option+Cmd+F zen, Cmd+Shift+I image, Alt+Enter callout, F6 / Shift+F6 drill down / up.
Known differences: Xmind uses Shift+Cmd+K for "link webpage"; here Cmd+K is the link and Shift+Cmd+K toggles the task checkbox (kept from round 1 so existing users don't lose it). Xmind's label key collides with its relationship key in Xmind's own table, so labels stay in the inspector. Cmd+N and Cmd+O are taken by the browser when the app runs in a browser tab; they work in the installed app.

## Import and export
| Feature | Status |
|---|---|
| Open .xmind (new JSON format and XMind 8 XML), .opml, .mm, .md, .txt, .json | have |
| Open a .zip that holds any of those (our own save wrapper, or a renamed .xmind) | **added** |
| Export PNG, SVG, PDF, Markdown, OPML, FreeMind .mm, .xmind, JSON backup | have (no watermark, any size) |
| Export plain-text outline (.txt) (MindMeister Basic's only export) | **added** |
| **Save back to the original extension** | **added**: every imported map remembers its file name and format; Cmd+S (or Export › Save to …) writes the same format with the same name. Multi-sheet .xmind files are written back as one file with all sheets. |
| How .xmind / .opml / .mm get past the download allowlist | The `downloads` allowlist (`apps/_ref/downloads.d.ts`) has no .xmind, .opml or .mm. The app first tries the real extension (works if the platform ever allows it); when refused with `rejected_extension` it saves **Plan.xmind.zip containing Plan.xmind**. On a Mac, double-clicking the zip in Downloads produces Plan.xmind next to it, ready to open; on Windows, open the zip and drag the file out. The first time this happens a short sheet explains it, and it's also under More › "Saving back to Xmind…" and the sidebar link. Markdown, PNG, SVG and PDF save directly with no zip; Xmind and MindNode both import Markdown. The old "remove the .zip ending" instruction is gone (it was wrong for a real zip). |
| Round-trip fidelity | Tested: topics, notes, markers, labels, links, images, boundaries, summaries, relationships, callouts, numbering, floating topics with positions, sheet names, structure, emoji icons all survive .xmind → app → .xmind (both content.json and XMind 8 content.xml readers). Numbering is now also written to XMind 8's content.xml as `<numbering number-format=… prepending-numbers=…>` (round 3) and read back from it. |

## Impossible
| Feature | Reason |
|---|---|
| Mobile apps (iOS / Android) | The app is a web artifact; it runs in the Claude app and browsers, not as a native mobile app. |
| Cloud sync between devices | Maps live in this computer's browser storage; the artifact has no account or sync service. |
| Real-time collaboration, sharing links, embed share links, comments (MindMeister, Miro, Xmind) | Needs a server that hosts the map for several people; this app is single-user and local. |
| Audio notes (Xmind) | Recording real audio is impossible: an artifact page never gets the microphone; the platform's `dictation` capability hands over text only. **Added instead (round 3): voice notes as text**: Note › Dictate note turns speech into the topic's note (live preview while speaking, undoable, typed fallback when dictation isn't offered). |
| Attachments, math equations, topic links (Xmind) | Pro-only in Xmind, out of scope for this free-tier round (equations would also need a math renderer loaded from a CDN). |
| Xmind Gantt view, ICS / Excel task export | Premium-only in Xmind; out of scope. |
| Native .xmind / .opml / .mm download without a zip | The platform's download allowlist doesn't include these extensions; the zip wrapper above is the zero-rename path. |
