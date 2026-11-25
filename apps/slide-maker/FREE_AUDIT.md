# AI Slide Maker vs. the free tiers (PowerPoint for the web, Google Slides, Gamma Free)

Sources: Microsoft "Compare PowerPoint features on different platforms" and "How certain features behave in web-based PowerPoint" (support.microsoft.com), Google Slides Help, Gamma pricing/guides (gamma.app, 2026). Checked 2026-11-26.

Status: **have** = already in the app before this round · **added** = built this round · **not added (reason)** = possible in principle but left out, with the reason · **impossible (reason)** = cannot work inside a sandboxed, offline, single-file artifact.

## Files and saving
| Feature | Where it's free | Status |
|---|---|---|
| Open .pptx with original design | PPT web, Slides | have |
| Save .pptx (untouched slides byte-identical) | PPT web, Slides | have |
| Open/export .pdf, .png per slide | all | have |
| Export PDF with speaker notes (notes pages) | PPT web (print notes), Slides | added |
| Export PDF handouts (3 / 6 slides per page) | PPT web (print handouts) | added |
| Print | all | impossible (no `window.print()` in artifacts; print the exported PDF instead) |
| Autosave | all | have (on this computer) |
| Version history (restore, open as copy, named versions) | PPT web, Slides | added (local snapshots every 10 min of editing + manual "Save a version") |
| Cloud sync / open from OneDrive or Drive | all | impossible (no network or accounts in an artifact) |
| Open legacy .ppt / .key | PPT desktop | impossible (binary formats; export as .pptx first) |

## Slides
| Feature | Where | Status |
|---|---|---|
| New, duplicate, delete, reorder (drag), hide slides | all | have |
| Slide sorter (grid) view | PPT web, Slides grid view | added |
| Sections (add, rename, remove, collapse; saved as PowerPoint sections) | PPT web | added |
| Layouts | all | have |
| Format background (color, gradient, picture; apply to all) | PPT web, Slides | added |
| Header & footer: slide numbers, date, footer text | PPT web, Slides | added (theme-styled slides; imported slides keep their own placeholders) |
| Slide size 16:9 / 4:3 | PPT web, Slides | not added (theme layouts are drawn for 16:9; imported 4:3 decks still save as 4:3 untouched) |
| Speaker notes | all | have |
| Find & replace (match case, whole words, notes included) | all | added |
| Spell check | all | have (system spell checker in every text box) |
| Comments (add, reply, resolve, delete; saved into the .pptx; read from .pptx) | all | added (single person; saved as PowerPoint comments) |
| @mentions, real-time co-authoring, sharing links | all | impossible (needs accounts and a server) |

## Insert
| Feature | Where | Status |
|---|---|---|
| Text box | all | added |
| Shapes: rectangles, ovals, triangles, polygons, stars, block arrows, callout, heart, plus, donut; lines and arrows | all | added (click-drag to draw, or click for default size) |
| Fill color, transparency, outline color/weight/dash, arrow heads, shadow | all | added |
| SmartArt-style diagrams (process, chevrons, cycle, hierarchy, pyramid, Venn, matrix, list, timeline) | PPT web (limited), Slides "Diagram" | added (saved as grouped, editable shapes) |
| Tables (insert any size, edit cells, add/remove rows and columns, header row, banded rows, cell shading, Tab adds a row) | all | added (table layout existed; free tables added) |
| Merge table cells | PPT web, Slides | not added (cell editing model is a plain grid) |
| Charts (column, bar, line, pie, doughnut) anywhere on a slide, edit data, paste from Excel | Slides, PPT desktop | added (chart layout existed) |
| Pictures: insert from file, paste, drag in, replace | all | have / added as free objects |
| Picture resize (aspect locked), crop (drag crop handles), crop to shape, transparency, brightness, contrast, alt text | all | added |
| Icons | PPT web, Slides | added (built-in icon set, recolorable) |
| Video and audio from a file (embedded in the .pptx, plays in Present) | Slides (Drive video), PPT desktop | added |
| Online video (YouTube), stock images, online pictures | all | impossible (no network or iframes) |
| Draw / ink with pen and highlighter | PPT web Draw tab, Slides scribble | added (saved as editable freeform shapes) |
| Hyperlinks | all | have |
| Equations | PPT web, Slides | not added (no way to save an editable PowerPoint equation without a math engine) |
| WordArt | PPT web, Slides | not added |
| Symbols / emoji | all | have (system character viewer) |

