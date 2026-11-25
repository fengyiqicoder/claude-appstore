# AI Spreadsheet vs. the free tier of Excel for the web / Google Sheets

Goal: someone who switches from free Excel for the web (or Google Sheets) never hits "my free tool did this and this one can't".
Sources: Microsoft Support, "Differences between using a workbook in the browser and in Excel" (lists what Excel for the web can edit: data validation, cell/number formatting, merged cells, most functions, tables incl. total rows, PivotTables with the field list, filters, slicers, timelines; sparklines and named items are display-only there) plus the everyday Home / Insert / Data / Review / View ribbon commands of Excel for the web.

Status: **have** = already in the app before this round, **added** = built this round, **impossible** = can't be done inside an artifact (reason given), **not added** = possible but left out this round (reason given).

## Files and workbook

| Feature | Status | Notes |
|---|---|---|
| Open .xlsx / .xlsm / .xls / .csv / .tsv / .ods, drag and drop, paste from Excel/Sheets | have | |
| Save as .xlsx (formulas, styles, widths, heights, merges, freeze panes) | have | |
| Save as CSV (one sheet / every sheet) | have | |
| Save as PDF | added | Export > PDF…: this sheet / selection / whole workbook, Letter/A4/Legal, portrait/landscape, fit all columns / actual size / fit on one page, gridlines, repeat frozen header rows, sheet name + page numbers, charts and pictures included, live preview of page 1. Pages are rendered as images (any language/font prints correctly). |
| Print | impossible | `window.print()` is blocked in artifacts. Save as PDF covers it. |
| AutoSave / recent workbooks | have | Kept on this computer (IndexedDB). |
| Version history | added | Automatic local snapshots every 10 minutes of editing and when a file is opened, "Save version" with a name, Restore (keeps a copy of the current state first) or open a version as a separate workbook. Last 40 per workbook. |
| Real-time co-authoring, sharing links, @mentions | impossible | No server/accounts inside an artifact; the app runs only on this computer. |
| Cloud storage / OneDrive / Drive sync | impossible | No network access to other hosts (CSP). |
| Undo / redo (whole session) | have | Now also covers every new feature (pivots, tables, validation, sparklines, slicers, hide/unhide, pictures…). |
| Multiple sheets: add, rename, duplicate, move, delete, hide/unhide | have | |
| Sheet tab color | added | Right-click a tab > Tab color…; saved to .xlsx. |
| Sheet protection | added (kept) | A protected sheet's protection settings are read and written back unchanged. Setting a new password is not offered (Excel for the web can't either). |
| Macros (VBA) | impossible | Excel for the web can't run them either; .xlsm opens, macros are dropped on save (user is told). |

## Editing and formatting

