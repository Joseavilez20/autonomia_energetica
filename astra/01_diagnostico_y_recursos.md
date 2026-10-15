# Diagnóstico y recursos

Versión 0.1 • 2026-10-15 • Todos los valores de diseño sin medición son ilustrativos.

## Cinco preguntas iniciales, con el estado de sus respuestas

1. ¿Dónde y en qué tipo de sitio empezarás? **Respuesta parcial: vivienda rural.** País, municipio, altitud, coordenadas aproximadas, espacio y sombras: pendientes.
2. ¿Hay corriente de agua aprovechable con desnivel? **Respuesta: sí, todo el año.** Caudal, altura útil, distancia, derechos de uso y estiaje: pendientes.
3. ¿Qué alcance tendrá el primer piloto? **Respuesta: también nevera y computador.** Sus características eléctricas y horarios todavía no se conocen.
4. ¿Cuál es el país/municipio y cómo son el recorrido del agua hasta la vivienda, el desnivel aproximado y el espacio soleado disponible?
5. ¿Qué indican tus facturas y equipos, cuánto puedes invertir en pruebas y luego en el piloto, qué herramientas/experiencia/horas semanales tienes y cuánto tiempo sin energía aceptarías con qué respaldo?

Las preguntas 4 y 5 completan las anteriores; no es necesario saber todo para iniciar mediciones. No se ha supuesto que la propiedad esté en Colombia por la ubicación de la cuenta.

## Inventario ilustrativo de cargas

| Carga | Potencia y uso supuestos | Energía AC diaria | Qué medir |
|---|---|---:|---|
| Nevera | 50 W de promedio temporal, NO potencia del compresor | 1.200 Wh | kWh/7 días, temperatura ambiente, aperturas; arranque por separado |
| Computador | 80 W, 8 h/día | 640 Wh | Consumo con tareas normales, monitor y cargador |
| Router | 12 W, 24 h/día | 288 Wh | W activos y tensión de alimentación |
| Luces | 4 × 7 W, 4 h/día | 112 Wh | Horarios reales y simultaneidad |
| Teléfonos | 10 W, 2 h/día equivalentes | 20 Wh | Energía de carga, sin duplicar computador si carga por USB |
| Otras cargas pequeñas | Reserva explícita, repartida uniformemente solo en el modelo | 380 Wh | Reemplazar por equipos concretos; no confundir reserva con consumo medido |
| **Total supuesto** | **Promedio 110 W** | **2.640 Wh = 2,64 kWh** | **Pendiente de medición** |

No se incluyen ducha, cocina eléctrica, aire acondicionado, bomba ni herramientas. Una resistencia de 3 kW durante 20 minutos añadiría 1 kWh: las cargas térmicas pueden cambiar por completo la arquitectura. La potencia de arranque no se deduce dividiendo kWh por horas.

Medición de demanda: medidor enchufable certificado y compatible con la red/carga, sin abrir tableros. Registrar siete días completos, ampliables a 14–30 si el uso varía. Revisar 12 meses de facturas y distinguir cargos fijos de energía. Para motores y circuitos fijos, pedir registrador/pinza con captura de arranque a una persona competente. Registrar duración de cada pico, tensión y simultaneidad.

## Plan de medición de recursos

| Recurso | Primera observación | Seguimiento necesario | Qué permite concluir y qué no |
|---|---|---|---|
| Agua | Cinco llenados de recipiente en una salida ya existente y accesible; croquis de recorrido y nivelación | Registro de nivel/caudal semanal y en cambios meteorológicos, abarcando lluvias y estiaje; idealmente un año y contraste histórico | La visita estima ese momento; no demuestra caudal de diseño de temporada seca |
| Desnivel | Nivel de agua transparente o topografía prestada; medir desnivel vertical, no longitud de pendiente | Verificación profesional antes de conducción de presión; medir pérdidas en operación | Altura bruta no equivale a altura neta |
| Sol | Mapa de sombras a las 8, 10, 12, 14 y 16 h en suelo seguro | Datos horarios multianuales del lugar, horizonte y sombras por estación; registro local de prueba 2–4 semanas | Un día soleado no representa el mes desfavorable |
| Viento | Reconocer obstáculos, sin comprar turbina | Anemómetro a altura de buje; preferiblemente al menos un año correlacionado con datos más largos | Viento sentido a nivel de suelo o un mapa regional no justifican producción anual |
| Residuos | Pesaje diario por tipo, agua disponible y uso actual | Al menos 2–4 semanas de inventario y continuidad estacional; ensayo de laboratorio de potencial si es candidato | kg húmedos no son m³ de metano; faltan sólidos y biodegradabilidad |
| Calor residual | Temperaturas de fuente y sumidero bajo operación normal | Horas de disponibilidad, flujo de calor y efecto del recuperador sobre el proceso | Una superficie caliente no demuestra potencia eléctrica recuperable |

La recomendación de campaña eólica está respaldada por [DOE, Small Wind Guidebook](https://www.energy.gov/cmei/systems/windexchange/small-wind-guidebook), consulta 2026-10-15. Las duraciones iniciales de carga, residuos y pruebas son un plan propuesto, no normas de certificación.

## Agua: balance que falta construir

`Q_utilizable = min(Q_disponible_tras_usos_y_restricciones, Q_admitido_por_captacion_y_tuberia, Q_admitido_por_turbina)`.

No derivar todo el caudal observado. Registrar usos existentes, devolución, paso de fauna, sedimentos, crecientes y acceso de mantenimiento. El mínimo ecológico y los permisos no se inventan: se consultan con la autoridad competente una vez conocida la ubicación. Disponer de terreno junto a una quebrada no demuestra autorización de uso.

Para caudales mayores que una salida pequeña, contratar medición de sección y velocidad u otro método adecuado. Un flotador superficial solo sirve como aproximación y exige correcciones; no usar un único factor arbitrario como dato final.

## Datos, incertidumbre y decisión

Mantener columnas separadas para observación, unidad, instrumento, fecha, incertidumbre y origen: medido / factura / climatología / supuesto. Para `P = rho g Q H eta`, una cota conservadora inicial suma los errores relativos de Q, H y eta. Con Q ±10%, H ±5% y eta ±20%, una cota de ingeniería es ±35%; no es un intervalo estadístico del 95%.

Un primer filtro propuesto para el ejemplo de 2,64 kWh/día es comprobar si el caudal de estiaje autorizado y el salto neto permiten al menos unos **156 W DC medios**, incluyendo un margen arbitrario del 20% sobre los 129,6 W necesarios antes de pérdidas de batería. A 12 m y eta=0,60 eso exige unos **2,20 L/s**. El margen no sustituye simulación temporal ni evaluación de paradas.

Si hay menos recurso, la hidráulica puede seguir siendo útil como complemento. Si las obras o permisos dominan el costo, avanzar en la alternativa solar mientras se resuelve la evaluación del agua.

## Entregables de fase 0

- Tabla de cargas reales y de cargas aplazables; demanda diaria, máxima simultánea y arranques.
- Croquis con cotas, distancias, sitio de toma/retorno y fotos de sombras, sin levantar estructuras.
- Primera serie de caudal y nivel con estación del año identificada.
- Lista de restricciones del sitio y de repuestos disponibles localmente.
- Decisión de qué experimentos efectuar con un techo de gasto aprobado por el propietario.

No están completados todavía: estos entregables requieren observación de la propiedad. Las plantillas vacías destinadas a registro están en `07`; el análisis y las guías del paquete sí contienen desarrollo completo.
