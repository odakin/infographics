# infographics

Single-page infographics (posters) on physics, math, and adjacent topics. Each one is typeset as an A4 PDF with LuaLaTeX + TikZ + pgfplots.

[Japanese version](README.ja.md)

## Why this exists

I keep finding educational infographics with subtle (or not-so-subtle) physics errors. Rather than just complaining, this repo accumulates *corrected* versions, each in its own self-contained folder, with the corrections and citations documented in `NOTES.md`.

## Entries

- **[cosmology-history/](cosmology-history/)** — Timeline of the history of the universe (9 stages from inflation to today, with redshift / age / temperature / events, plus a log-log plot of the energy densities of the main components). Corrects 3 physics errors + 3 numerical imprecisions from a circulating Japanese-language original. The poster is [cosmology-history.pdf](cosmology-history/cosmology-history.pdf); citations are in [NOTES.md](cosmology-history/NOTES.md).

## What's where

- `<topic>/<topic>.tex` — the infographic itself (LuaLaTeX); the built `<topic>.pdf` is the version to share
- `<topic>/NOTES.md` — sources, corrections from the original, design rationale
- `<topic>/index.html` — optional web version. For cosmology-history it is the second version from before the move to LaTeX and does not include later changes (the ninth stage, the redesigned density plot, etc.)
- [CLAUDE.md](CLAUDE.md) — repo conventions (build, new-entry workflow)
- [DESIGN.md](DESIGN.md) — design decisions and design system (color palette, typography, layout)

## Build

```bash
cd <topic>/
make        # PDF via lualatex
make png    # 300 DPI PNG for web sharing (needs poppler's pdftoppm)
```

The web version (`index.html`) can also be rendered to PDF / PNG with headless Chromium:

```bash
chromium --headless --disable-gpu --print-to-pdf=out.pdf \
  --no-pdf-header-footer "file://$(pwd)/<topic>/index.html"
```

## License

Content (TeX / HTML / SVG / text): CC BY-SA 4.0
