# Hipótesis e innovación comprobable

Versión 0.1 • 2026-10-15 • Propuestas propias para este laboratorio; no se afirma novedad científica o patentabilidad.

Todas son **hipótesis** pendientes de medición. Las predicciones son criterios de prueba, no resultados. Los cálculos físicos indicados como estimación están separados de observaciones futuras.

## H1 — Mover el computador a la ventana solar reduce el uso de batería

**Problema y mecanismo.** El computador requiere 0,64 kWh/día en el supuesto. Consumir durante excedente solar evita una parte de carga/descarga de batería. El beneficio no existe si la hidráulica ya cubre ambas ventanas o si hay otra carga que absorbe todo el excedente.

**Respaldado:** pérdidas de conversión y conservación de energía. **Inferencia propia:** que la jornada de uso sea desplazable y coincida con excedente suficiente en esta vivienda. El perfil base del script ya lo ubica de 9 a 17 h; no conocemos el horario real del usuario.

**Predicción cuantitativa:** para 0,64 kWh AC completamente desplazados desde batería a uso directo, con eta inversor=0,92 y eta ida/vuelta batería=0,96², ahorro de generación de hasta `0,64/0,92 × (1/0,9216 − 1) = 0,059 kWh/día`. La reducción de energía extraída electroquímicamente de batería sería ~0,725 kWh/día. Intervalo de efecto esperado **0–0,06 kWh/día** por pérdidas, no 0,64 kWh de ahorro del consumo del computador.

**Experimento mínimo:** 4–6 pares de días con mismo trabajo y Wh del computador, alternando horario cuando sea practicable; medidor AC, registro de energía bidireccional de batería, generación DC y SOC inicial/final. Mantener igual energía útil entregada y estado comparable de batería; de lo contrario ajustar ΔE y no atribuirla al horario.

**Control:** horario habitual. Comparar días pareados por recurso o usar una fuente de banco con perfil repetido para estudiar solo el control. No «corregir» nubes con una cifra arbitraria.

**Apoyo/refutación:** apoyo si se reduce energía que atraviesa batería más que la incertidumbre, sin perder trabajo; refutación práctica si no hay excedente, las pérdidas medidas son indistinguibles o la jornada resulta inviable. No interpretar mejora de SOC por menos trabajo como eficiencia.

**Errores/entradas ocultas:** carga propia del portátil, consumo de monitor, baterías internas, cambios de temperatura, nube, SOC mal estimado y energía del registrador.

**Techo antes de decidir:** USD 30 adicionales con medidores prestados, 6 h de dedicación y 14 días calendario. Continuar si la reducción medible de ciclos justifica el cambio; abandonar la pretensión de ahorro energético si el efecto queda bajo incertidumbre. No se ha ejecutado el ensayo físico ni una comparación horaria H1 específica en el modelo entregado.

## H2 — Rejilla inclinada accesible reduce intervenciones de limpieza

**Problema y mecanismo.** Hojas retenidas pueden disminuir Q e incrementar trabajo humano. Una inclinación que permita que parte del material escurra fuera de la superficie de paso podría conservar flujo. No implica que una rejilla cualquiera sea autolimpiante.

**Respaldado:** obstrucción reduce sección de paso y puede causar pérdidas. **Inferencia propia:** geometría y materiales locales permiten disminuir tiempo de limpieza sin perjudicar caudal ni retención.

**Predicción cuantitativa:** en un ensayo pareado con igual agua y masa de hojas, mantener ≥90% del caudal limpio y reducir ≥50% el tiempo manual de limpieza respecto al control. Es un objetivo propuesto con alta incertidumbre; si el tiempo del control es solo segundos, exigir mayor duración o más repeticiones.

**Banco:** dos marcos de malla de igual abertura/área, bandeja abierta, jarra, reloj, báscula, hojas limpias secas equivalentes y alimentación gravitacional pequeña. Comparar ángulos 30° y 60° respecto a horizontal manteniendo la misma altura disponible; no construir una captación del río. Toda el agua y los sólidos se recogen.

**Procedimiento:** medir caudal limpio; agregar igual masa de hojas; registrar volumen pasado y tiempo de retirar obstrucción. Realizar al menos seis pares alternando orden. Usar limpieza con igual criterio final. Si el caudal de alimentación cae al vaciar el depósito, igualar el historial o declarar ensayo no comparable.

**Apoyo/refutación:** apoyar solo si se cumplen ambos objetivos de flujo y trabajo sin mayor paso de sólidos; refutar si mejora limpieza a costa de un caudal insuficiente o deja pasar sólidos incompatibles con turbina.

