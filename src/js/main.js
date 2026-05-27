import { animate, inView, scroll, stagger } from 'motion'

/* ══════════════════════════════════════════════
   NAVIGATION
══════════════════════════════════════════════ */
const NAV_LINKS = [
  {
    label: 'Soluciones',
    children: [
      { label: 'Refrigeración', href: '/refrigeracion.html', icon: snowflakeIcon() },
      { label: 'Congelación',   href: '/congelacion.html',  icon: thermIcon()    },
      { label: 'Mantenimiento', href: '/mantenimiento.html', icon: wrenchIcon()   },
      { label: 'Refacciones',   href: '/refacciones.html',  icon: boxIcon()      },
    ],
  },
  {
    label: 'Empresa',
    children: [
      { label: 'Nosotros', href: '/nosotros.html',  icon: teamIcon()   },
      { label: 'Sectores', href: '/sectores.html',  icon: gridIcon()   },
      { label: 'Servicios',href: '/servicios.html', icon: listIcon()   },
    ],
  },
  { label: 'Contacto', href: '/contacto.html' },
]

function logoSVG() {
  return `<svg width="32" height="32" viewBox="0 0 32 32" fill="none" aria-hidden="true">
    <rect width="32" height="32" rx="8" fill="#0369A1"/>
    <path d="M16 5v22M5 16h22M9.1 9.1l13.8 13.8M22.9 9.1L9.1 22.9" stroke="white" stroke-width="2.2" stroke-linecap="round"/>
    <circle cx="16" cy="16" r="2.5" fill="white"/>
  </svg>`
}

function chevronDown() {
  return `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="transition-transform duration-200 group-open:rotate-180"><path d="M6 9l6 6 6-6"/></svg>`
}

function snowflakeIcon() {
  return `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M12 2v20M2 12h20M5 5l14 14M19 5L5 19"/><circle cx="12" cy="12" r="2"/></svg>`
}
function thermIcon() {
  return `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M14 14.76V3.5a2.5 2.5 0 0 0-5 0v11.26a4.5 4.5 0 1 0 5 0z"/></svg>`
}
function wrenchIcon() {
  return `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>`
}
function boxIcon() {
  return `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/></svg>`
}
function teamIcon() {
  return `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/></svg>`
}
function gridIcon() {
  return `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>`
}
function listIcon() {
  return `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/><line x1="8" y1="18" x2="21" y2="18"/><line x1="3" y1="6" x2="3.01" y2="6"/><line x1="3" y1="12" x2="3.01" y2="12"/><line x1="3" y1="18" x2="3.01" y2="18"/></svg>`
}
function menuIcon() {
  return `<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>`
}
function closeIcon() {
  return `<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>`
}

function buildDesktopNav() {
  return NAV_LINKS.map(link => {
    if (link.children) {
      return `
        <div class="relative group">
          <button class="nav-link flex items-center gap-1.5 py-2">
            ${link.label} ${chevronDown()}
          </button>
          <div class="absolute top-full left-1/2 -translate-x-1/2 pt-3 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 z-50">
            <div class="bg-white border border-navy-200 rounded-xl shadow-lg p-2 min-w-[200px]">
              ${link.children.map(c => `
                <a href="${c.href}" class="dropdown-item">
                  <span class="text-polar-700">${c.icon}</span>
                  ${c.label}
                </a>`).join('')}
            </div>
          </div>
        </div>`
    }
    return `<a href="${link.href}" class="nav-link py-2">${link.label}</a>`
  }).join('')
}

function buildMobileNav() {
  return NAV_LINKS.map(link => {
    if (link.children) {
      return `
        <div>
          <p class="text-xs font-semibold tracking-widest text-navy-400 uppercase px-1 mb-2">${link.label}</p>
          ${link.children.map(c => `
            <a href="${c.href}" class="flex items-center gap-3 px-2 py-2.5 text-sm font-medium text-navy-700 hover:text-polar-700 rounded-lg hover:bg-polar-50 transition-colors">
              <span class="text-polar-600">${c.icon}</span>${c.label}
            </a>`).join('')}
        </div>`
    }
    return `<a href="${link.href}" class="block px-2 py-2.5 text-sm font-medium text-navy-700 hover:text-polar-700">${link.label}</a>`
  }).join('')
}

