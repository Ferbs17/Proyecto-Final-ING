## Métrica externa de **Completitud de implementación funcional** : 

| Nombre de la métrica | Completitud de implementación funcional |
| --- | --- |
|Próposito de la Métrica | ¿Qué tan completa está la implementación funcional? |
| Método de aplicación: | Contar las funciones faltantes detectadas en la evaluación y comparar con el número de funciones descritas en la especificación de requisitos  |
| Medición, fórmula y cálculo de elementos de datos: | X = 1 - A/B |
| Interpretación del valor medido: | 0 <= X <= 1> , (lo más cercano a 1 es lo mejor)| 
| Tipo de escala Métrica: | Absoluta |
| Entrada para la medición: |Especificación de requisitos Diseño Código fuente Informe de revisión|
| Tipo de medida: | X = Cantidad, A = Cantidad, B = Cantidad|
| Referencia PCVS ISO/IEC 12207: | 6.6 Validación 6.6 Revisión conjunta |
| Audiencia objetivo: | Desarrollador y Usuario | 

*(A= número de funciones faltantes, B = número de funciones descritas en la especificación de requisitos)*

Tras el usuario y los desarrolladores hacer el recuento de funciones se llegó a la conclusión que hay un total requerido de 7 funciones. 
El usuario reviso la aplicación y pudo ubicar 6 por lo cual hay una función faltante.

A = 6

B = 7

X = 1 - A/B = 1 - (6/7) = 1 - 0.8571428571 = *0.142857142.* 

&nbsp;

## Métrica externa de **Tiempo de respuesta** : 

| Nombre de la métrica | Tiempo de respuesta |
| --- | --- |
|Próposito de la Métrica | ¿Cuál es el tiempo estimado para completar una tarea.? |
| Método de aplicación: | Evaluar la eficiencia de las llamadas al SO y a la aplicación, estimar el tiempo de respuesta basado en ello. |
| Medición, fórmula y cálculo de elementos de datos: | X = tiempo (calculado o simulado) |
| Interpretación del valor medido: | Entre más corto, mejor.| 
| Tipo de escala Métrica: | Proporción |
| Entrada para la medición: |Sistema operativo conocido & Tiempo estimado en llamadas al sistema |
| Tipo de medida: | X = Tiempo (segundos)|
| Referencia PCVS ISO/IEC 12207: | Verificación & Revisión conjunta |
| Audiencia objetivo: | Desarrollador y Usuario | 

Se realizo el cálculo con el usuario usando un cronometro para medir el tiempo de respuesta y a su vez la biblioteca “time” para que diera el tiempo de respuesta en tiempo real al usar la app. 

En un dispositivo android tarda 2.35 segundos en iniciar la app y permitirnos acceder a las funciones. En el sistema windows tarda aproximadamente 5.36 segundos.

**Esto nos da un promedio de respuesta de 3.855 segundos**