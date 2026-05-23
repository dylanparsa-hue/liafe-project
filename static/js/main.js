/* LIAFE — main.js */

// ── Navbar scroll effect ────────────────────────────────────────
const navbar = document.getElementById('mainNav');
if (navbar) {
  window.addEventListener('scroll', () => {
    navbar.classList.toggle('scrolled', window.scrollY > 50);
  }, { passive: true });
}

// ── Auto-dismiss alerts ─────────────────────────────────────────
document.querySelectorAll('.alert').forEach(alert => {
  setTimeout(() => {
    try { new bootstrap.Alert(alert).close(); } catch (_) {}
  }, 5000);
});

// ── Scroll reveal animations ────────────────────────────────────
const REVEAL_SELECTORS = [
  '.reveal',
  '.service-card',
  '.feature-card',
  '.pillar-card',
  '.pub-card',
  '.process-step',
  '.contact-info-card',
  '.contact-form-card',
  '.stat-tile',
  '.section-title',
  '.section-tag',
  '[data-reveal]',
];

const observerOptions = { threshold: 0.08, rootMargin: '0px 0px -40px 0px' };

const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const el = entry.target;
      const delay = el.dataset.delay || 0;
      setTimeout(() => el.classList.add('is-visible'), parseInt(delay));
      revealObserver.unobserve(el);
    }
  });
}, observerOptions);

function initReveal() {
  REVEAL_SELECTORS.forEach(sel => {
    document.querySelectorAll(sel).forEach((el, i) => {
      if (!el.classList.contains('no-reveal')) {
        el.classList.add('reveal-item');
        // stagger siblings inside the same parent row
        if (!el.dataset.delay) {
          const siblings = el.parentElement
            ? el.parentElement.querySelectorAll(sel)
            : [];
          const idx = [...siblings].indexOf(el);
          if (idx > 0) el.dataset.delay = idx * 80;
        }
        revealObserver.observe(el);
      }
    });
  });
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initReveal);
} else {
  initReveal();
}

// ── Smooth scroll for anchor links ─────────────────────────────
document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener('click', e => {
    const target = document.querySelector(a.getAttribute('href'));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
});

// ── Mobile nav: close on link click ────────────────────────────
document.querySelectorAll('#navbarNav .nav-link:not(.dropdown-toggle)').forEach(link => {
  link.addEventListener('click', () => {
    const collapse = document.querySelector('#navbarNav');
    if (collapse && collapse.classList.contains('show')) {
      new bootstrap.Collapse(collapse, { toggle: false }).hide();
    }
  });
});
