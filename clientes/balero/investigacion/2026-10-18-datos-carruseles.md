# Datos para reforzar los carruseles de noviembre (investigación del 18 oct 2026)

Preparado para Daniela. Nada de esto se ha cambiado en Notion ni en Metricool.

## Cómo leer los estados y una limitación importante

- **Verificado:** la cifra aparece en la fuente primaria o en 2 o más fuentes independientes.
- **Parcial:** solo vía resumen de prensa, blog de proveedor o una sola fuente secundaria.
- **Sin verificar:** no se encontró.
- **Limitación:** WebFetch no abrió ningún sitio (error de DNS en todos) y curl por el proxy dio 403. Todo se leyó en resultados y fragmentos de WebSearch, que a veces citan la fuente primaria (Workday, Stanford GSB, Wiley, Shopify, Google). Ningún dato se tomó de una página abierta completa. Antes de publicar, abre los enlaces marcados con (abrir) y confirma la cifra en la página.
- No se redondeó ni se mezcló ninguna cifra de fuentes distintas. Los cálculos propios están marcados como CÁLCULO.

---

## 1. ROAS mínimo (3 nov) — spec-roas-v2

### 1a. Fórmula y tabla de ROAS de equilibrio

| Dato | Fuente | Fecha | Alcance | Estado | Redacción permitida |
|---|---|---|---|---|---|
| ROAS de equilibrio = 1 / margen de ganancia (el margen es antes del gasto en anuncios y descuenta costos por pedido: producto, envío, comisiones de pago) | Shopify, "Break-Even ROAS Calculator" https://www.shopify.com/blog/break-even-roas-calculator (abrir) | 2026 (la página trae "2026" en el título) | Ecommerce, explicación general | Verificado | "ROAS de equilibrio = 1 ÷ margen." |
| Misma fórmula; ejemplo con margen de 25% y equilibrio de 4 | Triple Whale, calculadora https://www.triplewhale.com/free-tools/roas-calculator y https://www.triplewhale.com/blog/breakeven-roas (abrir) | s/f | Ecommerce | Verificado (segunda fuente independiente de Shopify) | Igual |
| Ejemplos de Shopify: margen 40% = 2.5; 50% = 2; 20% = 5.0; 30% = 3.33 | Shopify (mismo enlace y https://www.shopify.com/blog/target-roas) | 2026 | Ecommerce | Verificado | Se puede citar "Fuente: Shopify". |
| El equilibrio no cubre gastos fijos (sueldos, renta, impuestos) | Shopify y Triple Whale | 2026 | General | Verificado | "Es el mínimo para no perder en cada venta, no la ganancia total." |
| Tabla de equilibrio por margen (abajo) | CÁLCULO propio con 1 / margen | 18 oct 2026 | Aritmética | Verificado como cálculo | Etiquetar "ejemplo ilustrativo". |

Tabla (CÁLCULO, 1 ÷ margen):

| Margen | ROAS de equilibrio |
|---|---|
| 10% | 10.00 |
| 20% | 5.00 |
| 25% | 4.00 |
| 30% | 3.33 (3.333…) |
| 40% | 2.50 |
| 50% | 2.00 |
| 60% | 1.67 (1.666…) |

Nota: en Google Ads el ROAS se muestra en porcentaje (4.0 = 400%). Si se publica el porcentaje, 3.33 sería 333%.

### 1b. Ejemplo con números completos (ILUSTRATIVO, calculado)

Utilidad = ingreso − costo de producto − gasto en anuncios. Todos los números son inventados a propósito para enseñar y deben llevar la etiqueta "ejemplo ilustrativo".

| Caso | Gasto en anuncios | ROAS | Ingreso | Margen | Costo de producto | Utilidad | Equilibrio |
|---|---|---|---|---|---|---|---|
| A | $500 | 8 | $4,000 | 30% | $2,800 | **+$700** | 3.33 |
| B | $10,000 | 5 | $50,000 | 30% | $35,000 | **+$5,000** | 3.33 |
| C | $500 | 8 | $4,000 | 10% | $3,600 | **−$100** | 10 |
| D | $1,000 | 3 | $3,000 | 60% | $1,200 | **+$800** | 1.67 |
| E | $1,000 | 3 | $3,000 | 30% | $2,100 | **−$100** | 3.33 |
| F (slide 2) | $400 | 5 | $2,000 | 30% | $1,400 | **+$200** | 3.33 |
| G (slide 2) | $400 | 5 | $2,000 | 20% | $1,600 | **$0** | 5 |

Lo que demuestra cada par:
- **A contra B** (mismo margen de 30%): respalda el slide 5. Un ROAS de 8 con $500 deja $700. Un ROAS de 5 con $10,000 deja $5,000.
- **C contra D:** un ROAS de 8 pierde $100 con margen de 10%, y un ROAS de 3 gana $800 con margen de 60%. Así se muestra que un ROAS alto puede perder dinero.
- **D contra E:** respalda el slide 3. El mismo ROAS de 3 gana con margen de 60% y pierde con margen de 30%.
- **F y G:** el ejemplo del slide 2 ($400 → $2,000, ROAS 5) deja $200 con margen de 30% y queda exacto en $0 con margen de 20%.

### 1c. Benchmarks de ROAS

| Dato | Fuente | Fecha | Alcance | Estado | Redacción permitida |
|---|---|---|---|---|---|
| Mediana de ROAS en Meta: 1.88. En Google Ads: 3.27 | Triple Whale https://www.triplewhale.com/blog/facebook-ads-benchmarks y https://www.triplewhale.com/blog/google-ads-benchmarks (abrir) | Ventana móvil ago 2025 – jul 2026 (según el resumen; confirmar en la página) | Marcas de ecommerce que usan Triple Whale, ROAS atribuido por la plataforma, todas las industrias | Parcial (solo resumen de búsqueda) | "Mediana de marcas de ecommerce en Triple Whale: 1.88 en Meta y 3.27 en Google Ads. No es un objetivo ni aplica a servicios." |
| Medianas por industria: Meta de 1.13 (Media y Publicaciones) a 2.35 (Deportes y Aire libre). Google de 2.06 (Salud y Bienestar) a 4.35 (Deportes y Aire libre) | Triple Whale (mismos enlaces) | Igual | Igual | Parcial | Solo si se cita la industria. |
| Triple Whale 2025: promedio de Google Ads 3.68 en más de 18,000 marcas de ecommerce | Reportado en resumen de búsqueda sobre Shopify y Triple Whale | 2025 | Ecommerce | Parcial. Otra ventana distinta de la de arriba, **no mezclar** con 3.27. | No usar junto a 3.27. |
| Otros "benchmarks" (Benchmarketing, Polar Analytics, Ryze) con cifras que chocan entre sí | Blogs de proveedores | 2026 | Variado | Sin verificar | No usar. |
| Benchmark de ROAS para servicios, pymes de México o LATAM | No se encontró | n/a | n/a | **No encontrado** | No afirmar ninguno para México. |

### 1d. Qué dicen Google y Meta sobre ROAS frente a margen

| Dato | Fuente | Fecha | Alcance | Estado | Redacción permitida |
|---|---|---|---|---|---|
| Google: el ROAS objetivo es el valor de conversión promedio por cada dólar gastado (valor/costo). Tú defines el valor que quieres maximizar al configurar la medición, por ejemplo ingresos o margen de ganancia | Google Ads Help https://support.google.com/google-ads/answer/15099424 y https://support.google.com/google-ads/answer/7684216 (abrir) | s/f | Google Ads, Smart Bidding | Parcial (resumen de búsqueda; el lenguaje exacto de "profit margins" hay que confirmarlo abriendo la página) | "En Google Ads tú decides qué valor cuenta como conversión: ventas o margen." |
| Google: desde junio 2026 "Maximizar valor de conversión con ROAS objetivo" se llama "ROAS objetivo", mismo comportamiento | Google Ads Help (mismo resumen) | jun 2026 | Google Ads | Parcial | Solo para ajustar nombres. |
| Meta: el ROAS de compras es el valor de conversión atribuido entre el gasto. La Ayuda no dice qué valor enviar | Solo vía blogs de terceros | s/f | Meta Ads | **Sin verificar en fuente primaria** (no se encontró el artículo de Meta) | No atribuir a Meta una frase sobre margen. |
| Ninguna de las dos plataformas dice textualmente "el ROAS no incluye tus costos" | No se encontró | n/a | n/a | **No encontrado** | La afirmación "el panel no ve tus costos" es lógica, no una cita. Es seguro porque el panel solo recibe el valor que se le envía. |

### Propuesta para el carrusel del ROAS (6 slides, máximo 1 dato visual por slide)

| Slide | Hoy | Dato a añadir (1 por slide) | Estado del dato |
|---|---|---|---|
| 1 | "ROAS de 8 puede ganar menos que uno de 5" | Ninguno. Ya es el gancho. | n/a |
| 2 | Fórmula e ejemplo $400 → $2,000 | Una línea: "Con 20% de margen, ROAS 5 es justo el equilibrio" (caso G) | CÁLCULO ilustrativo |
| 3 | "El panel no ve tus costos" | Mini-tabla de 3 filas: margen 60% → 1.67, 30% → 3.33, 10% → 10. Así el "ROAS de 3 puede ser bueno o pérdida" se ve en números | CÁLCULO + fórmula verificada |
| 4 | "Tu ROAS mínimo: donde dejas de perder" | La fórmula 1 ÷ margen con la fuente "Shopify" | Verificado |
| 5 | "Más ROAS no siempre es más ganancia" | Casos A y B: "$700 contra $5,000 de utilidad", etiquetados ilustrativos | CÁLCULO |
| 6 | CTA | Ninguno. | n/a |

El caso C (ROAS 8 que pierde) puede ir en el caption o en el slide 3 en lugar de la mini-tabla. No pongas los dos en el mismo slide.

---

## 2. Enlaces en respuestas de IA de Google (9 nov) — spec-enlaces-v2

| Dato | Fuente | Fecha | Alcance | Estado | Redacción permitida |
|---|---|---|---|---|---|
| Google anunció que muestra enlaces en línea (inline) **más arriba** y **con más frecuencia** en respuestas de IA. Autora: Hema Budaraju, VP de producto | Google, "AI Mode and AI Overviews updates to explore the web" https://blog.google/products-and-platforms/products/search/updates-ai-mode-overviews-explore-web/ ; Search Engine Journal https://www.searchenginejournal.com/google-inline-links-higher-ai-search-responses/593089/ ; Search Engine Land (abrir) | 15 oct 2026 según el resumen (otros resultados traen fechas de mayo 2026 de anuncios anteriores, así que confirmar la fecha en el blog) | AI Mode y AI Overviews, global | Verificado en lo esencial (blog de Google, SEJ y SEL coinciden) | "Google anunció que mostrará enlaces en línea más arriba y más seguido en sus respuestas con IA." |
| Google no dijo cuánto aumentó la posición ni dio tamaño del cambio | SEJ (mismo enlace) | 15 oct 2026 | Igual | Parcial | "Google no dio cifras del cambio." |
| Prueba de una sección con sitios oficiales para búsquedas de tareas (solo prueba) | SEJ y Google | 15 oct 2026 | Pruebas | Parcial | Opcional. No afirmar que ya existe para todos. |
| Search Console asigna a todos los enlaces de un AI Overview la misma posición del resumen, así que subir un enlace no cambia su posición reportada | SEJ | 15 oct 2026 | Search Console | Parcial | Útil para el caption. |
| Search Console no separa clics de AI Overviews, AI Mode y búsqueda clásica. Los clics van dentro del tipo de búsqueda "Web" | Google Search Central https://developers.google.com/search/docs/appearance/ai-features ; blogs de terceros (abrir) | AI Mode cuenta en los totales desde 16 jun 2025; AI Overviews aclarado en ago 2024 | Search Console, global | Verificado en lo esencial (documentación de Google más terceros) | "Los clics de AI Mode y AI Overviews se cuentan en el informe de Rendimiento, dentro de Búsqueda web, sin separarlos." |
| Informe nuevo "Generative AI" en Search Console: muestra **impresiones** (no clics) de AI Overviews y AI Mode. Lanzado el 3 jun 2026 para algunos sitios y a todos el 31 ago 2026 | Google Search Console Help https://support.google.com/webmasters/answer/16984139 (abrir) | jun / ago 2026 | Global | Parcial (fechas vienen de resumen de búsqueda) | "Search Console ya muestra impresiones en funciones de IA, pero no clics por separado." |
| Cifra de clics en esos enlaces | Google no la publicó | n/a | n/a | **No encontrado** (consistente con el título del carrusel) | Se mantiene "sin datos de clics". |

**Hallazgo que afecta al diseño:** el pendiente de Notion dice que "más arriba" no estaba respaldado. Ahora sí lo respalda el blog de Google y SEJ, salvo que alguien lo desmienta al abrir el enlace. El slide 2 puede decir "más enlaces, más arriba". Además, el slide 3 puede matizar que hay impresiones pero no clics, porque "Google no publicó datos de clics" es cierto solo para clics.

Propuesta (4 slides):
- Slide 1: sin dato nuevo.
- Slide 2: un dato visual, la fecha "15 oct 2026" con "enlaces en línea más arriba y más seguido".
- Slide 3: un dato visual, "Search Console: impresiones sí, clics por separado no".
- Slide 4: la fuente cambia a "Google (blog, 15 oct 2026) y Search Engine Journal".

---

## 3. Trigger event en anuncios — spec-trigger-v2

**No se encontró evidencia sólida de que anuncios que parten de la situación del cliente rindan más que otros.** Lo que apareció es débil y no aísla el concepto.

| Dato | Fuente | Fecha | Alcance | Estado | Redacción permitida |
|---|---|---|---|---|---|
| Intercom reconstruye "el momento" (un lanzamiento o un error crítico que inunda la bandeja) para que el visitante se vea en su problema. Es una explicación del concepto, **sin cifras** | Jobs-to-be-Done Radio, Matt Hodges https://jobstobedone.org/radio/marketing-with-jobs-to-be-done/ (abrir) | s/f | SaaS (Intercom) | Parcial (resumen) | Puede citarse como ejemplo conceptual de que el enfoque se usa, **no como prueba de resultados**. |
| Molson Coors, anuncios según el clima: +89% de CTR y +33% de comentarios contra anuncios de control | Braze (proveedor), citado en un recopilatorio de experimentos | s/f | Canadá, campaña de cerveza | Parcial. Es publicidad contextual, no "trigger event" | Solo con la etiqueta "caso de Braze sobre anuncios según contexto (clima)". No equiparar con trigger event. |
| WordStream: titular de dolor ("Stop wasting money on ads that don't convert") +27% en inicios de prueba contra uno de beneficio | Blog de terceros que cita a WordStream | s/f | Cifra de segunda mano. No se encontró el original | **Sin verificar** | No usar. |
| CXL: +79.3% en conversión de un sitio de transporte tras 6 rondas de pruebas. Un titular con palabras reales de clientes fue una parte, y el ganador final fue uno más simple | CXL https://cxl.com/blog/case-study-how-we-improved-landing-page-conversion/ (abrir) | s/f | Un sitio de transporte, landing page | Parcial. No aísla el efecto | No usar como respaldo del concepto. |
| Cifras de Quasi del newsletter | Felipe Vergara (9 oct) | n/a | n/a | Sin verificar (ya descartado en Notion) | **No usar ni nombrar la marca.** |
| Ejemplo real de antes/después de un anuncio que empieza con la situación del cliente | No se encontró | n/a | n/a | **No encontrado** | Mantener "ejemplo ilustrativo" en el slide 3. |

Una advertencia metodológica útil: una de las fuentes recuerda que un titular ganador con dolor no prueba que el encuadre de dolor causara la mejora, salvo que el experimento esté diseñado para eso.

Propuesta (5 slides): no añadir cifras. Mantener el concepto, el ejemplo ilustrativo y la invitación a probar. Si Daniela quiere un dato, el slide 5 puede decir "Pruébalo en pocas piezas y compara con tu dato" (consejo, no dato). La única cita con cifra que se podría defender es la de Braze, y aun así solo si se rotula como contexto y no como trigger event. Mi recomendación es no usarla.

---

## 4. ChatGPT Ads (12 nov) — spec-chatgpt-v2

El spec actual **no trae ninguna cifra**. El cierre dice "Fuente: OpenAI". Si se añade el CTR, la fuente cambia (ver abajo).

| Dato | Fuente | Fecha | Alcance | Estado | Redacción permitida |
|---|---|---|---|---|---|
| CTR de México: 1.55%. CTR de EE.UU.: 0.73%. También Brasil 1.91%, Japón 1.53%, Corea del Sur 1.21%, Reino Unido 0.74%, Canadá 0.75% | Search Engine Journal https://www.searchenginejournal.com/chatgpt-ad-ctr-markets-report/591384/ ; Similarweb https://aisearch.similarweb.com/blog/chatgpt-ads-ctr-by-country/ ; PPC Land (abrir) | Reporte de Graphite publicado el 28 o 29 sep 2026, con datos hasta el 16 sep | Usuarios de planes Free y Go, panel de Similarweb, 9 mercados, entre 5 y 25 semanas de datos según el mercado | Verificado (SEJ, Similarweb y PPC Land coinciden; la cifra del CTR se leyó en resúmenes, no en la página) | "Según Graphite con datos de Similarweb (hasta el 16 sep 2026), el CTR acumulado de anuncios en ChatGPT fue de 1.55% en México y 0.73% en EE.UU." |
| Cómo se mide ese CTR: clics por intercambio con anuncio (un mensaje del usuario más la respuesta de ChatGPT), **no** por impresión | SEJ | 28 o 29 sep 2026 | Igual | Verificado | **Debe aclararse** y no comparar con el CTR de Google Search. |
| Alcance de usuarios elegibles que vieron al menos un anuncio: México 27.8% (el más bajo), EE.UU. 43.4%, Brasil 34.9% | SEJ y Similarweb | sep 2026 | Igual | Verificado | Opcional. |
| La cifra es de un panel agrupado, sin tamaños de muestra publicados | Similarweb / análisis de terceros | sep 2026 | Igual | Parcial | Añadir "datos de panel". |
| Medición: OpenAI ofrece pixel y Conversions API (CAPI) para compras, leads, instalaciones y registros. Socios: Hightouch, Tealium y LiveRamp envían datos de conversión; socios de atribución incluyen Triple Whale, AppsFlyer, Adjust, Rockerbox y otros | OpenAI https://ads.openai.com/blog/more-ways-to-measure ; Hightouch https://hightouch.com/blog/introducing-hightouch-capi-for-chatgpt-ads ; Search Engine Land (abrir) | Principios de oct 2026 (las fechas varían entre 5 y 15 oct según la fuente) | Global, anunciantes de ChatGPT Ads | Verificado en lo esencial (OpenAI y 2 fuentes más) | "OpenAI ya ofrece pixel y API de conversiones, y se conecta con herramientas de medición como Triple Whale y Hightouch." |
| OpenAI dice que una prueba de **un anunciante** (WeightWatchers, medido por DV Rockerbox) tuvo 15.3% menos CPA que el benchmark de búsqueda de pago | Blog de OpenAI (abrir) | 2026 | Un solo anunciante | Parcial. Es un solo caso y lo da el vendedor | **No usar como cifra general.** |
| Puja por CPA desde el 5 jun 2026. CAPI recomienda ventana de atribución de 30 días | ChatForest (blog de terceros) | jun 2026 | Global | Parcial | No usar. |
| Criteo: los usuarios que llegan desde ChatGPT convierten ~1.5 veces más que otros canales de referencia | Criteo, vía resumen | s/f | Tráfico referido, no anuncios | Parcial | No usar, no habla de anuncios. |
| Cifras de agencias del newsletter (cero conversiones en dos semanas, 100 clics contra 20 registros, retraso de 24 a 36 horas) | Newsletter | n/a | n/a | Sin verificar | No usar. |
| Benchmark independiente de conversión de ChatGPT Ads | No se encontró (un análisis dice que no existe benchmark entre anunciantes) | n/a | n/a | **No encontrado** | No afirmar tasas de conversión. |
| Lanzamiento en México | OpenAI lo anunció "en la próxima semana"; PPC Land lo titula como ya sumado a la lista de mercados | oct 2026 | México | Parcial | Confirmar en el blog de OpenAI antes de decir "ya disponible". |

Propuesta (5 slides): añadir **un** dato, en el slide 4 o en el slide 1, no en ambos. Opción recomendada, slide 3 (registrar la fuente) con "OpenAI ofrece pixel y API de conversiones". Si quieren cifra, el CTR 1.55% contra 0.73% va solo en el caption y con la aclaración de "por intercambio, no por impresión". Si se usa el CTR, el cierre debe decir "Fuentes: Graphite y Similarweb; OpenAI".

---

## 5. Stanford, títulos con pregunta (5 nov) — spec-stanford-v2

| Dato | Fuente | Fecha | Alcance | Estado | Redacción permitida |
|---|---|---|---|---|---|
| Artículo: "Titles framed as questions reduce reader engagement". Autores: David Fang y S. Christian Wheeler (Stanford Graduate School of Business). Revista: Journal of Consumer Psychology, vol. 36, núm. 4, pp. 470-481 | Wiley https://myscp.onlinelibrary.wiley.com/doi/10.1002/jcpy.70031 ; Stanford GSB https://www.gsb.stanford.edu/faculty-research/publications/titles-framed-questions-reduce-reader-engagement (abrir) | Versión de registro en línea: 9 jul 2026 (año 2026) | Cuatro estudios | Verificado (Wiley y GSB coinciden) | "Estudio de David Fang y S. Christian Wheeler (Stanford GSB), Journal of Consumer Psychology, 2026." |
| Posts de Reddit: N = 53,030 | Wiley y GSB | 2026 | Análisis de archivo | Verificado | Igual al slide 2: correcto. |
| Artículos académicos: N = 3,078,791 | Wiley y GSB | 2026 | Análisis de archivo | Verificado | Correcto. |
| Experimentos A/B de titulares de noticias en línea: N = 22,743 | Wiley y GSB | 2026 | Titulares de noticias | Verificado | Correcto. |
| Estudio de laboratorio preregistrado: N = 400 | Wiley y GSB | 2026 | Laboratorio | Verificado | Correcto. El slide dice "400 personas": es fiel. |
| Conclusión: los títulos con pregunta reducen la interacción porque se perciben como menos informativos. Los autores recomiendan evitar preguntas en títulos si se busca más interacción | Wiley y GSB | 2026 | Igual | Verificado | Correcto en el slide 3. |
| Porcentajes del newsletter (71.6% menos comentarios, 12.6% menos clics, etc.) | Newsletter | n/a | n/a | Sin verificar | No usar. |
| "El estudio cubre sobre todo medios occidentales" (frase del caption en Notion) | No se encontró en las fuentes revisadas | n/a | n/a | **Sin verificar** | Quitarla o confirmarla en el paper antes de publicar. |
| Estudio sobre anuncios o publicaciones de empresas (no títulos de noticias o posts) | No se encontró. Se estudian posts de Reddit, artículos académicos y titulares de noticias | n/a | n/a | **No encontrado** | Mantener "prueba en pocas piezas" como en el slide 4. |

Pendiente cerrado: Notion pedía autores, revista y año. Ya están. El slide 5 dice "Fuente: Stanford GSB" y puede completarse a "Fuente: Fang y Wheeler, Stanford GSB, Journal of Consumer Psychology (2026)".

Propuesta (5 slides): ya hay muchos datos en el slide 2 (4 viñetas, que cuentan como un bloque). No añadir cifras. Cambios mínimos: slide 3 o slide 5 con la cita completa (autores y revista).

---

## 6. Workday (5 nov, LinkedIn) — spec-workday-v2

| Dato | Fuente | Fecha | Alcance | Estado | Redacción permitida |
|---|---|---|---|---|---|
| "Close to 40% of AI time savings go to correcting errors, rewriting content, and checking outputs". Título del comunicado: "Nearly 40% of AI Time Savings Are Lost to Fixing Low-Quality Output" | Workday, "New Workday Research: Companies Are Leaving AI Gains on the Table" https://newsroom.workday.com/2026-01-14-New-Workday-Research-Companies-Are-Leaving-AI-Gains-on-the-Table y https://investor.workday.com/news-and-events/press-releases/news-details/2026/New-Workday-Research-Companies-Are-Leaving-AI-Gains-on-the-Table/default.aspx (abrir) | 14 ene 2026 | Empleados de tiempo completo de organizaciones con USD 100 millones o más de ingresos anuales que usan IA | Verificado (comunicado, Morningstar, Barchart, IT Brief, ERP Today) | "Casi 40% del tiempo que ahorra la IA se pierde corrigiendo, reescribiendo y verificando, según Workday (ene 2026)." |
| Muestra: 3,200 encuestados en Norteamérica, Asia-Pacífico y EMEA. Encuesta de Hanover Research en noviembre de 2025 | Mismo comunicado y syndicación | 14 ene 2026 (trabajo de campo nov 2025) | Igual | Verificado | El slide 3 dice "3,200 empleados de empresas con ingresos de USD 100 millones o más": es fiel. |
| Nombre del informe: "Beyond Productivity: Measuring the Real Value of AI" | Comunicado (otro medio lo escribió "What AI is Really Worth") | 2026 | Igual | Verificado (usar el nombre del comunicado) | Opcional. |
| Solo 14% de los empleados obtiene resultados netos claros y positivos de la IA | Comunicado y prensa | 14 ene 2026 | Igual | Verificado | Alternativa de dato para el slide 4. |
| Otras cifras del comunicado: 39% reinvierte el tiempo ahorrado en tecnología, 30% en desarrollo de empleados, 32% lo convierte en más carga de trabajo; 79% de quienes tienen buenos resultados recibió más capacitación | Comunicado (resumen) | 14 ene 2026 | Igual | Parcial (leídas en un solo resumen) | Solo si se confirman en el comunicado. |
| La cifra de 37% | ERP Today e Insights Media la reportan como el porcentaje de rework. El comunicado dice "close to 40%". En el comunicado, 37% es otra cosa (porcentaje de quienes tienen más retrabajo y reciben capacitación) | n/a | n/a | **Cifras en conflicto entre medios** | Usar solo "casi 40%", la redacción de Workday. No mezclar con 37%. |
| Verificación independiente de Workday | No se encontró (es encuesta comisionada por la propia empresa) | n/a | n/a | **No encontrado** | Mantener "estudio de Workday", no "estudio independiente". |
| Datos de pymes o de México | No se encontró | n/a | n/a | **No encontrado** | El slide 3 ya lo aclara bien. |
| Cifras de Supermetrics y Social Media Examiner citadas por CXL | Newsletter | n/a | n/a | Sin verificar | No usar. |

Nota sobre el slide 4 ("nada de lo que publicamos sale sin revisión"): el spec v2 ya no lo dice. Ahora dice "Mide cuánto tiempo te toma corregir lo que genera la IA". Confirmo que respeta la ficha (no afirma una práctica no registrada).

Propuesta (5 slides): los datos ya están bien repartidos (slide 2 con el 40% y la fecha, slide 3 con la muestra). Añadir como máximo el "14%" en el slide 4 o dejarlo en el caption. Cambiar "Estudio de Workday, 2026" del slide 1 por "Encuesta de Workday, ene 2026" para dar la fecha exacta.

---

## Resumen de qué añadir y dónde

| Pieza | Slides con dato nuevo | Qué | Estado |
|---|---|---|---|
| ROAS | 4 de 6 (2, 3, 4, 5) | Equilibrio al 20%, mini-tabla de 3 márgenes, fórmula con fuente, caso A contra B | CÁLCULO + fórmula verificada |
| Enlaces IA | 2 de 4 (2, 3) | Fecha 15 oct y "más arriba"; "impresiones sí, clics no" | Verificado / Parcial |
| Trigger | 0 | Sin cifras. No hay evidencia sólida | No encontrado |
| ChatGPT | 1 de 5 (slide 3) | Pixel y API de conversiones. CTR solo en caption | Verificado |
| Stanford | 0 a 1 | Cita completa (autores y revista) | Verificado |
| Workday | 0 a 1 | Fecha exacta; opcional 14% | Verificado |

Máximo un dato visual por slide en todos los casos.

## Lo que NO se encontró
- Benchmark de ROAS para servicios, México o LATAM.
- Texto de Meta sobre ROAS y margen (el artículo de Meta no apareció).
- Evidencia rigurosa o antes/después real de anuncios por trigger event.
- Cifras de clics de Google en enlaces de IA (Google no las publicó).
- Datos de conversión independientes de ChatGPT Ads.
- Verificación independiente de Workday, y datos de pymes.
- Aplicabilidad de Stanford a anuncios (el estudio es de posts, artículos y titulares).
