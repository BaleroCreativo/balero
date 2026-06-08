"use client";

import React, { useEffect, useRef } from "react";
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { cn } from "@/lib/utils";

if (typeof window !== "undefined") {
  gsap.registerPlugin(ScrollTrigger);
}

/* ──────────────────────────────────────────────────────────────
   BRAND TOKENS — Eje Ocho
   #2E3C41 dark teal | #04CCB5 teal | #FCE300 yellow | #C6D6E3 lt-blue
────────────────────────────────────────────────────────────── */
const INJECTED_STYLES = `
  :root {
    --eo-dark:   #2E3C41;
    --eo-teal:   #04CCB5;
    --eo-teal2:  #508590;
    --eo-ltblue: #C6D6E3;
    --eo-yellow: #FCE300;
    --eo-bg:     #F0F5F7;
    --eo-white:  #FEFDFB;
    --color-foreground: var(--eo-dark);
    --color-background: var(--eo-bg);
  }

  .gsap-reveal { visibility: hidden; }

  .film-grain {
    position: absolute; inset: 0; width: 100%; height: 100%;
    pointer-events: none; z-index: 50; opacity: 0.04; mix-blend-mode: overlay;
    background: url('data:image/svg+xml;utf8,<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"><filter id="noiseFilter"><feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="3" stitchTiles="stitch"/></filter><rect width="100%25" height="100%25" filter="url(%23noiseFilter)"/></svg>');
  }

  .bg-grid-eo {
    background-size: 60px 60px;
    background-image:
      linear-gradient(to right, rgba(4,204,181,0.07) 1px, transparent 1px),
      linear-gradient(to bottom, rgba(4,204,181,0.07) 1px, transparent 1px);
    mask-image: radial-gradient(ellipse at center, black 0%, transparent 70%);
    -webkit-mask-image: radial-gradient(ellipse at center, black 0%, transparent 70%);
  }

  /* Tagline text effects */
  .text-eo-3d {
    color: var(--eo-dark);
    text-shadow:
      0 8px 24px rgba(46,60,65,0.18),
      0 2px 4px rgba(46,60,65,0.08);
  }

  .text-eo-teal {
    background: linear-gradient(180deg, #04CCB5 0%, #508590 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    transform: translateZ(0);
    filter:
      drop-shadow(0px 8px 20px rgba(4,204,181,0.3))
      drop-shadow(0px 2px 4px rgba(4,204,181,0.15));
  }

  /* Card — Eje Ocho brand: dark teal premium */
  .eo-card {
    background: linear-gradient(145deg, #3a5260 0%, #1a2b31 50%, #0f1c20 100%);
    box-shadow:
      0 40px 100px -20px rgba(0,0,0,0.85),
      0 20px 40px -20px rgba(4,204,181,0.1),
      inset 0 1px 2px rgba(255,255,255,0.12),
      inset 0 -2px 4px rgba(0,0,0,0.6);
    border: 1px solid rgba(4,204,181,0.08);
    position: relative;
  }

  .card-sheen {
    position: absolute; inset: 0; border-radius: inherit; pointer-events: none; z-index: 50;
    background: radial-gradient(700px circle at var(--mouse-x,50%) var(--mouse-y,50%), rgba(4,204,181,0.05) 0%, transparent 50%);
    mix-blend-mode: screen; transition: opacity 0.3s;
  }

  /* Dashboard card inside hero */
  .dash-widget {
    background: linear-gradient(180deg, rgba(255,255,255,0.06) 0%, rgba(255,255,255,0.02) 100%);
    box-shadow:
      0 8px 20px rgba(0,0,0,0.35),
      inset 0 1px 1px rgba(255,255,255,0.06),
      inset 0 -1px 1px rgba(0,0,0,0.5);
    border: 1px solid rgba(4,204,181,0.08);
  }

  .floating-ui-badge {
    background: linear-gradient(135deg, rgba(4,204,181,0.1) 0%, rgba(4,204,181,0.02) 100%);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    box-shadow:
      0 0 0 1px rgba(4,204,181,0.15),
      0 20px 40px -12px rgba(0,0,0,0.8),
      inset 0 1px 1px rgba(255,255,255,0.12),
      inset 0 -1px 1px rgba(0,0,0,0.4);
  }

  /* CTA Buttons */
  .btn-eo-teal {
    background: linear-gradient(180deg, #06e6cd 0%, #04CCB5 100%);
    color: var(--eo-dark);
    font-weight: 700;
    box-shadow:
      0 0 0 1px rgba(4,204,181,0.3),
      0 4px 12px -2px rgba(4,204,181,0.5),
      0 12px 24px -4px rgba(0,0,0,0.5),
      inset 0 1px 1px rgba(255,255,255,0.4),
      inset 0 -2px 4px rgba(0,0,0,0.2);
    transition: all 0.35s cubic-bezier(0.25, 1, 0.5, 1);
  }
  .btn-eo-teal:hover {
    transform: translateY(-3px);
    background: linear-gradient(180deg, #FCE300 0%, #f0d800 100%);
    box-shadow:
      0 0 0 1px rgba(252,227,0,0.4),
      0 6px 16px -2px rgba(252,227,0,0.4),
      0 20px 32px -6px rgba(0,0,0,0.6),
      inset 0 1px 1px rgba(255,255,255,0.5),
      inset 0 -2px 4px rgba(0,0,0,0.15);
  }
  .btn-eo-teal:active { transform: translateY(1px); }

  .btn-eo-outline {
    background: transparent;
    color: rgba(255,255,255,0.7);
    border: 1px solid rgba(4,204,181,0.35);
    box-shadow: inset 0 1px 1px rgba(255,255,255,0.05);
    transition: all 0.3s cubic-bezier(0.25, 1, 0.5, 1);
  }
  .btn-eo-outline:hover {
    border-color: var(--eo-teal);
    color: var(--eo-teal);
    transform: translateY(-2px);
    box-shadow: 0 0 20px rgba(4,204,181,0.15), inset 0 1px 1px rgba(4,204,181,0.05);
  }

  .progress-ring {
    transform: rotate(-90deg);
    transform-origin: center;
    stroke-dasharray: 402;
    stroke-dashoffset: 402;
    stroke-linecap: round;
  }

  .eje-pill {
    background: rgba(4,204,181,0.08);
    border: 1px solid rgba(4,204,181,0.15);
    border-radius: 9999px;
    padding: 0.25rem 0.75rem;
    font-size: 0.6rem;
    font-weight: 700;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: rgba(4,204,181,0.9);
  }
`;

