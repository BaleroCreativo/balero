---
name: faq-generator
description: Generá secciones de FAQ optimizadas para SEO tradicional y para GEO (Generative Engine Optimization, o sea AI Overviews, ChatGPT, Perplexity, Claude). Investiga preguntas reales (People Also Ask, autocomplete, Reddit, Quora), escribe respuestas citables por IA (134 a 167 palabras, respuesta directa en las primeras 40 a 60 palabras, datos específicos con fuente) y devuelve el output en varios formatos (YAML para frontmatter, JSON-LD FAQPage, markdown). Usala cuando pidas "generá FAQs", "FAQ para SEO", "FAQs geo", "preguntas frecuentes" o "FAQ schema".
license: Distribuida gratis por Claura (claura-ai.com). Uso libre para tu marca; no la revendas como producto.
---

# faq-generator (standalone)

Una sección de FAQ bien hecha es el elemento de contenido con más ROI por palabra para SEO y GEO. Google la muestra en People Also Ask, los asistentes de IA la citan textual (si está bien escrita) y captura queries long-tail que el cuerpo del artículo no alcanza.

Esta skill genera FAQs que cumplen las dos reglas de oro:

1. **SEO tradicional**: match exacto con queries reales (PAA, autocomplete, related searches), no inventadas.
2. **GEO / citación por IA**: respuestas auto contenidas de 134 a 167 palabras, respuesta directa en las primeras 40 a 60 palabras, con datos específicos y fuentes cuando aplique.

Versión standalone: no depende de ninguna infraestructura. El contexto de tu marca (idioma, tono, artículos internos disponibles) lo pegás vos en un bloque.

## Cómo se usa

1. Pegá tu **bloque de contexto** (abajo).
2. Dale a la IA el **tema del artículo** (la entidad principal) y el **idioma**.
3. Pedile 4 a 7 FAQs siguiendo el workflow de 5 pasos de este archivo.
4. Curá con el checklist de validación antes de publicar.

### Bloque de contexto (completá y pegá)

```
ENTIDAD PRINCIPAL: <el tema exacto del artículo, ej: "Claude Opus 4.7">
IDIOMA Y REGISTRO: <ej: español rioplatense, voseo>
SITIO OFICIAL DE LA ENTIDAD: <URL autoritativa para linkear, ej: claude.ai>
ARTÍCULOS INTERNOS DISPONIBLES: <lista de URLs propias relacionadas para linkear, o "ninguno">
DATOS DUROS QUE PODÉS CITAR: <números, fechas, benchmarks reales del tema>
```

## Workflow (5 pasos)

### 1. Investigar queries reales (obligatorio, no inventar preguntas)

Antes de escribir una sola pregunta, investigá qué pregunta la gente de verdad. Fuentes en orden de prioridad:

1. **Google People Also Ask (PAA)**: buscá el keyword principal, expandí 2 o 3 niveles de PAA, capturá las preguntas.
2. **Google autocomplete**: prefijos `cómo`, `qué es`, `cuánto`, `por qué`, `cuándo`, `dónde`, `para qué`, `vale la pena`, `diferencia entre`.
3. **Related searches** (fondo del SERP): queries adyacentes.
4. **Reddit / Quora**: preguntas textuales con upvotes. Reddit representa buena parte de las citaciones de Perplexity.
5. **AlsoAsked / AnswerThePublic** si están disponibles.
6. **Búsqueda interna del sitio** (si tenés analytics): queries reales de tus usuarios.

Herramientas típicas: la búsqueda web de tu agente para PAA y autocomplete, y fetch sobre threads de Reddit/Quora relevantes.

**Regla dura**: cada pregunta del FAQ final debe poder trackear a una fuente real. Si inventás una pregunta "porque queda bien", la pregunta no se queda.

### 2. Clasificar las preguntas por intent

| Intent | Patrón | Ejemplo |
|--------|--------|---------|
| Definition | ¿Qué es X? / ¿Qué significa X? | ¿Qué es Extended Thinking? |
| How-to | ¿Cómo + verbo? | ¿Cómo subo archivos a Claude? |
| Comparison | ¿Diferencia entre X e Y? / ¿X vs Y? | ¿Diferencia entre Claude y ChatGPT? |
| Capability | ¿Puede X hacer Y? | ¿Claude puede leer PDFs? |
| Price/limit | ¿Cuánto cuesta? / ¿Cuál es el límite? | ¿Cuántos mensajes tiene el plan gratis? |
| Troubleshoot | ¿Por qué X no funciona? | ¿Por qué no me deja subir imágenes? |
| When/where | ¿Cuándo sale X? / ¿Dónde uso X? | ¿Cuándo salió Opus 4.7? |