## Arrange and format
| Feature | Where | Status |
|---|---|---|
| Select, move, resize, rotate, flip | all | added (also for objects of imported slides: move, resize, delete) |
| Multi-select (Shift-click, drag a box), Select All | all | added |
| Smart alignment guides and snapping; gridlines; snap to grid | all | added |
| Align / distribute | all | added |
| Group / ungroup | all | added |
| Bring to front / forward / backward / send to back | all | added |
| Duplicate, copy, cut, paste objects; nudge with arrows | all | added |
| Size & position by numbers | all | added |
| Format painter (copy / paste style) | PPT web, Slides paint format | added |
| Text: bold, italic, underline, strikethrough, color, highlight, size, font, super/subscript, link, clear | all | have + added (strikethrough, font, exact size) |
| Paragraph: align, vertical align, bullets, numbering, line spacing, indent (Tab) | all | added |
| Themes, theme colors and fonts, logo | all | have |
| Edit slide master | Slides (Edit theme); not in PPT web | added (master objects shown on every slide, saved into the PowerPoint slide master; "Hide background graphics" per slide) |
| Edit master/theme of an imported .pptx | PPT desktop | not added (imported slides keep their own master; restyle with a theme instead) |
| Zoom the editing canvas | all | added |
| Rulers | all | not added |
| Accessibility checker, alt text | PPT web | added |

## Animations and transitions
| Feature | Where | Status |
|---|---|---|
| Transitions: Fade, Push, Wipe, Split, Cover, Uncover, Cut, Zoom, Circle, Diamond, Plus, Dissolve, Random bars, Blinds, Wheel, Wedge, Checkerboard, Comb, Newsflash, Random; direction; speed; apply to all | PPT web (8), Slides | have (3) + added (rest) |
| Advance on click / after N seconds (self-running deck) | Slides auto-advance | added |
| Entrance: Appear, Fade, Fly In, Float In, Wipe, Zoom, Wheel; Emphasis: Pulse, Spin, Grow/Shrink, Transparency; Exit: Disappear, Fade, Fly Out, Wipe, Zoom | PPT web (37), Slides | added (saved as native PowerPoint timing XML) |
| Order, On click / With previous / After previous, duration, delay, by paragraph, preview | all | added |
| Animations from imported .pptx play in Present | all | added (common effects; other effects play as a fade and stay untouched in the file unless you edit that slide's list) |
| Motion paths, triggers | PPT desktop | not added |

## Present
| Feature | Where | Status |
|---|---|---|
| Slideshow from start / current slide, keyboard, black/white screen, go to slide number | all | have |
| Presenter view: notes, timer, clock, next slide | Slides, PPT desktop | have |
| Laser pointer, pen and erase during the show | PPT web, Slides | added |
| Live captions / subtitles, rehearse with coach, record slideshow | PPT web | impossible (needs Microsoft speech services) |
| Present online / broadcast, audience Q&A | PPT web, Slides | impossible (needs a server) |

## Fixed along the way (opening existing .pptx files)
- PowerPoint preset shapes (stars, arrows, chevrons, hearts…), freeform shapes and diagonal connector lines with arrow heads now draw correctly instead of as rectangles / not at all.
- Picture crops from PowerPoint (`srcRect`) are shown and kept; alt text is read and kept.
- Moving, resizing, cropping or deleting an object of an imported slide patches only that object's XML; the rest of the slide stays byte-identical. Grouped shapes move as one group.
- PptxGenJS gave tables the same shape id as another shape and left content-type entries for masters that don't exist; both are cleaned up on save.

## AI (already beyond the free tiers)
| Feature | Where | Status |
|---|---|---|
| Generate deck from a topic, text or file; outline review | Gamma Free (credits), PPT Copilot (paid) | have |
| Rewrite / shorten / translate / speaker notes / make visual | Gamma, Copilot (paid) | have |
| Gamma free-plan limits (credits, 10 slides, watermark) | Gamma Free | not applicable here (no credits, no watermark) |
