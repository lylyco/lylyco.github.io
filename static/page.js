(() => {
  'use strict';
  // Shared by the project pages: theme toggle, mobile menu, and section sizing.
  const root = document.documentElement;
  const $ = (s) => document.querySelector(s);
  const media = matchMedia('(prefers-color-scheme: dark)');
  const isDark = () => root.dataset.theme ? root.dataset.theme === 'dark' : media.matches;
  const syncThemeIcon = () => { if (isDark()) root.setAttribute('data-dark', ''); else root.removeAttribute('data-dark'); };
  try { const saved = localStorage.getItem('lc-theme'); if (saved) root.dataset.theme = saved; } catch (e) { /* storage unavailable */ }
  syncThemeIcon();
  media.addEventListener('change', syncThemeIcon);
  $('#themeToggle').addEventListener('click', () => {
    const next = isDark() ? 'light' : 'dark';
    root.dataset.theme = next;
    syncThemeIcon();
    try { localStorage.setItem('lc-theme', next); } catch (e) { /* ignore */ }
  });

  const sizeVars = () => {
    root.style.setProperty('--nav-h', `${$('.nav').offsetHeight}px`);
    root.style.setProperty('--footer-h', `${$('.footer').offsetHeight}px`);
  };
  sizeVars();
  addEventListener('resize', sizeVars);

  // Code snippets: show all / show less.
  document.querySelectorAll('.snippet').forEach((sn) => {
    const code = sn.querySelector('.snippet-code');
    const toggle = sn.querySelector('.snippet-toggle');
    toggle.addEventListener('click', () => {
      const open = code.classList.toggle('is-collapsed') === false;
      toggle.setAttribute('aria-expanded', String(open));
      toggle.textContent = open ? toggle.dataset.less : toggle.dataset.more;
      if (!open) sn.scrollIntoView({ block: 'nearest' });
    });
  });

  const navToggle = $('#navToggle'), navLinks = $('#navLinks');
  navToggle.addEventListener('click', () => {
    const open = navLinks.classList.toggle('open');
    navToggle.setAttribute('aria-expanded', String(open));
  });
})();