Un buen FAQ mezcla intents, no 5 definitions seguidas. Típicamente 4 a 7 FAQs por artículo, en orden de curiosidad creciente (la primera es la más buscada).

### 2.5. Definir el topic específico para el H2

La sección FAQ no se titula "Preguntas frecuentes" genérico. Se titula **"Preguntas frecuentes sobre {topic}"**, donde `{topic}` es la entidad principal del artículo (nombre del producto, modelo, técnica, marca).

Por qué:
- **SEO**: Google indexa mejor los H2 con entidad específica que los genéricos.
- **GEO**: los motores de IA usan el H2 como contexto para decidir si una FAQ responde la query. "Preguntas frecuentes sobre Kimi K2" matchea queries de Kimi K2 con mucha más confianza que "Preguntas frecuentes".
- **UX**: el usuario sabe al instante qué tipo de preguntas va a encontrar.

Reglas del topic:
- 1 a 4 palabras, sin artículos ni verbos. "Kimi K2" ok, "el modelo Kimi K2" no.
- Entidad específica, no genérico. "Claude Opus 4.7" ok, "inteligencia artificial" no.
- Coincide con la entidad principal del artículo (si el artículo es sobre X, el topic es X, no un subtopic).
- Si el artículo es una guía de varios items, usá el tema paraguas. Ej: "5 funciones de Claude" tiene topic `Claude`, no `funciones`.

En el output, entregá el topic junto con el YAML para que quien lo pegue lo agregue al frontmatter (campo `faqTopic` en la mayoría de los CMS).

### 3. Escribir respuestas con el template de citación

Cada respuesta sigue esta estructura de 3 bloques:

```
[BLOQUE 1: respuesta directa | 40 a 60 palabras]
Responde la pregunta literal en la primera oración. Sin warm-up, sin "Claro,
te explico". Si la respuesta es "sí" o "no", la primera palabra es "sí" o "no".

[BLOQUE 2: expansión con dato específico | 40 a 60 palabras]
Ampliá con un dato concreto: número, fecha, nombre de feature, ejemplo puntual.
Los asistentes de IA citan pasajes con datos, no con generalidades.

[BLOQUE 3: contexto o matiz opcional | 30 a 50 palabras]
Edge case, o "cuándo no aplica". Solo si aporta. Si no, cortá en el bloque 2.
```

**Target: 134 a 167 palabras totales por respuesta** (sweet spot de citabilidad según Ahrefs, dic 2025). Aceptable 100 a 200. Nunca menos de 80 ni más de 250.

Reglas de escritura:
- Cada oración debe ser citable sola (sin "esto" o "lo anterior" sin antecedente claro).
- Datos específicos ganan a frases vagas. "20 mensajes cada 5 horas" gana a "pocos mensajes".
- Fuente cuando haya un número o claim fuerte: inline, ej. "(según Ahrefs, 2025)".
- Voz activa. Párrafos cortos (1 a 2 oraciones).
- **Links permitidos** en las respuestas (ver sección 3.5). Usá sintaxis markdown `[texto](url)`. Al generar el JSON-LD, el markup se strippea a texto plano; el HTML sí muestra el link.
- **Markdown inline permitido**: `**bold**`, `*italic*`, `` `code` ``. Usá bold para remarcar datos críticos, precios, métricas: mejora la citabilidad y la escaneabilidad. Ej: "arranca **desde 1.500 USD al mes**". Evitá bold decorativo o en frases enteras.
- **Idioma igual al del artículo**. Si el artículo es en español rioplatense, las FAQs en español rioplatense (voseo). Mantené el tono del bloque de contexto.

### 3.5. Linking interno y externo (importante para SEO + GEO)

Cada FAQ debe tener **1 a 3 links**, ni más ni menos. Cero links es oportunidad perdida para consolidar autoridad. Más de 3 es dilución y señal de spam.