| Feature | Status | Notes |
|---|---|---|
| Font, size, bold, italic, text/fill color | have | |
| Underline button | added | Was keyboard-only. |
| Strikethrough | added | Toolbar + ⌘⇧X / Ctrl+5; read from and written to .xlsx. |
| Horizontal alignment | have | |
| Vertical alignment (top / middle / bottom) | added | |
| Wrap text | added | Toolbar toggle (wrapped text from files was already drawn). |
| Borders | added | Bottom, top, left, right, top+bottom, all, outside, inside, thick outside, thick bottom, no border, border color; ⌘⇧7 outline, ⌘⇧_ none. Thick borders now round-trip as thick. |
| Merge & center / unmerge | added (button) | Was only in the right-click menu. Also fixed: centered merged cells drew their text twice. |
| Format painter | added | Click to paint once, double-click to keep painting, Esc to stop. |
| Number formats | have + added | Added Comma, Accounting, Fraction, Short date (m/d/yyyy) to the list; Custom… accepts any Excel code. |
| Increase / decrease decimals | have | |
| Clear contents / clear formatting | have | ⌘\ also clears formatting (Google Sheets shortcut). |
| Fill handle, ⌘D / ⌘R, series fill | have | |
| AutoSum (Sum, Average, Count, Max, Min) | added | Σ button, ⌘⇧T, Alt+=; picks the numbers above or to the left like Excel; on a selected block puts totals under each column. |
| Find and replace (match case, entire cell) | have | |
| Paste special: values only / formatting only / formulas only / transposed | added | Right-click menu after copying in the workbook; ⌘⇧V pastes values. |
| Insert / delete rows and columns | have | |
| Hide / unhide rows and columns | added | Right-click headers, ⌘9 / ⌘0, ⇧⌘9 / ⇧⌘0, View > Unhide all; marked in the headers; read from and written to .xlsx. |
| Row height / column width, autofit | have | |
| Group / outline rows and columns | added (round 3) | Data > Group rows / Group columns (⌥⇧→ / ⌥⇧←, also right-click on headers), up to 7 levels. Outline gutter with brackets, −/+ buttons on the summary row/column and 1-2-3 level buttons, like Excel. Saved as native outlineLevel (+ outlineLevelRow/Col) and read from files. |
| Freeze panes | have | Also in View menu. |
| Gridlines on/off | added | View > Hide gridlines; saved to .xlsx. |
| Zoom | added | Status bar −/100%/+ (50–200%), saved per sheet to .xlsx. |
| Notes (cell comments) | added | Insert / edit / delete note (⇧F2), hover to read, orange marker; author kept from files; saved as Excel notes. |
| Threaded comments / @mentions | impossible | They need Microsoft 365 identities; threaded comments in files are read as notes. |
| Hyperlinks | added | Insert / edit / remove link, ⌘-click or "Open link"; internal links like #Sheet2!A1 jump inside the workbook. Links from files were already shown. |
| Insert pictures | added | Insert > Picture… (PNG/JPEG/GIF), drag to move, corner to resize, ✕ to delete; written to .xlsx as a real picture. Pictures in opened files are kept (have). |
| Spell check | have (via Claude) | No dictionary is available offline; the AI column "Clean up" task or Ask Claude fixes spelling. |

## Formulas