export function initNav() {
  const placeholder = document.getElementById('nav-placeholder')
  if (!placeholder) return

  placeholder.outerHTML = `
    <header id="site-header" class="fixed top-0 inset-x-0 z-40 bg-white/95 backdrop-blur-sm border-b border-navy-200">
      <div class="container mx-auto">
        <div class="flex items-center justify-between h-20">

          <!-- Logo -->
          <a href="/index.html" class="flex items-center gap-3 flex-shrink-0">
            ${logoSVG()}
            <div>
              <span class="text-lg font-bold text-navy-900 leading-none block">Polar Construct</span>
              <span class="text-xs text-navy-500 leading-none">Refrigeración Industrial</span>
            </div>
          </a>

          <!-- Desktop links -->
          <nav class="hidden lg:flex items-center gap-8" aria-label="Navegación principal">
            ${buildDesktopNav()}
          </nav>

          <!-- Desktop CTA -->
          <div class="hidden lg:flex items-center gap-3">
            <a href="/contacto.html" class="btn-primary">Cotizar ahora</a>
          </div>

          <!-- Mobile toggle -->
          <button id="mobile-toggle" class="lg:hidden p-2 -mr-2 text-navy-700 hover:text-polar-700 cursor-pointer" aria-label="Abrir menú" aria-expanded="false">
            <span id="toggle-icon">${menuIcon()}</span>
          </button>
        </div>
      </div>

      <!-- Mobile menu -->
      <div id="mobile-menu" class="hidden lg:hidden border-t border-navy-200 bg-white">
        <div class="container mx-auto py-6 space-y-4">
          ${buildMobileNav()}
          <div class="pt-4 border-t border-navy-200">
            <a href="/contacto.html" class="btn-primary w-full justify-center">Cotizar ahora</a>
          </div>
        </div>
      </div>
    </header>
    <div class="h-20"></div>`

  // Mobile toggle
  const toggle = document.getElementById('mobile-toggle')
  const menu   = document.getElementById('mobile-menu')
  const icon   = document.getElementById('toggle-icon')
  let open = false

  toggle?.addEventListener('click', () => {
    open = !open
    menu.classList.toggle('hidden', !open)
    icon.innerHTML = open ? closeIcon() : menuIcon()
    toggle.setAttribute('aria-expanded', String(open))
  })

  // Scroll shadow
  const header = document.getElementById('site-header')
  window.addEventListener('scroll', () => {
    header?.classList.toggle('shadow-sm', window.scrollY > 8)
  }, { passive: true })
}

