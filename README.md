# Xuanli Lin's academic website

Source for [xlin.io](https://xlin.io), migrated to the current [HugoBlox Academic CV template](https://hugoblox.com/templates/academic-cv).

## Build and preview

Requirements: **Hugo Extended 0.166.0**, **Node.js 22 or later**, and **Go** (deployment uses 1.27.1). Python 3 is used only for the output checker and the static preview below.

```sh
npm ci
npm run build
python scripts/check-site.py
python -m http.server 1313 --bind 127.0.0.1 --directory public
```

Open http://127.0.0.1:1313 to preview the complete production output, including search. `npm run build` regenerates `public/`, compiles Tailwind CSS, and indexes pages with Pagefind. Hugo fails on any warning, including path and translation warnings; warnings are not suppressed.

For live content/style editing, use `npm run dev`. Rebuild and use the static preview to test the production search index after content changes.

Netlify runs the same production build. Deploy previews and branch previews use their own base URL. The GitHub Actions workflow also builds with warnings treated as errors and checks generated links and metadata.

## Content and appearance

- `data/authors/xuanli.yaml`: profile using `hugoblox/author/v1`.
- `assets/media/authors/xuanli.jpg`: profile photograph.
- `content/_index.md`: homepage blocks and original section anchors.
- `content/publication/`: publications and their PDF, BibTeX, and slide bundles.
- `content/event/`: talks; existing `/talk/<title>/` URLs are preserved.
- `config/_default/params.yaml`: site settings under `hugoblox`, schema `2.0`.
- `data/themes/xlin.yaml`, `data/fonts/xlin.yaml`, `assets/css/custom.css`: original colors, Roboto/Montserrat typography, centered profile, and responsive two-column sections.

The dated biography, education, teaching history, publication status wording, and source files are preserved. This migration does not update the underlying CV facts.

### Current publication and event fields

Follow the official [publication example](https://github.com/HugoBlox/hugo-theme-academic-cv/blob/main/content/publications/conference-paper/index.md), [event example](https://github.com/HugoBlox/hugo-theme-academic-cv/blob/main/content/events/example/index.md), and [author example](https://github.com/HugoBlox/hugo-theme-academic-cv/blob/main/data/authors/me.yaml).

Publications use structured `publication.name` / `publication.short_name`, `hugoblox.ids.doi`, and typed `links`. A bundle's `<folder-name>.pdf` and `cite.bib` are discovered automatically; avoid declaring the same PDF a second time. Use bundle-relative filenames for slides so Hugo resolves the correct public URL.

Talks use `event_name`, `event_start`, `event_end`, and `event_all_day`. `date` is the page publication date, distinct from the talk's start time.

### Small local extensions

- `talk-summary` view retains talk dates, locations, summaries, and slide buttons.
- Author metadata highlights Xuanli Lin and keeps contribution notes without linking to unpublished author pages.
- The publication archive retains text, year, and publication-type filters, with all records available without JavaScript.
- A Pagefind hook includes abstracts and public metadata in site search, because the upstream template only marks titles and Markdown bodies for indexing.

## Upstream baseline

Migration checked against Academic CV commit `3aacb2ac2c3f6aeaecac4febe915c2fb30122903` (2026-09-13). Its [module pins](https://github.com/HugoBlox/hugo-theme-academic-cv/blob/3aacb2ac2c3f6aeaecac4febe915c2fb30122903/go.mod) use the latest framework module code, Blox `v0.0.0-20260527025321-61f41d3667f1`.

The template's minimum Hugo version is older than the installed version. Image settings and language configuration also use Hugo 0.166's current schema. Keep `go.sum` and `package-lock.json` committed for reproducible dependency resolution.
