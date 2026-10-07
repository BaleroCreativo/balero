# Lista de revisión visual

Marca cada punto como OK, Corregir o N/A por slide. Escribe en el informe solo lo que falle.

## Composición
- [ ] Ningún texto queda debajo de una ilustración, ícono, logo o elemento de interfaz.
- [ ] Rótulos pequeños (kicker, "LECCIÓN N", "PASO N") están visibles y no tapados.
- [ ] Pie y línea de fuente no chocan con el llamado a la acción ni con el ícono del cierre.
- [ ] Texto, logo, puntos de progreso e ilustraciones quedan dentro de los márgenes (8 % laterales y 6 % verticales); solo se acepta sangrado intencional en portada y cierre.
- [ ] Una idea y una ilustración por slide.
- [ ] Hay un punto de entrada claro para el ojo, que no compite con la ilustración.
- [ ] Los slides consecutivos alternan composición y fondo; no se ven todos iguales.

## Texto
- [ ] No hay palabras cortadas ni líneas de una sola palabra (viudas) en titulares.
- [ ] El cuerpo cabe sin reducir la fuente por debajo de lo legible en teléfono.
- [ ] Contraste suficiente. El índigo sobre lavanda solo en texto grande (40 px o más).
- [ ] Ortografía y acentos correctos; símbolos (flechas, ÷, ×) se ven en la fuente de marca.
- [ ] El texto coincide con el guion aprobado y los datos con su redacción permitida (por ejemplo, "según reportes").
- [ ] Si el hook promete un número, el carrusel desarrolla ese número.

## Marca
- [ ] Colores y fuentes de la ficha del cliente; nada de píldoras, botones ni números decorativos de fondo (en Balero).
- [ ] Ilustraciones del estilo definido, sin texto ni logos ajenos.
- [ ] Ilustraciones de baja resolución marcadas como borrador de IA.
- [ ] Logo en su lugar y tamaño.

## Portada
- [ ] La promesa se entiende en un segundo a tamaño de teléfono.
- [ ] Contraste fuerte entre frase principal y apoyo.
- [ ] Un elemento rompe la cuadrícula sin tapar texto.
- [ ] No se parece demasiado a la portada de la pieza anterior.

## Archivos
- [ ] PNG con el tamaño exacto (por ejemplo, 2160×2880).
- [ ] PDF con solo Poppins y Source Sans (comando `pdffonts`).
- [ ] Nombres de archivo ordenados (`<fecha>-1.png`, `<fecha>-2.png`, …).

## Problemas reales de octubre de 2026 (referencia)
| Problema | Cómo se resolvió |
|---|---|
| Línea de fuente del cierre envolvía y pisaba el llamado a la acción y el ícono | Acortar a "Fuente: Search Engine Journal." |
| Rótulo "PASO 2" oculto tras el ícono de una ruta | `layout: "bottom"`, `text_y` 230, `ill_w` 440, `title_px` 110 |
| Ícono de calculadora tapaba el cuerpo | Acortar el cuerpo, `ill_w` 400 y `body_px` 48 |
| Portada con elementos de texto superpuestos | Rediseño tipo póster: titular grande, caja de color en la palabra clave, ilustración que sangra por el borde |