/* ══════════════════════════════════════════════
   FOOTER
══════════════════════════════════════════════ */
export function initFooter() {
  const placeholder = document.getElementById('footer-placeholder')
  if (!placeholder) return

  placeholder.outerHTML = `
    <footer class="bg-navy-900 text-navy-400">
      <div class="container mx-auto">

        <!-- Top grid -->
        <div class="grid grid-cols-2 md:grid-cols-4 gap-10 py-16 border-b border-navy-700">

          <!-- Brand -->
          <div class="col-span-2 md:col-span-1">
            <a href="/index.html" class="flex items-center gap-3 mb-4">
              ${logoSVG()}
              <span class="text-white font-bold text-base">Polar Construct</span>
            </a>
            <p class="text-sm leading-relaxed mb-6">Diseñamos y fabricamos cámaras de refrigeración y congelación llave en mano para la industria alimentaria.</p>
            <div class="flex gap-3">
              <a href="https://facebook.com" target="_blank" rel="noopener" class="p-2 border border-navy-700 rounded-lg hover:border-polar-600 hover:text-polar-400 transition-colors" aria-label="Facebook">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg>
              </a>
              <a href="https://linkedin.com" target="_blank" rel="noopener" class="p-2 border border-navy-700 rounded-lg hover:border-polar-600 hover:text-polar-400 transition-colors" aria-label="LinkedIn">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6zM2 9h4v12H2z"/><circle cx="4" cy="4" r="2"/></svg>
              </a>
            </div>
          </div>

          <!-- Soluciones -->
          <div>
            <p class="text-white font-semibold text-sm mb-4">Soluciones</p>
            <ul class="space-y-2.5 text-sm">
              ${[['Refrigeración','/refrigeracion.html'],['Congelación','/congelacion.html'],['Mantenimiento','/mantenimiento.html'],['Refacciones','/refacciones.html']].map(([l,h])=>`<li><a href="${h}" class="hover:text-white transition-colors">${l}</a></li>`).join('')}
            </ul>
          </div>

          <!-- Empresa -->
          <div>
            <p class="text-white font-semibold text-sm mb-4">Empresa</p>
            <ul class="space-y-2.5 text-sm">
              ${[['Nosotros','/nosotros.html'],['Sectores','/sectores.html'],['Servicios','/servicios.html'],['Contacto','/contacto.html'],['Legal','/legal.html']].map(([l,h])=>`<li><a href="${h}" class="hover:text-white transition-colors">${l}</a></li>`).join('')}
            </ul>
          </div>

          <!-- Contacto -->
          <div>
            <p class="text-white font-semibold text-sm mb-4">Información</p>
            <ul class="space-y-3 text-sm">
              <li class="flex items-start gap-2">
                <svg class="mt-0.5 flex-shrink-0 text-polar-500" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
                <a href="mailto:info@polarconstruct.com" class="hover:text-white transition-colors">info@polarconstruct.com</a>
              </li>
              <li class="flex items-start gap-2">
                <svg class="mt-0.5 flex-shrink-0 text-polar-500" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
                <a href="tel:+56912345678" class="hover:text-white transition-colors">+56 9 1234 5678</a>
              </li>
              <li class="flex items-start gap-2">
                <svg class="mt-0.5 flex-shrink-0 text-polar-500" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
                <span>Av. Industrial 1250, Santiago</span>
              </li>
              <li class="flex items-start gap-2">
                <svg class="mt-0.5 flex-shrink-0 text-polar-500" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
                <span>Lun–Vie 8:00–18:00</span>
              </li>
            </ul>
          </div>
        </div>

        <!-- Newsletter -->
        <div class="py-10 border-b border-navy-700">
          <div class="max-w-xl">
            <p class="text-white font-semibold mb-1">Mantente informado</p>
            <p class="text-sm mb-4">Recibe novedades sobre soluciones de refrigeración y actualizaciones de nuestros servicios.</p>
            <form class="flex gap-3" onsubmit="return false">
              <input type="email" placeholder="Tu correo electrónico" class="flex-1 px-4 py-2.5 text-sm bg-navy-700 border border-navy-600 rounded-lg text-white placeholder:text-navy-400 focus:outline-none focus:border-polar-500" aria-label="Correo electrónico">
              <button type="submit" class="px-5 py-2.5 bg-polar-700 text-white text-sm font-semibold rounded-lg hover:bg-polar-800 transition-colors cursor-pointer flex-shrink-0">Suscribirse</button>
            </form>
            <p class="text-xs mt-2">Al suscribirte aceptas nuestra <a href="/legal.html" class="text-polar-400 hover:text-polar-300 underline">política de privacidad</a>.</p>
          </div>
        </div>

        <!-- Bottom bar -->
        <div class="flex flex-col sm:flex-row items-center justify-between gap-4 py-6 text-xs">
          <p>© ${new Date().getFullYear()} Polar Construct. Todos los derechos reservados.</p>
          <div class="flex gap-6">
            <a href="/legal.html" class="hover:text-white transition-colors">Política de privacidad</a>
            <a href="/legal.html" class="hover:text-white transition-colors">Términos de servicio</a>
            <a href="/legal.html" class="hover:text-white transition-colors">Cookies</a>
          </div>
        </div>
      </div>
    </footer>`
}

