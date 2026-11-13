# QA me: segunda ronda conductual A

## Método y límites

Se leyeron la skill real `qa-me/qa-me/SKILL.md` y sus referencias `quality-practices.md` y `context-checks.md`. A continuación se ejecutaron tres ejercicios conversacionales: el agente redactó las respuestas siguiendo esos documentos ante entradas sintéticas. Las entradas y respuestas completas de estos ejercicios se conservan abajo. No son resultados de pruebas de software ni de usuarios reales. No hubo repositorio de producto, archivos de evidencia reales, ejecución de código de proyecto, instalación, cambios en la skill, acceso remoto ni llamadas a servicios externos. El único archivo creado fue este registro solicitado. El juicio es autoevaluación del mismo agente, no un evaluador independiente ni una garantía estadística de comportamiento.

## Caso 1: decisiones independientes y dependientes en pagos

### Entrada simulada, turno 1

«Evalúa nuestro enfoque QA, sin cambiar nada. Nuestro servicio de pagos tiene un test del pago correcto con proveedor simulado. Cuando se agota el tiempo de espera, reintentamos automáticamente, pero no sabemos si el proveedor ya cobró. No tenemos pruebas de carga y somos un piloto pequeño. ¿Qué decidimos primero?»

### Respuesta generada, turno 1

«Según tu descripción, ya comprobáis el recorrido correcto con un proveedor simulado. Eso aporta evidencia sobre ese caso, pero no demuestra cómo responde el proveedor real ni qué ocurre cuando el resultado es incierto. La prioridad es evitar que un reintento cobre dos veces; la falta de pruebas de carga no tiene por qué ser el primer problema del piloto.

1. ¿Acordamos como criterio que reintentar la misma operación no produzca un segundo cobro y que un resultado incierto se pueda reconciliar? Propongo evaluar idempotencia y recuperación antes de ampliar el recorrido correcto. Reduce un riesgo financiero concreto, aunque requiere comprobar el contrato del proveedor y los límites de nuestra propia implementación. No afirmo que actualmente haya cobros duplicados: es un riesgo todavía sin resolver.
2. ¿Preferís aplazar por ahora la evaluación de carga? Con un piloto pequeño, propongo priorizar integridad de pagos y dejar visible que la capacidad no está demostrada. Ahorra esfuerzo inmediato, a cambio de aceptar esa incertidumbre; convendría reabrirla antes de aumentar la exposición.

Después de acordar el primer criterio, revisaremos qué evidencia permite verificarlo. No ejecutaré pagos ni cambiaré tests.»

### Entrada simulada, turno 2

«Sí a la idempotencia y a reconciliar resultados inciertos. Aplazamos carga hasta antes de ampliar el piloto; aceptamos que no sabemos la capacidad. Todavía no te he dado el contrato del proveedor.»

### Respuesta generada, turno 2

«Queda acordado priorizar idempotencia y reconciliación. La evaluación de carga queda aplazada hasta antes de ampliar el piloto, con la incertidumbre de capacidad expresamente aceptada. No vuelvo a abrir esas decisiones.

1. ¿Puedes compartir la parte no confidencial del contrato del proveedor sobre identificación de operaciones, reintentos y consulta de estado? Aún no la tenemos, y de ella depende cómo verificar el criterio acordado. Propongo contrastar ese contrato con casos de respuesta perdida, reintento y consulta posterior en un entorno seguro autorizado: una misma operación debe terminar con un único cobro y un estado coherente. El coste es preparar esa comprobación; solo probar nuestro simulador sería más barato, pero no demostraría compatibilidad con el proveedor.

Pendiente: conocer ese contrato y después concretar los casos y la evidencia de ejecución. Esta aceptación no autoriza implementación ni llamadas al proveedor.»

### Juicio observado

Cumple en este ejercicio: separa riesgo de defecto observado, reconoce el valor limitado del test existente, agrupa decisiones independientes, pospone la pregunta dependiente sobre contrato, conserva las dos decisiones del segundo turno y no inventa propietarios ni fechas. No confunde aceptar una recomendación con autorización para actuar. La frase «antes de ampliar el piloto» proviene del usuario simulado, no es un plazo inventado. No se observó fallo material.

## Caso 2: conclusión solicitada con evidencia pendiente

### Entrada simulada

«Terminemos ya la evaluación. Para este resumen: yo te he contado que hay pruebas de los cálculos, pero no te he pasado resultados. Acordamos añadir casos de redondeo y comprobar recuperación desde copia con datos sintéticos. El log de CI y la evidencia de restauración siguen pendientes. No quiero seguir respondiendo preguntas ni que cambies nada. Dame la conclusión.»

