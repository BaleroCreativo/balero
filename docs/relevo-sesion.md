# Relevo de sesión: marca personal de Daniela Rubio

Leer esto primero al empezar una sesión nueva. Estado al 26 de octubre de 2026.

## Reglas que no cambian
- Es la **marca personal de Daniela Rubio** (especialista en paid media, Guadalajara). **No** se mezcla con Balero Creativo: nada de "fundadora de", ni enlaces ni logos de la empresa, ni clientes con nombre.
- Voz: cercana, estratégica y directa. Primera persona, frases completas, sin emojis, sin "impulsa", "eleva" ni "soluciones integrales". Guía completa en `.claude/brand-voice-guidelines.md`.
- Titular de marca: **"Cada peso en pauta tiene que volver con margen."**
- No inventar cifras, resultados ni casos. Todo dato externo lleva fuente y la marca [VERIFICAR] hasta confirmarlo. Donde falta algo que solo ella sabe, se deja [TU EJEMPLO] o [TU CRITERIO].
- No generar imágenes si ella pide solo guiones y captions.
- Rama de trabajo: `claude/daniela-rubio-personal-site-mrpmkq`. No crear pull requests sin que lo pida.

## Qué existe y dónde
| Qué | Dónde |
|---|---|
| Sitio web (V5, paleta rojo quemado, ladrillo, arcilla, beige y lima) | `daniela-rubio.html`, `assets/daniela-rubio.jpg` |
| Sistema de diseño y tokens | `DESIGN.md` |
| Versiones exploradas y descartadas | `explorations/` |
| Guías de voz | `.claude/brand-voice-guidelines.md` |
| Estrategia de contenido de 90 días | `docs/estrategia-contenido-redes.md` |
| Calendario base (13 semanas desde el 26 oct 2026) | `docs/calendario-contenido.md` y `.csv` |
| Borradores de la semana 1 (con el carrusel del 26 oct en versión 2) | `docs/borradores-semana-1.md` |
| Plan del día de arranque y bios | `docs/hoy-26-octubre.md` |
| Competencia y pares analizados | `docs/investigacion-competidores.md`, `docs/competidores-plantilla.csv` |
| Borradores a partir de newsletters | `docs/borradores-newsletters.md` |
| Borradores a partir de blogs de Neil Patel y Felipe Vergara | `docs/borradores-blogs.md` |
| Láminas de la semana 1 (PNG y PDF) | `assets/posts/semana-1/` |

Cuentas: Instagram `@rubiagz`, TikTok `@rubiagz`, LinkedIn `linkedin.com/in/daniela-rubio-gonzalez`.

## Notion
- Página del proyecto (la que creó Daniela): https://app.notion.com/p/40533e5b02c080bc8db5fab2afabf3a8
- Cliente: https://app.notion.com/p/40533e5b02c081aeb099c96b37dc3040
- Base **Contenidos** (compartida con Balero): fuente de datos `collection://21e33e5b-02c0-814d-afbb-000b0ebd371e`. Las publicaciones de Daniela se distinguen por la relación "📂 Proyectos" = la página de arriba.
- 113 entradas: 85 del calendario base y 28 alternativas (de newsletters y blogs). Formatos: 29 carruseles, 58 posts, 26 reels.
- En la página hay una sección "Planeación de contenidos" con las vistas Calendario, Etapas y Lista por fecha, ya filtradas por el proyecto. La vista de galería sigue sin ese filtro.
- Las entradas de la semana 1 (26 al 29 oct) tienen las imágenes y el PDF en el cuerpo.
- Propiedades usadas: Nombre ("DD Mes · Día · Tema (red)"), Plataforma, Formato, Pilar de contenido, Etapa, Publicación (con hora de CDMX, -06:00), Responsable, 📂 Proyectos.
- Existe también un proyecto anterior con el mismo nombre (https://app.notion.com/p/40533e5b02c081fda4e8fc0f7b6ec60f), ahora sin entradas. No se ha borrado.

## Pendientes, en orden
1. **Regenerar las láminas del carrusel del lunes 26 oct** con el guion de 7 láminas (versión 2, con fuentes de Gartner, Meta y Avinash Kaushik). Las láminas actuales son de la versión 1. Mismo sistema de diseño (1080×1350).
2. **Alinear con esa lógica** el post de LinkedIn del martes 27 oct y el guion del video del jueves 29 oct (siguen con la lógica anterior).
3. **Resolver duplicados del calendario:** varios horarios tienen dos entradas, la del calendario base y una alternativa. Decidir cuál queda y archivar la otra.
4. **Verificar con la fuente original** antes de publicar: cifra de Gartner (7.7 % de ingresos, encuesta de 2025), guía de Meta sobre meta de costo por resultado, y los datos marcados [VERIFICAR] en los borradores de newsletters y blogs.
5. **Tres artículos no se pudieron leer** por bloqueo anti-bots: «Las 4 IAs de Meta Ads» y «La estrategia de Meta Ads que realmente funciona» (Felipe Vergara) y «AI & Paid Search» (Neil Patel). Se quitó de las piezas todo lo que solo venía de ellos.
6. **Definir el usuario "Responsable"** de las entradas de Notion: hoy es el que se usó al crearlas y no coincide con el encargado de la página nueva.
7. **Pedir a Daniela** sus datos reales: línea base de seguidores de cada red, su método real para el carrusel de LinkedIn del jueves 29, el nombre final de la oferta de entrada ("Revisión de cuenta de 20 minutos"), y resultados reales con permiso del cliente para las piezas de "Cifra".
8. **Pausas del calendario:** no hay entradas el 24, 25 y 31 de diciembre ni el 1 de enero.

## Limitaciones conocidas
- Socialinsider: el plan solo permite ventanas de 29 días y no se pueden agregar perfiles nuevos.
- Instagram no se puede abrir desde el entorno: el análisis de pares se hizo con capturas que envió Daniela.
- graphify: se instaló y se registró en un entorno que se reinicia. Para usarlo en una sesión nueva hay que conectarlo en https://claude.ai/customize/connectors antes de abrirla. El espacio que quiere usar es `balero-s-workspace`.
- Sitios de Neil Patel y Felipe Vergara: abren con `curl`, pero algunas páginas tienen verificación anti-bots. No se eludió.
