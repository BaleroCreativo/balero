# Proporción y armonía (sistema de layout "zonas")

Piloto aprobado para revisión de Daniela (nov 2026): ROAS 3 nov y WhatsApp 23 oct. Lo aprobado NO cambia (objeto 3D enorme, poco texto, portada elegida, colores, marcador amarillo, Instrument Serif solo como énfasis, barra rasgada, fondos con puntos, tipografías, contenido y cifras). Esto solo ordena proporción, ritmo, jerarquía y equilibrio. Lienzo 1080×1440, unidad base 8 px.

## Cómo se usa
Slide `"type": "zonas"` en el spec (aditivo; los tipos anteriores no cambian). Campos: `bg`, `chip` (+`chip_style:"w"`) o `kick` (línea fina Poppins Light), `title` (HTML; spans `y a l hl it`), `title_px` (88/112/144; por defecto 112), `body`, `body_w` (600 por defecto; 680 para texto largo), `table {caption, rows[{label,fig,tone:"a|y"}], note, w}`, `bar`, `note`, `icon {illustration,size S|M|L,anchor,bleed,bleed_pct,rot,dx,dy}`. Las portadas siguen en `hero` con `layers`, con los números de este documento.
QA: `python3 scripts/qa_overlap.py salida/` mide por píxeles si icono, texto, logo, puntos y pie se pisan (debe dar 0 px; en portadas la superposición calculadora/cifra es intencional).

## 1. Zonas verticales (alto 1440)
| Zona | y | Contenido |
|---|---|---|
| Cabecera | 86–186 | puntos (izq.) y logo (der.) |
| Titular | 200–~520 | fila de rótulo (alto fijo 64) + titular |
| Apoyo | ~520–750 | cuerpo, tabla o barra rasgada, nota |
| Héroe | 749–1368 (52–95 %) | icono |
| Pie | 1316–1354 | "BALERO CREATIVO" |
Columna de texto única a x = 86 (margen 8 %); ancho de texto 908 como máximo y 600 para cuerpo (680 solo si es largo).

## 2. Escala tipográfica (px)
| Nivel | px | Uso |
|---|---|---|
| Etiqueta | 32 | chip, caption de tabla, notas |
| Cuerpo | 40 | cuerpo y rótulos de fila (mínimo en celular); 48 para el apoyo de una portada |
| Línea fina | 64 | línea Poppins Light sobre el titular (portadas: 88 la fina y el titular) |
| Titular | 112 (88 si es largo; 144 si es muy corto) | Poppins ExtraBold + serif cursiva |
| Cifra | 96 (tablas); numerales de portada 600–940 | |
La línea fina y el titular cuentan como un solo nivel (octava 64/112). Máximo 3 niveles por slide: etiqueta · titular (con su línea fina) · cuerpo. Interlineado: cuerpo 1,3; titular 0,93; línea fina 1,0. Tracking −0,045 em solo en titular ExtraBold; word-spacing 0,1 em en titulares.

## 3. Espacios (múltiplos de 8)
Rótulo → titular 24 · titular → cuerpo 32 · cuerpo → tabla/barra 48 · barra → nota 24 · caption → fila 24 · fila → fila 16. Respiro mínimo icono ↔ texto 48 (en portadas ≥ 48 entre bloque de texto y pie).

## 4. Iconos
Tres tamaños por ancho visible: **S 48 % (518 px) · M 64 % (691) · L 82 % (886)**. Elegir el mayor que no pise el texto: altura libre = 1368 − (fin del texto + 48). Anclas: `br` (abajo-derecha, por defecto), `mr`, `bl` (solo iconos bajos y con tope 1290 por el pie). Sangrado por UN solo borde (`bleed` r|l|b), máximo 25 % del icono (`bleed_pct`). Los iconos altos y grandes no pueden anclarse con el borde izquierdo a menos de x = 360 si llegan a y > 1300 (chocan con el pie). Rotación ±4 a ±10°, sombra igual en todos. Equilibrio: texto arriba-izquierda, objeto abajo-derecha.

## 5. Componentes
Chip y sticker radio 12, sombra `0 8 24 rgba(0,0,0,.18)`; barra rasgada con la misma sombra (filter), padding 32/40, botón circular 80 px. Resaltador de cuerpo: padding .06em .28em, sin rotación; en titular .1em y −1,2°. En fondo índigo el énfasis del cuerpo va en amarillo (A9A4F7 sobre índigo da 2,2:1, no pasa).

## 6. 60-30-10
Fondo 60 %, objeto + texto principal 30 %, acento amarillo/índigo 10 %. Una sola zona de acento amarillo por slide (marcador o cifra, no ambos competidores).

## 7. Portadas
1 dominante (cifra gigante), 1 secundario (objeto, ≈ 48 % de ancho, sangra por un borde ≤ 25 %), 1 de apoyo (texto). Línea fina a y = 200, cifra con su borde derecho en el margen (x = 994), objeto superpuesto 40–60 px sobre la cifra, titular 88 a ≥ 64 px sobre el pie. Cifra a la derecha, objeto a la izquierda (o espejo).
