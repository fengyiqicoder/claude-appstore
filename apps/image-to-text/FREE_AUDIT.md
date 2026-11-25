# Image to Text vs. the free alternatives

Audit date: 2026-11-26. Compared against macOS Live Text, Google Lens (mobile and Chrome), Microsoft PowerToys Text Extractor and the free tiers of OCR apps.

Status: `have` = already shipped before this round, `added` = built this round, `impossible (reason)` = cannot be done in an artifact.

## Capture

| Free feature | Where | Status |
|---|---|---|
| Global shortcut that grabs text from anywhere on screen (Win+Shift+T, customizable) | PowerToys | **added**, partly. The desktop API has no screen capture: no `getDisplayMedia` and no way to read the pixels behind a transparent overlay window. The closest flow is now built: the person copies part of the screen (⌃⇧⌘4 on Mac, Win+Shift+S on Windows), presses the app's global shortcut, the window comes up with keyboard focus and a "Press ⌘V to read your screenshot" banner, ⌘V reads it, the text goes to the clipboard, the window hides and a notification shows what was copied. That is one extra key press (⌘V) compared with PowerToys. |
| Choose the shortcut | PowerToys | **added**: ⌥⇧O, ⌃⇧T, ⌥⇧T or ⌘⇧E in Settings. Needs the `shortcuts` permission. |
| Read the clipboard image without pasting | — | **added, best effort**: on the shortcut the app tries `navigator.clipboard.read()`. The desktop runtime documents `readText()` as refused and `read()` is probably refused too, so ⌘V stays the dependable path. |
| Menu bar / tray item | Live Text (system), PowerToys (tray) | **added**: "Read copied screenshot", "Open Image to Text", "History". Needs `menu-bar`. |
| Notification after copying | PowerToys (toast) | **added**: needs `notifications`. |
| Draw a selection rectangle over the live screen | PowerToys, Live Text | **impossible** (no screen capture API, and an overlay window cannot see what is beneath it). After pasting, the existing "drag over the image to read one area" covers cropping. |
| Paste, drop, open files | all | have |
| Photos from the camera | Google Lens | have on phones through the file picker's "Take Photo". A live camera viewfinder **was not built**: it needs the `camera` permission, and Lens's real-time scanning gains little over a photo. |
| Text in paused video frames | Live Text | **added**: open or drop an MP4/MOV/WebM, pause on a frame, "Read this frame". Frames can be added one after another. |
| PDF pages | Lens (Chrome), OCR apps | have (up to 60 pages, one image per page) |
| Batch of images | OCR apps | have |

## Recognition

| Free feature | Where | Status |
|---|---|---|
| Instant, offline OCR without a cloud service | Live Text, PowerToys (Windows OCR), Tesseract-based apps | **added, conditional**. Tesseract.js fails under the artifact CSP: its WASM build needs eval, and its language data (`eng.traineddata`, about 10 MB) is fetched at runtime, which `connect-src` blocks. I tested this locally with an emulated artifact CSP. Shipped instead: **ocrad.js** (a single 1.1 MB script from jsdelivr, no workers, no WASM, no data files), run on the main thread after a 2x upscale and Otsu binarization with dark-background inversion. On test screenshots it read clean English text almost perfectly in about 50 ms. It is used when the person picks "Text engine: Offline" or when Claude is not available. **Caveat**: ocrad's glue code calls `eval`. If the real artifact CSP lacks `'unsafe-eval'`, the app detects that and quietly falls back to Claude, hiding the offline option. |
| Many languages, handwriting | Live Text (about 20 languages), Lens (100+) | have, through Claude. The offline engine reads printed Latin text only. |
| Select text directly on the image | Live Text, Lens | **added**: "Select text" (key T) puts an invisible text layer over the image. Drag across words, ⌘C copies with line breaks kept, ⌘A selects all, and a floating bar offers Copy, Translate and Search. Line boxes come from Claude (quick model, JSON boxes) and are then snapped to the real ink lines found by local edge analysis. Offline, each detected ink line is read with ocrad. |
| Keep or join line breaks | PowerToys (single line option), OCR apps | have (setting plus Join, Remove line breaks, Remove extra spaces, Fix hyphenation, all undoable) |
| QR codes and barcodes | Lens, Live Text | have (BarcodeDetector, then ZXing, then jsQR, all on device) |

## Acting on the text

| Free feature | Where | Status |
|---|---|---|
| Data detectors: links, emails, phone numbers, dates, addresses | Live Text | **added**: chips above the result. Links: Open, Copy. Emails: Copy, Write an email (mailto, may do nothing). Phones: Copy, Call (tel:, may do nothing). Dates, including times and Chinese dates: Add to Google Calendar, Save calendar event (.ics inside a .zip, because .ics is not on the downloads allowlist), Copy. Addresses (US style and Chinese): Apple Maps, Google Maps, Copy. |
| Translate | Live Text, Lens | have (Translate mode for the whole image). **added**: translate just the selected words from the on-image selection bar, with a language picker. |
| Search the web for the text | Lens | **added**: selection bar "Search", and Export ▸ "Search the web for this text". |
| Look Up (dictionary) | Live Text | Covered by Explain mode and Search. A system dictionary popup is **impossible** (no API). |
| Listen (read aloud) | Lens | have (tts) |
| Copy to another device | Lens (copy to computer) | **impossible** without an account sync service. History stays on this computer. |
| Auto copy | PowerToys | have (setting); always on in quick capture |
| History | OCR apps | have (IndexedDB, search, Recent grid) |
| Export .txt .md .csv .xlsx .json, vCard | OCR apps | have; the .vcf-in-.zip save still works (tested) |