export interface EjeOchoHeroProps extends React.HTMLAttributes<HTMLDivElement> {
  onDiagnosticClick?: () => void;
  onEjesClick?: () => void;
}

export function EjeOchoHero({
  onDiagnosticClick,
  onEjesClick,
  className,
  ...props
}: EjeOchoHeroProps) {
  const containerRef = useRef<HTMLDivElement>(null);
  const mainCardRef  = useRef<HTMLDivElement>(null);
  const rafRef       = useRef<number>(0);

  /* Mouse parallax on card */
  useEffect(() => {
    const handleMouseMove = (e: MouseEvent) => {
      if (window.scrollY > window.innerHeight * 2) return;
      cancelAnimationFrame(rafRef.current);
      rafRef.current = requestAnimationFrame(() => {
        if (!mainCardRef.current) return;
        const rect = mainCardRef.current.getBoundingClientRect();
        mainCardRef.current.style.setProperty("--mouse-x", `${e.clientX - rect.left}px`);
        mainCardRef.current.style.setProperty("--mouse-y", `${e.clientY - rect.top}px`);
      });
    };
    window.addEventListener("mousemove", handleMouseMove);
    return () => { window.removeEventListener("mousemove", handleMouseMove); cancelAnimationFrame(rafRef.current); };
  }, []);

  /* GSAP scroll cinematic timeline */
  useEffect(() => {
    const isMobile = window.innerWidth < 768;
    const ctx = gsap.context(() => {
      /* initial states */
      gsap.set(".eo-tagline-1", { autoAlpha: 0, y: 60, scale: 0.88, filter: "blur(16px)", rotationX: -18 });
      gsap.set(".eo-tagline-2", { autoAlpha: 1, clipPath: "inset(0 100% 0 0)" });
      gsap.set(".eo-main-card", { y: window.innerHeight + 200, autoAlpha: 1 });
      gsap.set([".card-left-text", ".card-right-text", ".dash-mockup", ".floating-badge", ".dash-widget"], { autoAlpha: 0 });
      gsap.set(".eo-cta-wrapper", { autoAlpha: 0, scale: 0.82, filter: "blur(28px)" });

      /* intro */
      const intro = gsap.timeline({ delay: 0.25 });
      intro
        .to(".eo-tagline-1",  { duration: 1.8, autoAlpha: 1, y: 0, scale: 1, filter: "blur(0px)", rotationX: 0, ease: "expo.out" })
        .to(".eo-tagline-2",  { duration: 1.4, clipPath: "inset(0 0% 0 0)", ease: "power4.inOut" }, "-=1.0");

      /* scroll timeline */
      const tl = gsap.timeline({
        scrollTrigger: {
          trigger: containerRef.current,
          start: "top top",
          end: "+=7000",
          pin: true,
          scrub: 1,
          anticipatePin: 1,
        },
      });

      tl
        /* hero text fades back */
        .to([".eo-hero-text", ".bg-grid-eo"], { scale: 1.12, filter: "blur(18px)", opacity: 0.15, ease: "power2.inOut", duration: 2 }, 0)
        /* card rises */
        .to(".eo-main-card", { y: 0, ease: "power3.inOut", duration: 2 }, 0)
        /* card expands fullscreen */
        .to(".eo-main-card", { width: "100%", height: "100%", borderRadius: "0px", ease: "power3.inOut", duration: 1.5 })
        /* dashboard mockup enters with 3D */
        .fromTo(".dash-mockup",
          { y: 280, z: -400, rotationX: 45, rotationY: -25, autoAlpha: 0, scale: 0.65 },
          { y: 0, z: 0, rotationX: 0, rotationY: 0, autoAlpha: 1, scale: 1, ease: "expo.out", duration: 2.5 }, "-=0.8"
        )
        /* widgets stagger in */
        .fromTo(".dash-widget", { y: 36, autoAlpha: 0, scale: 0.93 }, { y: 0, autoAlpha: 1, scale: 1, stagger: 0.12, ease: "back.out(1.2)", duration: 1.4 }, "-=1.5")
        /* progress ring */
        .to(".progress-ring", { strokeDashoffset: 50, duration: 2, ease: "power3.inOut" }, "-=1.2")
        .to(".counter-val", { innerHTML: 8, snap: { innerHTML: 1 }, duration: 1.5, ease: "expo.out" }, "-=2.0")
        /* floating badges */
        .fromTo(".floating-badge", { y: 90, autoAlpha: 0, scale: 0.72, rotationZ: -8 }, { y: 0, autoAlpha: 1, scale: 1, rotationZ: 0, ease: "back.out(1.4)", duration: 1.4, stagger: 0.18 }, "-=2.0")
        /* card copy */
        .fromTo(".card-left-text",  { x: -44, autoAlpha: 0 }, { x: 0, autoAlpha: 1, ease: "power4.out", duration: 1.5 }, "-=1.4")
        .fromTo(".card-right-text", { x:  44, autoAlpha: 0, scale: 0.82 }, { x: 0, autoAlpha: 1, scale: 1, ease: "expo.out", duration: 1.5 }, "<")
        /* pause on full card */
        .to({}, { duration: 2.5 })
        /* switch to CTA view */
        .set(".eo-hero-text", { autoAlpha: 0 })
        .set(".eo-cta-wrapper", { autoAlpha: 1 })
        .to({}, { duration: 1.5 })
        /* pull back content before card exit */
        .to([".dash-mockup", ".floating-badge", ".card-left-text", ".card-right-text"], {
          scale: 0.88, y: -36, z: -180, autoAlpha: 0, ease: "power3.in", duration: 1.1, stagger: 0.04,
        })
        .to(".eo-main-card", {
          width: isMobile ? "92vw" : "85vw",
          height: isMobile ? "90vh" : "82vh",
          borderRadius: isMobile ? "28px" : "36px",
          ease: "expo.inOut", duration: 1.8,
        }, "pullback")
        .to(".eo-cta-wrapper", { scale: 1, filter: "blur(0px)", ease: "expo.inOut", duration: 1.8 }, "pullback")
        /* card exits */
        .to(".eo-main-card", { y: -(window.innerHeight + 300), ease: "power3.in", duration: 1.5 });

    }, containerRef);
    return () => ctx.revert();
  }, []);

  return (
    <div
      ref={containerRef}
      className={cn("relative w-screen h-screen overflow-hidden flex items-center justify-center", className)}
      style={{ perspective: "1500px", backgroundColor: "var(--eo-bg)", color: "var(--eo-dark)", fontFamily: "'Lato', sans-serif" }}
      {...props}
    >
      <style dangerouslySetInnerHTML={{ __html: INJECTED_STYLES }} />
      <div className="film-grain" aria-hidden="true" />
      <div className="bg-grid-eo absolute inset-0 z-0 pointer-events-none opacity-60" aria-hidden="true" />

      {/* ── LAYER 1: Hero taglines ───────────────────────────────── */}
      <div className="eo-hero-text absolute z-10 flex flex-col items-center justify-center text-center w-screen px-6 will-change-transform">
        <h1 className="eo-tagline-1 gsap-reveal text-eo-3d text-5xl md:text-7xl lg:text-[5.5rem] leading-none font-black tracking-tight mb-3"
          style={{ fontFamily: "'Yeseva One', serif" }}>
          Conectamos marketing,<br />ventas y experiencia
        </h1>
        <h1 className="eo-tagline-2 gsap-reveal text-eo-teal text-5xl md:text-7xl lg:text-[5.5rem] leading-none font-black tracking-tight"
          style={{ fontFamily: "'Yeseva One', serif" }}>
          en un sistema comercial
        </h1>
        <p className="mt-6 text-base md:text-lg font-light max-w-xl" style={{ color: "var(--eo-teal2)" }}>
          Sistema de crecimiento comercial para empresas B2B
        </p>
      </div>

      {/* ── LAYER 2: CTA final ───────────────────────────────────── */}
      <div className="eo-cta-wrapper absolute z-10 flex flex-col items-center justify-center text-center w-screen px-6 gsap-reveal pointer-events-auto will-change-transform">
        <span className="eje-pill mb-6">Primer paso</span>
        <h2
          className="text-4xl md:text-6xl lg:text-[5rem] font-black mb-5 tracking-tight leading-tight"
          style={{ fontFamily: "'Yeseva One', serif", color: "var(--eo-dark)" }}
        >
          Descubre en qué eje<br />
          <span style={{ color: "var(--eo-teal)" }}>se fuga tu crecimiento</span>
        </h2>
        <p className="text-base md:text-lg mb-10 max-w-lg mx-auto font-light leading-relaxed" style={{ color: "var(--eo-teal2)" }}>
          Diagnóstico breve y gratuito. Identifica si necesitas fundamentos, optimización o escalamiento.
        </p>
        <div className="flex flex-col sm:flex-row gap-4 sm:gap-6">
          <button
            onClick={onDiagnosticClick}
            className="btn-eo-teal flex items-center justify-center gap-3 px-8 py-4 rounded-2xl text-sm font-bold tracking-wide uppercase"
          >
            <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4" />
            </svg>
            Iniciar diagnóstico Eje Ocho
          </button>
          <button
            onClick={onEjesClick}
            className="btn-eo-outline flex items-center justify-center gap-3 px-8 py-4 rounded-2xl text-sm font-bold tracking-wide uppercase"
          >
            Conocer los 8 ejes
            <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17 8l4 4m0 0l-4 4m4-4H3" />
            </svg>
          </button>
        </div>
      </div>

      {/* ── LAYER 3: Premium dark-teal card ─────────────────────── */}
      <div className="absolute inset-0 z-20 flex items-center justify-center pointer-events-none" style={{ perspective: "1500px" }}>
        <div
          ref={mainCardRef}
          className="eo-main-card eo-card relative overflow-hidden gsap-reveal flex items-center justify-center pointer-events-auto w-[92vw] md:w-[85vw] h-[90vh] md:h-[82vh] rounded-[28px] md:rounded-[36px]"
        >
          <div className="card-sheen" aria-hidden="true" />

          <div className="relative w-full h-full max-w-7xl mx-auto px-5 lg:px-14 flex flex-col justify-evenly lg:grid lg:grid-cols-3 items-center lg:gap-10 z-10 py-8 lg:py-0">

            {/* Brand name — top on mobile, right on desktop */}
            <div className="card-right-text gsap-reveal order-1 lg:order-3 flex justify-center lg:justify-end z-20 w-full">
              <div className="text-center lg:text-right">
                <h2
                  className="text-5xl md:text-7xl lg:text-[6rem] font-black uppercase tracking-tighter leading-none"
                  style={{ fontFamily: "'Yeseva One', serif", background: "linear-gradient(180deg,#FFFFFF 0%,#A1A1AA 100%)", WebkitBackgroundClip: "text", WebkitTextFillColor: "transparent", backgroundClip: "text", filter: "drop-shadow(0px 10px 20px rgba(0,0,0,0.7))" }}
                >
                  Eje<br />Ocho
                </h2>
                <div className="mt-3 hidden lg:block" style={{ color: "rgba(4,204,181,0.6)", fontSize: "0.65rem", fontWeight: 700, letterSpacing: "0.2em", textTransform: "uppercase" }}>
                  Sistema de crecimiento comercial
                </div>
              </div>
            </div>

            {/* Dashboard mockup — center */}
            <div className="dash-mockup order-2 lg:order-2 relative w-full h-[300px] lg:h-[520px] flex items-center justify-center z-10" style={{ perspective: "1000px" }}>
              <div className="relative w-full h-full flex items-center justify-center transform scale-[0.7] md:scale-90 lg:scale-100">

                {/* Dashboard card */}
                <div className="relative w-[300px] lg:w-[340px] rounded-2xl overflow-hidden" style={{ background: "rgba(10,18,22,0.95)", border: "1px solid rgba(4,204,181,0.12)", boxShadow: "0 40px 80px -15px rgba(0,0,0,0.9), 0 15px 25px -5px rgba(0,0,0,0.7)" }}>

                  {/* Dashboard header */}
                  <div className="flex items-center justify-between px-5 py-4" style={{ borderBottom: "1px solid rgba(4,204,181,0.08)" }}>
                    <div>
                      <div style={{ fontSize: "0.6rem", color: "rgba(4,204,181,0.6)", fontWeight: 700, letterSpacing: "0.2em", textTransform: "uppercase" }}>Diagnóstico</div>
                      <div className="text-white font-bold text-sm mt-0.5">Sistema Eje Ocho</div>
                    </div>
                    <div className="w-8 h-8 rounded-full flex items-center justify-center text-xs font-bold" style={{ background: "rgba(4,204,181,0.15)", color: "#04CCB5", border: "1px solid rgba(4,204,181,0.2)" }}>
                      E8
                    </div>
                  </div>

                  {/* Progress ring */}
                  <div className="dash-widget relative w-36 h-36 mx-auto my-5 flex items-center justify-center" style={{ borderRadius: "50%" }}>
                    <svg className="absolute inset-0 w-full h-full" aria-hidden="true">
                      <circle cx="72" cy="72" r="64" fill="none" stroke="rgba(4,204,181,0.06)" strokeWidth="10" />
                      <circle className="progress-ring" cx="72" cy="72" r="64" fill="none" stroke="#04CCB5" strokeWidth="10" />
                    </svg>
                    <div className="text-center z-10 flex flex-col items-center">
                      <span className="counter-val text-4xl font-black text-white" style={{ fontFamily: "'Yeseva One', serif" }}>0</span>
                      <span style={{ fontSize: "0.55rem", color: "rgba(4,204,181,0.5)", textTransform: "uppercase", letterSpacing: "0.12em", fontWeight: 700 }}>ejes activos</span>
                    </div>
                  </div>

                  {/* Eje status widgets */}
                  <div className="px-4 pb-5 space-y-2.5">
                    {[
                      { n: "01", label: "Posicionamiento", pct: 85, color: "#04CCB5" },
                      { n: "02", label: "Demanda", pct: 60, color: "#508590" },
                      { n: "03", label: "Conversión digital", pct: 45, color: "#C6D6E3" },
                      { n: "04", label: "Oportunidades", pct: 72, color: "#04CCB5" },
                    ].map(({ n, label, pct, color }) => (
                      <div key={n} className="dash-widget rounded-xl p-3">
                        <div className="flex items-center justify-between mb-1.5">
                          <div className="flex items-center gap-2">
                            <span style={{ fontSize: "0.6rem", fontWeight: 700, color: "rgba(4,204,181,0.7)" }}>{n}</span>
                            <span style={{ fontSize: "0.72rem", color: "rgba(255,255,255,0.65)", fontWeight: 400 }}>{label}</span>
                          </div>
                          <span style={{ fontSize: "0.65rem", fontWeight: 700, color }}>{pct}%</span>
                        </div>
                        <div style={{ height: "3px", background: "rgba(255,255,255,0.04)", borderRadius: "9999px", overflow: "hidden" }}>
                          <div style={{ width: `${pct}%`, height: "100%", background: color, borderRadius: "9999px", boxShadow: `0 0 8px ${color}60` }} />
                        </div>
                      </div>
                    ))}
                  </div>
                </div>

                {/* Floating badges */}
                <div className="floating-badge absolute top-6 -left-16 lg:-left-24 floating-ui-badge rounded-xl p-3 flex items-center gap-3 z-30">
                  <div className="w-9 h-9 rounded-full flex items-center justify-center" style={{ background: "rgba(4,204,181,0.15)", border: "1px solid rgba(4,204,181,0.25)" }}>
                    <svg className="w-4 h-4" fill="none" stroke="#04CCB5" viewBox="0 0 24 24" aria-hidden="true">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6" />
                    </svg>
                  </div>
                  <div>
                    <p className="text-white text-xs font-bold">+240% conversión</p>
                    <p style={{ color: "rgba(4,204,181,0.5)", fontSize: "0.65rem" }}>promedio clientes</p>
                  </div>
                </div>

                <div className="floating-badge absolute bottom-10 -right-14 lg:-right-24 floating-ui-badge rounded-xl p-3 flex items-center gap-3 z-30">
                  <div className="w-9 h-9 rounded-full flex items-center justify-center" style={{ background: "rgba(252,227,0,0.12)", border: "1px solid rgba(252,227,0,0.2)" }}>
                    <svg className="w-4 h-4" fill="none" stroke="#FCE300" viewBox="0 0 24 24" aria-hidden="true">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                  </div>
                  <div>
                    <p className="text-white text-xs font-bold">$180M pipeline</p>
                    <p style={{ color: "rgba(252,227,0,0.5)", fontSize: "0.65rem" }}>generado para clientes</p>
                  </div>
                </div>
              </div>
            </div>

            {/* Left copy — bottom on mobile, left on desktop */}
            <div className="card-left-text gsap-reveal order-3 lg:order-1 flex flex-col justify-center text-center lg:text-left z-20 w-full px-4 lg:px-0">
              <div className="eje-pill mb-4 inline-block">Consultoría B2B</div>
              <h3
                className="text-white text-2xl md:text-3xl lg:text-4xl font-black mb-4 tracking-tight leading-tight"
                style={{ fontFamily: "'Yeseva One', serif", filter: "drop-shadow(0px 8px 16px rgba(0,0,0,0.6))" }}
              >
                El crecimiento<br />se ordena aquí
              </h3>
              <p className="hidden md:block text-sm md:text-base font-light leading-relaxed max-w-xs lg:max-w-none" style={{ color: "rgba(4,204,181,0.55)" }}>
                <span className="text-white font-semibold">Eje Ocho</span> integra marketing, ventas y experiencia del cliente en un sistema comercial medible para que el crecimiento deje de ser frágil.
              </p>
            </div>

          </div>
        </div>
      </div>
    </div>
  );
}
