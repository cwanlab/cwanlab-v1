# CWan Lab website (redesign, v1)

Redesign of [cwanlab.github.io](https://cwanlab.github.io). Plain Jekyll, built by GitHub Pages — no build step needed.

## Design

A blend of three lab sites:
[JHU LDR](https://jhuldr.github.io/) (Inter, intro beside a lab-photo slideshow, recruiting callout,
research directions on a line, news box, papers with a figure on the left),
[Hao AI Lab](https://haoailab.com/) (narrow column, one-line news, sponsors line) and
[Kai-Wei Chang's group at UCLA](https://web.cs.ucla.edu/~kwchang/) (topic tags on papers).
The dot-grid "cw" logo (after the [UW IDL](https://idl.uw.edu/) mark) and its maroon/blue colours are our own.

## Editing content

Almost everything lives in `_data/` — edit the YAML and push.

| What | File |
|---|---|
| News (home shows the latest 6, the rest fold away) | `_data/news.yml` |
| Lab photos (slideshow on Home and People) | `_data/photos.yml`, images in `images/lab/` |
| Publications (2026+ get `figure`, `figure_credit`, `tags`; figures in `images/papers/`) | `_data/publications.yml` |
| Research themes | `_data/research.yml` |
| Members & alumni | `_data/members.yml` (add `photo:` to replace initials) |
| Funding (shown on Research; sponsors line on Home) | `_data/funding.yml` |
| Talks & teaching | `talks.md` |
| Openings & contact | `openings.html` |
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
