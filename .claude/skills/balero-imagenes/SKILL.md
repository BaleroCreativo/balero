---
name: balero-imagenes
description: Guía y herramientas para generar imágenes de marca de Balero Creativo (carruseles de LinkedIn e Instagram, posts, portadas). Úsala siempre que se pida crear, rediseñar o ajustar piezas gráficas de Balero, o generar ilustraciones 3D para ellas. Incluye colores, tipografías (Poppins y Source Sans Pro), márgenes, formatos, estilo de ilustración 3D, logo, reglas de lo que no se usa y un generador que produce PNG y PDF.
---

# Balero Creativo: imágenes de marca

Reglas confirmadas por la dueña de la marca durante el diseño del carrusel de LinkedIn "Lo que ya no haríamos igual" (octubre 2026). Si una petición contradice algo de aquí, gana la petición, y conviene actualizar este archivo.

## Flujo rápido
1. Define formato y plataforma (ver "Formatos").
2. Escribe el contenido en un archivo JSON (ver `scripts/example-spec.json`).
3. Prepara las tipografías una sola vez: `bash scripts/setup_fonts.sh`.
4. Genera las ilustraciones 3D (ver `references/ilustraciones-3d.md`) y recórtalas con `scripts/cutout.sh`.
5. Genera las piezas: `python3 scripts/build_carousel.py mi-spec.json salida/`.
6. Revisa la lista de verificación y entrega PDF + PNG.

## Colores
| Uso | Valor |
|---|---|
| Titular de énfasis (índigo) | `#665FE9` |
| Texto, rótulos, pie, titular oscuro | `#000000` (negro puro, decisión del 4 oct 2026) |
| Fondo de slides interiores | `#F6F5FF` (lavanda) |
| Acento amarillo (solo dentro de ilustraciones) | `#FEC72E` |
| Portada: degradado vertical | `#F4D9EE` → `#F8E6DA` → `#FFF3D6` (rosa a crema) |
| Cierre: degradado vertical | `#FFF8E3` → `#F6EEFA` |

### Fondos alternativos (4 oct 2026)
Para variar un carrusel sin salirse de la marca, cada slide acepta `"bg"` en el JSON: `lila` (plano), `lila-profundo` (lavanda que se oscurece a morado suave abajo, `#DDD9FB`), `lila-diagonal`, `blanco` (`#FAFAFA`), `portada-diagonal` y `cierre-diagonal` (los degradados de portada y cierre en ángulo). Sin `bg` se usa el fondo clásico. Combínalos alternando, por ejemplo: portada diagonal, lila profundo, blanco, lila diagonal, cierre diagonal.

El índigo sobre lavanda da 4,4:1: úsalo solo en texto grande (titulares y énfasis de 40 px o más).

## Tipografías
- **Títulos: siempre Poppins, en cualquier peso.** Incluye la línea fina de la portada y el rótulo "LECCIÓN N" (Light 300) y los titulares fuertes (ExtraBold 800, mayúsculas, interletraje −0,045 em, interlineado 1,03).
- **Párrafos y subtítulos de portada: Source Sans Pro** (Regular 400, Bold 700 para énfasis).
- El pie "BALERO CREATIVO" va en Poppins Light, en mayúsculas.
- Tamaños de referencia en 1080×1440: titular 96 px, titular portada 104 px, línea fina 80 px, párrafo 48 px, rótulo 38 px, pie 30 px.
- Titulares con `text-wrap: balance` para evitar viudas.

## Formatos y márgenes
- **Formato por defecto: 1080×1440** (carruseles). Otros: 1080×1350 (post Instagram 4:5), 1080×1920 (stories).
- **Márgenes: 8% del borde a los lados y 6% arriba y abajo, en todas las piezas, portada incluida** (86 px laterales y 86 px verticales en 1080×1440). Texto, logo, pie, puntos de progreso e ilustraciones quedan dentro del margen.
- Logo arriba a la derecha, 96 px de ancho, sobre el margen. Archivo: `assets/logo-balero.png` (negro, fondo transparente).

## Composición
- Una idea por slide y una ilustración 3D por slide.
- **Puntos de progreso: permitidos (opcionales).** Arriba a la izquierda, con su borde superior sobre la línea del margen superior (misma altura que el borde superior del logo), punto activo en índigo `#665FE9` y los demás en `#DAD7F5`. Se activan con `"progress_dots": true` en el JSON.
- Alternar composiciones en lecciones consecutivas: ilustración abajo a la derecha, e ilustración arriba a la izquierda con el texto más abajo. Evita que todos los slides se vean iguales.
- Portada: línea fina + titular fuerte en la mitad inferior, ilustración arriba a la derecha, subtítulo, "DESLIZA" con flecha larga solo en la portada.
- Cierre: pregunta en Poppins (línea fina + índigo extranegrita), oferta en Source Sans Pro (negrita, con "gratis de 15 minutos" en índigo), acción en texto plano.

## Lo que Balero NO usa
Subtítulos en forma de píldora o "pill", botones, números decorativos de fondo, ni fuentes distintas de Poppins y Source Sans Pro (cuidado con símbolos como flechas que caen a otra fuente: dibújalos en SVG).

## Ilustraciones 3D
Estilo: objetos tipo arcilla brillante e inflada, como un emoji 3D, en índigo, amarillo y blanco, fondo liso lavanda `#F6F5FF`, un solo objeto por imagen, sin texto ni logos. Prompt base y banco de objetos en `references/ilustraciones-3d.md`. Se generan con la herramienta `generate-image` de Canva (formato cuadrado) y se marcan siempre como **borrador de IA**: las miniaturas son de 200 px, y para publicar hay que descargar la versión grande desde Canva.

## Voz
Frases cortas y directas, cercanas y un poco provocadoras. Lema: "No prometemos resultados, los mostramos." No inventar cifras, nombres de clientes ni citas: lo que falte se pregunta.

## LinkedIn
- Se sube como **documento PDF** (no imágenes sueltas). El enlace no es pulsable dentro de las páginas: va en el texto de la publicación, con UTM: `?utm_source=linkedin&utm_medium=social&utm_campaign=organico`.
- Horario del plan: martes y jueves, 11 am (hora de Ciudad de México).

## Lista de verificación antes de entregar
- [ ] `pdffonts salida/*.pdf` muestra solo Poppins y SourceSansPro (ninguna otra, ni DejaVu ni serif).
- [ ] Tamaño de cada PNG exacto (p. ej. 1080×1440).
- [ ] Márgenes medidos: 8% laterales y 6% verticales en todos los slides (el script imprime la caja de contenido: debe empezar en x≈86 e y≈86 en 1080×1440).
- [ ] Ninguna ilustración pisa texto ni logo.
- [ ] Sin pills, botones ni números de fondo (los puntos de progreso sí se permiten).
- [ ] Titulares sin viudas; contraste correcto.
- [ ] Ilustraciones marcadas como borrador si son de baja resolución.

## Trampas conocidas (aprendidas)
- Si el CSS pide `font-family:'Poppins'` pero el `@font-face` se llama distinto, Chrome cae a una fuente con serifa sin avisar: verifica con `pdffonts`.
- Para PNG de tamaño exacto usa `headless_shell` con `--window-size`; el Chrome normal en modo headless recorta alto por la barra.
- Las ilustraciones de Canva llegan con fondo liso: se recortan con ImageMagick (`cutout.sh`) antes de colocarlas.
- Los enlaces de trabajo de Canva son largos: cópialos exactos al consultar el estado del trabajo.
