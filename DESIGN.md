# Daniela Rubio — Design Language

Marca personal de especialista en paid media (Meta Ads, Google Ads).
Aplica a: sitio web (`daniela-rubio.html`) y posts en redes de la **marca personal Daniela Rubio**. Es independiente de la marca de su empresa (Balero Creativo), que queda fuera de este sistema.
Versiones exploradas y descartadas: `explorations/`.

## Dirección

- **Personalidad (confirmada por Daniela):** cercana, estratégica, directa.
- **Filosofía:** point-of-view-first. La marca defiende una postura sobre cómo se hace paid media y habla como ella habla.
- **Tema:** *cálida + directa + tipográfica.* Campos de color a pantalla completa, sin bordes ni tarjetas; la tipografía grande hace el trabajo.
- **Percepción buscada:** confianza, expertise, credibilidad. Público: empleadores, directores de marketing, comerciales, dueños de empresa.
- **Arquitectura:** una sola marca (branded house). El nombre es la marca.

## Fijos y variables

| Fijos (nunca cambian) | Variables (cambian por pieza) |
|---|---|
| Wordmark "Daniela Rubio" en Familjen Grotesk 700, sin símbolo | Qué color de campo domina la pieza |
| Paleta de 5 colores (abajo) | Cuál es la pregunta, cifra o frase protagonista |
| Cero bordes, cero sombras, cero tarjetas | Cuál palabra va resaltada en lima |
| Resaltador lima ladeado (-1°) sobre una palabra clave por pieza | Retrato o captura de resultados como imagen |
| Tipografía grande, apretada, alineada a la izquierda | Composición dentro del campo |

## Color

Sin ocre ni naranja-amarillo (descartados por Daniela).

| Token | Hex | Uso |
|---|---|---|
| `burnt` | `#6F1F14` | Rojo quemado: campo oscuro principal y texto sobre beige/lima |
| `brick` | `#A63A24` | Ladrillo: campo secundario, panel del retrato |
| `clay` | `#E8B7A4` | Arcilla rosada: campo suave (contacto, retratos) |
| `beige` | `#EFE6D6` | Fondo general |
| `lime` | `#C9F03B` | Verde lima: resaltador, botón secundario, números grandes |
| `ink` | `#1E0F0B` | Texto de lectura sobre beige, lima y arcilla |

**Contraste (WCAG):**

| Par | Ratio | Permitido |
|---|---|---|
| burnt / beige | 9.01 | Todo texto |
| lime / burnt | 8.51 | Todo texto |
| burnt / lime | 8.51 | Todo texto |
| beige / burnt | 9.01 | Todo texto |
| ink / lime | 14.19 | Todo texto |
| ink / clay | 10.40 | Todo texto |
| burnt / clay | 6.24 | Todo texto |
| white / brick | 6.46 | Todo texto |
| beige / brick | 5.22 | Todo texto |
| brick / beige | 5.22 | Todo texto |
| lime / brick | 4.92 | Todo texto |
| brick / clay | 3.61 | **Solo texto grande** (≥24px, o ≥18.7px en negrita) |

Reglas: sin gradientes, sin degradados de texto, sin sombras. El lima es el único color de choque: úsalo en una palabra o un elemento por pieza.

## Tipografía

Ambas gratuitas (SIL OFL) en Google Fonts.

- **Titulares y cifras:** Familjen Grotesk `[Google Fonts, OFL]`, peso 700, interlineado 0.98, tracking −0.035em.
- **Texto:** Hanken Grotesk `[Google Fonts, OFL]`, pesos 400–700, interlineado 1.65.
- **Fallbacks:** `'Familjen Grotesk', 'Helvetica Neue', Arial, sans-serif` · `'Hanken Grotesk', system-ui, sans-serif`.

| Rol | Tamaño | Notas |
|---|---|---|
| Titular hero | `clamp(2.7rem, 6.8vw, 6.4rem)` | |
| Titular de sección | `clamp(2.4rem, 6.4vw, 5.6rem)` | |
| Frase protagonista | `clamp(1.9rem, 4.4vw, 3.8rem)` | peso 600 |
| Texto | 1.0625rem | |
| Etiqueta | 0.95rem | peso 600 |

## Voz

Primera persona, frases completas, cálida y sin rodeos. Se habla de margen, de decisiones y de dinero ajeno bien gastado. Las respuestas del sitio se escriben como ella las diría en una llamada.
Cero "impulsa", "eleva", "soluciones integrales".
Titular confirmado por Daniela: **"Cada peso en pauta tiene que volver con margen."** ("con margen" va sobre el resaltador lima).

## Imagen

- **Retrato maestro:** `assets/daniela-rubio.jpg` (luz natural, fondo de plantas, blusa blanca, mirada a cámara). Se usa tal cual, sin filtros ni duotono. Para posts, recortar a medio cuerpo sobre el campo de color.
- **Capturas de resultados** (Ads Manager, Google Ads) recortadas como material gráfico, con datos de clientes ocultos.
- **Prohibido:** stock, imágenes generadas pulidas, íconos de línea genéricos, emojis como decoración.

## Sistema de posts (1080 × 1350)

Margen 80px. Pie fijo: "Daniela Rubio" en Familjen Grotesk 700 a la izquierda y número de lámina a la derecha.

| Tipo | Campo | Contenido |
|---|---|---|
| **Pregunta** | Rojo quemado | La pregunta de un cliente en lima, grande; la respuesta en beige debajo |
| **Postura** | Ladrillo | Una afirmación en beige con una palabra sobre resaltador lima |
| **Cifra** | Lima | Una cifra enorme en rojo quemado, recortada por el borde, y una línea de contexto en ink |
| **Retrato** | Arcilla | Retrato en alto contraste y una frase en rojo quemado |

## Movimiento

Mínimo: transiciones de color en hover. Sin parallax, rebotes ni brillos. Respetar `prefers-reduced-motion`.

## Anti-patrones (lo que delata una identidad genérica)

- Gradientes morado/azul o de cualquier color, blobs borrosos, nav de vidrio esmerilado.
- Bordes gruesos, sombras duras o tarjetas con hover que "flota".
- Crema + serif de display + terracota como combinación base.
- Copy de relleno ("Impulsa tu marca al siguiente nivel").
- Todo centrado y simétrico.

## Cuentas oficiales

- Instagram: `@rubiagz` · TikTok: `@rubiagz` · LinkedIn: `linkedin.com/in/daniela-rubio-gonzalez`

## Pendientes antes de publicar

- Resultados reales con cifras para los posts de "Cifra".
