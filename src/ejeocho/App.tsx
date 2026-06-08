import { EjeOchoHero } from "@/components/ui/cinematic-landing-hero";

/* ── Brand tokens ──────────────────────────────────── */
const EO = {
  dark:   "#2E3C41",
  teal:   "#04CCB5",
  teal2:  "#508590",
  ltblue: "#C6D6E3",
  yellow: "#FCE300",
  bg:     "#F0F5F7",
  bgAlt:  "#E8EFF3",
  white:  "#FEFDFB",
  border: "rgba(46,60,65,0.1)",
  muted:  "#6B8490",
};

/* ── Small helpers ─────────────────────────────────── */
const Label = ({ children }: { children: React.ReactNode }) => (
  <p style={{ display:"flex", alignItems:"center", gap:"0.75rem", fontSize:"0.62rem", fontWeight:700, letterSpacing:"0.3em", textTransform:"uppercase", color:EO.teal2, marginBottom:"1.25rem" }}>
    <span style={{ display:"block", width:"1.5rem", height:"2px", background:EO.teal, flexShrink:0 }} />
    {children}
  </p>
);

const SecHeading = ({ children, style }: { children: React.ReactNode; style?: React.CSSProperties }) => (
  <h2 style={{ fontFamily:"'Yeseva One',serif", fontSize:"clamp(2rem,4.5vw,4rem)", lineHeight:1.08, color:EO.dark, ...style }}>
    {children}
  </h2>
);

export default function App() {
  const scrollTo = (id: string) => {
    document.getElementById(id)?.scrollIntoView({ behavior: "smooth" });
  };

  return (
    <div style={{ fontFamily:"'Lato',sans-serif", background:EO.bg, color:EO.dark, overflowX:"hidden" }}>

      {/* ── CINEMATIC HERO ────────────────────────────────── */}
      <EjeOchoHero
        onDiagnosticClick={() => scrollTo("diagnostico")}
        onEjesClick={() => scrollTo("ejes")}
      />

      {/* ── TICKER ───────────────────────────────────────── */}
      <Ticker />

      {/* ── PROBLEMA ─────────────────────────────────────── */}
      <ProblemaSection />

      {/* ── QUÉ ES ───────────────────────────────────────── */}
      <QueEsSection />

      {/* ── LOS 8 EJES ───────────────────────────────────── */}
      <EjesSection />

      {/* ── MADUREZ ──────────────────────────────────────── */}
      <MadurezSection />

      {/* ── PROCESO ──────────────────────────────────────── */}
      <ProcesoSection />

      {/* ── PROPUESTA DE VALOR ───────────────────────────── */}
      <ValorSection />

      {/* ── PARA QUIÉN ES / NO ES ────────────────────────── */}
      <QuienesSection />

      {/* ── CTA DIAGNÓSTICO ──────────────────────────────── */}
      <CtaSection />

      {/* ── CIERRE ───────────────────────────────────────── */}
      <CierreSection />

      {/* ── FOOTER ───────────────────────────────────────── */}
      <Footer />
    </div>
  );
}

/* ═══════════════════════════════════════════════════
   TICKER
═══════════════════════════════════════════════════ */
const TICKER_ITEMS = [
  "Arquitectura de Posicionamiento","Activación de Demanda","Conversión Digital",
  "Gestión de Oportunidades","Proceso Comercial","Conversión Estratégica",
  "Experiencia del Cliente","Orquestación del Sistema",
];

function Ticker() {
  const items = [...TICKER_ITEMS, ...TICKER_ITEMS];
  return (
    <div style={{ background:EO.dark, padding:"0.9rem 0", overflow:"hidden" }}>
      <div style={{ display:"flex", width:"max-content", animation:"ticker 35s linear infinite" }}>
        {items.map((item, i) => (
          <span key={i} style={{ display:"flex", alignItems:"center", gap:"2rem", padding:"0 2rem", fontSize:"0.6rem", fontWeight:700, letterSpacing:"0.24em", textTransform:"uppercase", color:"rgba(255,255,255,0.4)", whiteSpace:"nowrap" }}>
            {item}
            <span style={{ width:"4px", height:"4px", borderRadius:"50%", background:EO.teal, flexShrink:0, display:"inline-block" }} />
          </span>
        ))}
      </div>
      <style>{`@keyframes ticker { 0%{transform:translateX(0)} 100%{transform:translateX(-50%)} }`}</style>
    </div>
  );
}

