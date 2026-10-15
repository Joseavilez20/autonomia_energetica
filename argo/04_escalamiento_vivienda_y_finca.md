# 04 — Arquitectura de Escalamiento Completo: Vivienda a Finca Productiva (Fases 4 a 7)

## 1. Mapa Completo de la Ruta por Fases (De Cero a Autonomía Productiva)

Esta tabla consolida la evolución completa desde el diagnóstico hasta la operación de la finca con criterios cuantitativos de aprobación ("Gatekeeper") para avanzar sin arriesgar capital:

| Fase | Objetivo Operativo | Entregable Físico en Taller / Campo | Costo Incremental (USD, 2026) | Criterio Medible para Avanzar a la Siguiente Fase |
| :--- | :--- | :--- | :---: | :--- |
| **Fase 0** | Diagnóstico de demanda y aforo de recursos en terreno | Matriz horaria de cargas + Registro de caudal de estiaje ($Q$) y desnivel ($H$) con manguera nivel + Horizonte solar | **\$0 - \$30** | Demanda esencial depurada a $<2.5\text{ kWh/día}$ y recursos físicos medidos sin depender solo de promedios anuales. |
| **Fase 1** | Pruebas básicas de principio físico | Calorímetro solar cero-desembolso + Celda Peltier/TEG en termosifón básico + Prueba hidrostática con manómetro | **\$25 - \$60** | Verificación experimental de $\ge 450\text{ W/m}^2$ térmicos al sol y generación eléctrica estable bajo carga resistiva conocida. |
| **Fase 2** | Prototipo instrumentado en banco | Módulo PVT de $50\text{--}100\text{ Wp}$ con espejo lateral + Bloque de 4 celdas TEG en fogón + Rodete Pelton/lavadora en banco cerrado[cite: 1] | **\$150 - \$320** | Integración de potencia ($\text{Wh}$) durante $\ge 4\text{ horas}$ continuas con registro de pérdidas térmicas y eficiencia global $\eta$ medida[cite: 1]. |
| **Fase 3** | Piloto para una carga real continua[cite: 1] | Alimentación 24/7 del Router Wi-Fi ($15\text{ W}$) e iluminación LED ($30\text{ W}$) con batería pequeña ($600\text{ Wh}$) y cogeneración en leña[cite: 1] | **\$280 - \$450** | **15 días continuos** sin caída de tensión en el router ($0\text{ horas}$ de apagón), incluyendo al menos 2 días nublados suplidos con fogón[cite: 1]. |
| **Fase 4** | Cargas esenciales de la vivienda[cite: 1] | Bus DC de $24\text{ V}$ o $48\text{ V}$ + Nevera modificada con PCM eutéctico ($0\text{ Wh}$ nocturnos) + Bombeo por ariete o solar directo a tanque alto[cite: 1] | **\$950 - \$1,600** | Superar una secuencia adversa de **4 días lluviosos** manteniendo la nevera entre $2^\circ\text{C}$ y $5^\circ\text{C}$ y el SOC de batería $>20\%$[cite: 1]. |
| **Fase 5** | Vivienda completa autónoma[cite: 1] | Arreglo PVT de $1.2\text{ a }1.8\text{ kWp}$ + Cogeneración en estufa Rocket ($80\text{--}120\text{ W}$) o Picohidráulica ($150\text{ W}$) + Banco $\text{LiFePO}_4$ ($5.12\text{ kWh}$)[cite: 1] | **\$1,200 - \$2,100** | Operación durante **3 meses continuos** cubriendo nevera, luces, router, bombeo, lavadora en frío y herramientas portátiles con $\text{LOLP} = 0\%$[cite: 1]. |
| **Fase 6** | Escalamiento a Finca Productiva[cite: 1] | Turbina hidráulica ($300\text{--}800\text{ W}$) + Ampliación solar a $3.0\text{ kWp}$ + Arrancadores suaves para motores agrícolas + Biodigestor tubular[cite: 1] | **\$1,800 - \$3,400** | Operación simultánea de vivienda + congelador agrícola + taller metalmecánico + riego sin caída de tensión $>3\%$ en líneas largas[cite: 1]. |
| **Fase 7** | Operación, mantenimiento y mejora continua[cite: 1] | Stock de repuestos críticos en taller (MOSFETs, rodamientos, BMS, sellos) + Bitácora anual de degradación de celdas y turbinas[cite: 1] | **\$80 - \$150 / año** | Costo recurrente anual $<2\%$ del valor del sistema y capacidad de reparar cualquier fallo en $<6\text{ horas}$ sin técnicos externos[cite: 1]. |

---

## 2. Arquitectura Eléctrica y Térmica Integrada (Vivienda + Finca)

