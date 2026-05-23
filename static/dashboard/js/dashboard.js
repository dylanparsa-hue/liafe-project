(function () {
  'use strict';

  /* ── Auto-dismiss alerts ──────────────────────────────────── */
  document.querySelectorAll('.alert[data-autohide]').forEach(el => {
    setTimeout(() => {
      el.style.transition = 'opacity .4s';
      el.style.opacity = '0';
      setTimeout(() => el.remove(), 400);
    }, 4000);
  });

  /* ── Mobile sidebar toggle ────────────────────────────────── */
  const sidebarToggle = document.getElementById('sb-toggle');
  const sidebar       = document.querySelector('.db-sidebar');
  const overlay       = document.getElementById('sb-overlay');

  function openSidebar()  { sidebar?.classList.add('open'); overlay?.classList.add('show'); document.body.style.overflow = 'hidden'; }
  function closeSidebar() { sidebar?.classList.remove('open'); overlay?.classList.remove('show'); document.body.style.overflow = ''; }

  sidebarToggle?.addEventListener('click', openSidebar);
  overlay?.addEventListener('click', closeSidebar);

  /* ── Image preview on file input change ──────────────────── */
  document.querySelectorAll('input[type="file"][data-preview]').forEach(input => {
    const previewId = input.dataset.preview;
    const preview   = document.getElementById(previewId);
    if (!preview) return;
    input.addEventListener('change', () => {
      const file = input.files[0];
      if (file && file.type.startsWith('image/')) {
        const reader = new FileReader();
        reader.onload = e => { preview.src = e.target.result; preview.style.display = 'block'; };
        reader.readAsDataURL(file);
      }
    });
  });

  /* ── Delete confirmation inline ───────────────────────────── */
  document.querySelectorAll('[data-confirm]').forEach(btn => {
    btn.addEventListener('click', e => {
      const msg = btn.dataset.confirm || 'Are you sure?';
      if (!confirm(msg)) e.preventDefault();
    });
  });

})();