| Feature | Status | Notes |
|---|---|---|
| Formula bar, autocomplete, F4 absolute refs, range highlighting, click-to-insert refs | have | |
| Argument hints while typing | added | e.g. `SUMIFS(sum_range, criteria_range1, **criteria1**, …)` for ~130 common functions. |
| Insert function (fx) | added | Click fx: searchable list of all functions with signatures. |
| Dynamic arrays: FILTER, SORT, SORTBY, UNIQUE, SEQUENCE, XLOOKUP, XMATCH, LET, TEXTSPLIT… | have | Checked in the app. |
| VSTACK, HSTACK, TAKE, DROP, CHOOSECOLS, CHOOSEROWS, TOCOL, TOROW, WRAPROWS, WRAPCOLS, EXPAND | added | |
| LAMBDA (inline call and named LAMBDAs), MAP, BYROW, BYCOL, REDUCE, SCAN, MAKEARRAY | added | Saved with Excel's `_xlfn.` / `_xlpm.` prefixes. |
| REGEXTEST, REGEXEXTRACT, REGEXREPLACE, ARRAYTOTEXT, VALUETOTEXT, HYPERLINK, ADDRESS, RANDARRAY, COUNTUNIQUE | added | |
| SUBTOTAL and AGGREGATE that skip filtered/hidden rows and nested subtotals | added | Previously ignored hidden rows. |
| Legacy names RANK, PERCENTILE, QUARTILE, STDEV, STDEVP, VAR, VARP, MODE, NORMDIST… | added | Mapped to the modern functions (were #NAME?). |
| COUNTBLANK over empty areas | added (fix) | Counted only the used range before. |
| SUMIFS, COUNTIFS, TEXT, dates (EOMONTH, NETWORKDAYS, WORKDAY, DATEDIF…), finance (PMT, NPV, IRR, XIRR…), stats | have | 300+ functions via formula.js; checked a list of ~150 in the app. |
| LET / LAMBDA names saved in Excel's format | added (fix) | LET variables were written without `_xlpm.`. |
| Structured references (Table1[Column]) | have | |
| Named ranges: create, edit, delete, go to | added | Data > Named ranges…, or type a new name in the Name Box and press Return (like Excel). Names from files were already used. |
| IMAGE() function | impossible | Images from other hosts can't load (CSP). |
| GROUPBY / PIVOTBY / PERCENTOF and eta functions (`=GROUPBY(B2:B9,C2:C9,SUM)`) | added (round 3) | Headers (auto / 0–3), grand totals (on/off/top), sort by any output column (negative = descending), filter array, multiple key and value columns; PIVOTBY with row and column totals. Bare function names work as LAMBDAs (also in BYROW, MAP…) and are saved as Excel's `_xleta.SUM`. Subtotal depth 2 is shown as a grand total only. |

## Data

| Feature | Status | Notes |
|---|---|---|
| Sort A→Z / Z→A | have | |
| Custom sort with several levels, "My data has headers" | added | Respects filtered and hidden rows like Excel. |
| AutoFilter (value list, conditions, search) | have | |
| Filters saved into the .xlsx | added | Filter criteria are written as real Excel AutoFilter criteria (value lists and custom conditions) with the filtered rows hidden, and read back from files. |
| Slicers | added | Insert > Slicer…: a floating button panel per column, click to filter, ⌘/Shift-click for several. Native slicer objects are not written to .xlsx; the filter they set is saved as a real AutoFilter. |
| Timeline slicer | added (round 3, app-only panel) | Insert > Slicer… offers a timeline for date columns: months strip, click a month or Shift-click a range. The date range is saved as a native AutoFilter (two custom filters joined with AND) and read back. Column filter menu also gained "Between". |
| Native Excel slicer / timeline objects in the .xlsx | impossible here | They need slicer caches tied to an Excel table or PivotTable, plus extension parts that no tool available to this test run can validate; a malformed slicer makes Excel show its repair dialog and drop content. The filter they set is saved natively instead. |
| Data validation: create and edit | added | Data > Data validation…: list (items or a range, with in-cell dropdown), whole number, decimal, date, time, text length, custom formula; between / not between / = / ≠ / > / < / ≥ / ≤; ignore blanks; input message (shown when the cell is selected); Stop / Warning / Information alerts enforced when typing; clear from a range; edit and delete rules; Circle invalid data. Saved as real Excel validation. |
| Remove duplicates, text to columns, trim, case, fill blanks | have | Clean panel (also in the Data menu). |
| Flash Fill | added | ⌘E / Data > Flash Fill: learns from one or two typed examples (first/last names, initials, email parts, reformatting, joining columns, case changes). Falls back to the Claude AI column when no pattern fits. |
| Format as Table (styles, banded rows, header row) | added | Insert > Table: 7 styles, structured references work immediately, filter buttons, written as a real Excel table; tables in files now show their style. Data > Convert table to range. |
| Table total row | added (round 3) | Data > Table total row (or right-click in a table): adds "Total" plus SUBTOTAL(109,…) sums for number columns; right-click a total to switch to Average / Count / Count numbers / Max / Min / None. Saved as a native totals row (totalsRowCount, totalsRowFunction/Label) for new and opened tables. |
| PivotTable | added | PivotTable panel: rows, optional columns, several values (Sum / Count / Average / Min / Max), order A→Z or largest first. Saved as a **real Excel PivotTable** (pivot cache + records, refreshes when opened in Excel, field list works there). In the app it refreshes when you open its sheet, from the Refresh button, and on every save; the source grows with new rows. Simple PivotTables made in Excel are re-opened as editable ones; complex ones stay read-only and are kept as-is. The earlier "live formula summary" is still available. |
| PivotChart | added (round 3, as a bound chart) | "Chart" next to each PivotTable inserts a chart bound to the PivotTable's cells; it re-points itself whenever the PivotTable refreshes and is re-bound when the file is reopened. In the .xlsx it is a normal native chart over the PivotTable cells, not an Excel PivotChart object (a native PivotChart must name the workbook file in its source, which the app can't know at save time). |
| Get & Transform / external data connections | impossible | No network access to other hosts. |

## Conditional formatting