Tipos de link y cuándo usar cada uno:

| Tipo | Cuándo | Ejemplo |
|------|--------|---------|
| Interno, artículo relacionado | La respuesta menciona otro tema con artículo propio en tu sitio | "por debajo de [Claude Opus 4.5](/tu-articulo)" |
| Interno, ancla en el mismo artículo | La respuesta refiere a una sección del mismo artículo | "ver [especificaciones técnicas](#especificaciones)" |
| Externo, fuente oficial | Hay una página oficial autoritativa del producto o dato | "descargalo desde [Hugging Face](https://huggingface.co/...)" |
| Externo, fuente primaria | La respuesta cita una estadística de un paper, estudio u outlet | "según [VentureBeat](https://venturebeat.com)" |

Reglas de linking:
- Linkeá la **primera mención** de la entidad, no las siguientes. Si "Claude" aparece 3 veces, linkeá solo la primera.
- El anchor text debe ser la entidad o concepto, nunca "click acá" ni "este link".
- Links externos abren en pestaña nueva; internos, no.
- No linkees a competencia directa salvo autoridad inevitable (Wikipedia, GitHub, Hugging Face).
- **Cada respuesta que nombra un producto/marca/modelo con sitio oficial debe linkear a ese sitio oficial en la primera mención**, no solo a artículos internos. Recién después agregá 1 o 2 internos a guías propias relacionadas.
- **La sección FAQ entera debe tener al menos 1 link externo**. Si las 5 FAQs linkean solo a artículos internos, falta la fuente.

Antes de escribir cada respuesta, listá:
0. Qué **entidad principal** nombra la respuesta y cuál es su URL oficial (del bloque de contexto). Esa es el primer link.
1. Qué entidades adicionales menciona (otros productos, técnicas, conceptos).
2. Cuáles de esas tienen artículo propio en tu sitio (de tu lista del bloque de contexto), para linkear la primera mención como segundo link.
3. Qué secciones del mismo artículo profundizan algún punto, para un ancla si aplica.

Anti-patterns de linking:

| Mal | Bien |
|-----|------|
| "Es más barato que Claude" (sin link) | "Es más barato que [Claude Sonnet 4.6](/tu-articulo)" |
| "[Más información acá](/x)" | "[Más funciones de Claude](/tu-articulo)" |
| 7 links en una respuesta | 1 a 3 links |
| Linkear cada mención de "Claude" | Linkear solo la primera |
| 5 links, todos internos (cero externos con productos nombrados) | Mix: entidad principal al sitio oficial + 1 o 2 internos |

### 4. Generar el output en el formato que pidas

Tres formatos soportados. Preguntá cuál si no está claro, o generá los tres.

#### Formato A: YAML para frontmatter

```yaml
faqTopic: Claude
faqs:
  - question: ¿Cómo puedo subir archivos a Claude para que los analice?
    answer: >-
      Podés subir PDFs, Word, Excel e imágenes directamente al chat de
      [Claude](https://claude.com) haciendo clic en el ícono de clip [...]
  - question: ¿Qué son los Proyectos en Claude y cómo los uso?
    answer: >-
      Los Proyectos son carpetas donde Claude guarda contexto permanente [...]
```

Notas:
- `faqTopic` arriba de `faqs`. 1 a 4 palabras, entidad principal.
- Usá `>-` (folded + strip) para respuestas multilínea; indentá 6 espacios el cuerpo.
- No envuelvas la pregunta en comillas salvo que contenga `:` o empiece con un char YAML especial.

#### Formato B: JSON-LD FAQPage schema

Para inyectar en `<script type="application/ld+json">`:

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "¿Cómo puedo subir archivos a Claude?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Podés subir PDFs, Word, Excel e imágenes..."
      }
    }
  ]
}
```

Caveat: Google ya casi no muestra rich snippets de FAQPage en resultados comerciales (desde mediados de 2023). Sigue sirviendo para motores de IA que leen schema, sitios informativos (news, gov, nonprofit) donde Google sí lo renderiza, y el entity graph general. Implementalo igual, pero no esperes rich snippet en SERP comercial. El markup markdown de las respuestas se strippea a texto plano en el campo `text`.

#### Formato C: Markdown plano

Para docs, Notion o el cuerpo del artículo:

```markdown
## Preguntas frecuentes sobre Claude