### 2.1 Elección de Tensión del Bus Principal DC: ¿Por qué migrar de $12\text{ V}$ a $48\text{ V}$ nominales ($51.2\text{ V }\text{LiFePO}_4$)?
En los experimentos de las Fases 1 a 3 trabajamos en $12\text{ V DC}$, pero al escalar a la vivienda completa (Fase 4/5) y a la finca (Fase 6), la Ley de Joule ($P_{\text{pérdida}} = I^2 \cdot R$) hace inviable mantener $12\text{ V}$:
* Para entregar $2,400\text{ W}$ a un motor o soldador en $12\text{ V}$, circulan **$200\text{ Amperios}$** (exigiendo cables gruesos y costosos de calibre AWG 2/0).
* En un bus de **$48\text{ V}$ ($16$ celdas $\text{LiFePO}_4$ en serie = $51.2\text{ V}$)**, los mismos $2,400\text{ W}$ requieren apenas **$47\text{ Amperios}$**, reduciendo las pérdidas por calentamiento en los cables en **16 veces** ($4^2 = 16$) y permitiendo usar cable estándar AWG 6 o AWG 8.

### 2.2 Diagrama Unifilar de Bloques para la Finca (Fase 5 y 6)

```text
[GENERACIÓN MULTIFUENTE]                              [ALMACENAMIENTO HÍBRIDO]                 [CARGAS JERARQUIZADAS]
                                                                                              
1. Arreglo Solar PVT + Espejos ──► [MPPT Solar] ──┐   ┌──► [Banco LiFePO4 51.2V]               ┌──► Bus DC Directo (48V->12V/24V):
   (1.8 a 3.0 kWp)                                │   │    (100Ah = 5.12 kWh a 10.24 kWh)      │    - Router Wi-Fi / Cámaras (24/7)
                                                  ▼   ▼    + BMS Activo JK 2A                  │    - Iluminación LED Casa y Galpón
2. Turbina Pelton / Vórtice ─────► [Rectificador]─┼───┼──► [BARRAJE COLECTOR DC 48V] ──────────┤    - Cerca Eléctrica Rural
   (150W a 600W continuos 24/7)    + [Controlador │   │    (Fusibles Clase T + Seccionador)    │
                                     Dump Load] ──┘   │                                        ├──► Inversor Onda Pura Baja Frecuencia:
                                         │            ├──► [Batería Térmica Fría (PCM)]        │    - Salida 1 (Crítica): Nevera / Congelador
3. Fogón Leña Rocket + TEG/TA ───► [Boost MPPT] ──────┘    (Placas Eutécticas -6°C y -11°C)    │    - Salida 2 (Relé Voltaje Alto >53.6V):
   (60W a 120W en lluvia)                │                                                     │      Bomba agua, Taller, Lavadora, Picapasto
                                         ▼                                                     │
                               [Resistencia Derivación] ──► [Tanque Agua Caliente 150L] ───────┴──► Agua Caliente Sanitaria + Biodigestor
```

---

## 3. Dimensionamiento Matemático Riguroso en 3 Escenarios Climáticos

Siguiendo la regla de dimensionar sobre energía útil entregada a las cargas sin contar dos veces las pérdidas[cite: 1], definimos la cadena de eficiencias verificables:

- $\eta_{\text{MPPT/Control}} = 0.96$ ($4\%$ de pérdida electrónica).
- $\eta_{\text{cableado DC/AC}} = 0.98$ ($2\%$ de pérdida óhmica).
- $\eta_{\text{inversor}} = 0.91$ ($9\%$ de pérdida en transformación DC $\rightarrow$ AC para cargas en alterna).
- $\eta_{\text{batería LiFePO4}} = 0.94$ ($6\%$ de pérdida en ciclo carga/descarga, aplicable solo a la fracción nocturna $f_{\text{noct}}$ que pasa por la batería).

La energía bruta diaria ($E_{\text{bruta gen}}$) que deben producir los generadores en bornes antes de los controladores para satisfacer una demanda útil $E_{\text{útil}}$ (donde una fracción $f_{\text{diurna}}$ se consume directamente de día y $f_{\text{noct}} = 1 - f_{\text{diurna}}$ pasa por la batería) es:

$$
E_{\text{bruta gen}} = \frac{E_{\text{útil}}}{\eta_{\text{MPPT}} \cdot \eta_{\text{cable}} \cdot \eta_{\text{inversor}}} \times \left( f_{\text{diurna}} + \frac{f_{\text{noct}}}{\eta_{\text{batería}}} \right)
$$