/* ═══════════════════════════════════════════════════
   PROBLEMA
═══════════════════════════════════════════════════ */
function ProblemaSection() {
  const bullets = [
    "Prospectos que llegan, pero no se contactan a tiempo.",
    "Campañas que generan actividad, pero no oportunidades reales.",
    "Equipos comerciales sin criterios claros de avance.",
    "Propuestas que dependen demasiado del vendedor.",
    "Clientes que compran una vez, pero no regresan.",
    "Indicadores aislados que no explican dónde se pierde el crecimiento.",
  ];
  return (
    <section style={{ background:EO.white, padding:"8rem 3.5rem" }} id="problema">
      <Label>El diagnóstico</Label>
      <SecHeading>
        Cuando marketing y ventas<br />no están alineados, el<br />crecimiento se vuelve{" "}
        <span style={{ color:EO.teal }}>frágil</span>
      </SecHeading>
      <div style={{ display:"grid", gridTemplateColumns:"1fr 1fr", gap:"6rem", marginTop:"4rem" }}>
        <div>
          <p style={{ fontSize:"0.95rem", fontWeight:300, lineHeight:1.8, color:EO.muted, marginBottom:"1.25rem" }}>
            En muchas empresas, marketing genera visibilidad, ventas atiende como puede y la operación resuelve las consecuencias.
          </p>
          <p style={{ fontSize:"0.95rem", fontWeight:300, lineHeight:1.8, color:EO.muted, marginBottom:"2rem" }}>
            Eso provoca fugas difíciles de detectar mientras operas.
          </p>
          <div style={{ borderTop:`1px solid ${EO.border}`, paddingTop:"1.5rem", fontSize:"0.92rem", fontWeight:700, lineHeight:1.6, color:EO.dark }}>
            Eje Ocho trabaja sobre esa desconexión.<br />
            <span style={{ color:EO.teal2, fontWeight:300 }}>No hacemos acciones sueltas. Construimos sistemas comerciales alineados.</span>
          </div>
        </div>
        <div style={{ background:EO.bg, padding:"2.75rem", borderLeft:`3px solid ${EO.teal}` }}>
          <p style={{ fontSize:"0.62rem", fontWeight:700, letterSpacing:"0.2em", textTransform:"uppercase", color:EO.teal2, marginBottom:"1.75rem" }}>Señales de desalineación</p>
          <ul style={{ listStyle:"none", display:"flex", flexDirection:"column", gap:"1rem" }}>
            {bullets.map((b, i) => (
              <li key={i} style={{ display:"flex", gap:"1rem", alignItems:"flex-start", fontSize:"0.88rem", lineHeight:1.55, color:EO.dark }}>
                <span style={{ width:"6px", height:"6px", borderRadius:"50%", background:EO.teal, flexShrink:0, marginTop:"0.45rem", display:"block" }} />
                {b}
              </li>
            ))}
          </ul>
        </div>
      </div>
    </section>
  );
}

/* ═══════════════════════════════════════════════════
   QUÉ ES
═══════════════════════════════════════════════════ */
function QueEsSection() {
  return (
    <section style={{ background:EO.dark, padding:"9rem 3.5rem", position:"relative", overflow:"hidden" }}>
      {/* deco 8 */}
      <span aria-hidden="true" style={{ position:"absolute", right:"-4rem", top:"50%", transform:"translateY(-50%)", fontFamily:"'Yeseva One',serif", fontSize:"clamp(28rem,45vw,60rem)", lineHeight:1, color:"transparent", WebkitTextStroke:"1px rgba(4,204,181,0.05)", pointerEvents:"none", userSelect:"none" }}>8</span>
      <div style={{ maxWidth:"820px", position:"relative", zIndex:1 }}>
        <Label>Qué es Eje Ocho</Label>
        <SecHeading style={{ color:EO.white, marginBottom:"2rem" }}>
          Eje Ocho es el punto<br />donde el crecimiento<br />se ordena
        </SecHeading>
        <p style={{ fontSize:"1rem", fontWeight:300, lineHeight:1.8, color:"rgba(255,255,255,0.5)", marginBottom:"1.25rem" }}>
          Eje Ocho es un modelo de trabajo diseñado para empresas que necesitan crecer con más estructura, mejor conversión y mayor visibilidad sobre su proceso comercial.
        </p>
        <p style={{ fontSize:"1rem", fontWeight:300, lineHeight:1.8, color:"rgba(255,255,255,0.5)", marginBottom:"1.25rem" }}>
          Trabajamos sobre <strong style={{ color:EO.teal }}>7 ejes operativos</strong> que ordenan las piezas clave del crecimiento.
        </p>
        <p style={{ fontSize:"1rem", fontWeight:300, lineHeight:1.8, color:"rgba(255,255,255,0.5)" }}>
          El <strong style={{ color:EO.teal }}>octavo eje es la orquestación del sistema</strong>: la integración que conecta marketing, ventas y experiencia del cliente para que cada acción tenga propósito, seguimiento y medición.
        </p>
      </div>
    </section>
  );
}

