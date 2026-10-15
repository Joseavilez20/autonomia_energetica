# Bitácora de mediciones, fallos y decisiones

Versión 0.1 • 2026-10-15. Plantillas listas para copiar; ninguna fila pendiente representa una medición realizada.

## Identificación de la prueba

| Campo | Registro |
|---|---|
| ID / versión de montaje | Pendiente |
| Fecha, hora inicial/final y zona horaria | Pendiente |
| Sitio y responsable | Pendiente |
| Objetivo / hipótesis antes de probar | Pendiente |
| Tratamiento y control | Pendiente |
| Frontera energética y entradas posibles | Pendiente |
| Instrumentos, rango, resolución, exactitud y última comparación | Pendiente |
| Material recuperado y verificación | Pendiente |
| Criterio de aceptación / límite de parada | Pendiente |
| Techo de gasto y de horas | Pendiente |

## Registro de cargas

| Equipo | Modelo / tensión | W activos | VA / FP si disponible | Pico y duración medidos | Horas | Wh diarios | Prioridad | Origen y fecha |
|---|---|---:|---|---|---:|---:|---|---|
| Nevera | Pendiente | — | — | — | — | — | Esencial | Pendiente de medición |
| Computador y monitor | Pendiente | — | — | — | — | — | Según jornada | Pendiente de medición |

Anotar temperatura ambiente, ciclos de uso y cambios de equipos. No reemplazar W activos por VA sin factor de potencia. La reserva de 380 Wh/día del modelo se elimina o desglosa al completar el inventario.

## Recurso hidráulico

| Fecha/hora | Método | Volumen L | Tiempo s | Caudal L/s | Altura bruta/netas m | Lluvia/estación | Restricciones/usos | Incertidumbre |
|---|---|---:|---:|---:|---|---|---|---|
| Pendiente | Pendiente | — | — | — | — | — | — | — |

Conservar cada repetición, no solo el promedio. Registrar si el caudal es total del cauce, derivado, autorizado o medido en salida de banco; son cantidades distintas.

## Energía eléctrica sincronizada

| Tiempo y Δt | V entrada | I entrada | W entrada | Wh entrada | W salida | Wh útiles | Wh auxiliares | Energía batería inicial/final | Observaciones |
|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| Pendiente | — | — | — | — | — | — | — | — | — |

Para AC registrar potencia activa del medidor y si el instrumento puede medir la carga. Para batería conservar Ah/Wh bidireccionales, temperatura, límites y método de SOC; el porcentaje de una pantalla no es por sí solo una medida precisa de energía.

## Calor y controles

| Ensayo | Recipiente/posición | Masa inicial/final | T inicial/final | T ambiente | Tiempo | Energía agua | Control emparejado | Condiciones |
|---|---|---|---|---|---|---|---|---|
| Pendiente | — | — | — | — | — | — | — | — |

Si no hay irradiancia medida, reportar energía térmica obtenida y diferencia contra control, no eficiencia solar. Registrar si cambiaron tapas, masa, aislamiento o viento.

## Balance y cierre de ensayo

`Residual = E_entrada − E_útil − E_auxiliares − E_pérdidas_estimadas − ΔE_almacenamiento − E_descartada`.

Si alguna pérdida no se midió, puede aparecer en el residual: no asignarla con certeza a un componente. No «ajustar» entradas para conseguir rendimiento deseado. Expresar incertidumbre y resolución de instrumentos.

| Resultado | Valor |
|---|---|
| Energía útil y servicio logrado | Pendiente |
| Entradas incluidas y posibles entradas no medidas | Pendiente |
| Almacenamiento inicial y final | Pendiente |
| Incertidumbre / dispersión entre repeticiones | Pendiente |
| ¿Apoya, refuta o deja indeterminada la hipótesis? | Pendiente |
| Decisión: continuar / modificar / abandonar | Pendiente |
| Cambio concreto para siguiente ensayo | Pendiente |

## Fallos y mantenimiento

| Fecha | Síntoma | Condición antes de fallar | Energía/servicio perdido | Causa confirmada o hipótesis | Acción | Repuesto y USD | Horas propias | Resultado |
|---|---|---|---|---|---|---:|---|
| Pendiente | — | — | — | — | — | — | — | — |

Mantener separada causa confirmada de sospecha. Un reinicio por baja tensión no confirma batería defectuosa: puede ser cable, arranque, conexión o configuración.

## Gastos y decisiones de compra

| Fecha | Elemento/cantidad | Estimado o pagado | Moneda | Precio | Impuesto/envío | Vida/garantía documentada | Trabajo propio | Motivo |
|---|---|---|---|---:|---|---|---|---|
| Pendiente | — | — | — | — | — | — | — | — |

Registrar también consumibles regalados y su costo de reposición. No convertir monedas sin fecha y tasa identificadas.

## Resultados ya existentes en este paquete

**estimación**, ejecución Python 3.12.14: 11 casos horarios sintéticos, ver [resultados.md](modelo/salida/resultados.md), [resultados.json](modelo/salida/resultados.json) y [series_horarias.json](modelo/salida/series_horarias.json). El usuario aportó características del sitio, pero no medidas instrumentales. No se ha construido ni probado físicamente ningún prototipo.

Primeras decisiones documentadas: priorizar diagnóstico hidráulico; mantener solar como alternativa; no comprar equipos de potencia con los valores supuestos; registrar demanda y recurso antes de ajustar el modelo.
