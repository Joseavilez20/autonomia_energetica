# 07 — Bitácora de Laboratorio, Plantillas de Medición y Árbol de Decisiones

> **Instrucciones de uso:** Copia estas tablas para cada corrida experimental en tu taller[cite: 1]. Ninguna modificación pasa de la Fase 2 (Prototipo) a la Fase 4 (Vivienda) sin haber completado al menos **3 corridas reproducibles** en la Plantilla A[cite: 1].

---

## 1. Plantilla A: Registro de Corrida Experimental y Balance Energético Simultáneo

* **ID de Experimento:** `EXP-____` | **Hipótesis evaluada:** `[H1: Fogón TEG / H2: Solar PVT / H3: Nevera PCM / H4: Termoacústico / Hidro]`
* **Fecha:** `AAAA-MM-DD` | **Hora Inicio ($t_0$):** `HH:MM:SS` | **Hora Fin ($t_f$):** `HH:MM:SS` | **Duración ($\Delta t$):** `____ horas`
* **Estado Inicial Almacenamiento ($SOC_0$):** Voltaje en reposo $V_0 = \text{\_\_\_\_ V}$ | Lectura Contador Entrada $E_{\text{bat},0} = \text{\_\_\_\_ Wh}$[cite: 1]

| Minuto / Hora | Recurso Entrada Medido ($I_{\text{sol}}$ en $\text{W/m}^2$, $T_{\text{caliente}}$ en $^\circ\text{C}$, o $Q$ en $\text{L/s}$ y $P$ en $\text{PSI}$) | Temp. Lado Frío / Celda ($T_{\text{fría}}$, $^\circ\text{C}$) | Voltaje Bajo Carga ($V_L$, en $\text{V}$) | Corriente en Carga ($I_L$, en $\text{A}$) | Potencia Eléctrica Bruta ($P_{\text{bruta}} = V_L \cdot I_L$, en $\text{W}$) | Consumo Auxiliares ($P_{\text{aux}}$, en $\text{W}$) | Potencia Neta Útil ($P_{\text{neta}} = P_{\text{bruta}} - P_{\text{aux}}$, en $\text{W}$) | Energía Acumulada Integrador ($E_{\text{acum}}$, en $\text{Wh}$) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $t = 0\text{ min}$ | | | | | | | | $0.0\text{ Wh}$ |
| $t = 15\text{ min}$ | | | | | | | | |
| $t = 30\text{ min}$ | | | | | | | | |
| $t = 45\text{ min}$ | | | | | | | | |
| $t = 60\text{ min}$ | | | | | | | | |
| $t = 90\text{ min}$ | | | | | | | | |
| $t = 120\text{ min}$ | | | | | | | | |
| **PROMEDIO / TOTAL** | **Entrada Media: ____ W** | **$T_{\text{máx}}$: ____ °C** | **$V_{\text{med}}$: ____ V** | **$I_{\text{med}}$: ____ A** | **$P_{\text{bruta med}}$: ____ W** | **$P_{\text{aux med}}$: ____ W** | **$P_{\text{neta med}}$: ____ W** | **Energía Total Neta: ____ Wh** |

* **Verificación de Cierre de Balance ($\Delta SOC$):** Voltaje final en reposo (tras $1\text{ h}$) $V_f = \text{\_\_\_\_ V}$ | Diferencia neta en batería $\Delta E_{\text{bat}} = \text{\_\_\_\_ Wh}$[cite: 1].
* **Eficiencia Global Real Medida ($\eta_{\text{real}}$):**
  $$\eta_{\text{real}} (\%) = \left( \frac{\text{Energía Eléctrica Neta Total (Wh)} + \text{Energía Térmica Útil en Agua (Wh)}}{\text{Energía del Recurso de Entrada Integrada (Wh)}} \right) \times 100 = \text{\_\_\_\_\_\_ } \%$$

---

## 2. Plantilla B: Registro de Fallos, Diagnóstico de Raíz y Lecciones Aprendidas (FMEA de Taller)

| Fecha | Subsistema / Prototipo | Modo de Fallo Observado (Qué se rompió o cayó en rendimiento) | Causa Física Raíz Identificada (Medida, no supuesta) | Acción Correctiva en Diseño o Materiales | Costo del Error (USD) | ¿Se Resolvió en Prueba Posterior? (Sí/No) |
| :---: | :--- | :--- | :--- | :--- | :---: | :---: |
| *Ej. 1* | *Bloque TEG Fogón* | *Potencia cayó de $18\text{ W}$ a $4\text{ W}$ al minuto 40.* | *Tornillos M6 de acero condujeron calor al bloque frío y perdieron tensión al dilatarse.* | *Aislar tornillos con bujes de fibra de vidrio y añadir arandelas elásticas Belleville.* | *\$0* | *Pendiente* |
| | | | | | | |
| | | | | | | |

---

## 3. Plantilla C: Matriz de Decisión por Fase (Continuar / Modificar / Abandonar)

Al cumplir el tiempo o costo máximo asignado a cada prototipo (definido en `05_hipotesis_y_experimentos.md`), aplica esta regla de decisión sin apego emocional[cite: 1]:

1. **DECISIÓN: ESCALAR A LA SIGUIENTE FASE (Semáforo Verde)**
   * El prototipo entrega $\ge 80\%$ de la potencia predicha en el cálculo físico.
   * No requiere intervención manual constante durante la prueba de 2 a 24 horas.
   * El costo por vatio continuo o por $\text{Wh/día}$ proyectado es inferior o competitivo frente a ampliar paneles y baterías comerciales.
2. **DECISIÓN: ITERAR / MODIFICAR EN TALLER (Semáforo Amarillo — Máximo 2 iteraciones)**
   * El mecanismo físico funciona claramente (hay gradiente, resonancia o par mecánico), pero una pérdida parásita identificada (fuga hidráulica, resistencia de contacto, desadaptación de impedancia eléctrica) se lleva más del $40\%$ de la potencia.
3. **DECISIÓN: ABANDONAR O DEJAR SOLO COMO DEMOSTRADOR EDUCATIVO (Semáforo Rojo)**
   * Tras 2 iteraciones de corrección, la potencia neta descontando auxiliares ($P_{\text{neta}} = P_{\text{bruta}} - P_{\text{aux}}$) es marginal ($<5\text{ W}$ para uso de casa) o la fatiga de materiales destruye el prototipo en menos de $50\text{ horas}$ de operación[cite: 1].