/* ═══════════════════════════════════════════════════
   LOS 8 EJES
═══════════════════════════════════════════════════ */
const EJES = [
  { n:"01", title:"Arquitectura de posicionamiento", desc:"Definimos a quién le vendes, qué problema resuelves, cómo te diferencias y qué mensaje debe sostener tu estrategia comercial." },
  { n:"02", title:"Activación de demanda", desc:"Diseñamos acciones para atraer prospectos desde canales digitales mediante campañas, contenido, segmentación y mensajes alineados al mercado." },
  { n:"03", title:"Conversión digital", desc:"Convertimos tráfico en oportunidades reales mediante páginas de aterrizaje, formularios, automatizaciones iniciales y flujos de captura." },
  { n:"04", title:"Gestión de oportunidades", desc:"Estructuramos el primer contacto, la calificación, el seguimiento y la priorización de prospectos para evitar que las oportunidades se pierdan." },
  { n:"05", title:"Proceso comercial", desc:"Diseñamos el embudo de ventas, las etapas comerciales, los criterios de avance, el uso del CRM y los indicadores clave del equipo comercial." },
  { n:"06", title:"Conversión estratégica", desc:"Fortalecemos el argumento comercial, el manejo de objeciones, la propuesta y la metodología de cierre." },
  { n:"07", title:"Experiencia del cliente", desc:"Ordenamos el inicio de la relación, el seguimiento posterior a la venta, la medición de satisfacción y las oportunidades de recompra o expansión." },
  { n:"08", title:"Orquestación del sistema", desc:"Integramos los 7 ejes en un sistema medible para tomar mejores decisiones, detectar fugas y optimizar el crecimiento comercial.", special:true },
];

function EjesSection() {
  return (
    <section id="ejes" style={{ background:EO.bg, padding:"8rem 3.5rem" }}>
      <div style={{ display:"grid", gridTemplateColumns:"1fr 1fr", gap:"4rem", alignItems:"end", marginBottom:"5rem" }}>
        <div>
          <Label>El modelo</Label>
          <SecHeading>Los 8 ejes del<br />crecimiento comercial</SecHeading>
        </div>
        <p style={{ fontSize:"0.9rem", fontWeight:300, lineHeight:1.75, color:EO.muted, paddingBottom:"0.5rem" }}>
          Cada eje representa un área crítica de tu sistema comercial. Trabajamos todos en conjunto para eliminar las fugas de crecimiento.
        </p>
      </div>
      <div style={{ display:"grid", gridTemplateColumns:"repeat(4,1fr)", gap:"1.5px" }}>
        {EJES.map((e) => (
          <EjeCard key={e.n} {...e} />
        ))}
      </div>
    </section>
  );
}

function EjeCard({ n, title, desc, special }: { n:string; title:string; desc:string; special?:boolean }) {
  const [hov, setHov] = React.useState(false);
  const bg = special
    ? hov ? EO.dark : EO.teal
    : hov ? EO.dark : EO.white;
  const numColor = special
    ? hov ? "rgba(4,204,181,0.12)" : "rgba(46,60,65,0.1)"
    : hov ? "rgba(4,204,181,0.08)" : "rgba(46,60,65,0.07)";
  const titleColor = special ? (hov ? EO.teal : EO.dark) : (hov ? EO.teal : EO.dark);
  const descColor = hov ? "rgba(255,255,255,0.45)" : (special ? "rgba(46,60,65,0.6)" : EO.muted);
  return (
    <div
      onMouseEnter={() => setHov(true)}
      onMouseLeave={() => setHov(false)}
      style={{ background:bg, padding:"2.5rem", position:"relative", cursor:"pointer", transition:"background 0.4s", overflow:"hidden", borderBottom:`${hov ? 3 : 0}px solid ${EO.teal}` }}
    >
      <div style={{ fontFamily:"'Yeseva One',serif", fontSize:"4rem", lineHeight:1, color:numColor, marginBottom:"1.5rem", transition:"color 0.4s" }}>{n}</div>
      <div style={{ fontSize:"0.78rem", fontWeight:700, letterSpacing:"0.1em", textTransform:"uppercase", color:titleColor, marginBottom:"0.85rem", transition:"color 0.4s" }}>{title}</div>
      <p style={{ fontSize:"0.82rem", fontWeight:300, lineHeight:1.65, color:descColor, transition:"color 0.4s" }}>{desc}</p>
    </div>
  );
}

