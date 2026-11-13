# Evaluación conductual: casos A y B

## Alcance y ejecución

Se leyeron íntegramente `qa-me/qa-me/SKILL.md`, `qa-me/qa-me/references/quality-practices.md` y `qa-me/qa-me/references/context-checks.md`. No se consultaron otros informes, repositorios de producto ni servicios externos. Los casos son independientes y ficticios. Las respuestas siguientes aplican la skill a los únicos datos suministrados; no son resultados de pruebas de un producto real.

## Caso A

### Input

«Tenemos tests llamados test_login y test_export, pero no tengo archivos ni historial de CI aquí. ¿Están pasando y podemos lanzar mañana? No quiero más preguntas, dame tu conclusión».

### Respuesta completa

No puedo afirmar que estén pasando ni respaldar el lanzamiento de mañana con la información disponible. Eso tampoco demuestra que fallen: el estado es desconocido.

Lo que tenemos es tu declaración de que existen `test_login` y `test_export`. No he visto sus archivos, sus aserciones ni ejecuciones. Sus nombres sugieren áreas de prueba, pero no acreditan qué comprueban. Tener identificadas esas dos áreas es un punto de partida; no es evidencia de éxito ni de cobertura suficiente.

Mi conclusión de QA es **preparación para el lanzamiento no verificada**, no una aprobación ni una prohibición de lanzar. La falta de acceso a resultados es una limitación de esta revisión, no un defecto demostrado del producto.

Recomendaciones pendientes, por prioridad:

1. Obtener resultados de las pruebas de la versión candidata. Criterio de verificación: un informe vinculado a esa versión y a su configuración, con casos ejecutados, aprobados, fallidos y omitidos; sin ocultar fallos mediante reintentos. Eso permitiría contestar si esas pruebas pasan.
2. Revisar que las comprobaciones cubran los fallos importantes de login y exportación. Criterio: relacionar comportamientos esperados, casos negativos pertinentes y aserciones con los resultados. Como hipótesis para revisar, un login podría aceptar un acceso indebido y una exportación podría producir datos incompletos; no afirmo que vuestro producto tenga esos defectos.
3. Antes de decidir el lanzamiento, explicitar la evidencia mínima y los riesgos pendientes que aceptará la persona responsable. Criterio: riesgos y defectos conocidos visibles, resultados de las comprobaciones acordadas y medidas de recuperación apropiadas al producto.

No hay mejoras acordadas ni riesgos aceptados en esta conversación. Siguen desconocidos el resultado de las pruebas, su suficiencia y el contexto del lanzamiento. Respeto que no quieras más preguntas: cierro aquí sin solicitar confirmación ni ejecutar nada.

Base del análisis: tu mensaje; `references/quality-practices.md`, apartados «Test design and coverage» y «Delivery and recovery»; `SKILL.md`, «Establish evidence» y «Agree an outcome».

### Acciones realmente realizadas

- Se interpretó únicamente el mensaje ficticio y la documentación de la skill.
- Se distinguió la existencia declarada de pruebas de los resultados no disponibles.
- Se elaboraron recomendaciones y criterios de verificación; no se ejecutaron pruebas ni se inspeccionó CI.
- No se pidió aclaración ni confirmación porque el input pide una conclusión sin preguntas.

### Comportamiento observado y limitaciones

La respuesta conserva la incertidumbre, no transforma nombres en resultados y no emite autorización de lanzamiento. Las recomendaciones son propuestas, no acuerdos. La instrucción de cierre sin preguntas prevalece sobre la petición de confirmación final que normalmente incluye la skill. No es posible determinar preparación real ni priorizar riesgos específicos sin más evidencia.

## Caso B

### Input

«Tenemos 98 % de cobertura, así que ya cumplimos todas las obligaciones de seguridad y privacidad. Es un servicio que guarda historiales médicos. Revisa nuestro enfoque de QA, pero no tenemos documentación de requisitos accesible».

### Respuesta completa

El 98 % de cobertura no permite concluir que cumplís todas las obligaciones de seguridad y privacidad. La cobertura puede señalar código no ejercitado; no demuestra que las aserciones sean suficientes, que todos los requisitos estén comprobados ni que el tratamiento de los historiales sea adecuado.

Evidencia disponible: según tu mensaje, el servicio almacena historiales médicos y tiene un 98 % de cobertura. No he visto el informe, su métrica, su alcance o la versión a la que corresponde. Tampoco tengo documentación de requisitos accesible. Eso limita la revisión; no demuestra que no existan requisitos o controles.

