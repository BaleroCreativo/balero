import { animate, inView, scroll, stagger } from 'motion'

/* ══════════════════════════════════════════════
   NAVIGATION (dark glass)
══════════════════════════════════════════════ */
const NAV_LINKS = [
  {
    label: 'Soluciones',
    children: [
      { label: 'Refrigeración', href: '/refrigeracion.html', icon: snowflakeIcon() },
      { label: 'Congelación',   href: '/congelacion.html',   icon: thermIcon()     },
      { label: 'Mantenimiento', href: '/mantenimiento.html', icon: wrenchIcon()    },
      { label: 'Refacciones',   href: '/refacciones.html',   icon: boxIcon()       },
    ],
  },
  {
    label: 'Empresa',
    children: [
      { label: 'Nosotros',  href: '/nosotros.html',  icon: teamIcon() },
      { label: 'Sectores',  href: '/sectores.html',  icon: gridIcon() },
      { label: 'Servicios', href: '/servicios.html', icon: listIcon() },
    ],
  },
  { label: 'Contacto', href: '/contacto.html' },
]

function logoSVG() {
  return `<svg width="34" height="34" viewBox="0 0 34 34" fill="none" aria-hidden="true">
    <rect width="34" height="34" rx="9" fill="url(#lg)"/>
    <defs><linearGradient id="lg" x1="0" y1="0" x2="34" y2="34" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#0063b0"/>
      <stop offset="100%" stop-color="#00ccf5"/>
    </linearGradient></defs>
    <path d="M17 5v24M5 17h24M9.4 9.4l15.2 15.2M24.6 9.4L9.4 24.6" stroke="white" stroke-width="2.2" stroke-linecap="round"/>
    <circle cx="17" cy="17" r="2.8" fill="white"/>
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
            <div style="background:var(--bg-surface);border:1px solid var(--glass-border);backdrop-filter:blur(20px)" class="rounded-2xl shadow-2xl p-2 min-w-[220px]">
              ${link.children.map(c => `
                <a href="${c.href}" class="dropdown-item">
                  <span style="color:var(--accent)">${c.icon}</span>
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
          <p class="text-xs font-semibold tracking-widest uppercase px-1 mb-2" style="color:var(--text-3)">${link.label}</p>
          ${link.children.map(c => `
            <a href="${c.href}" class="flex items-center gap-3 px-2 py-2.5 text-sm font-medium rounded-xl transition-colors" style="color:var(--text-2)" onmouseover="this.style.color='var(--accent)';this.style.background='var(--accent-dim)'" onmouseout="this.style.color='var(--text-2)';this.style.background=''">
              <span style="color:var(--accent)">${c.icon}</span>${c.label}
            </a>`).join('')}
        </div>`
    }
    return `<a href="${link.href}" class="block px-2 py-2.5 text-sm font-medium" style="color:var(--text-2)">${link.label}</a>`
  }).join('')
}

export function initNav() {
  const placeholder = document.getElementById('nav-placeholder')
  if (!placeholder) return

  placeholder.outerHTML = `
    <header id="site-header" style="background:rgba(3,13,28,.88);border-bottom:1px solid var(--glass-border);backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px)" class="fixed top-0 inset-x-0 z-40">
      <div class="container mx-auto">
        <div class="flex items-center justify-between h-20">

          <a href="/index.html" class="flex items-center gap-3 flex-shrink-0">
            ${logoSVG()}
            <div>
              <span class="text-base font-bold leading-none block" style="color:var(--text-1)">Polar Construct</span>
              <span class="text-xs leading-none" style="color:var(--text-3)">Refrigeración Industrial</span>
            </div>
          </a>

          <nav class="hidden lg:flex items-center gap-8" aria-label="Navegación principal">
            ${buildDesktopNav()}
          </nav>

          <div class="hidden lg:flex items-center gap-3">
            <a href="/contacto.html" class="btn-primary">Cotizar ahora</a>
          </div>

          <button id="mobile-toggle" class="lg:hidden p-2 -mr-2 cursor-pointer" style="color:var(--text-2)" aria-label="Abrir menú" aria-expanded="false">
            <span id="toggle-icon">${menuIcon()}</span>
          </button>
        </div>
      </div>

      <div id="mobile-menu" class="hidden lg:hidden" style="border-top:1px solid var(--glass-border);background:rgba(3,13,28,.97)">
        <div class="container mx-auto py-6 space-y-4">
          ${buildMobileNav()}
          <div class="pt-4" style="border-top:1px solid var(--glass-border)">
            <a href="/contacto.html" class="btn-primary w-full justify-center">Cotizar ahora</a>
          </div>
        </div>
      </div>
    </header>
    <div class="h-20"></div>`

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

  const header = document.getElementById('site-header')
  window.addEventListener('scroll', () => {
    const scrolled = window.scrollY > 8
    header?.style.setProperty('box-shadow', scrolled
      ? '0 4px 24px rgba(0,0,0,.4), 0 1px 0 rgba(0,212,255,.06)'
      : 'none')
  }, { passive: true })
}

/* ══════════════════════════════════════════════
   FOOTER
══════════════════════════════════════════════ */
export function initFooter() {
  const placeholder = document.getElementById('footer-placeholder')
  if (!placeholder) return

  placeholder.outerHTML = `
    <footer style="background:var(--bg-deep);border-top:1px solid var(--glass-border)">
      <div class="container mx-auto">

        <div class="grid grid-cols-2 md:grid-cols-4 gap-10 py-16" style="border-bottom:1px solid var(--glass-border)">

          <div class="col-span-2 md:col-span-1">
            <a href="/index.html" class="flex items-center gap-3 mb-4">
              ${logoSVG()}
              <span class="font-bold text-base" style="color:var(--text-1)">Polar Construct</span>
            </a>
            <p class="text-sm leading-relaxed mb-6" style="color:var(--text-3)">Diseñamos y fabricamos cámaras de refrigeración y congelación llave en mano para la industria alimentaria.</p>
            <div class="flex gap-3">
              <a href="https://facebook.com" target="_blank" rel="noopener" class="p-2 rounded-xl transition-all" style="border:1px solid var(--glass-border);color:var(--text-3)" onmouseover="this.style.borderColor='var(--accent)';this.style.color='var(--accent)'" onmouseout="this.style.borderColor='var(--glass-border)';this.style.color='var(--text-3)'" aria-label="Facebook">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg>
              </a>
              <a href="https://linkedin.com" target="_blank" rel="noopener" class="p-2 rounded-xl transition-all" style="border:1px solid var(--glass-border);color:var(--text-3)" onmouseover="this.style.borderColor='var(--accent)';this.style.color='var(--accent)'" onmouseout="this.style.borderColor='var(--glass-border)';this.style.color='var(--text-3)'" aria-label="LinkedIn">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6zM2 9h4v12H2z"/><circle cx="4" cy="4" r="2"/></svg>
              </a>
            </div>
          </div>

          <div>
            <p class="font-semibold text-sm mb-4" style="color:var(--text-1)">Soluciones</p>
            <ul class="space-y-2.5 text-sm">
              ${[['Refrigeración','/refrigeracion.html'],['Congelación','/congelacion.html'],['Mantenimiento','/mantenimiento.html'],['Refacciones','/refacciones.html']]
                .map(([l,h])=>`<li><a href="${h}" style="color:var(--text-3)" onmouseover="this.style.color='var(--text-1)'" onmouseout="this.style.color='var(--text-3)'" class="transition-colors">${l}</a></li>`).join('')}
            </ul>
          </div>

          <div>
            <p class="font-semibold text-sm mb-4" style="color:var(--text-1)">Empresa</p>
            <ul class="space-y-2.5 text-sm">
              ${[['Nosotros','/nosotros.html'],['Sectores','/sectores.html'],['Servicios','/servicios.html'],['Contacto','/contacto.html'],['Legal','/legal.html']]
                .map(([l,h])=>`<li><a href="${h}" style="color:var(--text-3)" onmouseover="this.style.color='var(--text-1)'" onmouseout="this.style.color='var(--text-3)'" class="transition-colors">${l}</a></li>`).join('')}
            </ul>
          </div>

          <div>
            <p class="font-semibold text-sm mb-4" style="color:var(--text-1)">Información</p>
            <ul class="space-y-3 text-sm">
              <li class="flex items-start gap-2">
                <svg class="mt-0.5 flex-shrink-0" style="color:var(--accent)" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
                <a href="mailto:info@camarafria.com" style="color:var(--text-3)" onmouseover="this.style.color='var(--text-1)'" onmouseout="this.style.color='var(--text-3)'" class="transition-colors">info@camarafria.com</a>
              </li>
              <li class="flex items-start gap-2">
                <svg class="mt-0.5 flex-shrink-0" style="color:var(--accent)" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
                <a href="tel:+56912345678" style="color:var(--text-3)" onmouseover="this.style.color='var(--text-1)'" onmouseout="this.style.color='var(--text-3)'" class="transition-colors">+56 9 1234 5678</a>
              </li>
              <li class="flex items-start gap-2">
                <svg class="mt-0.5 flex-shrink-0" style="color:var(--accent)" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
                <span style="color:var(--text-3)">Av. Industrial 1250, Santiago</span>
              </li>
              <li class="flex items-start gap-2">
                <svg class="mt-0.5 flex-shrink-0" style="color:var(--accent)" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
                <span style="color:var(--text-3)">Lun–Vie 8:00–18:00</span>
              </li>
            </ul>
          </div>
        </div>

        <div class="py-10" style="border-bottom:1px solid var(--glass-border)">
          <div class="max-w-xl">
            <p class="font-semibold mb-1" style="color:var(--text-1)">Mantente informado</p>
            <p class="text-sm mb-4" style="color:var(--text-3)">Novedades sobre soluciones de refrigeración y actualizaciones de nuestros servicios.</p>
            <form class="flex gap-3" onsubmit="return false">
              <input type="email" placeholder="Tu correo electrónico"
                style="background:rgba(255,255,255,.04);border:1px solid var(--glass-border);color:var(--text-1)"
                class="flex-1 px-4 py-2.5 text-sm rounded-xl focus:outline-none placeholder:opacity-40"
                onfocus="this.style.borderColor='var(--accent)'" onblur="this.style.borderColor='var(--glass-border)'"
                aria-label="Correo electrónico">
              <button type="submit" class="btn-primary flex-shrink-0">Suscribirse</button>
            </form>
            <p class="text-xs mt-2" style="color:var(--text-4)">Al suscribirte aceptas nuestra <a href="/legal.html" style="color:var(--accent)" class="underline">política de privacidad</a>.</p>
          </div>
        </div>

        <div class="flex flex-col sm:flex-row items-center justify-between gap-4 py-6 text-xs" style="color:var(--text-4)">
          <p>© ${new Date().getFullYear()} Polar Construct · Piscis Refrigeración. Todos los derechos reservados.</p>
          <div class="flex gap-6">
            ${[['Privacidad','/legal.html'],['Términos','/legal.html'],['Cookies','/legal.html']]
              .map(([l,h])=>`<a href="${h}" onmouseover="this.style.color='var(--text-1)'" onmouseout="this.style.color='var(--text-4)'" class="transition-colors">${l}</a>`).join('')}
          </div>
        </div>
      </div>
    </footer>`
}

/* ══════════════════════════════════════════════
   FROST CANVAS — ice crystal particles
══════════════════════════════════════════════ */
export function initFrostCanvas() {
  const canvas = document.getElementById('frost-canvas')
  if (!canvas) return
  const ctx = canvas.getContext('2d')
  let particles = []
  let raf

  function resize() {
    canvas.width  = canvas.parentElement.offsetWidth
    canvas.height = canvas.parentElement.offsetHeight
  }

  function randomParticle() {
    const types = ['dot', 'hex', 'cross', 'dot', 'dot']
    return {
      x:        Math.random() * canvas.width,
      y:        canvas.height + 20,
      size:     Math.random() * 3.5 + 1.2,
      vy:       -(Math.random() * 0.65 + 0.2),
      vx:       (Math.random() - 0.5) * 0.25,
      opacity:  Math.random() * 0.45 + 0.15,
      rot:      Math.random() * Math.PI * 2,
      rotSpeed: (Math.random() - 0.5) * 0.025,
      type:     types[Math.floor(Math.random() * types.length)],
      drift:    Math.random() * 100,
    }
  }

  function drawHex(ctx, size) {
    ctx.beginPath()
    for (let i = 0; i < 6; i++) {
      const a = (i * Math.PI) / 3 - Math.PI / 6
      const m = i === 0 ? 'moveTo' : 'lineTo'
      ctx[m](Math.cos(a) * size, Math.sin(a) * size)
    }
    ctx.closePath()
    ctx.stroke()
  }

  function drawCross(ctx, size) {
    for (let i = 0; i < 3; i++) {
      ctx.beginPath()
      ctx.moveTo(-size, 0)
      ctx.lineTo(size, 0)
      ctx.stroke()
      ctx.rotate(Math.PI / 3)
    }
    // Arms
    for (let i = 0; i < 6; i++) {
      ctx.beginPath()
      ctx.moveTo(size * 0.5, 0)
      ctx.lineTo(size * 0.75, size * 0.25)
      ctx.stroke()
      ctx.beginPath()
      ctx.moveTo(size * 0.5, 0)
      ctx.lineTo(size * 0.75, -size * 0.25)
      ctx.stroke()
      ctx.rotate(Math.PI / 3)
    }
  }

  function frame() {
    ctx.clearRect(0, 0, canvas.width, canvas.height)

    // Spawn
    if (particles.length < 55 && Math.random() < 0.25) {
      particles.push(randomParticle())
    }

    particles = particles.filter(p => p.y > -30)

    particles.forEach(p => {
      p.y   += p.vy
      p.x   += p.vx + Math.sin(p.y * 0.008 + p.drift) * 0.28
      p.rot += p.rotSpeed

      const r = Math.floor(180 + Math.random() * 40)
      const g = Math.floor(220 + Math.random() * 30)
      ctx.globalAlpha = p.opacity
      ctx.strokeStyle = `rgba(${r},${g},255,${p.opacity})`
      ctx.fillStyle   = `rgba(${r},${g},255,${p.opacity * 0.6})`
      ctx.lineWidth   = p.size * 0.3

      ctx.save()
      ctx.translate(p.x, p.y)
      ctx.rotate(p.rot)

      if (p.type === 'dot') {
        ctx.beginPath()
        ctx.arc(0, 0, p.size, 0, Math.PI * 2)
        ctx.fill()
      } else if (p.type === 'hex') {
        drawHex(ctx, p.size * 1.2)
      } else {
        drawCross(ctx, p.size * 1.5)
      }

      ctx.restore()
    })
    ctx.globalAlpha = 1
    raf = requestAnimationFrame(frame)
  }

  window.addEventListener('resize', resize, { passive: true })
  resize()
  frame()

  return () => { cancelAnimationFrame(raf); window.removeEventListener('resize', resize) }
}

/* ══════════════════════════════════════════════
   3D TILT — card perspective effect
══════════════════════════════════════════════ */
export function initTilt3D() {
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches
  if (reduced) return

  document.querySelectorAll('[data-tilt]').forEach(card => {
    // Inject spotlight element
    const spot = document.createElement('div')
    spot.className = 'card-spotlight'
    card.appendChild(spot)

    card.addEventListener('mousemove', e => {
      const r = card.getBoundingClientRect()
      const x = (e.clientX - r.left) / r.width  - 0.5
      const y = (e.clientY - r.top)  / r.height - 0.5

      card.style.transform = `perspective(900px) rotateY(${x * 13}deg) rotateX(${-y * 10}deg) translateZ(8px)`
      card.style.setProperty('--mx', `${e.clientX - r.left}px`)
      card.style.setProperty('--my', `${e.clientY - r.top}px`)
    })

    card.addEventListener('mouseleave', () => {
      card.style.transform = ''
    })
  })
}

/* ══════════════════════════════════════════════
   ANIMATIONS (Motion.js)
══════════════════════════════════════════════ */
export function initAnimations() {
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches

  // ── Scroll progress bar ──────────────────────
  const bar = document.createElement('div')
  bar.setAttribute('aria-hidden', 'true')
  Object.assign(bar.style, {
    position: 'fixed', top: '0', left: '0', right: '0', height: '2px',
    background: 'linear-gradient(to right, #0063b0, #00ccf5)',
    transformOrigin: '0 0', transform: 'scaleX(0)', zIndex: '9999',
    pointerEvents: 'none',
    boxShadow: '0 0 8px rgba(0,200,255,.6)',
  })
  document.body.appendChild(bar)
  scroll(animate(bar, { scaleX: [0, 1] }))

  if (reduced) return

  // ── Reveal up ────────────────────────────────
  inView('.reveal-up', ({ target }) => {
    animate(target, { opacity: [0, 1], y: [52, 0] }, { duration: .75, easing: [.16,1,.3,1] })
  }, { margin: '0px 0px -80px 0px' })

  // ── Reveal left ──────────────────────────────
  inView('.reveal-left', ({ target }) => {
    animate(target, { opacity: [0, 1], x: [-60, 0] }, { duration: .75, easing: [.16,1,.3,1] })
  }, { margin: '0px 0px -80px 0px' })

  // ── Reveal right ─────────────────────────────
  inView('.reveal-right', ({ target }) => {
    animate(target, { opacity: [0, 1], x: [60, 0] }, { duration: .75, easing: [.16,1,.3,1] })
  }, { margin: '0px 0px -80px 0px' })

  // ── Scale in ─────────────────────────────────
  inView('.reveal-scale', ({ target }) => {
    animate(target, { opacity: [0, 1], scale: [.88, 1] }, { duration: .65, easing: [.16,1,.3,1] })
  }, { margin: '0px 0px -80px 0px' })

  // ── Section labels ───────────────────────────
  inView('.section-label', ({ target }) => {
    animate(target, { opacity: [0, 1], scale: [.7, 1], y: [10, 0] }, { duration: .4, easing: [.34,1.56,.64,1] })
  }, { margin: '0px 0px -40px 0px' })

  // ── Stagger groups ───────────────────────────
  inView('.stagger-group', ({ target }) => {
    animate(
      target.querySelectorAll('.stagger-item'),
      { opacity: [0, 1], y: [44, 0], scale: [.93, 1] },
      { duration: .65, delay: stagger(.1), easing: [.16,1,.3,1] }
    )
  }, { margin: '0px 0px -60px 0px' })

  // ── Float badges ─────────────────────────────
  document.querySelectorAll('.float-badge').forEach((el, i) => {
    animate(el, { y: [0, -12, 0] }, { duration: 3 + i * .9, repeat: Infinity, easing: 'ease-in-out' })
  })

  // ── Pulsing dots ─────────────────────────────
  document.querySelectorAll('.status-dot').forEach(el => {
    animate(el, { opacity: [1, .3, 1], scale: [1, 1.6, 1] }, { duration: 2.5, repeat: Infinity, easing: 'ease-in-out' })
  })

  // ── Animated bars ────────────────────────────
  document.querySelectorAll('.animated-bar').forEach(el => { el.style.width = '0' })
  inView('.animated-bar', ({ target }) => {
    animate(target, { width: `${target.dataset.w ?? 50}%` }, { duration: 1.3, delay: .4, easing: [.16,1,.3,1] })
  })

  // ── Hero parallax ────────────────────────────
  const heroVis = document.querySelector('.hero-visual')
  if (heroVis) {
    const section = heroVis.closest('section')
    if (section) scroll(animate(heroVis, { y: [0, 36] }), { target: section, offset: ['start start', 'end start'] })
  }

  // ── Magnetic buttons ─────────────────────────
  document.querySelectorAll('.btn-primary').forEach(btn => {
    btn.addEventListener('mousemove', e => {
      const r = btn.getBoundingClientRect()
      animate(btn,
        { x: (e.clientX - r.left - r.width / 2) * .2, y: (e.clientY - r.top - r.height / 2) * .2 },
        { duration: .2, easing: 'ease-out' }
      )
    })
    btn.addEventListener('mouseleave', () => {
      animate(btn, { x: 0, y: 0 }, { duration: .5, easing: [.16,1,.3,1] })
    })
  })
}

/* ══════════════════════════════════════════════
   COUNTER ANIMATION
══════════════════════════════════════════════ */
export function initCounters() {
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches
  inView('.stat-counter', ({ target }) => {
    const end    = parseFloat(target.dataset.value)
    const suffix = target.dataset.suffix || ''
    const prefix = target.dataset.prefix || ''
    if (reduced) { target.textContent = prefix + end + suffix; return }
    animate(0, end, {
      duration: 2,
      easing: [.22,.61,.36,1],
      onUpdate: v => {
        target.textContent = prefix + (Number.isInteger(end) ? Math.round(v) : v.toFixed(1)) + suffix
      },
    })
  })
}

/* ══════════════════════════════════════════════
   FAQ ACCORDION
══════════════════════════════════════════════ */
export function initFAQ() {
  document.querySelectorAll('.faq-item').forEach(item => {
    const btn = item.querySelector('.faq-btn')
    btn?.addEventListener('click', () => {
      const isOpen = item.classList.contains('open')
      document.querySelectorAll('.faq-item.open').forEach(o => o.classList.remove('open'))
      if (!isOpen) item.classList.add('open')
    })
  })
}