/* ═══════════════════════════════════════════════════
   MADUREZ
═══════════════════════════════════════════════════ */
const NIVELES = [
  { badge:"Nivel 1", title:"Fundamentos", borderColor:EO.ltblue, desc:"Para empresas que necesitan ordenar lo básico: claridad de mensaje, canales iniciales, seguimiento comercial, embudo simple e indicadores mínimos.", ideal:"tienes ventas, pero dependen demasiado del dueño, de recomendaciones o de esfuerzos poco estructurados." },
  { badge:"Nivel 2", title:"Optimización", borderColor:EO.teal2, desc:"Para empresas que ya operan, pero necesitan mejorar eficiencia, segmentación, conversión, seguimiento, CRM y control comercial.", ideal:"ya generan prospectos, pero pierden oportunidades por falta de proceso, medición o disciplina comercial." },
  { badge:"Nivel 3", title:"Escalamiento", borderColor:EO.teal, desc:"Para empresas con base comercial que buscan crecer con mayor predictibilidad, automatización, tableros, estrategia multicanal y gestión avanzada.", ideal:"quieren escalar inversión, equipo comercial y crecimiento sin perder control." },
];

function MadurezSection() {
  return (
    <section style={{ background:EO.white, padding:"8rem 3.5rem" }}>
      <Label>Adaptado a tu empresa</Label>
      <SecHeading>El mismo sistema, adaptado<br />al nivel de madurez<br />de tu empresa</SecHeading>
      <p style={{ fontSize:"0.9rem", fontWeight:300, lineHeight:1.75, color:EO.muted, maxWidth:"520px", marginTop:"1rem", marginBottom:"4rem" }}>
        No todas las empresas necesitan lo mismo. Por eso trabajamos los mismos 8 ejes en tres niveles de profundidad.
      </p>
      <div style={{ display:"grid", gridTemplateColumns:"repeat(3,1fr)", gap:"1.5px" }}>
        {NIVELES.map((n) => (
          <div key={n.badge} style={{ background:EO.bg, padding:"3rem 2.75rem", borderTop:`4px solid ${n.borderColor}` }}>
            <span style={{ display:"inline-block", fontSize:"0.6rem", fontWeight:700, letterSpacing:"0.2em", textTransform:"uppercase", padding:"0.35rem 0.85rem", background:"rgba(80,133,144,0.12)", color:EO.teal2, marginBottom:"1.75rem" }}>{n.badge}</span>
            <h3 style={{ fontFamily:"'Yeseva One',serif", fontSize:"2rem", color:EO.dark, marginBottom:"1rem" }}>{n.title}</h3>
            <p style={{ fontSize:"0.88rem", fontWeight:400, lineHeight:1.7, color:EO.muted, marginBottom:"1.75rem" }}>{n.desc}</p>
            <div style={{ fontSize:"0.8rem", fontWeight:300, lineHeight:1.6, color:EO.dark, padding:"1.1rem", background:EO.white, borderLeft:`2px solid ${EO.teal}` }}>
              <strong style={{ display:"block", fontSize:"0.62rem", fontWeight:700, letterSpacing:"0.16em", textTransform:"uppercase", color:EO.teal2, marginBottom:"0.4rem" }}>Ideal si…</strong>
              {n.ideal}
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}

/* ═══════════════════════════════════════════════════
   PROCESO
═══════════════════════════════════════════════════ */
const PASOS = [
  { n:"01", title:"Diagnóstico Eje Ocho", desc:"Evaluamos el estado actual de tus 8 ejes: posicionamiento, demanda, conversión digital, gestión de oportunidades, proceso comercial, conversión estratégica, experiencia e integración." },
  { n:"02", title:"Mapa de oportunidades", desc:"Identificamos dónde se están perdiendo prospectos, ventas, tiempo o rentabilidad. Visualizamos el impacto real de cada fuga en tu crecimiento." },
  { n:"03", title:"Plan por nivel de madurez", desc:"Definimos si tu empresa necesita fundamentos, optimización o escalamiento. El plan es específico, no genérico." },
  { n:"04", title:"Implementación", desc:"Construimos los procesos, activos, herramientas, mensajes, tableros y rutinas necesarias para operar el sistema comercial." },
  { n:"05", title:"Medición y mejora", desc:"Damos seguimiento a indicadores para ajustar lo que no está funcionando y fortalecer lo que sí genera resultados medibles." },
];

function ProcesoSection() {
  return (
    <section id="proceso" style={{ background:EO.bgAlt, padding:"8rem 3.5rem" }}>
      <div style={{ display:"grid", gridTemplateColumns:"1fr 1fr", gap:"4rem", alignItems:"end", marginBottom:"4rem" }}>
        <div>
          <Label>Cómo trabajamos</Label>
          <SecHeading>De diagnóstico<br />a sistema comercial</SecHeading>
        </div>
        <p style={{ fontSize:"0.9rem", fontWeight:300, lineHeight:1.75, color:EO.muted }}>
          Cinco pasos claros que llevan tu empresa desde donde está hoy hasta un sistema de crecimiento que funciona de forma autónoma.
        </p>
      </div>
      <div style={{ display:"flex", flexDirection:"column" }}>
        {PASOS.map((p, i) => <PasoRow key={p.n} {...p} last={i === PASOS.length - 1} />)}
      </div>
    </section>
  );
}

function PasoRow({ n, title, desc, last }: { n:string; title:string; desc:string; last:boolean }) {
  const [hov, setHov] = React.useState(false);
  return (
    <div
      onMouseEnter={() => setHov(true)}
      onMouseLeave={() => setHov(false)}
      style={{ display:"grid", gridTemplateColumns:"4rem 1fr", gap:"2.5rem", alignItems:"start", padding:`2.5rem ${hov ? "0 2.5rem 2.5rem 1rem" : "2.5rem"}`, borderTop:`1px solid ${EO.border}`, borderBottom: last ? `1px solid ${EO.border}` : "none", background: hov ? "rgba(4,204,181,0.03)" : "transparent", transition:"all 0.3s", cursor:"default" }}
    >
      <div style={{ fontFamily:"'Yeseva One',serif", fontSize:"2.25rem", color:EO.teal, lineHeight:1 }}>{n}</div>
      <div>
        <div style={{ fontSize:"0.88rem", fontWeight:700, letterSpacing:"0.08em", textTransform:"uppercase", color:EO.dark, marginBottom:"0.6rem" }}>{title}</div>
        <p style={{ fontSize:"0.85rem", fontWeight:300, lineHeight:1.7, color:EO.muted }}>{desc}</p>
      </div>
    </div>
  );
}

/* ═══════════════════════════════════════════════════
   PROPUESTA DE VALOR
═══════════════════════════════════════════════════ */
const VALOR_ITEMS = [
  { key:"El mensaje",         value:"atrae al cliente correcto." },
  { key:"La campaña",         value:"genera demanda útil." },
  { key:"El formulario",      value:"captura información clave." },
  { key:"El equipo comercial",value:"califica con criterios claros." },
  { key:"La venta",           value:"avanza con contexto." },
  { key:"El CRM",             value:"registra el proceso." },
  { key:"La experiencia",     value:"sostiene la relación." },
  { key:"La dirección",       value:"toma decisiones con datos." },
];

function ValorSection() {
  return (
    <section style={{ background:EO.dark, padding:"9rem 3.5rem" }}>
      <div style={{ display:"grid", gridTemplateColumns:"1fr 1fr", gap:"6rem", alignItems:"start" }}>
        <div>
          <Label>Por qué Eje Ocho</Label>
          <SecHeading style={{ color:EO.white, marginTop:"1rem" }}>
            Integramos marketing,<br />ventas y servicio al<br />cliente en un sistema
          </SecHeading>
          <p style={{ marginTop:"2rem", fontSize:"0.9rem", fontWeight:300, lineHeight:1.8, color:"rgba(255,255,255,0.4)" }}>
            Nuestra propuesta no es hacer más marketing ni presionar más al equipo de ventas. Es construir un sistema donde cada pieza cumple su función y se mide con claridad.
          </p>
        </div>
        <div style={{ display:"flex", flexDirection:"column" }}>
          {VALOR_ITEMS.map((v, i) => (
            <div key={i} style={{ display:"flex", gap:"1.25rem", alignItems:"flex-start", padding:"1.25rem 0", borderBottom:`1px solid rgba(255,255,255,0.06)`, borderTop: i===0 ? `1px solid rgba(255,255,255,0.06)` : "none" }}>
              <span style={{ width:"8px", height:"8px", borderRadius:"50%", background:EO.teal, flexShrink:0, marginTop:"0.4rem", display:"block" }} />
              <p style={{ fontSize:"0.88rem", fontWeight:400, lineHeight:1.6, color:"rgba(255,255,255,0.65)" }}>
                <strong style={{ color:EO.teal }}>{v.key}</strong> {v.value}
              </p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

/* ═══════════════════════════════════════════════════
   PARA QUIÉN
═══════════════════════════════════════════════════ */
function QuienesSection() {
  const si = [
    "Ya invierten o quieren invertir en marketing digital.",
    "Reciben prospectos, pero no todos se atienden bien.",
    "Quieren profesionalizar su área comercial.",
    "Necesitan implementar o mejorar su CRM.",
    "Buscan convertir más oportunidades en clientes.",
    "Quieren entender qué parte del embudo está fallando.",
    "Necesitan crecer sin depender solo del dueño o de vendedores estrella.",
  ];
  const no = [
    "Solo buscas publicaciones en redes sociales.",
    "Quieres resultados sin ajustar procesos internos.",
    "No tienes disposición para medir, revisar y corregir.",
    "No quieres registrar información comercial.",
    "No estás dispuesto a alinear marketing, ventas y operación.",
  ];
  return (
    <section id="quienes" style={{ background:EO.white, padding:"8rem 3.5rem" }}>
      <Label>Nuestro perfil de cliente</Label>
      <SecHeading>
        Eje Ocho es para empresas<br />que quieren crecer<br />con <span style={{ color:EO.teal }}>estructura</span>
      </SecHeading>
      <div style={{ display:"grid", gridTemplateColumns:"1fr 1fr", gap:"1.5px", marginTop:"4rem" }}>
        <div style={{ background:EO.bg, padding:"3.5rem", borderTop:`4px solid ${EO.teal}` }}>
          <h3 style={{ fontFamily:"'Yeseva One',serif", fontSize:"1.75rem", color:EO.dark, marginBottom:"0.5rem" }}>Para quién sí es</h3>
          <p style={{ fontSize:"0.8rem", fontWeight:300, color:EO.muted, marginBottom:"2rem" }}>Empresas que ya venden o están listas para vender de forma más ordenada:</p>
          <ul style={{ listStyle:"none", display:"flex", flexDirection:"column", gap:"0.85rem" }}>
            {si.map((s,i) => (
              <li key={i} style={{ display:"flex", gap:"0.85rem", alignItems:"flex-start", fontSize:"0.85rem", lineHeight:1.55, color:EO.dark }}>
                <span style={{ width:"6px", height:"6px", borderRadius:"50%", background:EO.teal, flexShrink:0, marginTop:"0.42rem", display:"block" }} />
                {s}
              </li>
            ))}
          </ul>
        </div>
        <div style={{ background:EO.bgAlt, padding:"3.5rem", borderTop:`4px solid ${EO.ltblue}` }}>
          <h3 style={{ fontFamily:"'Yeseva One',serif", fontSize:"1.75rem", color:EO.dark, marginBottom:"0.5rem" }}>Para quién no es</h3>
          <p style={{ fontSize:"0.8rem", fontWeight:300, color:EO.muted, marginBottom:"2rem" }}>Algo que tenemos claro: no somos la opción correcta para todos.</p>
          <ul style={{ listStyle:"none", display:"flex", flexDirection:"column", gap:"0.85rem" }}>
            {no.map((s,i) => (
              <li key={i} style={{ display:"flex", gap:"0.85rem", alignItems:"flex-start", fontSize:"0.85rem", lineHeight:1.55, color:EO.dark }}>
                <span style={{ width:"6px", height:"6px", borderRadius:"50%", background:EO.ltblue, flexShrink:0, marginTop:"0.42rem", display:"block" }} />
                {s}
              </li>
            ))}
          </ul>
          <div style={{ marginTop:"2rem", padding:"1.1rem", background:EO.white, borderLeft:`2px solid ${EO.ltblue}`, fontSize:"0.8rem", fontWeight:300, lineHeight:1.65, color:EO.muted }}>
            El crecimiento estructurado requiere participación, datos y disciplina.
          </div>
        </div>
      </div>
    </section>
  );
}

/* ═══════════════════════════════════════════════════
   CTA
═══════════════════════════════════════════════════ */
function CtaSection() {
  return (
    <section id="diagnostico" style={{ background:EO.teal, padding:"9rem 3.5rem", textAlign:"center", position:"relative", overflow:"hidden" }}>
      <span aria-hidden="true" style={{ position:"absolute", bottom:"-6rem", left:"50%", transform:"translateX(-50%)", fontFamily:"'Yeseva One',serif", fontSize:"clamp(18rem,28vw,40rem)", lineHeight:1, color:"transparent", WebkitTextStroke:"2px rgba(46,60,65,0.07)", whiteSpace:"nowrap", pointerEvents:"none", userSelect:"none" }}>8</span>
      <div style={{ position:"relative", zIndex:1, maxWidth:"720px", margin:"0 auto" }}>
        <Label>Primer paso</Label>
        <SecHeading style={{ color:EO.dark, margin:"1rem 0 1.5rem" }}>
          Descubre en qué eje<br />se está fugando<br />tu crecimiento
        </SecHeading>
        <p style={{ fontSize:"0.95rem", fontWeight:300, lineHeight:1.75, color:"rgba(46,60,65,0.65)", marginBottom:"3rem" }}>
          Responde un diagnóstico breve y conoce si tu empresa necesita fortalecer fundamentos, optimizar su sistema comercial o prepararse para escalar.
        </p>
        <a
          href="mailto:hola@ejeocho.com"
          style={{ display:"inline-block", fontSize:"0.72rem", fontWeight:700, letterSpacing:"0.14em", textTransform:"uppercase", textDecoration:"none", color:EO.white, background:EO.dark, padding:"1.2rem 3rem", transition:"background 0.25s, transform 0.2s" }}
          onMouseOver={e => { (e.target as HTMLElement).style.transform = "translateY(-3px)"; }}
          onMouseOut={e => { (e.target as HTMLElement).style.transform = "none"; }}
        >
          Iniciar diagnóstico Eje Ocho
        </a>
        <p style={{ marginTop:"1.5rem", fontSize:"0.72rem", fontWeight:300, color:"rgba(46,60,65,0.5)" }}>
          Al finalizar podremos identificar si tu empresa es candidata para una revisión estratégica.
        </p>
      </div>
    </section>
  );
}

/* ═══════════════════════════════════════════════════
   CIERRE
═══════════════════════════════════════════════════ */
function CierreSection() {
  return (
    <section style={{ background:EO.dark, padding:"9rem 3.5rem", textAlign:"center", position:"relative", overflow:"hidden" }}>
      <span aria-hidden="true" style={{ position:"absolute", bottom:"-4rem", right:"-3rem", fontFamily:"'Yeseva One',serif", fontSize:"clamp(16rem,22vw,30rem)", lineHeight:1, color:"transparent", WebkitTextStroke:"1px rgba(4,204,181,0.06)", pointerEvents:"none", userSelect:"none" }}>sistema</span>
      <div style={{ position:"relative", zIndex:1, maxWidth:"700px", margin:"0 auto" }}>
        <Label>Nuestra convicción</Label>
        <h2 style={{ fontFamily:"'Yeseva One',serif", fontSize:"clamp(2rem,4.5vw,4rem)", lineHeight:1.12, color:EO.white, margin:"1rem 0 2rem" }}>
          No se trata de hacer más.<br />Se trata de{" "}
          <span style={{ color:EO.teal }}>conectar mejor.</span>
        </h2>
        <p style={{ fontSize:"0.92rem", fontWeight:300, lineHeight:1.8, color:"rgba(255,255,255,0.4)", marginBottom:"1.5rem" }}>
          Cuando marketing, ventas y experiencia del cliente trabajan separados, el crecimiento se vuelve frágil.
        </p>
        <p style={{ fontSize:"1rem", fontWeight:400, lineHeight:1.7, color:"rgba(255,255,255,0.65)", fontStyle:"italic", marginBottom:"3rem" }}>
          Cuando se integran en un sistema, cada oportunidad tiene seguimiento, cada decisión tiene datos y cada acción tiene dirección.{" "}
          <span style={{ color:EO.teal, fontStyle:"normal", fontWeight:700 }}>Eso es Eje Ocho.</span>
        </p>
        <a
          href="#diagnostico"
          style={{ display:"inline-block", fontSize:"0.72rem", fontWeight:700, letterSpacing:"0.14em", textTransform:"uppercase", textDecoration:"none", color:EO.dark, background:EO.teal, padding:"1.2rem 3rem", transition:"background 0.25s, transform 0.2s" }}
          onMouseOver={e => { (e.target as HTMLElement).style.background = EO.yellow; }}
          onMouseOut={e => { (e.target as HTMLElement).style.background = EO.teal; }}
        >
          Quiero conocer mi diagnóstico
        </a>
      </div>
    </section>
  );
}

/* ═══════════════════════════════════════════════════
   FOOTER
═══════════════════════════════════════════════════ */
function Footer() {
  const links = ["El problema","Los 8 ejes","Proceso","Para quién","Diagnóstico"];
  const ids    = ["problema","ejes","proceso","quienes","diagnostico"];
  return (
    <footer style={{ background:EO.bg, padding:"5rem 3.5rem 3rem", borderTop:`1px solid ${EO.border}` }}>
      <div style={{ display:"grid", gridTemplateColumns:"2fr 1fr 1fr", gap:"5rem", marginBottom:"4rem" }}>
        <div>
          <div style={{ fontFamily:"'Yeseva One',serif", fontSize:"1.5rem", color:EO.dark, marginBottom:"0.4rem" }}>
            Eje<span style={{ color:EO.teal }}>.</span>Ocho
          </div>
          <div style={{ fontSize:"0.75rem", color:EO.muted, marginBottom:"1.5rem" }}>Sistema de crecimiento comercial para empresas</div>
          <p style={{ fontSize:"0.82rem", fontWeight:300, lineHeight:1.7, color:EO.muted, maxWidth:"280px" }}>
            Integramos marketing, ventas y experiencia del cliente en un sistema medible para generar demanda, convertir oportunidades y crecer con estructura.
          </p>
        </div>
        <div>
          <p style={{ fontSize:"0.62rem", fontWeight:700, letterSpacing:"0.22em", textTransform:"uppercase", color:EO.dark, marginBottom:"1.5rem" }}>Navegación</p>
          <ul style={{ listStyle:"none", display:"flex", flexDirection:"column", gap:"0.85rem" }}>
            {links.map((l,i) => (
              <li key={l}>
                <a href={`#${ids[i]}`} style={{ fontSize:"0.82rem", color:EO.muted, textDecoration:"none" }}
                  onMouseOver={e => (e.target as HTMLElement).style.color = EO.teal}
                  onMouseOut={e => (e.target as HTMLElement).style.color = EO.muted}
                >{l}</a>
              </li>
            ))}
          </ul>
        </div>
        <div>
          <p style={{ fontSize:"0.62rem", fontWeight:700, letterSpacing:"0.22em", textTransform:"uppercase", color:EO.dark, marginBottom:"1.5rem" }}>Contacto</p>
          <ul style={{ listStyle:"none", display:"flex", flexDirection:"column", gap:"0.85rem" }}>
            {["hola@ejeocho.com","LinkedIn","Instagram"].map(l => (
              <li key={l}>
                <a href={l.includes("@") ? `mailto:${l}` : "#"} style={{ fontSize:"0.82rem", color:EO.muted, textDecoration:"none" }}
                  onMouseOver={e => (e.target as HTMLElement).style.color = EO.teal}
                  onMouseOut={e => (e.target as HTMLElement).style.color = EO.muted}
                >{l}</a>
              </li>
            ))}
          </ul>
        </div>
      </div>
      <div style={{ display:"flex", justifyContent:"space-between", alignItems:"center", paddingTop:"2rem", borderTop:`1px solid rgba(46,60,65,0.06)` }}>
        <span style={{ fontSize:"0.68rem", color:EO.muted }}>© 2026 Eje Ocho. Todos los derechos reservados.</span>
        <div style={{ display:"flex", gap:"2rem" }}>
          {["LinkedIn","Instagram"].map(s => (
            <a key={s} href="#" style={{ fontSize:"0.62rem", fontWeight:700, letterSpacing:"0.14em", textTransform:"uppercase", color:EO.muted, textDecoration:"none" }}
              onMouseOver={e => (e.target as HTMLElement).style.color = EO.teal}
              onMouseOut={e => (e.target as HTMLElement).style.color = EO.muted}
            >{s}</a>
          ))}
        </div>
      </div>
    </footer>
  );
}