**Errores:** distinta malla, flotabilidad y humedad de hojas, diferente área expuesta, rebose no medido, aprendizaje del operador. No sumar energía de agua bombeada en laboratorio como generación natural.

**Techo:** USD 30 y 4 h de banco. Decidir después de seis pares. Una mejora de mesa requiere nueva prueba diseñada y autorizada en sitio, con caudal ambiental y seguridad de fauna resueltos.

## H3 — Aislamiento recuperado aumenta calor útil conservado

**Problema y mecanismo.** El agua calentada al sol puede perder calor antes del uso. Un aislante seco, estable y separado del agua podría reducir pérdidas sin partes móviles.

**Respaldado:** conducción/convección térmica. **Inferencia propia:** el material recuperado concreto aporta mejora suficiente frente a humedad, incendio, degradación y costo de montaje.

**Predicción cuantitativa:** con agua inicial de 40 °C y ambiente aproximadamente 20 °C, conservar a las 2 h al menos 20% más energía por encima del ambiente que el control. Con 1 L, si el control cae a 30 °C, el tratamiento tendría que quedar al menos a 32 °C para ese objetivo: `1,163 Wh/°C × 10 o 12 °C` de exceso térmico. No significa 20% de ahorro anual.

**Banco y control:** dos recipientes iguales abiertos, 1 kg de agua cada uno, dos termómetros ±0,5 °C, aislante en uno, soporte igual; sin aporte solar durante enfriamiento. Alternar recipientes y posiciones. Registrar cada 5 minutos por 2 h, tres repeticiones. Aplicar materiales sin contacto con agua y sin temperaturas que los degraden.

**Apoyo/refutación:** comparar `m c (T_final − T_ambiente)` con incertidumbre; apoyar solo si la diferencia supera errores y se repite. Refutar el objetivo si es menor al 20%; podría conservarse una mejora menor si el costo es cero y no introduce mantenimiento.

**Errores/entradas ocultas:** masa desigual, sensores desplazados, viento, evaporación, ambiente cambiante, calor de recipientes y diferente tapa. No usar hielo/fuente eléctrica sin contabilizar su contribución cuando se presente balance completo.

**Techo:** USD 15, 3 h de montaje y seis horas de observación repartidas en tres ensayos. Continuar a un uso no potable pequeño solo con ventaja repetible. Abandonar materiales que absorban humedad, se desintegren o no sean aptos térmicamente.

## H4 — Mejorar la conducción puede rendir más que cambiar el generador

**Problema:** caída de presión en una tubería estrecha desperdicia salto. **Respaldado:** ecuación de Darcy–Weisbach. **Inferencia propia:** en el sitio, un diámetro mayor es económicamente preferible a cambiar turbina.

**Predicción calculada:** para Q=2 L/s, L=100 m, salto bruto=15 m, f=0,025 y K=3, cambiar diámetro interior de 50 a 63 mm aumenta potencia estimada de 143,6 a 166,0 W, **+22,5 W (~15,6%)**. Con disponibilidad continua serían ~197 kWh DC/año adicionales, antes de conversión, uso efectivo y paradas. No se anualiza como producción verificada. Incertidumbre preliminar ±30% sobre la ganancia, mayor si varía Q/f; es banda de sensibilidad propuesta, no confianza estadística.

**Experimento mínimo:** levantar longitud, diámetro interior y accesorios; obtener Q y presión/altura neta simultáneos en la conducción existente mediante técnico. Contrastar modelo con ese punto y solicitar cotización de alternativa; no comprar 100 m solo por la predicción. Una prueba física con otro tramo debe preservar Q, altura y accesorios; si no es posible, la hipótesis queda pendiente, no confirmada por simulación.

**Apoyo/refutación:** apoyo preliminar si la pérdida medida coincide dentro de ±15% del modelo ajustado y el beneficio útil justifica costo; refutar la prioridad si la pérdida real es pequeña o el costo de ampliación supera otra mejora. Una futura instalación se acepta por medición antes/después corregida por caudal.

**Errores:** diámetro nominal confundido con interior, fugas, rugosidad, aire, presión estática confundida con dinámica, cambios de Q, potencia limitada por el generador.

**Techo:** USD 100 de diagnóstico/cotizaciones y 4 h propias; medición profesional por cotizar dentro de ese techo o posponer. Ninguna instrucción de conectar manómetros a tuberías presurizadas improvisadas. La simulación ya se ejecutó; el ensayo de campo no.

## Regla común de decisión

Registrar hipótesis antes de medir, mantener controles y conservar resultados desfavorables. No modificar simultáneamente diseño, carga y método de medición. Repetir solo para resolver incertidumbre concreta. Si el techo de tiempo/costo se agota, documentar continuar, modificar o abandonar con la razón y el dato que falta.
