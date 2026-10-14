# Daniela Rubio — Design Language

Marca personal de especialista en paid media (Meta Ads, Google Ads).
Aplica a: sitio web (`daniela-rubio.html`) y posts en redes.

## Dirección

- **Filosofía:** point-of-view-first. La marca defiende una postura sobre cómo se hace paid media; el estilo la sirve.
- **Tema:** *precisa + directa + editorial.* Revista de economía con tus resultados como titulares (A), con la escala monumental de un cartel (C) como firma.
- **Arquetipo:** Sage (credibilidad, expertise) + toque editorial de Outlaw (riesgo, postura).
- **Percepción buscada:** confianza, expertise, credibilidad. Público: empleadores, directores de marketing, comerciales, dueños de empresa.
- **Arquitectura:** una sola marca (branded house). El nombre es la marca. Productos nuevos se nombran de forma descriptiva bajo "Daniela Rubio".

## Elementos fijos / variables

| Fijos (nunca cambian) | Variables (cambian por pieza) |
|---|---|
| Wordmark "Daniela Rubio" en serif, sin símbolo | Cuál es la cifra o la frase protagonista |
| Paleta de 4 colores (abajo) | Fondo de la pieza: papel, tinta o acento |
| Reglas (líneas) gruesas de tinta como estructura | Composición dentro de la grilla |
| Serif para titulares, sans para texto, etiquetas en mayúsculas | Recorte de la cifra gigante (siempre cortada por un borde) |
| Esquinas rectas (radio 0) | Retrato vs. captura de resultados como imagen |

## Color

| Token | Hex | Uso |
|---|---|---|
| `paper` | `#F2EBDC` | Fondo principal (papel cálido, no blanco puro) |
| `paper-2` | `#E6DCC8` | Fondo secundario, hover de filas |
| `ink` | `#14110F` | Texto, reglas, fondos oscuros |
| `accent` | `#C8401A` | Bloques grandes, cifras gigantes, subrayados. **Un solo acento** |
| `accent-deep` | `#A93212` | Acento para texto pequeño sobre papel |
| `accent-light` | `#E2562B` | Acento para texto pequeño sobre tinta |
| `muted` | `#5C5249` | Texto secundario sobre papel |

**Contraste (WCAG):**

| Par | Ratio | Permitido |
|---|---|---|
| ink / paper | 15.84 | Todo texto |
| muted / paper | 6.41 | Todo texto |
| accent-deep / paper | 5.61 | Texto pequeño |
| accent-deep / paper-2 | 4.90 | Texto pequeño |
| accent-light / ink | 5.01 | Texto pequeño |
| accent / paper | 4.21 | **Solo texto grande** (≥24px, o ≥18.7px en negrita) y decoración |
| paper / accent | 4.21 | **Solo texto grande** sobre bloque de acento |
| ink / accent | 3.76 | **Solo texto grande** sobre bloque de acento |

Reglas: sin gradientes, sin degradados de texto, sin brillos ni sombras difusas. El acento nunca va en texto de cuerpo pequeño; para eso, `accent-deep` o `accent-light`.

## Tipografía

Ambas gratuitas (SIL OFL) en Google Fonts.

- **Display / titulares / cifras:** Bodoni Moda `[Google Fonts, OFL]`. Alto contraste, pesos 500–900, cursiva para la palabra clave de cada titular. Registro: autoridad editorial.
- **Texto / etiquetas / UI:** Archivo `[Google Fonts, OFL]`. Eje de ancho (75–125) para etiquetas anchas en mayúsculas. Registro: neutral y legible.
- **Fallbacks:** `'Bodoni Moda', 'Didot', 'Bodoni 72', Georgia, serif` · `'Archivo', system-ui, sans-serif`.

| Rol | Tamaño | Peso | Notas |
|---|---|---|---|
| Titular hero | `clamp(2.8rem, 10vw, 8.5rem)` | 800 | interlineado 0.92, tracking −0.03em |
| Cifra monumental | `clamp(14rem, 44vw, 40rem)` | 900 | siempre recortada por un borde |
| Titular de sección | `clamp(2rem, 5vw, 4rem)` | 700 | interlineado 1.0 |
| Texto | 1.0625rem | 400 | interlineado 1.6 |
| Etiqueta | 0.75rem | 600 | mayúsculas, tracking +0.14em, ancho 115 |

## Voz

Frases cortas. Una cifra o una postura por pieza. Cero "impulsa", "eleva", "soluciones integrales". Se habla de margen, de decisiones y de dinero ajeno bien gastado.
Postura provisional (confirmar o cambiar): **"Menos ROAS bonito. Más margen real."**

## Imagen

- **Retrato maestro:** medio cuerpo, fondo plano papel o tinta, luz dura lateral, mirada a cámara, sin sonrisa de stock. Tratamiento: alto contraste, sin filtros suaves.
- **Capturas de resultados** (Ads Manager, Google Ads) recortadas como material gráfico, con datos de clientes ocultos.
- **Prohibido:** stock, imágenes generadas pulidas, íconos de línea genéricos, emojis como decoración.

## Sistema de posts (1080 × 1350)

Margen 72px. Pie fijo: `DANIELA RUBIO — PAID MEDIA` a la izquierda y número de lámina a la derecha, en etiqueta de 0.75rem.

| Tipo | Fondo | Contenido |
|---|---|---|
| **Cifra** | Acento | Una cifra enorme recortada por el borde + una línea de contexto |
| **Postura** | Tinta | Una afirmación en serif, con una palabra en cursiva color `accent-light` |
| **Editorial** | Papel | Titular + regla gruesa + 3 puntos cortos |
| **Retrato** | Papel o tinta | Retrato en alto contraste + una frase |

## Movimiento

Sobrio: revelados y cortes. Nada de rebotes, brillos ni parallax. Respetar `prefers-reduced-motion`.

## Anti-patrones (lo que delata una identidad genérica)

- Gradientes morado/azul o terracota→dorado, blobs borrosos, nav de vidrio esmerilado.
- Tarjetas redondeadas con hover que "flota".
- Botones en píldora, etiquetas en píldora.
- Copy de relleno ("Impulsa tu marca al siguiente nivel").
- Simetría centrada en todo.
