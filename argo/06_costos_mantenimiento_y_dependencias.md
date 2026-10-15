```markdown
# 06 — Presupuesto por Fases, Costo Nivelado (LCOE), Mantenimiento y Soberanía Técnica

## 1. Análisis Económico en Horizonte de 15 Años (Vivienda Completa + Finca Base)

Evaluamos los costos reales en **Dólares Estadounidenses (USD, octubre de 2026)** durante un horizonte explícito de **15 años ($5,475\text{ días}$)** para el sistema híbrido recomendado (**Escenario Central: $1.2\text{ kWp}$ Solar PVT + Cogeneración Fogón Leña + Ariete Hidráulico + Nevera Eutéctica + $5.12\text{ kWh }\text{LiFePO}_4$**), separando el desembolso en efectivo del valor de tu trabajo en taller[cite: 1]:

### 1.1 Desglose de Inversión Inicial (CAPEX), Operación (OPEX) y Reposiciones

| Subsistema | CAPEX en Efectivo (Materiales y Equipos, USD) | Horas de Taller Propias Estimadas | Valor Imputado Trabajo Propio (Ref. $10/h, separado) | Reposiciones en 15 Años (Año y Costo USD) | Mantenimiento Anual (OPEX en Efectivo, USD/año) |
| :--- | :---: | :---: | :---: | :--- | :---: |
| **Instrumentación y Laboratorio (Fases 1-2)** | $145 | $20\text{ h}$ | $200 | Puntas de prueba y baterías de medidores ($15 en año 7) | $5 / año |
| **Captación Solar PVT ($3\times 450\text{ Wp}$) + Reflectores y Serpentín** | $340 | $35\text{ h}$ | $350 | Renovación de lámina Mylar reflectiva y pasta térmica ($60 en año 8) | $8 / año (agua destilada/limpieza y pintura estructura) |
| **Cogeneración en Estufa Rocket (16x TEG + Termosifón + Tanque 150L)** | $260 | $40\text{ h}$ | $400 | Reemplazo preventivo de 4 módulos TEG y sellos ($55 en año 6 y año 12) | $10 / año (deshollinado y ánodo de magnesio en tanque) |
| **Bombeo por Ariete Hidráulico + Modificación Nevera Eutéctica** | $115 | $18\text{ h}$ | $180 | Empaques de caucho de válvula de ímpetu y termostato ($20 total en 15 años) | $4 / año |
| **Banco Almacenamiento ($16\times$ Celdas $\text{LiFePO}_4$ $100\text{Ah}$ + JK-BMS)** | $680 | $12\text{ h}$ | $120 | Reemplazo de placa BMS por reserva ($65 en año 9; celdas duran los 15 años al $80\%$) | $0 / año (verificación semestral de torque en bornes) |
| **Electrónica de Potencia (MPPT $40\text{A}$ + Inversor Toroidal $3\text{kW}$ + Protecciones DC/AC)** | $540 | $15\text{ h}$ | $150 | Reparación de etapa MOSFET/Capacitores del inversor en año 9 ($90 en componentes) | $10 / año (limpieza de polvo en disipadores y pasta térmica) |
| **OPCIONAL FINCA: Picohidráulica Pelton/Lavadora ($250\text{ W}$) + $100\text{m}$ Polietileno** | $420 | $45\text{ h}$ | $450 | Cambio de rodamientos SKF 2RS cada $2.5\text{ años}$ ($6 \times $12 = $72) | $15 / año (grasa sintética y mallas desarenador) |
| **TOTAL SISTEMA VIVIENDA (Sin Hidro)** | **$2,080 USD** | **$140\text{ h}$** | *$1,400 USD* | **$305 USD (en 15 años)** | **$37 USD / año ($555 en 15 años)** |
| **TOTAL SISTEMA FINCA COMPLETA (Con Hidro)** | **$2,500 USD** | **$185\text{ h}$** | *$1,850 USD* | **$377 USD (en 15 años)** | **$52 USD / año ($780 en 15 años)** |

### 1.2 Cálculo del Costo Nivelado de la Energía Útil (LCOE)
Durante los 15 años, el sistema de vivienda entrega de forma efectiva:
* **Energía eléctrica útil consumida:** $2.65\text{ kWh/día} \times 365\text{ días} \times 15\text{ años} = \mathbf{14,508\text{ kWh}_{\text{eléctricos}}}$.
* **Energía térmica y mecánica directa desplazada (agua caliente solar/fogón + bombeo por ariete):** Equivalente a $3.2\text{ kWh/día} \times 365 \times 15 = \mathbf{17,520\text{ kWh}_{\text{térmicos/mecánicos}}}$.
* **Energía total útil entregada por tu sistema:** **$32,028\text{ kWh}$**.
* **Costo total del ciclo de vida en efectivo (CAPEX + Reposiciones + OPEX 15 años):** $\$2,080 + \$305 + \$555 = \mathbf{\$2,940\text{ USD}}$.

$$\text{LCOE}_{\text{eléctrico puro}} = \frac{\$2,940\text{ USD}}{14,508\text{ kWh}} = \mathbf{\$0.202\text{ USD/kWh}} \quad (\text{vs. } \$0.85\text{ USD/kWh con generador de gasolina})$$

$$\text{LCOE}_{\text{integral (Eléctrico + Térmico + Bombeo)}} = \frac{\$2,940\text{ USD}}{32,028\text{ kWh}} = \mathbf{\$0.091\text{ USD/kWh}}$$

> **Conclusión financiera contundente:** A partir del **año 3.5** (comparado contra usar una planta eléctrica de gasolina/diésel en una zona sin red, que gasta $\sim \$850\text{ USD/año}$ en combustible y aceite), toda la energía de tu vivienda y finca tiene un costo marginal cercano a cero ($\sim \$3\text{ a }\$4\text{ USD/mes}$ para mantenimiento preventivo)[cite: 1].

---

## 2. La Paradoja del Último 5% de Autonomía (Curva Costo vs. Gestión de Cargas)

En sistemas 100% desconectados (*Off-Grid*), el costo no crece de forma lineal al acercarse al $100.0\%$ de disponibilidad rígida[cite: 1]:

| Nivel de Autonomía Rígida (Sin Gestión Humana) | Qué implica técnicamente | Inversión Requerida (Índice Base = 100%) | Estrategia Inteligente para Lograr el 100% de Continuidad al Costo del 95% |
| :---: | :--- | :---: | :--- |
| **90% del tiempo ($328\text{ días/año}$)** | Cubre todos los días soleados y nublados normales. | **$75\%$ ($1,560 USD)** | Insuficiente si trabajas con internet y refrigeración continua. |
| **97% del tiempo ($354\text{ días/año}$)** | Soporta 3 días seguidos de tormenta tropical severa. | **$100\%$ ($2,080 USD)** | **Punto Óptimo de Diseño:** El $3\%$ restante ($11\text{ días}$ extremos al año) se cubre **gestionando cargas** (no usar lavadora ni taller pesado en temporal) y **encendiendo 2 horas extra el fogón de leña cogenerador**[cite: 1]. |
| **100% Rígido "Ciego" ($365\text{ días/año}$ sin mirar el clima ni usar leña)** | Exige diseñar paneles y baterías para la peor semana de lluvia del siglo (ej. 8 días sin sol) manteniendo el mismo consumo. | **$240\%$ ($4,990 USD)** | **Ineficiente:** Compras $\$2,900\text{ USD}$ adicionales en paneles y baterías que permanecen ociosos $354\text{ días}$ al año[cite: 1]. |

---

## 3. Estrategia de "Cero Dependencia" y Stock de Repuestos en Taller (Fase 7)

Para no depender de garantías lentas ni de proveedores comerciales cuando vivas en el campo[cite: 1], tu taller debe almacenar en una caja hermética con gel de sílice este **Kit de Supervivencia Electrónica y Mecánica ($95 USD total)**:

1. **Para reparar el Inversor y Controladores en tu propio banco:**
   * 8 Transistores **MOSFET de potencia canal N** del mismo código que use tu inversor/controlador (ej. HY4008 / IRFB4110 de $80\text{--}100\text{ V}, 180\text{ A}$) y 4 **IGBT** de puente H ($600\text{ V}, 40\text{ A}$). El $85\%$ de las fallas de inversores por rayos o sobrecargas son simplemente 2 o 4 MOSFETs en cortocircuito que cambias con tu cautín en $30\text{ minutos}$.
   * 4 Optoacopladores **TLP250 / PC817** (drivers de compuerta de los MOSFETs, siempre se queman junto con el MOSFET).
   * 4 Capacitores electrolíticos de bajo ESR ($100\text{ V}, 2200\text{ }\mu\text{F}$) y 2 varistores de óxido metálico (**MOV 14D471K**) para absorber picos de tormentas eléctricas.
2. **Para la Turbina Hidráulica y el Ariete:**
   * 2 Pares de **rodamientos sellados en caucho (sufijo 2RS)** del código exacto del eje de tu generador, guardados en su empaque engrasado.
   * 1 Metro cuadrado de **caucho de neumático de camión con lona textil interna** ($4\text{--}6\text{ mm}$ de espesor) y sacabocados para cortar sellos nuevos de la válvula de ímpetu del ariete cada 2 años.
3. **Para el Sistema de Refrigeración y Fogón:**
   * 2 Termostatos digitales de repuesto (**W1209 / STC-1000**, cuestan $3 USD c/u).
   * 1 Relé amperimétrico de arranque PTC o kit de arranque de estado sólido universal para el compresor de la nevera.
   * 4 Módulos **TEG** de repuesto y un bote de óxido de zinc en polvo.

---

## 4. Cronograma de Mantenimiento Preventivo

| Frecuencia | Tarea Específica | Tiempo | Herramienta / Verificación |
| :--- | :--- | :---: | :--- |
| **Semanal** | Limpieza de rejilla toma-agua (hidro/ariete) y purga de aire o adición de aire en cámara del ariete. | $15\text{ min}$ | Inspección visual de manómetro (la presión estática debe ser idéntica). |
| **Mensual** | Limpieza con agua (en la mañana, con el vidrio frío) de paneles PVT y espejos reflectores; deshollinado de la cara caliente del bloque TEG en la estufa Rocket. | $40\text{ min}$ | Comparar corriente de cortocircuito o potencia a mediodía contra línea base de bitácora. |
| **Semestral** | Reapriete de todos los terminales de potencia DC (baterías, MPPT, inversor) y verificación de tensión individual de las 16 celdas $\text{LiFePO}_4$ ($\Delta V_{\text{celdas}} < 0.015\text{ V}$). | $45\text{ min}$ | Llave dinamométrica ($5\text{--}8\text{ N}\cdot\text{m}$) y cámara termográfica o dorso de la mano buscando bornes tibios. |
| **Cada 2 Años** | Purga de lodos en el fondo del tanque termosifón, revisión del ánodo de sacrificio de magnesio y reemplazo preventivo de rodamientos de la turbina hidráulica. | $3\text{ h}$ | Extractor de poleas de 3 garras y multímetro. |