---
name: investigacion-verificada
description: Busca temas y noticias para el contenido mensual de un cliente (newsletters del correo, búsqueda web, dudas de su cliente ideal), verifica cada dato en fuentes públicas y entrega una lista de datos con su fuente y estado (verificado, parcial, sin verificar o descartado), más la propuesta de qué noticia ocupa qué hueco del calendario. Es la etapa 3 del sistema de contenido mensual. Úsala siempre que el usuario pida "investiga temas", "busca noticias para el mes", "revisa los newsletters", "verifica estos datos", "qué hay de nuevo en [Meta, Google, SEO, ChatGPT Ads...]", "llena los huecos de noticias" o quiera respaldar un post con datos, incluso si solo dice "busca más cosas o temas".
---

# Investigación verificada

Produce el material de datos del que se alimentan los guiones: temas con fuente, cifras confirmadas y noticias con impacto en el cliente. El valor de esta etapa está en lo que **descarta**. Un dato bonito sin respaldo es peor que no tener dato, porque llega al cliente final con la firma de la agencia.

## La regla que sostiene todo
Nada sin verificar se presenta como hecho. Cada dato queda en uno de cuatro estados y los guiones solo usan los dos primeros:
- **Verificado:** confirmado en fuente primaria (documentación oficial, estudio original) o en dos fuentes independientes confiables.
- **Parcial:** confirmado solo en fuente secundaria. Se puede usar con "según reportes" o "según [fuente]", nunca como afirmación propia.
- **Sin verificar:** no se pudo confirmar. No se usa. Se anota para revisar más adelante.
- **Descartado:** contradice una fuente confiable, es de otro mercado sin relevancia o ya no está vigente.

Por qué tantas reglas: en octubre de 2026 los porcentajes y los autores de un estudio citado en un newsletter no se pudieron confirmar y hubo que sacarlos de la pieza. Un enlace roto de un artículo del blog también pasó a "no verificado". Anotar el estado desde el principio evita descubrirlo cuando el diseño ya está hecho.

## Flujo

### 1. Leer ficha y plan
Abre `clientes/<slug>/ficha.md` (pilares, cliente ideal, fuentes de investigación, reglas de verdad) y las filas del mes en Notion. Identifica dos necesidades:
- **Huecos de noticias** sin tema.
- **Piezas con tema ya definido** que necesitan datos o ejemplos que las respalden.

### 2. Recolectar candidatos
Fuentes, de más a menos confiable:
1. **Documentación oficial** de las plataformas (Meta, Google, OpenAI, Metricool y las que use el cliente).
2. **Newsletters** del correo del cliente o de la agencia, que son la mejor señal de lo reciente. Busca por remitente y fechas (herramientas de Gmail). El texto plano de estos correos suele traer solo enlaces; el contenido está en el HTML, que se guarda en archivo y se lee con un script.
3. **Búsqueda web** (WebSearch, `scout:search`). Algunos sitios están bloqueados desde este entorno; cuando un sitio no abra, busca la misma nota en otra fuente, no la des por buena solo por el resumen del newsletter.
4. **Dudas reales** del cliente ideal: preguntas que le hacen al cliente, objeciones, temas de sus propios clientes.
Para ideas de temas sin base en noticias, usa `idea-generator` como apoyo, pero tratálas como ideas, no como datos.

### 3. Filtrar con el criterio de ubicación
Cada candidato pasa por tres preguntas:
- ¿Es **reciente**? (Anota la fecha del anuncio o del estudio.)
- ¿Tiene **impacto inmediato** para el cliente ideal? (¿Tiene que hacer algo esta semana o este mes?)
- ¿Aplica al **mercado del cliente**? (País, idioma, disponibilidad del producto.)

Si cumple las tres, va a un hueco libre del mes en curso. Si no cumple, se guarda para el mes siguiente con su fecha de vigencia. Si no aplica al mercado, se descarta y se dice por qué.

### 4. Verificar cada dato
Para cada cifra, fecha, nombre o afirmación que vaya a aparecer en una pieza:
- Busca la fuente primaria. Anota el enlace y la fecha de consulta.
- Confirma **qué dice exactamente**: población, periodo, método, alcance (global o por país). Un porcentaje sin contexto engaña, por ejemplo una cifra global usada para hablar de México.
- Revisa que la fecha de entrada en vigor y las condiciones sigan vigentes.
- Si solo hay fuentes secundarias, estado **Parcial** y la redacción obligada ("según reportes").
- Si dos fuentes se contradicen, anota ambas y no elijas por tu cuenta.

Nunca completes un dato faltante "razonablemente" (autores, cifras, precios, nombres). Déjalo vacío y explícalo.

### 5. Entregar el informe
Guarda el informe en `clientes/<slug>/investigacion/AAAA-MM.md` con el formato de `references/formato-informe.md`. Incluye:
- Tabla de datos por tema con fuente, fecha, estado y redacción permitida.
- Propuesta de qué noticia ocupa cada hueco y qué pasa al mes siguiente.
- Lista de lo descartado y el motivo.
- Pendientes de verificación y qué habría que hacer para cerrarlos (por ejemplo, confirmar con un cliente si un servicio ya está disponible en su cuenta).

### 6. Punto de aprobación
Presenta al usuario un resumen corto antes de pasar a guiones: temas propuestos por hueco, cuáles datos son Verificados o Parciales y cuáles quedaron fuera. La persona responsable decide qué entra. No avances a los guiones con temas que no aprobó.

### 7. Actualizar Notion
Con lo aprobado, actualiza las filas de Notion de cada tema: título de trabajo definitivo, sección "Datos y fuentes (verificar antes de publicar)" con los datos y sus estados, y la regla para el guion ("usar 'según reportes'", "no citar autores"). Si un dato tiene fecha de vigencia corta, anótalo para volver a verificarlo antes de publicar.

### 8. Cerrar
Resume en pocas líneas qué se aprobó, qué quedó pendiente y el siguiente paso: `guion-pieza` para escribir hook, caption y guion de cada pieza.

## Qué no hacer
- No uses un dato del newsletter sin buscar el original.
- No cites estudios por su titular; abre el estudio o su resumen oficial.
- No mezcles cifras globales con afirmaciones locales sin decirlo.
- No des por válida una cifra porque "suena a lo que dicen todos".
- No ofrezcas servicios nuevos del cliente (por ejemplo, anunciarse en una plataforma nueva) como parte de una noticia sin que el cliente lo confirme en su ficha.
- No publiques ni programes nada desde aquí.

## Paralelizar
Si hay muchos temas, investiga varios a la vez con subagentes, uno por tema, y cada uno devuelve su tabla de datos con estados. Tú reúnes y revisas las contradicciones; la decisión sobre qué entra sigue siendo de la persona.
