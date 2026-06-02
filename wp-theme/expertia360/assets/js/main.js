(function () {
  'use strict';

  /* -------------------------------------------------------
     Dynamic date in top bar (backup for PHP rendering)
     ------------------------------------------------------- */
  const dateEls = document.querySelectorAll('.top-bar__date');
  if (dateEls.length) {
    const now = new Date();
    const formatted = now.toLocaleDateString('es-MX', {
      day: 'numeric', month: 'long', year: 'numeric'
    });
    dateEls.forEach(el => {
      if (el.textContent.trim() === '') {
        el.textContent = 'Actualizado: ' + formatted;
      }
    });
  }

  /* -------------------------------------------------------
     Mobile navigation toggle
     ------------------------------------------------------- */
  const toggle = document.querySelector('.nav-toggle');
  const navPrimary = document.querySelector('.nav-primary');
  const navSecondary = document.querySelector('.nav-secondary');
  const activeNav = navPrimary || navSecondary;

  if (toggle && activeNav) {
    toggle.addEventListener('click', function () {
      const isOpen = activeNav.classList.toggle('is-open');
      this.setAttribute('aria-expanded', String(isOpen));
    });

    // Close on outside click
    document.addEventListener('click', function (e) {
      if (!e.target.closest('.site-header')) {
        activeNav.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });
  }

  /* -------------------------------------------------------
     Smooth scroll to #newsletter on "Suscríbete" click
     ------------------------------------------------------- */
  document.querySelectorAll('a[href="#newsletter"]').forEach(function (link) {
    link.addEventListener('click', function (e) {
      const target = document.getElementById('newsletter');
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        const input = target.querySelector('input[type="email"]');
        if (input) setTimeout(function () { input.focus(); }, 600);
      }
    });
  });

  /* -------------------------------------------------------
     Load more (AJAX) – archive pages
     ------------------------------------------------------- */
  const loadMoreBtn = document.getElementById('load-more-btn');
  const postsGrid   = document.getElementById('posts-grid');

  if (loadMoreBtn && postsGrid) {
    loadMoreBtn.addEventListener('click', function () {
      const page     = parseInt(this.dataset.page,  10);
      const maxPages = parseInt(this.dataset.max,   10);
      const cat      = parseInt(this.dataset.cat,   10) || 0;

      loadMoreBtn.disabled    = true;
      loadMoreBtn.textContent = 'Cargando…';

      const body = new URLSearchParams({
        action : 'expertia360_load_more',
        nonce  : expertia360.nonce,
        page   : page,
        cat    : cat,
      });

      fetch(expertia360.ajaxUrl, {
        method  : 'POST',
        headers : { 'Content-Type': 'application/x-www-form-urlencoded' },
        body    : body.toString(),
      })
        .then(function (r) { return r.json(); })
        .then(function (data) {
          if (data.success && data.data.html) {
            // Append new cards
            const temp = document.createElement('div');
            temp.innerHTML = data.data.html;
            while (temp.firstChild) {
              postsGrid.appendChild(temp.firstChild);
            }

            const nextPage = page + 1;
            loadMoreBtn.dataset.page = nextPage;

            if (nextPage > data.data.max_pages) {
              loadMoreBtn.style.display = 'none';
            } else {
              loadMoreBtn.disabled    = false;
              loadMoreBtn.textContent = 'Ver más';
            }
          } else {
            loadMoreBtn.style.display = 'none';
          }
        })
        .catch(function () {
          loadMoreBtn.disabled    = false;
          loadMoreBtn.textContent = 'Ver más';
        });
    });
  }

})();
