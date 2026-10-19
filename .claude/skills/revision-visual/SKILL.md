---
name: revision-visual
description: Revisa un carrusel o pieza gráfica ya renderizada (PNG y PDF) antes de subirla a Metricool, detecta texto encimado, íconos que tapan texto, texto cortado, jerarquía débil, portadas que no paran el scroll y violaciones de marca, y propone o aplica la corrección en el JSON del diseño hasta que quede limpia. Es la etapa 6 del sistema de contenido mensual y funciona bien como agente aparte, uno por carrusel. Úsala siempre que el usuario diga "revisa el diseño", "verifica la composición", "revisa los carruseles", "hay texto encimado", "que la portada pare el scroll" o cuando acaben de generarse imágenes nuevas, aunque no pida la revisión de forma explícita.
---

# Revisión visual

Mira las imágenes terminadas como las vería un lector que desliza rápido, y corrige lo que falle antes de que llegue a Metricool. En octubre de 2026 casi cada tanda de carruseles tuvo al menos un problema que solo se veía con la imagen delante: un rótulo oculto tras un ícono, una línea de fuente que pisaba el llamado a la acción, un ícono encima del cuerpo. Esta etapa existe porque el generador no los detecta y los textos se aprueban antes de que se vea el diseño.

## Qué entra y qué sale
- **Entra:** carpeta con los PNG (y PDF si hay) de una pieza, el JSON con el que se generaron, la ficha del cliente (marca y "lo que nunca se usa") y el guion aprobado.
- **Sale:** informe por slide (OK, Corregir o Rehacer), correcciones aplicadas al JSON, imágenes regeneradas y un veredicto final para que la persona responsable dé el visto bueno a la portada.

## Flujo

### 1. Revisiones mecánicas (rápidas)
Corre `scripts/checks.py <carpeta> [--ancho 1080 --alto 1440 --escala 2 --fuentes Poppins,SourceSans]`. Verifica tamaño exacto de cada PNG, informa dónde cae el contenido respecto a los márgenes (8 % laterales y 6 % verticales) y revisa las fuentes de los PDF contra las fuentes de la marca (`--fuentes`, por defecto Poppins y Source Sans; nombres sin espacios). Un sangrado en portada y cierre es intencional; lo demás es motivo de revisar. El script no entiende composición, así que un resultado limpio no significa que la pieza esté bien.

### 2. Mirar cada imagen, una por una
Abre cada PNG con la herramienta de lectura de imágenes y revisa la lista de `references/lista-de-revision.md`. Mira primero el slide completo y luego las zonas de riesgo: bordes, cruces entre ilustración y texto, pie y logo. No des un slide por bueno desde una miniatura.

Las cinco preguntas que más problemas atrapan:
1. ¿Algo tapa algo? (texto contra ilustración, rótulo contra ícono, pie contra llamado a la acción)
2. ¿Se lee todo, sin cortes, sin líneas viudas y con contraste suficiente?
3. ¿Hay una sola idea y una sola cosa que mira primero el ojo?
4. ¿Cumple las reglas de marca de la ficha y no usa nada de "lo que nunca se usa"?
5. ¿El texto del slide coincide con el guion aprobado y con los datos verificados?

### 3. La portada, con más exigencia
La portada decide si alguien se detiene. Evalúa:
- ¿Se entiende la promesa en un segundo, a tamaño de teléfono?
- ¿Hay contraste fuerte de tamaño y de color entre la frase principal y el resto?
- ¿Hay un elemento que rompa la cuadrícula (ilustración que sangra, caja de color en la palabra clave) sin tapar texto?
- ¿Se parece demasiado a la portada de la pieza anterior? Alternar fondo negro, índigo y claro entre piezas ayuda a que el perfil no se vea monótono.
Si la portada es correcta pero tímida, propón una variante más audaz (más grande, otro fondo, otra ilustración) y deja que la persona elija; no cambies la promesa del hook.

### 4. Corregir de forma mínima
Por cada problema, cambia lo menos posible en el JSON y vuelve a generar solo esa pieza. Los ajustes que funcionaron:
- **Ilustración tapa texto:** reducir `ill_w`, mover `text_y`, o cambiar `layout` de la lección entre `top` y `bottom`.
- **Rótulo o kicker oculto:** `layout: "bottom"` con `text_y` más alto.
- **Texto largo que choca:** acortar el cuerpo (más corto es casi siempre mejor que bajar el tamaño), reducir `body_px` o `body_w`.
- **Línea de fuente en el cierre que se desborda:** acortarla ("Fuente: Search Engine Journal.").
- **Titular que se rompe mal:** ajustar `title_px` o reescribir el titular con la persona responsable.
Cambiar palabras de un slide implica que el guion también cambie: avisa para que el texto de Notion y los captions se mantengan iguales.
Los detalles de los campos del JSON están en `balero-imagenes/SKILL.md`.

### 5. Repetir hasta limpiar, con tope
Regenera, vuelve a mirar solo lo corregido y los slides vecinos. Haz como máximo tres rondas; si una pieza sigue con problemas, dilo y pide una decisión en vez de iterar sin fin (suele significar que el guion tiene demasiado texto o que la ilustración no encaja).

### 6. Entregar
Resume en una tabla corta: slide, problema, qué se hizo, estado. Cierra con el veredicto y la pregunta de la portada (visto bueno o variante). Cuando haya visto bueno, la pieza pasa a `publicar-metricool`.

## Reglas
- No apruebes con base en el script solo ni en descripciones del JSON: la verdad está en la imagen.
- No inventes un problema para parecer minucioso. Si todo está bien, dilo.
- No cambies hook, datos ni mensaje por razones de estética sin avisar.
- No subas nada a Metricool ni a Notion desde esta etapa.

## Como agente en paralelo
Con varios carruseles, lanza un subagente por pieza con esta misma instrucción. Cada uno devuelve su informe y las correcciones propuestas; las correcciones las aplicas tú para evitar que dos agentes editen el mismo archivo.