Gracias a nuestra Hipótesis 3 (Nevera con PCM eutéctico y bombeo diurno a tanque alto), logramos desplazar el consumo para que $f_{\text{diurna}} = 0.70$ ($70\%$ de día) y solo $f_{\text{noct}} = 0.30$ ($30\%$ de noche). Sustituyendo los valores:

$$
E_{\text{bruta gen}} = \frac{E_{\text{útil}}}{0.96 \times 0.98 \times 0.91} \times \left( 0.70 + \frac{0.30}{0.94} \right) = \frac{E_{\text{útil}}}{0.856} \times 1.019 = 1.190 \times E_{\text{útil}}
$$

Es decir, necesitamos generar un **$19.0\%$ adicional** sobre la energía útil consumida por los equipos para cubrir todas las pérdidas físicas del sistema.

### 3.1 Tabla de Dimensionamiento en 3 Escenarios

**Vivienda:** $E_{\text{útil}} = 2,550\text{ Wh/día} \rightarrow E_{\text{bruta gen}} = 3,035\text{ Wh/día}$.

| Parámetro / Componente | Escenario Conservador (Mes Crítico de Tormentas: 2.5 HSP, sin río) | Escenario Central (Mes Lluvioso Estándar: 3.6 HSP + Fogón Leña) | Escenario Favorable (Terreno con Quebrada + Sol Medio: 4.5 HSP) |
| :--- | :--- | :--- | :--- |
| **Aporte Térmico/Cogeneración (Fogón Leña TEG/TA)** | $360\text{ Wh/día}$ ($90\text{ W} \times 4\text{ h}$) | $300\text{ Wh/día}$ ($100\text{ W} \times 3\text{ h}$) | $150\text{ Wh/día}$ (uso ligero) |
| **Aporte Picohidráulica (24/7)** | $0\text{ Wh/día}$ (terreno seco) | $0\text{ Wh/día}$ (solo ariete mecánico) | $2,400\text{ Wh/día}$ ($100\text{ W}$ continuos) |
| **Déficit a cubrir con Solar FV ($E_{\text{solar req}}$)** | $2,675\text{ Wh/día}$ | $2,735\text{ Wh/día}$ | $485\text{ Wh/día}$ |
| **Potencia Solar Nominal sin PVT** ($P_{\text{FV}} = \frac{E_{\text{solar}}}{HSP \cdot 0.85}$) | $1,260\text{ Wp}$ (3 paneles de $450\text{ Wp}$) | $895\text{ Wp}$ (2 paneles de $450\text{ Wp}$) | $130\text{ Wp}$ (1 panel de $200\text{ Wp}$) |
| **Potencia Solar con Innovación PVT + Reflectores ($+25\%$)** | $1,010\text{ Wp}$ (2 paneles de $500\text{ Wp}$) | $715\text{ Wp}$ (2 paneles de $400\text{ Wp}$) | $100\text{ Wp}$ (1 panel de $100\text{ Wp}$) |
| **Días de Autonomía en Batería Quím. + Térmica** | $3.0\text{ días}$ (sin bajar del $15\%$ SOC) | $2.5\text{ días}$ | $1.5\text{ días}$ (la turbina carga de noche) |
| **Capacidad Banco $\text{LiFePO}_4$ Requerida** | $6.14\text{ kWh}$ ($48\text{ V}\ 120\text{ Ah}$) | $5.12\text{ kWh}$ ($48\text{ V}\ 100\text{ Ah}$) | $2.56\text{ kWh}$ ($24\text{ V}\ 100\text{ Ah}$) |

## 4. Ingeniería para la Finca (Fase 6): Distancias, Motores y Arranques Pesados

Cuando pases de la vivienda a las cargas productivas de la finca (bombas alejadas, picapasto, compresor, taller)[cite: 1], se presentan tres desafíos físicos que destruyen los sistemas mal diseñados:

### 4.1 Cálculo de Caída de Tensión por Distancia (Del Río o Galpón a la Casa)

Si la quebrada donde instalas la turbina picohidráulica está a una distancia $L$ (en metros, un solo sentido; el recorrido total del electrón es $2L$) de la casa, la resistencia del cable de cobre ($\rho_{\text{Cu}} = 0.0175\ \Omega\cdot\text{mm}^2/\text{m}$) provocará una caída de voltaje $\Delta V$:

$$
S_{\text{sección mínima}}\ \text{(mm}^2\text{)} = \frac{2 \times 0.0175 \times L\ \text{(m)} \times I\ \text{(A)}}{\Delta V_{\text{máx permitido}}\ \text{(V)}}
$$

**Ejemplo práctico de finca:** Si tu turbina entrega $300\text{ W}$ y está a $150\text{ metros}$ de la casa:

1. **Error mortal (transmitir en $12\text{ V DC}$):** $I = 300 / 12 = 25\text{ A}$. Para no perder más del $5\%$ ($0.6\text{ V}$), necesitarías un cable monstruoso de $S = \frac{2 \times 0.0175 \times 150 \times 25}{0.6} = 218\text{ mm}^2$ (más caro que toda la finca).
2. **Solución de ingeniería (transmitir en alta tensión $120\text{--}220\text{ V AC/DC}$ y bajar a $48\text{ V}$ en la casa):** Si bobinas o conectas el generador en estrella para que entregue $150\text{ V DC}$ en la quebrada, la corriente baja a apenas $I = 300 / 150 = 2.0\text{ A}$. Permitiendo un $5\%$ de caída ($7.5\text{ V}$), la sección necesaria es:

   $$
   S = \frac{2 \times 0.0175 \times 150 \times 2.0}{7.5} = 1.4\text{ mm}^2 \quad (\text{Basta un cable económico AWG 14 o AWG 12})
   $$

Al llegar a la casa, entras con esos $142\text{ V DC}$ directamente a la entrada de un controlador solar MPPT de $150\text{ V}$ o $250\text{ V}$ (ajustado con carga de desvío), el cual lo convierte limpiamente a $48\text{ V}$ para las baterías.

### 4.2 Arranque de Motores Agrícolas y Herramientas (Picos Inductivos)

Un motor de inducción monofásico de $1.5\text{ HP}$ ($1,100\text{ W}$) con capacitor de arranque exige durante los primeros $200\text{ milisegundos}$ entre 5 y 7 veces su corriente nominal ($5,500\text{ a }7,700\text{ VA}$) para vencer la inercia del rotor[cite: 1].

**Tres soluciones técnicas obligatorias en finca:**

1. **Inversor de Baja Frecuencia con Transformador Toroidal de Cobre Pesado (*Low-Frequency Inverter*):** A diferencia de los inversores baratos de alta frecuencia (que pesan $3\text{ kg}$ y se queman al primer chispazo de un motor), un inversor de baja frecuencia de $3,000\text{ W}$ tiene un núcleo toroidal de hierro-silicio de $18\text{ kg}$ que almacena energía magnética y soporta picos del $300\%$ ($9,000\text{ W}$) durante $5\text{ a }10\text{ segundos}$ sin apagar el sistema.
2. **Variador de Frecuencia (VFD — *Variable Frequency Drive*) o Arrancador Suave (*Soft-Starter*):** Para bombas grandes, picapasto o torno mecánico, usa motores trifásicos de $220\text{ V}$ alimentados desde tu línea monofásica de $220\text{ V}$ mediante un VFD económico ($65\text{ USD}$). Configura una rampa de aceleración de $4\text{ segundos}$ (de $0\text{ Hz}$ a $60\text{ Hz}$): el pico de arranque desaparece por completo ($I_{\text{arranque}} \le 1.1 \times I_{\text{nominal}}$).
3. **Acoplamiento Mecánico Directo cuando sea posible:** Si tienes caída de agua o un eje mecánico, puedes acoplar una despulpadora de café, un molino de granos o un compresor de aire de pistón directamente con polea al rodete Pelton, ahorrando el $30\%$ de pérdidas de convertir agua en electricidad y electricidad de nuevo en giro mecánico[cite: 1].

## 5. Requisitos Profesionales y Límites de Seguridad Normativa

En cumplimiento estricto de la seguridad de ingeniería para instalaciones de potencia[cite: 1]:

- **Prohibición de retroalimentación improvisada:** Jamás conectes la salida de un inversor a un tomacorriente doméstico mediante un cable con dos enchufes macho ("cable suicida").
- **Distribución AC y protecciones:** Toda distribución AC de la vivienda debe partir de un tablero dedicado con disyuntor termomagnético general, interruptor diferencial (RCD/GFCI de $30\text{ mA}$) y barra de puesta a tierra conectada a jabalina de cobre[cite: 1].
- **Recipientes a presión y gas:** El biodigestor tubular de polietileno debe operar siempre a baja presión hidrostática ($<15\text{ cm}$ de columna de agua $\approx 0.015\text{ bar}$) regulada mediante una válvula de seguridad física consistente en una "T" sumergida en una botella con agua al exterior (si la presión sube, el gas burbujea al aire libre sin riesgo de explosión)[cite: 1]. Si construyes el motor termoacústico presurizado a $4\text{ bar}$, el tubo debe ser de acero inoxidable *Schedule 40* sin costura probado previamente de forma hidrostática (lleno al $100\%$ de agua sin aire con una bomba manual de plomería a $8\text{ bar}$) antes de usar gas comprimido[cite: 1].