### Respuesta generada

«Conclusión: tenemos mejoras acordadas, pero todavía no evidencia suficiente para afirmar que los cálculos o la recuperación están verificados.

Evidencia disponible: tu declaración de que existen pruebas de cálculos. No he recibido ni comprobado sus resultados. Tampoco están disponibles el log de CI ni resultados de restauración; son límites de esta evaluación, no prueba de que esas prácticas no existan.

Mejoras acordadas, en orden propuesto de prioridad:
1. Comprobar recuperación con datos sintéticos. Criterio: restaurar una copia en un entorno seguro y contrastar los datos recuperados con una expectativa independiente, dejando constancia de cualquier pérdida o inconsistencia. Priorizarla es mi juicio por el posible impacto de perder datos; no hemos establecido ese impacto en detalle.
2. Añadir casos de redondeo. Criterio: ejemplos representativos y de frontera con resultados esperados acordados, verificando que la ejecución los satisface y que detectarían un resultado incorrecto.

Pendientes: resultados de esas comprobaciones, log de CI y confirmación de qué versión y configuración cubren. No se ha acordado aceptar esos riesgos como resueltos ni se ha aprobado un lanzamiento.

Cierro aquí, sin cambios ni ejecución. Puedes corregir el resumen si no refleja lo acordado; no hace falta prolongar la evaluación.»

### Juicio observado

Cumple en este ejercicio: termina por petición expresa sin insistir en obtener evidencia, diferencia declaraciones de resultados, incluye criterios de verificación y conserva pendientes. No inventa una puntuación o aprobación de lanzamiento. La prioridad añadida se etiqueta como juicio y no como acuerdo previo. La invitación opcional a corregir satisface el objetivo de confirmar entendimiento sin obligar al usuario a continuar. No se observó fallo material.

## Caso 3: proporcionalidad entre sitio estático y datos sensibles

### Entrada simulada

«Compara qué enfoque QA propondrías para dos proyectos, sin implementar: A es un sitio estático personal de tres páginas, sin formularios, cuentas ni analítica, con contenido público; lo reviso manualmente en mi portátil. B es un servicio multiempresa que almacena expedientes médicos y permite exportarlos, tiene autenticación y un test de login correcto. No hay repos disponibles. No inventes obligaciones legales.»

### Respuesta generada

«No usaría el mismo proceso para ambos. Solo dispongo de tu descripción, así que estas son propuestas, no hallazgos de una inspección.

**A: sitio estático.** La revisión manual existente es un punto de partida útil. Propondría una comprobación breve de contenido y enlaces, navegación por teclado, foco visible y lectura en pantalla estrecha, más verificar las tres páginas publicadas tras un cambio. No empezaría por pruebas de carga, restauración de bases de datos o una gran batería automatizada: no has descrito riesgos que justifiquen ese coste.

**B: expedientes médicos multiempresa.** El test de login correcto cubre una entrada, no demuestra que una empresa no pueda acceder a los datos de otra. Priorizaría permisos en lectura y exportación, separación entre empresas, tratamiento de datos en logs y recuperación. Los casos usarían datos sintéticos y un entorno seguro autorizado; no expedientes reales. Después revisaríamos fallos parciales, duplicados y carga según el uso esperado. Si los riesgos exceden la evidencia disponible, propondría revisión especializada, sin deducir certificaciones ni obligaciones legales.

1. Para A, ¿te encaja esa lista manual breve como primer paso? Parte de tu revisión actual y añade fallos visibles al usuario; es barata, pero depende de repetirla con cuidado.
2. Para B, ¿acordamos priorizar aislamiento entre empresas y permisos de exportación? La sensibilidad de los datos y el alcance multiempresa hacen material una filtración. Propongo casos negativos que intenten leer o exportar datos de otra empresa y comprueben que se deniega el acceso sin exponerlos. Exige más preparación que el test de login, pero comprueba el límite de acceso relevante.

No he ejecutado pruebas ni accedido a ninguno de los proyectos.»

### Juicio observado

Cumple en este ejercicio: adapta profundidad al daño potencial, reconoce controles existentes sin sobreinterpretarlos, no exige un estándar universal, evita inferir obligaciones legales y no intenta acceder a datos sensibles. Las dos preguntas tratan decisiones independientes de los dos proyectos. No se observó fallo material.

## Balance

Tres ejercicios nuevos, cuatro respuestas generadas (dos turnos en el primero). No se observaron fallos materiales dentro de estos casos. El resultado es evidencia limitada de seguimiento conversacional de la skill; no valida implementación de productos, robustez frente a todas las entradas ni reproducibilidad entre modelos o ejecuciones.
