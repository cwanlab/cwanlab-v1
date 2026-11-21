"""Generate the dot-grid logo and the home-page banner.

Run from the repo root:  python3 scripts/make_art.py images
"""
import math, random, sys, os, re, zlib
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

# ---- theme illustrations for the home page ----
def field(w, h, centers, n, seed, cols, edge=40, stroke="#b3aaa5", m=14, accents=(), grid=10, sigma=None):
    rnd = random.Random(seed)
    sigma = sigma or min(w, h) / 5
    pts = []
    for cx, cy, ci in centers:
        for _ in range(n):
            rr = abs(rnd.gauss(0, sigma)); a = rnd.random() * 6.283
            x, y = cx + rr * math.cos(a), cy + rr * math.sin(a)
            if m < x < w - m and m < y < h - m:
                pts.append((x, y, ci if rnd.random() < .82 or not accents else rnd.choice(accents)))
    lines = []
    for i, (x, y, _) in enumerate(pts):
        for d, j in sorted((math.hypot(x - u, y - v), j) for j, (u, v, _) in enumerate(pts) if j != i)[:2]:
            if d < edge and i < j:
                lines.append(f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{pts[j][0]:.1f}" y2="{pts[j][1]:.1f}"/>')
    dots = [f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{rnd.choice([2.5,3.5,3.5,4.5,5.5,7])}" fill="{cols[c]}" fill-opacity="{rnd.choice([.7,.85,1])}"/>' for x, y, c in pts]
    lattice = "".join(f'<circle cx="{gx}" cy="{gy}" r=".9"/>' for gx in range(grid // 2, w, grid) for gy in range(grid // 2, h, grid))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid slice" aria-hidden="true">'
            f'<g fill="#ebe6e2">{lattice}</g>'
            f'<g stroke="{stroke}" stroke-opacity=".35" stroke-width="1" stroke-linecap="round">' + "".join(lines) + "</g>" + "".join(dots) + "</svg>")


def theme(name, cols, seed, centers, extra=""):
    svg = field(480, 300, centers, 20, seed, cols, edge=34, sigma=34, m=16)
    open(os.path.join(out, f"theme-{name}.svg"), "w").write(svg.replace("</svg>", extra + "</svg>"))

# graph learning: one connected network spanning the frame
theme("graph", ["#ecbfc3", "#d9a1a8", "#e2c7a8"], 51,
      [(90, 90, 0), (200, 170, 1), (310, 100, 0), (400, 210, 1), (140, 230, 2), (270, 240, 0)])
# spatial biology: a tumour niche with a dashed boundary, immune cells outside it
theme("spatial", ["#b2d0ed", "#8fb3d9", "#d8c3e5"], 52,
      [(190, 150, 0), (230, 170, 1), (160, 130, 0), (380, 90, 2), (400, 230, 2), (70, 250, 2)],
      '<ellipse cx="200" cy="152" rx="112" ry="84" fill="none" stroke="#8fb3d9" stroke-width="1.2" stroke-dasharray="3 5"/>')
# clinical AI: three data sources converging on one decision
hub = "".join(f'<line x1="{x}" y1="{y}" x2="372" y2="150" stroke="#86bba2" stroke-opacity=".55" stroke-width="1.2"/>' for x, y in [(110, 70), (90, 160), (120, 245)])
theme("clinical", ["#add7c4", "#e2c7a8", "#b2d0ed"], 53,
      [(110, 70, 0), (90, 160, 1), (120, 245, 2)],
      hub + '<circle cx="372" cy="150" r="15" fill="#fff" stroke="#86bba2" stroke-width="1.4"/><circle cx="372" cy="150" r="6.5" fill="#86bba2"/>')
