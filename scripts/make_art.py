"""Generate the dot-grid "cw" logo.

Run from the repo root:  python3 scripts/make_art.py images
"""
import sys, os
out = sys.argv[1]

# ---- logo: "cw" on a 10x5 grid of cells ----
C = [".###", "#...", "#...", "#...", ".###"]
W = ["#...#", "#...#", "#.#.#", "#.#.#", ".#.#."]
rows = [c + "." + w for c, w in zip(C, W)]
maroon = ["#8c2a36", "#a5505b", "#c17d85"]   # dark -> light, ordered (not random)
blue = ["#4d719a", "#6d8fb5", "#94b0cf"]
s, r = 10, 4.2
cells = []
for y, row in enumerate(rows):
    for x, ch in enumerate(row):
        cx, cy = x * s + s / 2, y * s + s / 2
        if ch == "#":
            lx = x if x < 4 else x - 5                      # letter-local column
            t = (lx + y) / (7 if x < 4 else 8)              # 0 top-left -> 1 bottom-right
            col = (maroon if x < 4 else blue)[min(2, int(t * 3))]
            cells.append(f'<circle class="d" cx="{cx}" cy="{cy}" r="{r}" fill="{col}"/>')
        else:
            cells.append(f'<circle class="g" cx="{cx}" cy="{cy}" r="1.5" fill="#e6e0dc"/>')
vb = f'0 0 {len(rows[0])*s} {len(rows)*s}'
svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-label="CWan Lab">' + "".join(cells) + "</svg>"
open(os.path.join(out, "logo-cw.svg"), "w").write(svg)
# Inline copy for the page header: a faint static "ghost" of the letters plus the live
# cells, which burst outward on hover and spring back (see assets/js/site.js).
ghost = "".join(c.replace('class="d"', 'class="ghost"') for c in cells if 'class="d"' in c)
inline = (f'<svg class="logo-cw" viewBox="{vb}" overflow="visible" aria-hidden="true">'
          + "".join(c for c in cells if 'class="g"' in c)
          + f'<g opacity=".16">{ghost}</g>'
          + "".join(c for c in cells if 'class="d"' in c) + "</svg>\n")
open(os.path.join(out, "..", "_includes", "logo-cw.svg"), "w").write(inline)
