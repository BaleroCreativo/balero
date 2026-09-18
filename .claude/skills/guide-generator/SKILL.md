---
name: guide-generator
description: Convertí un post, hilo, video o carrusel (o un tema suelto) en una guía pública expandida, optimizada para SEO y para GEO (que las IA la citen). Genera el artículo en Markdown/MDX con frontmatter completo, estructura de secciones, FAQs basadas en preguntas reales y links útiles. Usala cuando tengas un contenido corto que rinde y quieras convertirlo en una página indexable que después entregás como lead magnet o recurso. Version standalone: no depende de ninguna infraestructura, los datos de tu marca y tu sitio los pegás en un bloque.
license: Distribuida gratis por Claura (claura-ai.com). Uso libre para tu marca; no la revendas como producto.
---

# guide-generator (standalone)

Skill para transformar una pieza corta (un carrusel, un reel, un hilo, un video) o un
tema suelto en una **guía larga publicable** que rankea en Google y que las IA citan
cuando alguien pregunta por el tema. La lógica es simple: el post prueba que el ángulo
interesa, la guía lo expande a algo que existe para siempre en tu dominio y que podés
entregar por DM, newsletter o CTA. Version standalone: no depende de ningún CMS ni
base de datos, la config de tu sitio y tu marca las pegás vos en un bloque.

## Cómo se usa

1. Pegá tu **bloque de sitio y marca** (abajo) una sola vez.
2. Dale a la IA la **fuente**: el texto del post/hilo/transcripción, o solo el tema.
3. Pedile la guía siguiendo la estructura y las reglas de este archivo.
4. Generá las **FAQs** con el método de abajo (preguntas reales, no inventadas).
5. Revisá contra el checklist final y publicá en tu sitio.

### Bloque de sitio y marca (completá y pegá)

```
SITIO: <dominio, ej: tumarca.com>
RUTA DE GUIAS: <ej: /recursos o /blog> (así se arma la URL pública: SITIO + RUTA + slug)
FORMATO DEL ARCHIVO: <MDX / Markdown / HTML> (según tu CMS)
CATEGORIAS VALIDAS: <lista cerrada de tu sitio, ej: claude, prompts, herramientas, automatizacion, general>
REGISTRO: <voseo / tuteo / neutro>
TONO: <3 adjetivos, ej: directo, sin relleno, práctico>
NO USAR: <killwords, clichés, emojis si no van, em dash>
GUIAS EXISTENTES (para linkear internamente): <slug: título por línea, o "ninguna todavía">
PRUEBA SOCIAL / DATOS REALES: <números o hechos que SÍ podés citar>
```

Todo lo que otra versión sacaría de una base de datos o un design system, en esta
version sale de este bloque. Si un dato no está acá, se pregunta, nunca se inventa.

## Qué NO es esta skill

- No es para posts efímeros (memes, chismes, contenido descartable).
- No es para opiniones puras sin nada accionable adentro.
- No reemplaza tu criterio editorial: genera el borrador optimizado, vos curás.

## Paso 1: Slug y fechas

El slug es kebab-case, sin acentos ni ñ, sin el prefijo `guia-` (el título sí puede
decir "Guía: X"). Cortos. Regla de transformación:

```
"6 tips para dominar la IA en marketing"  ->  "6-tips-dominar-ia-marketing"
```

- Minúsculas, acentos a su vocal simple, ñ a n.
- Fuera todo lo que no sea letra, número, espacio o guión.
- Espacios a guiones, colapsar repetidos, recortar a ~80 chars.

`publishedAt` y `updatedAt` en la fecha de creación, ISO `YYYY-MM-DD`.

## Paso 2: Frontmatter (metadata)

El frontmatter es lo que decide cómo aparece la guía en el índice y qué entiende Google.
Campos base (adaptá los nombres a los que tu CMS espera):

```yaml
---
title: 'Guía: [Título humano completo con la keyword adentro]'
slug: [slug-kebab-case]
category: [una de las CATEGORIAS VALIDAS de tu bloque]
excerpt: >-
  2 a 3 oraciones que describen el contenido. Aparece en el índice y como
  meta description. Con la keyword principal, sin relleno marketero.
cover: [ruta a tu imagen de portada, ej: /covers/{slug}.jpg]
publishedAt: 'YYYY-MM-DD'
updatedAt: 'YYYY-MM-DD'
readingMinutes: N   # estimar ~200 palabras por minuto
sourceLinks:
  - platform: x | instagram | tiktok | youtube | linkedin | web
    url: 'https://...'
    label: 'Post original'
faqTopic: [Entidad principal, 1 a 4 palabras]
faqs:
  - question: ¿Pregunta real 1?
    answer: >-
      Respuesta de 134 a 167 palabras (ver Paso 4).
---
```

Reglas del frontmatter:

- `title`: patrón "Guía: [tema]" con la keyword principal literal adentro.
- `category`: solo de la lista cerrada de tu bloque. Si ninguna encaja, preguntá.
- `excerpt`: es tu meta description. Que arranque fuerte y contenga la keyword.
- `sourceLinks`: array vacío si no aplica, no lo omitas.
- `readingMinutes`: real, no inflado. Típico 4 a 7.

