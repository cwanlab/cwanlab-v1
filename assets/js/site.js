// Light / dark theme toggle (the choice is remembered per browser).
document.querySelector('.theme-toggle')?.addEventListener('click', () => {
  const dark = document.documentElement.dataset.theme !== 'dark';
  if (dark) document.documentElement.dataset.theme = 'dark';
  else delete document.documentElement.dataset.theme;
  try { localStorage.setItem('theme', dark ? 'dark' : 'light'); } catch (e) {}
});

// Logo: a port of the idl.uw.edu mark, which is a tiny d3-force simulation.
// The cursor is a fixed node with charge -100 (acting between 10 and 40 screen px);
// every cell is tied to its home spot by a zero-length link of strength 0.3.
// Cells are pushed live while the pointer moves and spring home when it leaves.
// Constants and integration follow d3-force defaults so the feel matches.
const still = matchMedia('(prefers-reduced-motion: reduce)').matches;
document.querySelectorAll('.logo-cw').forEach((svg) => {
  if (still) return;
  const CHARGE = -100, DMIN = 10, DMAX = 40, LINK = 0.3;   // px, as on idl.uw.edu
  const ALPHA_MIN = 0.001, ALPHA_DECAY = 1 - ALPHA_MIN ** (1 / 300), KEEP = 0.6;
  const cells = [...svg.querySelectorAll('circle.d')].map((el) => {
    const hx = +el.getAttribute('cx'), hy = +el.getAttribute('cy');
    return { el, hx, hy, x: hx, y: hy, vx: 0, vy: 0 };
  });
  let px = 1;                          // screen px per viewBox unit
  let cx = 1e4, cy = 1e4, alpha = 0, running = false;

  const tick = () => {
    alpha += -alpha * ALPHA_DECAY;
    const s = CHARGE / (px * px), dmin2 = (DMIN / px) ** 2, dmax2 = (DMAX / px) ** 2;
    cells.forEach((c) => {
      // charge: only the cursor repels
      let x = cx - c.x, y = cy - c.y, l = x * x + y * y;
      if (l < dmax2) {
        if (l < dmin2) l = Math.sqrt(dmin2 * l) || 1e-6;
        const w = s * alpha / l;
        c.vx += x * w; c.vy += y * w;
      }
      // link: spring back to the home spot (fixed node, bias 0.5)
      x = c.hx - c.x - c.vx; y = c.hy - c.y - c.vy;
      if (x || y) { c.vx += x * alpha * LINK * 0.5; c.vy += y * alpha * LINK * 0.5; }
      c.x += (c.vx *= KEEP); c.y += (c.vy *= KEEP);
      // snap to whole screen pixels, like the original
      const dx = Math.round((c.x - c.hx) * px) / px, dy = Math.round((c.y - c.hy) * px) / px;
      c.el.setAttribute('transform', dx || dy ? `translate(${dx} ${dy})` : '');
    });
    if (alpha >= ALPHA_MIN) requestAnimationFrame(tick); else running = false;
  };

  const point = (x, y) => {
    cx = x; cy = y; alpha = 1;
    if (!running) { running = true; requestAnimationFrame(tick); }
  };
  const local = (e) => {
    const m = svg.getScreenCTM();
    px = m.a;
    return new DOMPoint(e.clientX, e.clientY).matrixTransform(m.inverse());
  };

  const host = svg.closest('a') || svg;
  host.addEventListener('pointermove', (e) => { const p = local(e); point(p.x, p.y); });
  host.addEventListener('pointerdown', (e) => { const p = local(e); point(p.x, p.y); });
  host.addEventListener('pointerout', () => point(1e4, 1e4));
});