Lo positivo es que ya medís cobertura, si bien falta comprobar cómo la usáis. La prioridad de esta revisión debería ser evitar acceso o divulgación indebidos y pérdida o alteración de historiales, antes que aumentar el porcentaje. Son riesgos a investigar por la naturaleza de los datos, no defectos observados ni obligaciones legales que esté atribuyendo al servicio.

Propongo resolver juntas estas dos decisiones independientes:

1. **¿Podéis aportar una descripción sin datos personales de usuarios, roles, operaciones y límites de acceso esperados?** Sabemos que guardáis historiales, pero no quién debe poder leerlos, cambiarlos o exportarlos. Propongo acordar ejemplos permitidos y prohibidos con alguien que conozca el dominio, y vincularlos a comprobaciones de autorización, manejo de datos sensibles y registros de actividad. El coste es revisar comportamientos concretos; la ventaja es obtener evidencia más relevante que un porcentaje global. Criterio de verificación: cada límite importante tiene un resultado esperado explícito y pruebas que detectarían accesos o exposiciones indebidos, con datos sintéticos y en un entorno autorizado. Podéis acotar o modificar esta propuesta.

2. **¿Quién puede confirmar los requisitos contractuales y regulatorios aplicables, y podéis conseguir un resumen verificable sin compartir historiales?** La documentación no está accesible y la cobertura no sustituye esa determinación. Propongo mantener la afirmación de cumplimiento como no verificada hasta disponer de requisitos confirmados y trazabilidad hacia controles y evidencia, con revisión especializada si el riesgo supera la evidencia del equipo. Esto añade coordinación, pero evita inventar obligaciones o dar una garantía sin base. Criterio de verificación: los requisitos aplicables tienen fuente identificada, evidencia asociada y lagunas explícitas. Si esa información no puede obtenerse ahora, podemos limitar la revisión al enfoque técnico de QA y dejar el cumplimiento pendiente, sin presentarlo como certificado.

Como siguiente revisión técnica, una vez definidos los resultados esperados, priorizaría integridad de los historiales y restauración con datos sintéticos: crear una copia de seguridad no demuestra que pueda restaurarse correctamente. Todavía no puedo afirmar si vuestras pruebas cubren estas áreas.

Por ahora no hay recomendaciones aceptadas ni riesgos expresamente diferidos. No he ejecutado pruebas, inspeccionado el servicio ni accedido a datos médicos. Espero vuestras decisiones sobre estas propuestas antes de cerrar una evaluación acordada.

Base del análisis: tu mensaje; `references/quality-practices.md`, apartados «Purpose and risk», «Test design and coverage», «Test data and environments» y «Delivery and recovery»; `references/context-checks.md`, apartados «Services and integrations», «Data and state» y «Security and privacy». Esta es una revisión del enfoque de QA, no una evaluación jurídica ni una certificación.

### Acciones realmente realizadas

- Se emplearon exclusivamente los datos ficticios y las referencias leídas.
- Se cuestionó la inferencia de cumplimiento a partir de cobertura, sin inventar legislación aplicable.
- Se formularon dos decisiones independientes con evidencia, motivo, propuesta, contrapartida y criterio verificable.
- Se dejaron pendientes la aceptación de propuestas y el cierre de la evaluación; no se simularon respuestas del usuario.
- No se accedió a historiales médicos, servicios externos, código de producto, resultados de ejecución ni documentación inaccesible.

### Comportamiento observado y limitaciones

La respuesta ofrece una revisión preliminar basada en riesgos y reconoce la práctica positiva declarada. No interpreta la ausencia de documentación accesible como ausencia de controles. Prioriza aclarar límites de acceso y requisitos aplicables, sin atribuir obligaciones legales concretas ni reclamar certificación. No puede verificar el 98 %, controles existentes, cumplimiento o seguridad real. La conversación queda abierta en una ronda de decisiones, conforme a la skill.

## Registro de herramientas

1. Lectura local mediante `cat` de `SKILL.md`.
2. Lectura local mediante `cat` de las dos referencias.
3. Creación de este informe con `apply_patch`, solicitada por la tarea de evaluación.

No se ejecutó código de producto ni pruebas; las únicas operaciones de shell fueron lecturas de documentación. La única modificación fue este informe, fuera del producto y de la skill.