## Paso 3: Cuerpo de la guía

Markdown puro. Esqueleto que rinde para SEO + lectura escaneable:

```markdown
## ¿Qué es [tema]? / Por qué importa ahora

Intro de 2 a 3 párrafos. Contexto y por qué le conviene al lector leer esto hoy.

---

## Contexto / Lo que casi nadie explica

1. Punto 1
2. Punto 2
3. Punto 3

---

## [Sección principal 1]  (ej: Tip 1, Feature 1, Paso 1)

Explicación con **bold** en lo clave. Bullets cuando ayudan a escanear.

Tabla cuando comparás opciones:

| Columna | Columna |
|---|---|
| A | B |

---

## [Sección principal 2]
...
## [Sección principal N]
...

---

## ¿Cómo lo aplico hoy?

Pasos accionables numerados. Concretos, no "empezá a usar IA".

---

## Links útiles

- Recurso 1: [url](url)
- Recurso interno relacionado: [/ruta/slug-relacionado](/ruta/slug-relacionado)
```

Reglas de escritura:

- **No técnico**: escribí como si el lector no supiera del tema.
- **Práctico**: cada sección deja algo que se puede hacer.
- **Ejemplos concretos**: casos reales de tu rubro, no genéricos.
- **Longitud**: mínimo 800 palabras, ideal 1200 a 1800.
- **Tono y registro**: los del bloque. Sin "estimado lector" ni fórmulas de venta.
- **Bold selectivo**: solo lo que importa si alguien escanea.
- **Divisores `---`** entre secciones grandes.
- **Un solo link interno relevante** por sección como máximo, sin CTA comercial pesado.

## Paso 4: FAQs para GEO (que las IA te citen)

Las FAQs son lo que hace que un modelo cite tu guía cuando alguien pregunta por el tema.
No se inventan: se sacan de preguntas reales.

Método:

1. **Investigá preguntas reales**: mirá el bloque "People Also Ask" de Google para tu
   keyword, el autocomplete, e hilos de Reddit/foros del rubro. Anotá las que se repiten.
2. **Escribí 4 a 7 FAQs**. Cada respuesta de **134 a 167 palabras**: es el largo dulce
   para que entre entera como snippet citable, ni cortada ni inflada.
3. **Datos concretos**: cada respuesta con al menos un número, entidad o hecho real
   (de tu bloque de prueba social, jamás inventado).
4. **1 a 3 links por respuesta**: mezcla de interno (otras guías de tu sitio, de tu
   bloque de guías existentes) y externo cuando suma autoridad.
5. `faqTopic`: la entidad principal en 1 a 4 palabras. Va como campo aparte.

Validación de las FAQs:

- 4 a 7 preguntas, ninguna inventada.
- Cada respuesta entre 100 y 200 palabras (ideal 134 a 167).
- Cada respuesta con al menos un link.
- Respuesta que se entiende sola, sin leer el resto de la guía.

## Paso 5: Publicar

- Guardá el archivo donde tu CMS lee las guías (según FORMATO del bloque).
- Copiá la imagen de portada a la ruta que declaraste en `cover`. Si es PNG y tu loader
  falla, convertila a JPG (`sips -s format jpeg in.png --out out.jpg` en macOS, o
  ImageMagick).
- Actualizá tu índice/listado si tu sitio lo tiene (sino la guía existe pero no aparece).
- La URL pública final es `SITIO + RUTA DE GUIAS + slug`. Ese es el link que entregás
  por DM, newsletter o CTA cuando alguien pide el recurso.

## Checklist final (antes de publicar)

- [ ] Slug limpio, sin acentos, sin prefijo `guia-`.
- [ ] `title` con la keyword literal adentro.
- [ ] `excerpt` sirve como meta description (con keyword, sin relleno).
- [ ] `category` es una de las válidas de tu bloque.
- [ ] `cover` apunta a un archivo que existe.
- [ ] `publishedAt` en el pasado o en hoy, nunca en el futuro.
- [ ] Cuerpo de 800+ palabras, con secciones, al menos una tabla o lista.
- [ ] 4 a 7 FAQs de preguntas reales, 134 a 167 palabras, con links.
- [ ] Cero datos inventados: todo número sale de la fuente o del bloque.
- [ ] Registro correcto (voseo/tuteo/neutro) y sin killwords ni em dash.
- [ ] Índice/listado actualizado y URL pública verificada.

## Errores comunes

| Error | Fix |
|---|---|
| `cover` apunta a un path inexistente | Copiá la imagen primero, después referenciala |
| `category` inventada | Solo de la lista cerrada de tu bloque |
| FAQs de una sola oración | Expandí a 134 a 167 palabras, citables como snippet |
| Preguntas de FAQ inventadas | Sacalas de PAA/autocomplete/foros reales |
| Guía sin link interno | Linkeá al menos una guía relacionada de tu sitio |
| Olvidar actualizar el índice | El artículo existe pero no aparece en el listado |
| CTA comercial pesado en el cuerpo | La guía es contenido; máximo un link interno por sección |

---

Framework de creación de guías SEO + GEO sintetizado por Claura. Más skills en
https://claura-ai.com/skills
