---
name: cliente-onboarding
description: Crea o actualiza la ficha de un cliente de la agencia (marca, cliente ideal, tono, pilares de contenido, reglas de lo que se puede afirmar, conexiones a Notion y Metricool y quién aprueba). Es la primera etapa del sistema de contenido mensual y la que leen todas las demás. Úsala siempre que el usuario mencione un cliente nuevo, "onboarding", "ficha del cliente", "preparar a un cliente para hacer su contenido", "actualizar la marca o el tono de un cliente", o antes de planear el calendario de un cliente que todavía no tiene ficha en clientes/<cliente>/ficha.md, aunque no pida la ficha de forma explícita.
---

# Cliente onboarding: la ficha del cliente

La ficha es un solo archivo, `clientes/<slug>/ficha.md`, que concentra todo lo que las demás etapas del sistema necesitan saber de un cliente: plan mensual, investigación, guiones, diseño y publicación. Sin ficha, cada etapa pregunta lo mismo otra vez o, peor, supone. Con ficha, cambiar de cliente es cambiar de archivo.

## Principio que manda todo lo demás

La ficha dice la verdad sobre lo que se sabe y lo que no. Todo dato que el cliente no confirmó se escribe como `[POR CONFIRMAR]`, nunca se rellena con una suposición razonable. Por qué: en el trabajo con Balero, las dos veces que apareció un error grave fue por un dato o una anécdota que sonaba bien y no estaba verificada. Una ficha con huecos honestos es útil; una ficha completa pero inventada contamina todo el mes.

## Flujo

### 1. Detectar si es cliente nuevo o actualización
Busca `clientes/*/ficha.md`. Si el cliente ya tiene ficha, léela, muestra qué cambió y edita solo lo que cambia. Si no, parte de `references/plantilla-ficha.md`. Para ver cómo queda una ficha ya llena, consulta `clientes/balero/ficha.md` (la de la propia agencia, armada con lo trabajado en octubre de 2026).

El slug es el nombre del cliente en minúsculas, sin acentos y con guiones (`huevo-puerta-coyotes`).

### 2. Reunir lo que ya existe antes de preguntar
El cliente pierde paciencia con cuestionarios largos, así que primero extrae lo que se pueda de fuentes:
- **Sitio web y redes:** léelos (WebFetch, `scout:fetch` o `scout:search`) para sacar tono real, servicios, ciudad, ofertas, hashtags y estilo visual.
- **Documentos de marca:** busca en Notion, Drive o la carpeta del repo guías de marca, logos, fuentes y piezas anteriores. Para un cliente nuevo sin guía, `brand-guidelines` y `brand-voice` (discover-brand) pueden ayudar a derivar una.
- **Cliente ideal:** `icp-builder` si no hay una definición clara.
- **Metricool y Notion:** si ya existen, lee la configuración de la marca en Metricool (zona horaria, redes conectadas) y localiza la base de contenidos en Notion. Estos IDs se anotan, no se adivinan.

Marca cada dato con su origen: `[sitio]`, `[redes]`, `[documento]`, `[cliente]` o `[POR CONFIRMAR]`.

### 3. Preguntar solo lo que falta
Haz como máximo dos rondas cortas de preguntas, agrupadas, con opciones cerradas cuando se pueda. Lo que casi siempre falta:
- A quién le vende y qué problema suyo resuelve (en palabras del cliente, no de marketing).
- Qué no se puede decir: promesas, precios, comparaciones, certificaciones, nombres de otros clientes.
- Qué casos reales tiene y si hay permiso para mostrarlos con nombre, anónimos o no.
- Quién aprueba el contenido y cuánto tarda en responder.
- Oferta o llamado a la acción vigente (diagnóstico, cotización, WhatsApp) y enlace con UTM.

Si el usuario no sabe una respuesta, déjala como `[POR CONFIRMAR]` y sigue. No bloquees la ficha por un dato que no es esencial.

### 4. Escribir la ficha
Guarda `clientes/<slug>/ficha.md` con la estructura de `references/plantilla-ficha.md`. Reglas de escritura:
- Frases cortas y concretas. La ficha la leen otros skills, así que lo ambiguo se paga luego.
- Los pilares de contenido van con una frase de qué cubre cada uno y una proporción sugerida.
- Las **Reglas de verdad** son su propia sección, con tres listas: se puede afirmar, no se puede afirmar, requiere permiso. Es la sección que más consultará la etapa de guiones.
- En **Conexiones** van los IDs reales: base de Notion, relación de proyecto, marca y zona horaria de Metricool, redes conectadas. Si falta alguno, queda como pendiente visible.

### 5. Sección de marca visual
La etapa de diseño necesita colores, fuentes, estilo de ilustración y márgenes. Anótalos en la ficha con valores exactos (hex y nombre de fuente). Con esos valores crea `clientes/<slug>/marca/brand.json` (formato en `balero-imagenes/references/marca-por-cliente.md`) y descarga las fuentes con `balero-imagenes/scripts/brand_fonts.py`. Deja la ficha apuntando a ese archivo.

### 6. Cerrar con un resumen
Termina siempre con tres bloques cortos, sin repetir la ficha completa:
1. **Qué quedó confirmado.**
2. **Qué está por confirmar y con quién** (cliente, tú, un tercero).
3. **Siguiente paso:** normalmente planear el mes (`plan-mensual`) cuando las reglas de verdad y los pilares estén confirmados.

Ofrece guardar una copia de la ficha como página en Notion si el cliente comparte espacio con la agencia. El archivo del repo es la fuente de verdad.

## Qué no hacer
- No inventes cifras, casos, testimonios, certificaciones ni alianzas para que la ficha se vea completa.
- No copies tal cual el texto del sitio del cliente como "tono": describe cómo habla (formal o cercano, tuteo o usted, frases largas o cortas) con un par de ejemplos reales.
- No publiques ni programes nada desde este skill. Su único producto es la ficha.
