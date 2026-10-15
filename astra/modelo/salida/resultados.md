# Resultados calculados — modelo 0.1.0

Estimaciones con series sinteticas; no son mediciones ni una garantia de autonomia anual.

| Caso | Generacion DC kWh | Demanda AC kWh | AC no atendida kWh | Energia atendida % | Horas con deficit | Inicio / fin bateria util kWh |
|---|---:|---:|---:|---:|---:|---:|
| hibrido_conservador | 73.10 | 79.20 | 19.23 | 75.72 | 377 | 0.00 / 0.00 |
| hibrido_central | 178.25 | 79.20 | 0.00 | 100.00 | 0 | 3.20 / 3.20 |
| hibrido_favorable | 318.42 | 79.20 | 0.00 | 100.00 | 0 | 3.20 / 3.20 |
| hibrido_central_adverso | 161.94 | 79.20 | 4.16 | 94.74 | 43 | 3.20 / 3.20 |
| hibrido_adverso_bateria_degradada | 161.94 | 79.20 | 4.67 | 94.10 | 50 | 2.56 / 2.56 |
| hibrido_adverso_bateria_8kwh | 161.94 | 79.20 | 1.46 | 98.16 | 14 | 6.40 / 6.40 |
| solar_0.8kwp_central | 76.54 | 79.20 | 14.74 | 81.39 | 212 | 0.17 / 0.00 |
| solar_0.8kwp_conservador | 44.85 | 79.20 | 40.85 | 48.42 | 544 | 0.00 / 0.00 |
| solar_2kwp_central | 191.36 | 79.20 | 0.00 | 100.00 | 0 | 2.47 / 2.47 |
| solar_2kwp_conservador | 112.12 | 79.20 | 0.00 | 100.00 | 0 | 2.44 / 2.42 |
| hidro_central_sola | 101.71 | 79.20 | 0.00 | 100.00 | 0 | 3.04 / 3.04 |

El porcentaje es cobertura de ENERGIA; no disponibilidad temporal. Se contabiliza la diferencia de almacenamiento.

Ver entradas.json, resultados.json y series_horarias.json para entradas, perdidas, vertimiento y limites.