/* ══════════════════════════════════════════════
   ANIMATIONS (Motion.js)
══════════════════════════════════════════════ */
export function initAnimations() {
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches
  if (reduced) return

  // ── Scroll progress bar ──────────────────────
  const bar = document.createElement('div')
  bar.setAttribute('aria-hidden', 'true')
  Object.assign(bar.style, {
    position: 'fixed', top: '0', left: '0', right: '0', height: '3px',
    background: 'linear-gradient(to right, #0369A1, #0EA5E9)',
    transformOrigin: '0 0', transform: 'scaleX(0)', zIndex: '9999',
    pointerEvents: 'none',
  })
  document.body.appendChild(bar)
  scroll(animate(bar, { scaleX: [0, 1] }))

  // ── Standard reveal-up (spring deceleration) ─
  inView('.reveal-up', ({ target }) => {
    animate(target, { opacity: [0, 1], y: [48, 0] }, {
      duration: 0.7, easing: [0.16, 1, 0.3, 1],
    })
  }, { margin: '0px 0px -80px 0px' })

  // ── Reveal from left (2-col left side) ───────
  inView('.reveal-left', ({ target }) => {
    animate(target, { opacity: [0, 1], x: [-64, 0] }, {
      duration: 0.75, easing: [0.16, 1, 0.3, 1],
    })
  }, { margin: '0px 0px -80px 0px' })

  // ── Reveal from right (2-col right side) ─────
  inView('.reveal-right', ({ target }) => {
    animate(target, { opacity: [0, 1], x: [64, 0] }, {
      duration: 0.75, easing: [0.16, 1, 0.3, 1],
    })
  }, { margin: '0px 0px -80px 0px' })

  // ── Scale-in (for dashboard panels) ──────────
  inView('.reveal-scale', ({ target }) => {
    animate(target, { opacity: [0, 1], scale: [0.88, 1] }, {
      duration: 0.65, easing: [0.16, 1, 0.3, 1],
    })
  }, { margin: '0px 0px -80px 0px' })

  // ── Section labels: spring bounce pop ────────
  inView('.section-label', ({ target }) => {
    animate(target, { opacity: [0, 1], scale: [0.7, 1], y: [10, 0] }, {
      duration: 0.4, easing: [0.34, 1.56, 0.64, 1],
    })
  }, { margin: '0px 0px -40px 0px' })

  // ── Stagger card groups (more dramatic) ──────
  inView('.stagger-group', ({ target }) => {
    animate(target.querySelectorAll('.stagger-item'),
      { opacity: [0, 1], y: [44, 0], scale: [0.94, 1] },
      { duration: 0.6, delay: stagger(0.09), easing: [0.16, 1, 0.3, 1] }
    )
  }, { margin: '0px 0px -60px 0px' })

  // ── Continuous float on hero badges ──────────
  document.querySelectorAll('.float-badge').forEach((el, i) => {
    animate(el, { y: [0, -12, 0] }, {
      duration: 3 + i * 0.9,
      repeat: Infinity,
      easing: 'ease-in-out',
    })
  })

  // ── Pulsing status dots ───────────────────────
  document.querySelectorAll('.status-dot').forEach(el => {
    animate(el, { opacity: [1, 0.35, 1], scale: [1, 1.5, 1] }, {
      duration: 2.5, repeat: Infinity, easing: 'ease-in-out',
    })
  })

  // ── Animated progress bars ───────────────────
  document.querySelectorAll('.animated-bar').forEach(el => { el.style.width = '0' })
  inView('.animated-bar', ({ target }) => {
    animate(target, { width: `${target.dataset.w ?? 50}%` }, {
      duration: 1.3, delay: 0.4, easing: [0.16, 1, 0.3, 1],
    })
  })

  // ── Hero visual parallax ─────────────────────
  const heroVis = document.querySelector('.hero-visual')
  if (heroVis) {
    const section = heroVis.closest('section')
    if (section) {
      scroll(animate(heroVis, { y: [0, 36] }), {
        target: section, offset: ['start start', 'end start'],
      })
    }
  }

  // ── Magnetic CTA buttons ─────────────────────
  document.querySelectorAll('.btn-primary').forEach(btn => {
    btn.addEventListener('mousemove', e => {
      const r = btn.getBoundingClientRect()
      animate(btn,
        { x: (e.clientX - r.left - r.width / 2) * 0.22, y: (e.clientY - r.top - r.height / 2) * 0.22 },
        { duration: 0.2, easing: 'ease-out' }
      )
    })
    btn.addEventListener('mouseleave', () => {
      animate(btn, { x: 0, y: 0 }, { duration: 0.5, easing: [0.16, 1, 0.3, 1] })
    })
  })
}

/* ── Counter animation ─────────────────────── */
export function initCounters() {
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches
  inView('.stat-counter', ({ target }) => {
    const end    = parseFloat(target.dataset.value)
    const suffix = target.dataset.suffix || ''
    const prefix = target.dataset.prefix || ''
    if (reduced) { target.textContent = prefix + end + suffix; return }
    animate(0, end, {
      duration: 2,
      easing: [0.22, 0.61, 0.36, 1],
      onUpdate: v => {
        target.textContent = prefix + (Number.isInteger(end) ? Math.round(v) : v.toFixed(1)) + suffix
      },
    })
  })
}
