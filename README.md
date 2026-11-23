# CWan Lab website (redesign, v1)

Redesign of [cwanlab.github.io](https://cwanlab.github.io). Plain Jekyll, built by GitHub Pages — no build step needed.

## Design

Layout and type follow the [Hao AI Lab](https://haoailab.com/) site (UC San Diego): system fonts,
one narrow column, a centred logo, the intro in a bracketed Georgia quote, one-line news, and a
light/dark toggle. The dot-grid "cw" logo (after the [UW IDL](https://idl.uw.edu/) mark) and its
maroon/blue colours are our own.

## Editing content

Almost everything lives in `_data/` — edit the YAML and push.

| What | File |
|---|---|
| News (homepage shows the latest 8) | `_data/news.yml` |
| Publications | `_data/publications.yml` |
| Research themes | `_data/research.yml` |
| Members & alumni | `_data/members.yml` (add `photo:` to replace initials) |
| Funding (shown on Research; sponsors line on Home) | `_data/funding.yml` |
| Talks & teaching | `talks.md` |
| Contact & openings | `contact.html` |
| PI bio / CV | `cv.md` |
| Site name, PI info, navigation | `_config.yml` |

To regenerate the logo:

```bash
python3 scripts/make_art.py images
```

## Preview locally

```bash
gem install jekyll jekyll-seo-tag jekyll-sitemap jekyll-redirect-from webrick
JEKYLL_NO_BUNDLER_REQUIRE=true jekyll serve
```

## Where it is served

`url` and `baseurl` are not set in `_config.yml`; GitHub Pages fills them in from the repository.
The same files therefore work in any repository of the lab account (served at
`cwanlab.github.io/<repo>/`) and in `cwanlab/cwanlab.github.io` itself.