| Feature | Status | Notes |
|---|---|---|
| Highlight rules (>, <, between, =, ≠, contains, begins, blank, duplicates, unique, top/bottom N, above/below average, formula) | have | |
| ≥ / ≤, text ends with, date occurring (today, yesterday, last 7 days, this/last/next week and month) | added | Saved as Excel's own rule types. |
| Color scales | have + added | 8 presets (2- and 3-color); colors from files are kept. |
| Data bars | have | Color follows the chosen style. |
| Icon sets | added | Arrows, traffic lights, flags, symbols (3-icon sets, 33/67%); read from and written to .xlsx. |
| Edit a rule, reorder rules (priority), first rule wins | added | Click a rule to edit; ↑/↓ to reorder. Fixed: the app used to let the last rule win, opposite to Excel. |

## Charts and visuals

| Feature | Status | Notes |
|---|---|---|
| Column, bar, line, area, pie, doughnut, scatter | have | Written as native Excel charts. |
| Combo chart (columns + lines, optional second axis) | added | Native Excel combo; re-opened as editable. |
| Stacked and 100% stacked column / bar / line / area | added | |
| Edit a chart after inserting (data range, type, title, axis titles, legend position or none, data labels) | added | ✎ on the chart or double-click its title bar; changes apply live and are saved to the native chart. |
| Move / resize / delete chart, save chart as PNG | have | |
| Sparklines (line, column, win/loss, markers, color) | added | Insert > Sparklines…; saved as real Excel sparklines; sparklines in files are now shown and kept (they were dropped before). |
| Trendlines (linear, exponential, polynomial 2, moving average 2) and error bars (standard error, 5%, 1 standard deviation) | added (round 3) | Chart panel; drawn in the app and saved as native `c:trendline` / `c:errBars` (read back when reopened). As in Excel, trendlines are not offered on stacked or pie charts. "1 standard deviation" bars are drawn around each point (Excel draws them around the series mean). |
| Waterfall and funnel charts | added (round 3, built from stacked bars) | Waterfall: increases green, decreases red, rows labelled Total/Net/Ending… become total bars. Funnel: centered horizontal bars. Saved as native stacked column/bar charts with literal values, so Excel shows them correctly but they don't update if the data changes in Excel, and the app reopens them as kept-as-is charts. Excel's own waterfall/funnel (chartex) was not used: no tool here can validate it and Excel rejects malformed chartex parts. |
| Chart styles gallery, map charts | not added | Map charts need Bing geodata (no network). Existing ones in files are kept as-is. |

## View, keyboard, accessibility

| Feature | Status | Notes |
|---|---|---|
| Excel keyboard shortcuts | have + added | Added ⌘E, ⌘⇧X/Ctrl+5, ⌘⇧T/Alt+=, ⇧F2, ⌘9/⌘0 (+⇧), ⌘⇧7, ⌘⇧_, ⌘⇧V, ⌘\. |
| Status bar Sum / Average / Count / Min / Max | have | |
| Dark mode | have | |
| Narrow window (400 px) | have | New panels checked at 400 px. |

## Excel-file fidelity checked this round (saved by the app, read by openpyxl, re-opened in the app)

Hidden rows/columns, filter criteria + filterMode, tab color, gridlines off, zoom, frozen panes, icon sets, 2-/3-color scales, data bars, timePeriod and endsWith rules, list/whole/date validations with prompts and error messages, named ranges, notes, strikethrough and thick borders, a new Excel table with style, two native PivotTables (one with a column field, one with three value fields; 2,000 cache records each), stacked and combo charts, sparklines, a new picture next to a picture kept from the file. Re-saving a file the app created does not duplicate its PivotTables.

Round 3 additionally checked with openpyxl: row/column outline levels + sheetFormatPr outline levels, table totals row (totalsRowCount, totalsRowFunction="average", totalsRowLabel), PivotChart sheet, trendline/errBars on line and column charts, waterfall/funnel as stacked bar charts, timeline filter as AND custom filters, `_xlfn.GROUPBY(…,_xleta.SUM)`. Claude features were run against a test stub (Ask with tools: aggregate, writeCells, addHighlight, makeChart, then "Undo these changes"; AI column; Standardize values) plus Export .xlsx and Save as PDF through a stubbed downloads capability; no regressions. Fixed on the way: the AI column's default output name ("Category") silently overwrote an existing "Category" column; it now creates "Category 2".

Not verified: opening the files in desktop Excel itself (no Excel available to the test run; files were checked structurally with openpyxl and by re-opening in the app).
