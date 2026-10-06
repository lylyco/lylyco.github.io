(() => {
  'use strict';

  // Same query the Python build uses (build.py checks they match).
  const PAGE_QUERY = `query Portfolio {
  profile { name headlineLead headlineEmphasis summary industriesLine tags email photo { src thumb alt } links { label url kind } }
  about { title titleEmphasis paragraphs }
  platforms { id name blurb connectsTo }
  expertise { title body }
  projects { title titleEmphasis items { title summary url } }
  recommendations { title titleEmphasis source sourceLabel sourceUrl items { name photo title relationship date quote paragraphs } }
  contact { title titleEmphasis body }
  tagline
  footer { credit sourceLabel sourceUrl legal }
}`;

  const PREBUILT = window.__PORTFOLIO__ || null;   // set by build.py for static hosting
  const ENDPOINT = '/graphql';
  const $ = (s, r = document) => r.querySelector(s);
  const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const bold = (s) => esc(s).replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
  const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;

  // ---------- Icons (simple line drawings) ----------
  const ICON = {
    gear: '<circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M2 12h3M19 12h3M4.9 19.1 7 17M17 7l2.1-2.1"/>',
    target: '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/>',
    users: '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7M18 14.2A6.5 6.5 0 0 1 21.5 20"/>',
    flag: '<path d="M5 21V4"/><path d="M5 4h12l-2 4 2 4H5"/>',
    layers: '<path d="m12 3 9 5-9 5-9-5 9-5z"/><path d="m3 13 9 5 9-5"/>',
    box: '<path d="M3 7.5 12 3l9 4.5v9L12 21l-9-4.5v-9z"/><path d="M3 7.5 12 12l9-4.5M12 12v9"/>',
    compass: '<circle cx="12" cy="12" r="9"/><path d="m15.5 8.5-2 5-5 2 2-5 5-2z"/>',
    link: '<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1"/><path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/>',
    chart: '<path d="M4 20V4M4 20h16"/><path d="M8 16v-4M12 16V8M16 16v-6"/>',
    eye: '<path d="M2 12s3.6-7 10-7 10 7 10 7-3.6 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
    mail: '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>',
    linkedin: '<path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-4 0v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/>',
    github: '<path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/>',
  };
  const icon = (name) => `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${ICON[name] || ''}</svg>`;

  // ---------- GraphQL ----------
  async function gql(query, variables) {
    const t0 = performance.now();
    const res = await fetch(ENDPOINT, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query, variables }),
    });
    if (!res.ok) throw new Error(`Server returned ${res.status}`);
    const json = await res.json();
    if (json.errors) throw new Error(json.errors.map((e) => e.message).join('; '));
    return { data: json.data, ms: Math.round(performance.now() - t0) };
  }

  // ---------- Theme ----------
  const root = document.documentElement;
  const media = matchMedia('(prefers-color-scheme: dark)');
  const isDark = () => root.dataset.theme ? root.dataset.theme === 'dark' : media.matches;
  const syncThemeIcon = () => { if (isDark()) root.setAttribute('data-dark', ''); else root.removeAttribute('data-dark'); };
  try { const saved = localStorage.getItem('lc-theme'); if (saved) root.dataset.theme = saved; } catch (e) { /* storage unavailable */ }
  syncThemeIcon();
  media.addEventListener('change', syncThemeIcon);
  new MutationObserver(syncThemeIcon).observe(root, { attributes: true, attributeFilter: ['data-theme'] });
  $('#themeToggle').addEventListener('click', () => {
    const next = isDark() ? 'light' : 'dark';
    root.dataset.theme = next;
    try { localStorage.setItem('lc-theme', next); } catch (e) { /* ignore */ }
  });

  // ---------- Keep section sizing in step with the real nav/footer height ----------
  const sizeVars = () => {
    root.style.setProperty('--nav-h', `${$('.nav').offsetHeight}px`);
    root.style.setProperty('--footer-h', `${$('.footer').offsetHeight}px`);
  };
  sizeVars();
  addEventListener('resize', sizeVars);

  // ---------- Section arrows that go back to the profile ----------
  document.addEventListener('click', (e) => {
    const a = e.target.closest('[data-top]');
    if (!a) return;
    e.preventDefault();
    window.scrollTo({ top: 0, behavior: reduceMotion ? 'auto' : 'smooth' });
    history.replaceState(null, '', location.pathname + location.search);
  });

  // ---------- Logo: back to top ----------
  $('.nav-logo').addEventListener('click', (e) => {
    e.preventDefault();
    window.scrollTo({ top: 0, behavior: reduceMotion ? 'auto' : 'smooth' });
    history.replaceState(null, '', location.pathname + location.search);
  });

  // ---------- Mobile nav ----------
  const navToggle = $('#navToggle'), navLinks = $('#navLinks');
  navToggle.addEventListener('click', () => {
    const open = navLinks.classList.toggle('open');
    navToggle.setAttribute('aria-expanded', String(open));
  });
  navLinks.addEventListener('click', (e) => {
    if (e.target.closest('a')) { navLinks.classList.remove('open'); navToggle.setAttribute('aria-expanded', 'false'); }
  });

  // ---------- Render ----------
  let DATA = null;
  const bind = (key, value) => document.querySelectorAll(`[data-bind="${key}"]`).forEach((el) => { el.textContent = value; });

  function ctaButtons(profile) {
    const email = `<button type="button" class="btn btn-primary" data-copy="${esc(profile.email)}">${icon('mail')}<span>${esc(profile.email)}</span></button>`;
    const links = profile.links.map((l) =>
      `<a class="btn btn-ghost" href="${esc(l.url)}" target="_blank" rel="noopener">${icon(l.kind)}${esc(l.label)}</a>`).join('');
    return email + links;
  }

  function render(d) {
    const p = d.profile;
    bind('name', p.name);
    bind('headlineLead', p.headlineLead);
    bind('headlineEmphasis', p.headlineEmphasis);
    bind('summary', p.summary);
    bind('industriesLine', p.industriesLine);
    bind('aboutTitle', d.about.title);
    bind('aboutEmphasis', d.about.titleEmphasis);
    bind('contactTitle', d.contact.title);
    bind('contactEmphasis', d.contact.titleEmphasis);
    bind('contactBody', d.contact.body);
    const f = d.footer;
    $('.footer').innerHTML = `<p>${esc(f.credit)} <a href="${esc(f.sourceUrl)}" target="_blank" rel="noopener">${esc(f.sourceLabel)}</a></p>
      <p>${esc(f.legal)}</p>
      <a class="footer-logo" href="/"><img src="/static/img/logo.png" alt="LydiaCo, Los Angeles" width="118" height="118"></a>`;

    $('#tags').innerHTML = p.tags.map((t) => `<li class="tag">${esc(t)}</li>`).join('');
    $('#heroCta').innerHTML = ctaButtons(p);
    $('#contactCta').innerHTML = ctaButtons(p);

    $('#portrait').innerHTML = `<div class="portrait-frame"><img src="${esc(p.photo.src)}" alt="${esc(p.photo.alt)}" width="720" height="846" loading="lazy"></div>
      <figcaption><strong>${esc(p.name)}</strong>${esc(d.tagline)}</figcaption>`;
    $('#aboutText').innerHTML = d.about.paragraphs.map((t) => `<p>${bold(t)}</p>`).join('');

    $('#expertiseGrid').innerHTML = d.expertise.map((e) => `
      <article class="disco">
        <canvas aria-hidden="true"></canvas>
        <div class="disco-copy">
          <h3>${esc(e.title)}</h3>
          <p>${esc(e.body)}</p>
        </div>
      </article>`).join('');
    startDisco();

    bind('projectsTitle', d.projects.title);
    bind('projectsEmphasis', d.projects.titleEmphasis);
    $('#projectGrid').innerHTML = d.projects.items.map((pr) => `
      <article class="card project">
        <h3>${pr.url
          ? `<a class="project-link" href="${esc(pr.url)}">${esc(pr.title)}</a>`
          : `<span class="project-link is-soon">${esc(pr.title)}</span>`}</h3>
        <p>${esc(pr.summary)}</p>
        ${pr.url ? '' : '<span class="project-soon">Coming soon</span>'}
      </article>`).join('');

    const rec = d.recommendations;
    bind('recTitle', rec.title);
    bind('recEmphasis', rec.titleEmphasis);
    $('#recGrid').innerHTML = rec.items.map((r) => `
      <article class="rec">
        <blockquote class="rec-quote">${esc(r.quote)}</blockquote>
        <details class="rec-full">
          <summary>Read full recommendation</summary>
          ${r.paragraphs.map((t) => `<p>${esc(t)}</p>`).join('')}
        </details>
        <footer class="rec-by">
          <img class="rec-avatar" src="${esc(r.photo)}" alt="" width="40" height="40" loading="lazy">
          <span><strong>${esc(r.name)}</strong><span class="rec-meta">${esc(r.title)}</span><span class="rec-meta">${esc(r.relationship)} · ${esc(r.date)}</span></span>
        </footer>
      </article>`).join('');
    $('#recSource').innerHTML = `${esc(rec.source)} <a href="${esc(rec.sourceUrl)}" target="_blank" rel="noopener">${esc(rec.sourceLabel)} <span aria-hidden="true">↗</span></a>`;

    buildMap(d.platforms);
  }

  // ---------- Copy email ----------
  document.addEventListener('click', (e) => {
    const btn = e.target.closest('[data-copy]');
    if (!btn) return;
    const text = btn.dataset.copy, span = btn.querySelector('span');
    const done = () => {
      btn.classList.add('copied'); span.textContent = 'Copied!';
      setTimeout(() => { btn.classList.remove('copied'); span.textContent = text; }, 1800);
    };
    const selectFallback = () => {
      const r = document.createRange(); r.selectNodeContents(span);
      const sel = getSelection(); sel.removeAllRanges(); sel.addRange(r);
    };
    try {
      navigator.clipboard.writeText(text).then(done, selectFallback);
    } catch (err) { selectFallback(); }
  });

  // ---------- Card spotlight ----------
  document.addEventListener('pointermove', (e) => {
    const card = e.target.closest && e.target.closest('.card');
    if (!card) return;
    const r = card.getBoundingClientRect();
    card.style.setProperty('--mx', `${e.clientX - r.left}px`);
    card.style.setProperty('--my', `${e.clientY - r.top}px`);
  });

  // ---------- Expertise disco balls ----------
  let discoRaf = 0;
  function startDisco() {
    cancelAnimationFrame(discoRaf);
    const canvases = [...document.querySelectorAll('#expertiseGrid .disco canvas')];
    const hash = (a, b, c) => { const s = Math.sin(a * 127.1 + b * 311.7 + c * 74.7) * 43758.5453; return s - Math.floor(s); };
    const norm = (v) => { const m = Math.hypot(...v); return v.map((x) => x / m); };
    const L = norm([-0.45, 0.6, 0.66]), H = norm([L[0], L[1], L[2] + 1]);
    const visible = new Set();
    const io = new IntersectionObserver((es) => es.forEach((en) => en.isIntersecting ? visible.add(en.target) : visible.delete(en.target)));
    canvases.forEach((c) => io.observe(c));

    function draw(c, rot, seed, t) {
      const dpr = window.devicePixelRatio || 1, w = c.clientWidth;
      if (!w) return;
      const size = Math.round(w * dpr);
      if (c.width !== size) c.width = c.height = size;
      const ctx = c.getContext('2d'), cx = size / 2, cy = size / 2, R = size * 0.495;
      const dark = root.hasAttribute('data-dark');
      ctx.clearRect(0, 0, size, size);
      const g = ctx.createRadialGradient(cx - R * 0.35, cy - R * 0.4, R * 0.1, cx, cy, R);
      g.addColorStop(0, dark ? '#6b4a55' : '#d9c4cb'); g.addColorStop(1, dark ? '#2a1a20' : '#8c6b76');
      ctx.fillStyle = g; ctx.beginPath(); ctx.arc(cx, cy, R, 0, Math.PI * 2); ctx.fill();
      const P = (la, lo) => [cx + R * Math.cos(la) * Math.sin(lo), cy - R * Math.sin(la)];
      const bands = 18, glints = [];
      for (let b = 0; b < bands; b++) {
        const la0 = -Math.PI / 2 + b * Math.PI / bands, la1 = la0 + Math.PI / bands, lac = (la0 + la1) / 2;
        const n = Math.max(6, Math.round(36 * Math.cos(lac)));
        const dLa = (la1 - la0) * 0.07, step = Math.PI * 2 / n, dLo = step * 0.07;
        for (let k = 0; k < n; k++) {
          const lo0 = k * step + rot, lo1 = lo0 + step, loc = lo0 + step / 2;
          const nx = Math.cos(lac) * Math.sin(loc), ny = Math.sin(lac), nz = Math.cos(lac) * Math.cos(loc);
          if (nz < 0.01) continue;
          const rnd = hash(b, k, seed);
          const diff = Math.max(0, nx * L[0] + ny * L[1] + nz * L[2]);
          const spec = Math.pow(Math.max(0, nx * H[0] + ny * H[1] + nz * H[2]), 60);
          const tw = 0.5 + 0.5 * Math.sin(t * 1.6 + rnd * 40);
          let v = 0.42 + 0.38 * diff + 0.2 * (rnd - 0.5) + 0.08 * tw + spec * 0.6;
          v = Math.min(1, v * (0.55 + 0.45 * Math.sqrt(nz)));
          const rose = rnd > 0.85 ? 0.35 : 0;
          const s = dark ? 0.55 : 1;
          const r = Math.round((150 + 105 * v) * s), gg = Math.round((120 + 130 * v - rose * 60) * s), bb = Math.round((130 + 122 * v - rose * 40) * s);
          const a = P(la0 + dLa, lo0 + dLo), b2 = P(la0 + dLa, lo1 - dLo), c2 = P(la1 - dLa, lo1 - dLo), d = P(la1 - dLa, lo0 + dLo);
          ctx.fillStyle = `rgb(${r},${gg},${bb})`;
          ctx.beginPath(); ctx.moveTo(...a); ctx.lineTo(...b2); ctx.lineTo(...c2); ctx.lineTo(...d); ctx.closePath(); ctx.fill();
          if (!reduceMotion && (spec > 0.55 || (rnd > 0.975 && tw > 0.85 && nz > 0.3))) glints.push([...P(lac, loc), Math.max(spec, tw * 0.7)]);
        }
      }
      const rim = ctx.createRadialGradient(cx, cy, R * 0.7, cx, cy, R);
      rim.addColorStop(0, 'rgba(255,255,255,0)'); rim.addColorStop(1, dark ? 'rgba(255,255,255,0.12)' : 'rgba(255,255,255,0.35)');
      ctx.fillStyle = rim; ctx.beginPath(); ctx.arc(cx, cy, R, 0, Math.PI * 2); ctx.fill();
      glints.forEach(([x, y, s]) => {
        const len = (6 + 10 * s) * dpr;
        ctx.strokeStyle = `rgba(255,255,255,${0.5 + 0.5 * s})`; ctx.lineWidth = 1.2 * dpr;
        ctx.beginPath(); ctx.moveTo(x - len, y); ctx.lineTo(x + len, y); ctx.moveTo(x, y - len); ctx.lineTo(x, y + len); ctx.stroke();
        ctx.fillStyle = '#fff'; ctx.beginPath(); ctx.arc(x, y, 1.6 * dpr, 0, Math.PI * 2); ctx.fill();
      });
    }

    const t0 = performance.now();
    const frame = (now) => {
      const t = reduceMotion ? 0 : (now - t0) / 1000;
      canvases.forEach((c, i) => { if (reduceMotion || visible.has(c)) draw(c, t * 0.12 + i * 0.9, i, t); });
      if (!reduceMotion) discoRaf = requestAnimationFrame(frame);
    };
    canvases.forEach((c, i) => draw(c, i * 0.9, i, 0));
    discoRaf = requestAnimationFrame(frame);
    if (reduceMotion) {
      addEventListener('resize', () => canvases.forEach((c, i) => draw(c, i * 0.9, i, 0)));
      new MutationObserver(() => canvases.forEach((c, i) => draw(c, i * 0.9, i, 0))).observe(root, { attributes: true, attributeFilter: ['data-dark'] });
    }
  }

  // ---------- Systems map ----------
  const NS = 'http://www.w3.org/2000/svg';
  const el = (tag, attrs = {}, parent) => {
    const n = document.createElementNS(NS, tag);
    for (const k in attrs) n.setAttribute(k, attrs[k]);
    if (parent) parent.appendChild(n);
    return n;
  };
  function buildMap(platforms) {
    const svg = $('#systemsMap');
    svg.innerHTML = '';
    const cx = 220, cy = 200, rx = 160, ry = 138, R = 38;
    const pos = {};
    platforms.forEach((p, i) => {
      const a = (-90 + i * (360 / platforms.length)) * Math.PI / 180;
      pos[p.id] = { x: cx + rx * Math.cos(a), y: cy + ry * Math.sin(a) };
    });

    const gEdges = el('g', {}, svg), gPackets = el('g', {}, svg), gNodes = el('g', {}, svg);
    const edges = [];
    const addEdge = (a, b, ax, ay, bx, by, spoke) => {
      const line = el('line', { x1: ax, y1: ay, x2: bx, y2: by, class: 'edge' + (spoke ? ' spoke' : '') }, gEdges);
      edges.push({ a, b, ax, ay, bx, by, line, spoke });
    };
    platforms.forEach((p) => addEdge('hub', p.id, cx, cy, pos[p.id].x, pos[p.id].y, true));
    const seen = new Set();
    platforms.forEach((p) => p.connectsTo.forEach((q) => {
      const key = [p.id, q].sort().join('|');
      if (seen.has(key) || !pos[q]) return;
      seen.add(key);
      addEdge(p.id, q, pos[p.id].x, pos[p.id].y, pos[q].x, pos[q].y, false);
    }));

    // Hub: Lydia's photo at the center of the systems she connects
    const HR = 50;
    const hub = el('g', { class: 'hub' }, gNodes);
    const defs = el('defs', {}, svg);
    const clip = el('clipPath', { id: 'hubClip' }, defs);
    el('circle', { cx, cy, r: HR }, clip);
    el('circle', { cx, cy, r: HR, class: 'ring' }, hub);
    el('circle', { cx, cy, r: HR }, hub);
    const img = el('image', { x: cx - HR, y: cy - HR, width: HR * 2, height: HR * 2, 'clip-path': 'url(#hubClip)', preserveAspectRatio: 'xMidYMid slice' }, hub);
    img.setAttribute('href', DATA.profile.photo.thumb);
    el('title', {}, hub).textContent = DATA.profile.name;
    el('circle', { cx, cy, r: HR - 2, class: 'photo-ring' }, hub);
    el('circle', { cx, cy, r: HR + 1, class: 'photo-edge' }, hub);

    const nodes = {};
    platforms.forEach((p) => {
      const g = el('g', { class: 'node' }, gNodes);
      el('circle', { cx: pos[p.id].x, cy: pos[p.id].y, r: R }, g);
      el('text', { x: pos[p.id].x, y: pos[p.id].y + 4.5 }, g).textContent = p.name;
      el('title', {}, g).textContent = `${p.name}: ${p.blurb}`;
      nodes[p.id] = g;
      g.addEventListener('pointerenter', () => highlight(p.id));
    });
    svg.addEventListener('pointerleave', () => highlight(null));

    function highlight(id) {
      const linked = new Set(id ? [id] : []);
      edges.forEach((ed) => {
        const on = id && (ed.a === id || ed.b === id);
        ed.line.classList.toggle('on', !!on);
        if (on) { linked.add(ed.a); linked.add(ed.b); }
      });
      for (const k in nodes) {
        nodes[k].classList.toggle('on', k === id);
        nodes[k].classList.toggle('dim', !!id && !linked.has(k));
      }
    }

    // Data packets moving along the lines
    if (!reduceMotion) {
      const packets = Array.from({ length: 9 }, () => ({ dot: el('circle', { r: 3, class: 'packet' }, gPackets), e: null, t: 0, v: 0 }));
      const pick = (pk) => {
        pk.e = edges[Math.floor(Math.random() * edges.length)];
        pk.t = 0; pk.v = 0.004 + Math.random() * 0.006; pk.rev = Math.random() < 0.5;
      };
      packets.forEach((pk) => { pick(pk); pk.t = Math.random(); });
      let last = performance.now();
      const tick = (now) => {
        const dt = Math.min(50, now - last) / 16.7; last = now;
        packets.forEach((pk) => {
          pk.t += pk.v * dt;
          if (pk.t >= 1) pick(pk);
          const t = pk.rev ? 1 - pk.t : pk.t;
          const ed = pk.e;
          pk.dot.setAttribute('cx', ed.ax + (ed.bx - ed.ax) * t);
          pk.dot.setAttribute('cy', ed.ay + (ed.by - ed.ay) * t);
          pk.dot.setAttribute('opacity', Math.sin(pk.t * Math.PI).toFixed(2));
        });
        requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
    }
  }

  // ---------- Boot ----------
  async function boot() {
    try {
      DATA = PREBUILT || (await gql(PAGE_QUERY)).data;
      render(DATA);
      sizeVars();
    } catch (err) {
      console.error(`Could not load content: ${err.message}. Is the Python server running?`);
    }
  }
  boot();
})();
