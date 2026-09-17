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
- `assets/media/authors/xuanli.jpg`: active profile photograph. Replace this file to update the photo; the legacy `content/authors/xuanli/avatar.jpg` is no longer used by the theme. Rebuild with `npm run build`, then reload the preview.
- `content/_index.md`: homepage blocks and original section anchors.
- `content/publication/`: publications and their PDF, BibTeX, and slide bundles.
- `content/event/`: talks; existing `/talk/<title>/` URLs are preserved.
- `config/_default/params.yaml`: site settings under `hugoblox`, schema `2.0`.
- `data/themes/xlin.yaml`, `data/fonts/xlin.yaml`, `assets/css/custom.css`: original colors, Roboto/Montserrat typography, centered profile, and responsive two-column sections.

The dated biography, education, and teaching history are preserved. Publications and talks were reconciled with the complete Google Scholar profile in September 2026; see [publication sources and abstract verification](docs/publication-sources.md).

### Current publication and event fields

Follow the official [publication example](https://github.com/HugoBlox/hugo-theme-academic-cv/blob/main/content/publications/conference-paper/index.md), [event example](https://github.com/HugoBlox/hugo-theme-academic-cv/blob/main/content/events/example/index.md), and [author example](https://github.com/HugoBlox/hugo-theme-academic-cv/blob/main/data/authors/me.yaml).

Publications use structured `publication.name` / `publication.short_name`, `hugoblox.ids.doi`, and typed `links`. A bundle's `<folder-name>.pdf` and `cite.bib` are discovered automatically; avoid declaring the same PDF a second time. Use bundle-relative filenames for slides so Hugo resolves the correct public URL.

Every publication has a concise editorial `summary` in its front matter and the full original abstract under `## Abstract` in its Markdown body. Write the summary from the verified abstract; do not repeat it in an Overview section or store the full abstract in front matter. The summary appears in the page metadata and supplies previews and descriptions; both it and the full abstract are searchable. Source verification and any publisher-access fallbacks are recorded in [publication sources](docs/publication-sources.md), without a separate abstract-source line on the public pages.

Papers without a retrieved local PDF have `pdf_status: pending` and a visible availability note. To add a missing PDF, place it in the matching bundle, remove the pending status and link, and replace the availability note. Preprints and patent applications retain their own publication types.

Talks use `event_name`, `event_start`, `event_end`, and `event_all_day`. `date` is the page publication date, distinct from the talk's start time.

### Small local extensions

- `talk-summary` view retains talk dates, locations, summaries, and slide buttons.
- Author metadata highlights Xuanli Lin, preserves author order and contribution notes, and links recurring coauthors to their profiles. Ten coauthors have stored biographies and portraits, with eight currently public; Zhaofeng Zhang and Alena Chang are temporarily hidden. See [author sources and visibility settings](docs/author-sources.md). Profile data lives in `data/authors/`, portraits in `assets/media/authors/`, and author visibility settings in `content/authors/`. Publication and talk author lists use the matching profile slugs. Hidden or unprofiled authors retain their full names without links, portraits, or bio cards. Article structured data credits every author in order.
- The publication archive retains text, year, and publication-type filters, with all records available without JavaScript.
- Publication summaries and body abstracts are indexed directly by Pagefind. A hook also indexes public author/venue/tag metadata and event abstracts.

## Upstream baseline

Migration checked against Academic CV commit `3aacb2ac2c3f6aeaecac4febe915c2fb30122903` (2026-09-13). Its [module pins](https://github.com/HugoBlox/hugo-theme-academic-cv/blob/3aacb2ac2c3f6aeaecac4febe915c2fb30122903/go.mod) use the latest framework module code, Blox `v0.0.0-20260527025321-61f41d3667f1`.

The template's minimum Hugo version is older than the installed version. Image settings and language configuration also use Hugo 0.166's current schema. Keep `go.sum` and `package-lock.json` committed for reproducible dependency resolution.
