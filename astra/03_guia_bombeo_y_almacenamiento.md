# Bombeo directo y almacenamiento útil

Versión 0.1 • 2026-10-15 • Complemento para la finca, sujeto a necesidad de agua.

## Objetivo y energía

**demostrado:** un ariete usa energía de agua descendente para elevar una fracción del caudal sin motor eléctrico. [NC State Extension, Hydraulic Ram Pumps, revisión de marzo de 1996](https://content.ces.ncsu.edu/hydraulic-ram-pumps). El principio sigue siendo útil; no se toman sus precios o proveedores como actuales.

Dos rutas: **sol → bomba → tanque → riego por gravedad**; **agua con caída → ariete → fracción elevada → tanque**, con el resto retornando al cauce. El tanque almacena agua y energía previamente suministrada.

**Estimación:** elevar 5 m³ a 20 m requiere 0,2725 kWh hidráulicos; con eficiencia total 45%, 0,606 kWh eléctricos. Para hacerlo en 4 h se necesitan ~151 W eléctricos medios, sin contar arranque ni pérdidas adicionales fuera de esos 20 m totales.

Un tanque de 1 m³ a 10 m almacena apenas **0,02725 kWh potenciales**, antes de pérdidas. Sería poco práctico proponerlo como batería de varios kWh; puede ser excelente para abastecer agua sin bomba nocturna.

## Fases 0–2: prueba pequeña y medición

Medir demanda diaria de agua, altura total, presión requerida, pérdidas de conducción y días de reserva. No asumir que los 20 m de altura geométrica incluyen fricción.

Banco de mesa: una bomba comercial de 5 V y ≤5 W apta para agua, fuente USB certificada con límite de corriente, medidor USB Wh, dos recipientes abiertos, manguera y regla; retorno libre. Provisión **USD 20–60**, instrumentos comunes aparte, presupuesto minorista internacional de 2026-10-15. Recuperar recipientes limpios y soportes; no recuperar una fuente dañada ni abrirla.

1. Con fuente desconectada, colocar bomba según su manual y salida a 0,2–0,5 m de altura en soporte estable. Conservar electrónica USB seca.
2. Alimentar por conector diseñado para ello. No obstruir totalmente salida ni dejar funcionar en seco si el fabricante no lo permite.
3. Medir volumen elevado en 60 s, altura, V/I o Wh de entrada y tiempo. Repetir tres veces a cada altura, sin exceder límites.
4. Calcular energía hidráulica `m g H` y compararla con eléctrica de entrada. Si recircula, toda la electricidad de bombeo sigue siendo una entrada; no hay generación neta.

Aceptación: volumen reproducible dentro de ±10%, balance físico coherente y operación dentro de especificaciones. Una bomba de acuario no predice la curva de una bomba de finca.

## Ariete: estudio y piloto profesional

Ejemplo supuesto: Q de alimentación=0,5 L/s; caída=2 m; elevación=20 m; rendimiento=50%. `q_elevado = Q × caída × eta / elevación = 0,025 L/s`, o **2,16 m³/día**. Los otros ~0,475 L/s se descargan; deben tener retorno seguro y autorizado. Caídas y elevaciones aquí deberían ser netas para comparar energía.

Componentes a cotizar: 1 ariete comercial adecuado a Q/H, conducción de impulso dimensionada, cámara/elementos de presión certificados, válvulas, anclajes, descarga, tanque apto y medición. Provisión inicial **USD 300–1.000** solo para conjunto pequeño instalado con acceso sencillo; tanque y conducciones extensas excluidos. No es precio observado.

No se incluyen instrucciones para fabricar cámaras de aire presurizadas: la presión transitoria y fatiga requieren diseño. Solicitar ensayo de caudal entregado a la altura de servicio y operación segura antes de recepción.

## Fases 3–7: servicio y límite

Piloto: abastecer un uso no crítico durante 30 días; registrar litros útiles, horas de intervención y nivel de reserva. Para finca, programar bomba solar cuando hay excedentes y usar control de nivel, protección contra trabajo en seco y rebose seguro. Dimensionar tanque por demanda y continuidad hídrica, no por su capacidad de producir electricidad al vaciarse.

Mantener accesibles filtros y válvulas; inspección semanal inicial, más frecuente según sedimentos. Conservar repuestos identificados. Un mismo caudal no se asigna completo a ariete y turbina simultáneamente: comparar en paralelo o en cascada según caudales y alturas realmente disponibles. El límite es el servicio de agua; no promete autonomía eléctrica.