### ¿Cómo puedo subir archivos a Claude?

Podés subir PDFs, Word, Excel e imágenes directamente...

### ¿Qué son los Proyectos en Claude?

Los Proyectos son carpetas...
```

### 5. Validar antes de entregar

Checklist obligatorio antes de cerrar el output:

- [ ] Cada pregunta viene de una fuente real (PAA, autocomplete, Reddit, analytics). Cero inventadas.
- [ ] Mezcla de intents (no 5 "¿Qué es...?" seguidas).
- [ ] Cada respuesta entre 100 y 200 palabras, ideal 134 a 167.
- [ ] Cada respuesta responde literal en las primeras 40 a 60 palabras.
- [ ] Cada respuesta incluye al menos un dato específico (número, fecha, nombre).
- [ ] Cada respuesta tiene 1 a 3 links (mezcla interno + externo según aplique).
- [ ] Cada respuesta que menciona un producto/marca/modelo con sitio oficial linkea a ese sitio oficial en la primera mención.
- [ ] La sección FAQ entera tiene al menos 1 link externo.
- [ ] Anchor text de cada link es la entidad o concepto, no "acá" ni "click".
- [ ] Primera mención de cada entidad linkeada, no las siguientes.
- [ ] Las preguntas mantienen el fraseo natural del usuario (el keyword viene solo).
- [ ] Idioma y tono coinciden con el artículo host.
- [ ] 4 a 7 FAQs (menos de 4 es thin, más de 7 es fatiga y dilución).
- [ ] `faqTopic` definido (entidad principal, 1 a 4 palabras).
- [ ] Output en el formato solicitado, parseable sin modificaciones.

## Anti-patterns (no hacer)

| Mal | Bien |
|-----|------|
| "¿Por qué X es el mejor?" (marketing-speak) | "¿X o Y es mejor para programar?" |
| "X es una IA increíble que..." (fluff) | "X es un asistente de IA lanzado en 2023..." |
| Respuesta de 40 palabras | Respuesta de 134 a 167 palabras |
| "Como mencionamos arriba..." | Cada respuesta auto contenida |
| Respuesta enterrada en el párrafo 3 | Respuesta directa en la primera oración |
| FAQs recicladas entre 10 artículos | FAQs específicas al topic del artículo |
| Preguntas sin investigar | Preguntas sacadas de PAA real |

## Ejemplo (antes / después)

Tema: "Claude Opus 4.7, el nuevo modelo".

Mal (inventado, genérico, corto):
```yaml
- question: ¿Qué es Claude?
  answer: >-
    Claude es un asistente de IA creado por Anthropic. Es muy potente.
```

Bien (de PAA real, citable, específico):
```yaml
- question: ¿Qué diferencia hay entre Claude Opus 4.7 y Sonnet 4.6?
  answer: >-
    Opus 4.7 es el modelo más potente de Anthropic; Sonnet 4.6 es el modelo
    intermedio. Opus 4.7 gana en tareas agénticas largas, razonamiento
    complejo y coding de varios archivos, con un 74.5% en SWE-bench Verified
    contra 72% de Sonnet 4.6. Sonnet 4.6 es unas 5 veces más barato por token
    y responde más rápido, por lo que sigue siendo el default para chat y
    escritura. Regla práctica: empezá con Sonnet 4.6, subí a Opus 4.7 cuando
    la tarea requiera más de 10 minutos de trabajo continuo o varios pasos
    con estado.
```

La segunda responde una pregunta que la gente busca de verdad, da la respuesta directa en la primera oración, incluye datos específicos (74.5%, 5 veces), suma una regla accionable y ronda las 150 palabras.

## Output final

Salvo que pidas otra cosa, entregá:

1. El **bloque YAML** listo para pegar en el frontmatter.
2. Una **nota corta** con la fuente de cada pregunta (1 línea por FAQ, ej. `Q1: Google PAA "claude vs chatgpt"`).
3. **Scoring interno**: word count por respuesta + check de los items del checklist de validación.

Nada más. No sobre-expliques.

---

Framework sintetizado por Claura a partir de prácticas públicas de SEO y GEO. Más skills en https://claura-ai.com/skills
