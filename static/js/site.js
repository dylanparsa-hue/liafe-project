(function () {
  'use strict';

  /* ── Reveal on scroll ──────────────────────────────────────── */
  const io = ('IntersectionObserver' in window)
    ? new IntersectionObserver(
        (entries) => entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }),
        { threshold: 0.1, rootMargin: '0px 0px -40px 0px' }
      )
    : null;

  document.querySelectorAll('.reveal-js').forEach(el => io ? io.observe(el) : el.classList.add('in'));

  /* ── Mobile menu ───────────────────────────────────────────── */
  const menuBtn  = document.getElementById('menu-btn');
  const mobileMenu = document.getElementById('mobile-menu');
  const menuIconOpen  = document.getElementById('menu-icon-open');
  const menuIconClose = document.getElementById('menu-icon-close');

  if (menuBtn && mobileMenu) {
    menuBtn.addEventListener('click', () => {
      const isOpen = mobileMenu.classList.toggle('open');
      document.body.style.overflow = isOpen ? 'hidden' : '';
      if (menuIconOpen)  menuIconOpen.style.display  = isOpen ? 'none'         : 'block';
      if (menuIconClose) menuIconClose.style.display = isOpen ? 'block'        : 'none';
    });

    mobileMenu.querySelectorAll('a').forEach(a => {
      a.addEventListener('click', () => {
        mobileMenu.classList.remove('open');
        document.body.style.overflow = '';
        if (menuIconOpen)  menuIconOpen.style.display  = 'block';
        if (menuIconClose) menuIconClose.style.display = 'none';
      });
    });
  }

  /* ── Services dropdown ──────────────────────────────────────── */
  const dropdowns = document.querySelectorAll('.dropdown');

  dropdowns.forEach(dd => {
    const trigger = dd.querySelector('.dropdown-toggle');
    const menu    = dd.querySelector('.dropdown-menu');
    let closeTimer;

    const open          = () => { clearTimeout(closeTimer); dd.classList.add('open'); };
    const scheduleClose = () => { closeTimer = setTimeout(() => dd.classList.remove('open'), 300); };

    // Hover: attach to trigger AND menu separately so crossing the gap cancels the timer
    if (trigger) {
      trigger.addEventListener('mouseenter', open);
      trigger.addEventListener('mouseleave', scheduleClose);
      trigger.addEventListener('click', e => { e.stopPropagation(); dd.classList.toggle('open'); });
    }
    if (menu) {
      menu.addEventListener('mouseenter', open);
      menu.addEventListener('mouseleave', scheduleClose);
    }

    // Keyboard
    dd.addEventListener('focusin',  open);
    dd.addEventListener('focusout', e => { if (!dd.contains(e.relatedTarget)) scheduleClose(); });
  });

  // Close on outside click
  document.addEventListener('click', e => {
    dropdowns.forEach(dd => { if (!dd.contains(e.target)) dd.classList.remove('open'); });
  });

  /* ── Hero Slideshow ────────────────────────────────────────── */
  const slider = document.getElementById('heroSlider');
  if (slider) {
    const bgs      = slider.querySelectorAll('.hs-bg');
    const contents = document.querySelectorAll('.hs-content');
    const dots     = document.querySelectorAll('.hs-dot');
    const total    = bgs.length;
    let current    = 0;
    let autoTimer;

    const goTo = (index) => {
      bgs[current].classList.remove('active');
      contents[current] && contents[current].classList.remove('active');
      dots[current]     && dots[current].classList.remove('active');
      current = ((index % total) + total) % total;
      bgs[current].classList.add('active');
      contents[current] && contents[current].classList.add('active');
      dots[current]     && dots[current].classList.add('active');
    };

    const startAuto = () => {
      clearInterval(autoTimer);
      if (total > 1) autoTimer = setInterval(() => goTo(current + 1), 5500);
    };

    document.querySelector('.hs-next')?.addEventListener('click', () => { goTo(current + 1); startAuto(); });
    document.querySelector('.hs-prev')?.addEventListener('click', () => { goTo(current - 1); startAuto(); });
    dots.forEach((dot, i) => dot.addEventListener('click', () => { goTo(i); startAuto(); }));

    // Pause on hover
    const heroSection = document.getElementById('heroSection');
    heroSection?.addEventListener('mouseenter', () => clearInterval(autoTimer));
    heroSection?.addEventListener('mouseleave', startAuto);

    startAuto();
  }

  /* ── Smooth scroll for hash links ──────────────────────────── */
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
      const target = document.querySelector(a.getAttribute('href'));
      if (target) { e.preventDefault(); target.scrollIntoView({ behavior: 'smooth', block: 'start' }); }
    });
  });

  /* ── Contact/inquiry form: mark read on admin open ─────────── */
  /* (handled server-side via form save) */

})();
