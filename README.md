# CWan Lab website (redesign, v1)

Redesign of [cwanlab.github.io](https://cwanlab.github.io). Plain Jekyll, built by GitHub Pages — no build step needed.

## Design

Clean white pages in Inter, soft rounded cards and pill tags, with the maroon/blue of the
dot-grid "cw" logo (after the [UW IDL](https://idl.uw.edu/) mark) as accents. Ideas borrowed from
[Stanford CRFM](https://crfm.stanford.edu/) (airy white space, soft grey text, small uppercase labels),
[Hao AI Lab](https://haoailab.com/) (quiet one-line news) and [JHU LDR](https://jhuldr.github.io/)
(each paper shown beside a figure from the paper).

Figure credits for paper images are kept in `_data/publications.yml` (`figure_credit`) and shown
as the image's hover text.

## Editing content

Almost everything lives in `_data/` — edit the YAML and push.

| What | File |
|---|---|
| News (home shows the latest 6; "Show all news" opens the rest) | `_data/news.yml` |
| Lab photos (banner on Home and People; `wide` is a 16:7 crop, `src` the 4:3 photo used on phones) | `_data/photos.yml`, images in `images/lab/` |
| Publications (2026+ get `figure`, `figure_credit`, `tags`; figures in `images/papers/`) | `_data/publications.yml` |
| Research themes (home cards use `short_title`, `home`, `image`) | `_data/research.yml` |
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
