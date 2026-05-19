# infographics

Single-page infographics on physics, math, and adjacent topics — HTML + CSS + inline SVG, no build step.

[Japanese version](README.ja.md)

## Why this exists

I keep finding educational infographics with subtle (or not-so-subtle) physics errors. Rather than just complaining, this repo accumulates *corrected* versions, each in its own self-contained folder, with the corrections and citations documented in `NOTES.md`.

Open `<topic>/index.html` in a browser. That's it.

## Entries

- **[cosmology-history/](cosmology-history/)** — History of the universe (8 stages from inflation to today, with redshift / age / temperature / events). Corrects 3 physics errors + 3 numerical imprecisions from a circulating Japanese-language original. See [NOTES.md](cosmology-history/NOTES.md) for citations.

## What's where

- `<topic>/index.html` — the infographic itself, self-contained
- `<topic>/NOTES.md` — sources, corrections from the original, design rationale
- [CLAUDE.md](CLAUDE.md) — repo conventions (export pipeline, new-entry workflow)
- [DESIGN.md](DESIGN.md) — design system (color palette, typography, grid)

## Export

Headless Chromium renders to PDF / PNG:

```bash
chromium --headless --disable-gpu --print-to-pdf=out.pdf \
  --no-pdf-header-footer "file://$(pwd)/<topic>/index.html"
```

## License

Content (HTML / SVG / text): CC BY-SA 4.0
