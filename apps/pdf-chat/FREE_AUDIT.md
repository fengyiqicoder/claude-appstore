# PDF Chat vs. free Acrobat Reader and macOS Preview

Sources: Adobe's Acrobat Reader page (adobe.com/acrobat/pdf-reader.html) and Fill & Sign pages; Apple's Preview guide (annotate a PDF, add/delete/move pages, combine PDFs). Checked 2026-11-26.

Status: **have** = was already in the app, **added** = built this round, **impossible** = can't be done inside an artifact (reason given).

## Reading

| Feature | Free in | Status | Notes |
|---|---|---|---|
| Open PDF (picker, drag and drop, paste) | both | have | Word, PowerPoint and text files open too |
| Open password-protected PDF | both | have | In-page password prompt, retries on a wrong password |
| Recent files, reopen without picking again | both | have | Kept on this device; unsaved edits are restored too (added) |
| Page thumbnails | both | have | |
| Bookmarks / outline from the file | both | have | |
| Add your own bookmarks (Preview ⌘D) | Preview | added | Stored on this device, listed under Bookmarks |
| File attachments panel | Reader | added | Listed under Bookmarks; saving works for allowed file types |
| Search with highlighted matches, next/previous | both | have | ⌘F, ⌘G, ⇧⌘G |
| Zoom in/out, fit width, fit page | both | have | |
| Page navigation (field, arrows, Home/End) | both | have | |
| Clickable links (web links and links inside the document) | both | added | |
| Rotate view | both | added | ⇧⌘+ / ⇧⌘− (Acrobat), ⌘R; view only. Rotating pages in the file is under Organize |
| Two-page view, two pages with cover | both | added | |
| Full screen | both | added | ⌘L; falls back to a chrome-free mode if the host blocks the Fullscreen API |
| Dark reading mode (replace page colors) | Reader | added | "Dark pages" in the View menu |
| Select and copy text | both | have | |
| Read aloud (Read Out Loud) | Reader | added | This page or to the end, with Pause and Stop; uses the `tts` capability |
| Document properties | both | added | Title, author, dates, producer, page size, security, forms |
| Hand tool | Reader | added | H, or hold Space |
| Print | both | impossible | `window.print()` is not allowed in artifacts. Workaround: Save, then print the file |
| Export page as image | Preview | added | PNG or JPEG, with your comments drawn in |

## Comments and markup

| Feature | Free in | Status | Notes |
|---|---|---|---|
| Highlight text | both | added | From the selection toolbar or the Highlight tool; color and opacity |
| Underline, strikethrough | both | added | |
| Sticky notes | both | added | |
| Comment on a highlight | both | added | Selection toolbar "Comment", or click any markup |
| Text box / typewriter text | both | added | Size, color, white box, border; resizable; any language |
| Freehand drawing | both | added | Color, width, opacity |
| Shapes: rectangle, oval, line, arrow | both | added | Shift keeps squares and 45° lines |
| Stamps (Approved, Draft, Confidential…) | Reader | added | Standard stamp names where they exist |
| Move, resize, recolor, delete comments | both | added | Drag, handles, inspector, Delete key |
| Undo / redo | both | added | ⌘Z / ⇧⌘Z, includes page changes and form fields |
| Comments list panel | Reader | added | "Comments" tab: grouped by page, click to jump; author name; export to Markdown/text/Notes |
| Edit comments already in a PDF | both | added | Highlights, underlines, strike-outs, notes, ink, text boxes, shapes and lines from other apps become editable; untouched ones are saved back byte-for-byte |
| Comment replies / threads | Reader | added | Reply from the comment panel; saved as standard `/IRT` reply annotations (`/RT /R`). Replies from other apps are imported and shown in the thread; untouched ones are saved back unchanged |
| Shared review / cloud comments | Reader | impossible | Needs Adobe's cloud service |

## Forms, Fill & Sign

| Feature | Free in | Status | Notes |
|---|---|---|---|
| Fill AcroForm fields (text, multiline, checkbox, radio, dropdown, list) | both | added | Tab moves between fields; values sync across duplicate widgets |
| Clear form | Reader | added | Document menu |
| Signature field "Sign here" | both | added | Places your signature inside the field |
| Signature: type, draw, image | both | added | 4 handwriting fonts, ink colors; image background removed; saved on this device |
| Initials | both | added | |
| Add text anywhere on flat forms | both | added | Fill & Sign "Add text" |
| Today's date, check mark, cross, dot | Reader | added | |
| Flatten on save | Reader (Fill & Sign) | added | "Flatten" checkbox when saving, or "Save a flattened copy" |
| Form calculations / JavaScript actions | Reader | impossible | pdf.js scripting needs a sandboxed worker/iframe, not allowed in artifacts |
| XFA (dynamic LiveCycle) forms | Reader | impossible | No browser library renders XFA; pdf.js shows a partial view at best |
| Certificate-based digital signatures (PKI) | Reader | impossible | Needs a certificate store and a signing service; signatures here are visual, like Preview's |
| Request signatures from others | Reader | impossible | Needs Adobe's e-sign cloud service and email |
| Autofill from a saved personal profile | Reader | added | "My profile" (name, email, phone, address, company…) kept on this device; fills only empty text fields whose names match; one undo step |

## Save and export

| Feature | Free in | Status | Notes |
|---|---|---|---|
| Save a real PDF with standard annotations and filled fields | both | added | pdf-lib; annotations have appearance streams, so Acrobat, Preview, Chrome and MuPDF show them; comments stay editable |
| Non-Latin text in text boxes and fields | both | added | Text boxes use an image appearance when Helvetica can't draw the text; fields fall back to NeedAppearances |
| Save edits to a password- or permissions-locked PDF | both | added (limited) | Filled fields save via pdf.js; comments can only be saved as a flattened image copy (pdf-lib can't re-encrypt) |
| Save in place (overwrite the original file) | both | impossible | Artifacts can't write to the original file; Save downloads a new file through the `downloads` capability |
| Cloud storage, share link, sync across devices | Reader | impossible | Needs Adobe's cloud; edits are kept on this device only |
| Add or remove a password | Preview | impossible | No browser PDF library here can encrypt |

## Organize pages (free in Preview)

| Feature | Free in | Status | Notes |
|---|---|---|---|
| Reorder pages (drag) | Preview | added | Organize view and sidebar thumbnails |
| Rotate pages in the file | Preview | added | |
| Delete pages | Preview | added | |
| Insert blank page | Preview | added | |
| Insert pages from another PDF / drop a PDF on the thumbnails | Preview | added | |
| Combine open PDFs into one | Preview | added | Document menu; result opens as Combined.pdf |
| Extract pages to a new PDF | Preview | added | |
| Organize, crop or redact protected PDFs | Preview | impossible | Same encryption limit as above |
| Deleted pages truly gone from the saved file | Preview | added | Saved files drop every object nothing references, so deleted pages and replaced content don't linger in the bytes |
| Crop pages | both | added | Drag the area; this page, all, odd, even or the Organize selection; writes a real `/CropBox`; "Remove crop" restores it |
| Redaction | Preview (Acrobat Pro) | added | Mark areas or selected text, then Apply. True removal: each redacted page is rasterized with black boxes, and links/comments/field values under the boxes are deleted. The UI says the page's text becomes unselectable. Unused objects are purged from the saved file |
| Adjust color / image effects | Preview | not added | Rarely needed for PDFs |
| Edit existing page text and images | neither (paid Acrobat) | not in scope | |
