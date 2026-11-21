# CWan Lab website (redesign)

Redesign of [cwanlab.github.io](https://cwanlab.github.io), served from
<https://tuner12.github.io/cwanlab.github.io/>. Plain Jekyll, built by GitHub Pages — no build step needed.

## Design

White paper, hairline rules, serif display type (Newsreader) over Lato, and one maroon accent.
The page structure follows the [Rajpurkar Lab](https://www.rajpurkarlab.hms.harvard.edu/) site;
the dot-grid "cw" logo (after the [UW IDL](https://idl.uw.edu/) mark) and the pastel cell
illustrations are our own.

## Editing content

Almost everything lives in `_data/` — edit the YAML and push.

| What | File |
|---|---|
| News (homepage shows the latest 6) | `_data/news.yml` |
| Publications | `_data/publications.yml` |
| Research themes & publication groups | `_data/research.yml` |
| Members & alumni | `_data/members.yml` (add `photo:` to replace initials) |
| Funding | `_data/funding.yml` |
| Talks & teaching | `talks.md` |
| PI bio / CV | `cv.md` |
| Site name, PI info, navigation | `_config.yml` |

To regenerate the logo and theme illustrations:

```bash
python3 scripts/make_art.py images
```

## Preview locally

```bash
gem install jekyll jekyll-seo-tag jekyll-sitemap jekyll-redirect-from webrick
JEKYLL_NO_BUNDLER_REQUIRE=true jekyll serve
```

## Moving this design to cwanlab/cwanlab.github.io

Set `url: "https://cwanlab.github.io"` and `baseurl: ""` in `_config.yml`. Nothing else changes.
