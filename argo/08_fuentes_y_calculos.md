# 08 — Memoria de Cálculo, Física Aplicada, Fuentes Verificables y Límites Termodinámicos

> **Propósito del documento:** Servir como manual de referencia física y matemática del laboratorio. Cada ecuación incluye sus unidades en el Sistema Internacional (SI), los supuestos adoptados, un ejemplo numérico paso a paso reproducible con calculadora o hoja de cálculo, y las fuentes científicas de respaldo.

---

## 1. Fundamentos de Unidades y Equivalencias Físicas

Para evitar errores de escala entre potencia instantánea y energía acumulada:

* **Potencia ($P$):** Velocidad a la que se transfiere o convierte la energía por unidad de tiempo.
  * $1\text{ W (Vatio)} = 1\text{ J/s (Joule por segundo)}$
  * $1\text{ kW} = 1,000\text{ W}$
  * $1\text{ HP (Caballo de fuerza mecánico)} = 745.7\text{ W}$
* **Energía ($E$):** Trabajo total realizado o calor transferido durante un intervalo de tiempo $\Delta t$.
  * $1\text{ Wh (Vatio-hora)} = 3,600\text{ J}$
  * $1\text{ kWh} = 1,000\text{ Wh} = 3,600,000\text{ J} = 3.6\text{ MJ}$
  * $1\text{ kcal (Kilocaloría térmica)} = 4,184\text{ J} = 1.1622\text{ Wh}$
* **Presión Hidráulica y Cabeza Hidrostática ($H$):**
  * $1\text{ m.c.a. (metro de columna de agua)} = 9,806.65\text{ Pa} \approx 9.81\text{ kPa} = 1.4223\text{ PSI} = 0.0981\text{ bar}$
  * $10\text{ metros verticales de agua} = 14.22\text{ PSI} = 0.981\text{ bar}$

---

## 2. Memoria de Cálculos Paso a Paso por Subsistema

### 2.1 Termoelectricidad en Fogón de Leña (Efecto Seebeck, Conducción de Fourier y Termosifón)

Cuando colocas un arreglo de $N$ módulos termoeléctricos entre la placa difusora caliente de tu estufa de leña ($T_H$) y el bloque enfriado por agua ($T_C$), ocurren tres fenómenos simultáneos que debes calcular:

#### A. Fuerza Electromotriz en Circuito Abierto ($V_{oc}$) y Potencia Máxima ($P_{\text{máx}}$)
Cada módulo contiene $n_p$ pares de elementos semiconductores tipo P y tipo N (por ejemplo, $127$ pares en un módulo estándar TEC1-12706, o $126$ pares en un módulo de potencia TEG1-12611). El coeficiente Seebeck efectivo de un módulo completo ($\alpha_M$, en $\text{V/K}$ o $\text{V/}^\circ\text{C}$) es aproximadamente $\alpha_M \approx 0.042\text{ a }0.052\text{ V/}^\circ\text{C}$.

$$V_{oc} = N_{\text{serie}} \cdot \alpha_M \cdot (T_H - T_C)$$

Cuando conectas una carga externa cuya resistencia eléctrica iguala a la resistencia interna total del arreglo ($R_{\text{carga}} = R_{\text{int\_total}}$), el voltaje en carga cae exactamente a la mitad ($V_{\text{carga}} = \frac{1}{2} V_{oc}$) y la potencia eléctrica entregada a la carga alcanza su máximo físico:

$$P_{\text{eléctrica máx}} = \frac{V_{oc}^2}{4 \cdot R_{\text{int\_total}}} = \frac{N_{\text{total}} \cdot \left[\alpha_M \cdot (T_H - T_C)\right]^2}{4 \cdot r_{\text{módulo}}}$$

* **Ejemplo numérico reproducible (Arreglo de $16\text{ módulos}$ en configuración $4\text{ serie} \times 4\text{ paralelo}$):**
  * Temperatura placa caliente medida con termopar: $T_H = 195^\circ\text{C}$
  * Temperatura media del agua en el bloque frío: $T_C = 45^\circ\text{C}$
  * Gradiente efectivo en caras cerámicas (descontando $10^\circ\text{C}$ de caída en interfases de pasta térmica): $\Delta T_{\text{efectivo}} = (195 - 45) - 10 = 140^\circ\text{C}$
  * Parámetros de cada módulo a $120^\circ\text{C}$ de temperatura media: $\alpha_M = 0.048\text{ V/}^\circ\text{C}$, resistencia interna por módulo $r_{\text{módulo}} = 2.4\text{ }\Omega$.
  * **Paso 1 (Voltaje por módulo en vacío):** $v_{oc} = 0.048 \times 140 = 6.72\text{ V}$.
  * **Paso 2 (Voltaje del arreglo de 4 en serie en vacío):** $V_{oc} = 4 \times 6.72\text{ V} = 26.88\text{ V}$.
  * **Paso 3 (Resistencia interna total del arreglo $4\text{S}4\text{P}$):** Como hay 4 ramas iguales de 4 módulos en serie, $R_{\text{int\_total}} = \frac{4 \times 2.4\text{ }\Omega}{4} = 2.4\text{ }\Omega$.
  * **Paso 4 (Voltaje y corriente en el punto de máxima potencia MPPT):**
    $$V_{\text{MPPT}} = \frac{26.88\text{ V}}{2} = 13.44\text{ V} \quad ; \quad I_{\text{MPPT}} = \frac{13.44\text{ V}}{2.4\text{ }\Omega} = 5.60\text{ A}$$
  * **Paso 5 (Potencia eléctrica bruta generada):**
    $$P_{\text{eléctrica máx}} = 13.44\text{ V} \times 5.60\text{ A} = \mathbf{75.26\text{ W}}$$
  * **Paso 6 (Potencia neta tras convertidor DC-DC al $93\%$ de eficiencia):** $P_{\text{neta}} = 75.26 \times 0.93 = \mathbf{70.0\text{ W continuos}}$.

#### B. Flujo Térmico que Cruza los Módulos y Caudal de Agua Requerido en el Termosifón
La conductancia térmica de cada módulo de $40 \times 40\text{ mm}$ es $K_{\text{term}} \approx 0.65\text{ W/}^\circ\text{C}$. Para 16 módulos con $\Delta T = 140^\circ\text{C}$, el calor conducido hacia el bloque de agua (sumando un $20\%$ de calor parásito del bloque) es:

$$Q_{\text{calor al agua}} = 1.20 \times N_{\text{total}} \cdot K_{\text{term}} \cdot \Delta T = 1.20 \times 16 \times 0.65 \times 140 = \mathbf{1,747\text{ W térmicos}}$$

Para que el agua que entra al bloque frío a $T_{\text{entrada}} = 25^\circ\text{C}$ salga por la tubería superior a $T_{\text{salida}} = 50^\circ\text{C}$ ($\Delta T_{\text{agua}} = 25^\circ\text{C}$) por simple flotabilidad térmica (termosifón sin bomba), el caudal másico necesario ($\dot{m}$) es:

$$\dot{m} = \frac{Q_{\text{calor al agua}}}{c_p \cdot \Delta T_{\text{agua}}} = \frac{1,747\text{ J/s}}{4,184\text{ J/(kg}\cdot^\circ\text{C)} \times 25^\circ\text{C}} = 0.0167\text{ kg/s} = \mathbf{1.00\text{ Litro/minuto}}$$

*(Un tubo de $3/4\text{''}$ con una elevación de tanque de $0.8\text{ m}$ mueve por convección natural entre $1.2$ y $1.8\text{ L/min}$ a ese gradiente, demostrando que el termosifón se sostiene sin bombas eléctricas).*

---

### 2.2 Motor Termoacústico de Onda Viajera (Dimensionamiento de Resonador y Frecuencia)

La longitud del tubo resonador ($L_{\text{tubo}}$) y la frecuencia de oscilación acústica ($f$) dependen de la velocidad del sonido ($a$) en el gas de trabajo a la temperatura media absoluta ($T_m$ en Kelvin):

$$a = \sqrt{\gamma \cdot R_{\text{esp}} \cdot T_m}$$

Donde para el **aire**: $\gamma = 1.4$ (relación de calores específicos) y $R_{\text{esp}} = 287\text{ J/(kg}\cdot\text{K)}$.
* A una temperatura media en el resonador de $T_m = 80^\circ\text{C} = 353.15\text{ K}$:
  $$a = \sqrt{1.4 \times 287 \times 353.15} = \mathbf{376.7\text{ m/s}}$$
* Para un resonador de **cuarto de longitud de onda ($\lambda / 4$)** terminado en el diafragma del alternador lineal (que actúa como impedancia acústica alta):
  $$f = \frac{a}{4 \cdot L_{\text{efectiva}}}$$
  Si construyes el tubo con $L_{\text{efectiva}} = 1.25\text{ m}$:
  $$f = \frac{376.7\text{ m/s}}{4 \times 1.25\text{ m}} = \mathbf{75.3\text{ Hz}}$$
* **Espaciado hidráulico crítico de la malla del regenerador ($r_h$ vs. $\delta_\kappa$):**
  Para que el gas intercambie calor de forma cuasi-isotérmica (ciclo Stirling real dentro de la malla de acero inoxidable), el radio hidráulico de los poros de la malla debe ser menor que la **profundidad de penetración térmica ($\delta_\kappa$)** del gas a la frecuencia $f$:
  $$\delta_\kappa = \sqrt{\frac{2 \cdot k_{\text{gas}}}{\rho_{\text{gas}} \cdot c_p \cdot (2 \pi f)}}$$
  A $4\text{ bar}$ de presión con aire a $75\text{ Hz}$, $\delta_\kappa \approx 0.14\text{ mm}$ ($140\text{ }\mu\text{m}$). Una **malla de acero inoxidable #120 a #150** tiene una abertura de poro de $0.10\text{ a }0.12\text{ mm}$, cumpliendo la condición termodinámica de Swift ($\delta_\kappa / r_h > 1$).

---

### 2.3 Panel Híbrido Fotovoltaico-Térmico (PVT) con Concentración Plana V-Trough

#### A. Ganancia Óptica Geométrica de Reflectores Planos Laterales
Con dos espejos laterales planos de ancho igual al del panel e inclinados un ángulo $\theta_{\text{espejo}} = 60^\circ$ respecto a la vertical ($120^\circ$ respecto al plano del panel), la relación de concentración geométrica efectiva ($C_{\text{opt}}$) considerando la reflectancia especular del aluminio anodizado o Mylar ($\rho_{\text{esp}} = 0.85$) y la fracción de radiación directa ($f_{\text{dir}} = 0.75$ en horas centrales) es:

$$G_{\text{efectiva}} = G_{\text{global}} \cdot \left[ 1 + f_{\text{dir}} \cdot \rho_{\text{esp}} \cdot (C_{\text{geom}} - 1) \right]$$

Para $C_{\text{geom}} = 1.50$:
$$G_{\text{efectiva}} = G_{\text{global}} \cdot \left[ 1 + 0.75 \times 0.85 \times 0.50 \right] = \mathbf{1.318 \cdot G_{\text{global}}} \quad (\text{Aumento del } 31.8\% \text{ en fotones incidentes})$$

#### B. Ganancia por Enfriamiento Hidráulico Trasero
* **Panel estándar en seco bajo $1,000\text{ W/m}^2$ y ambiente a $28^\circ\text{C}$:** Alcanza $T_{\text{celda, seco}} = 63^\circ\text{C}$. Con coeficiente térmico $\beta = -0.0039\text{ }^\circ\text{C}^{-1}$:
  $$\eta_{\text{rel, seco}} = 1 - 0.0039 \times (63 - 25) = 1 - 0.1482 = 0.8518 \quad (85.2\% \text{ de su potencia nominal})$$
* **Panel PVT enfriado con agua circulante a $24^\circ\text{C}$:** La celda se estabiliza en $T_{\text{celda, PVT}} = 33^\circ\text{C}$:
  $$\eta_{\text{rel, PVT}} = 1 - 0.0039 \times (33 - 25) = 1 - 0.0312 = 0.9688 \quad (96.9\% \text{ de su potencia nominal})$$
* **Recuperación pura por enfriamiento:** $\frac{0.9688 - 0.8518}{0.8518} = \mathbf{+13.7\%}$ de potencia eléctrica extra (incluso antes de abrir los espejos reflectores).

---

### 2.4 Hidráulica: Pérdidas de Carga, Tobera Pelton, Vórtice y Ariete

#### A. Ejemplo Completo de Turbina Pelton en Finca
Supongamos que en el terreno que elijas mides con manguera nivel un desnivel vertical bruto $H_{\text{bruta}} = 22.0\text{ m}$ y desvías por una manguera lisa de polietileno de alta densidad (HDPE) de **$2\text{ pulgadas}$ de diámetro interno ($D = 0.0508\text{ m}$)** de longitud $L = 85\text{ m}$ un caudal $Q = 3.5\text{ L/s}$ ($0.0035\text{ m}^3/\text{s}$):

1. **Pérdida de altura por fricción en la manguera ($h_f$, fórmula de Hazen-Williams con $C=150$):**
   $$h_f = 10.67 \times 85 \times \frac{(0.0035)^{1.852}}{(150)^{1.852} \times (0.0508)^{4.87}} = 906.95 \times \frac{0.00002843}{10,838 \times 0.000000511} = \mathbf{4.65\text{ m}}$$
2. **Cabeza Neta disponible en la tobera ($H_{\text{neta}}$):**
   $$H_{\text{neta}} = 22.0\text{ m} - 4.65\text{ m} = \mathbf{17.35\text{ m}} \quad (\text{El manómetro antes de la tobera marcará } 17.35 \times 1.422 = \mathbf{24.7\text{ PSI}})$$
3. **Velocidad real del chorro de agua ($v_{\text{chorro}}$):**
   $$v_{\text{chorro}} = 0.96 \times \sqrt{2 \times 9.81 \times 17.35} = 0.96 \times 18.45 = \mathbf{17.71\text{ m/s}}$$
4. **Diámetro exacto que debes taladrar en la tobera ($d_{\text{tobera}}$):**
   $$d_{\text{tobera}} = \sqrt{\frac{4,000 \times 3.5\text{ L/s}}{\pi \times 17.71\text{ m/s}}} = \sqrt{\frac{14,000}{55.64}} = \sqrt{251.6} = \mathbf{15.86\text{ mm}} \quad (\text{Broca de } 5/8\text{''} = 15.875\text{ mm})$$
5. **Potencia Eléctrica Continua en Baterías ($\eta_{\text{turbina}} = 0.68$, $\eta_{\text{gen+rect}} = 0.76 \rightarrow \eta_{\text{global}} = 0.517$):**
   $$P_{\text{eléctrica}} = 9.81 \times 3.5\text{ L/s} \times 17.35\text{ m} \times 0.517 = \mathbf{308\text{ W continuos las 24 horas}}$$
6. **Energía Diaria Entregada:**
   $$E_{\text{diaria}} = 308\text{ W} \times 24\text{ h} = \mathbf{7,392\text{ Wh/día}} \quad (7.39\text{ kWh/día — Abastece casa y finca sobradamente})$$

#### B. Turbina de Vórtice Gravitacional (Para Terrenos con Poca Pendiente: $H = 1.5\text{ a }2.5\text{ m}$)
En un tanque cilíndrico de radio $R_{\text{tanque}}$ con entrada tangencial y orificio central inferior de radio $r_{\text{orificio}} \approx 0.18 \cdot R_{\text{tanque}}$, la conservación del momento angular ($v_\theta \cdot r = \text{constante}$) acelera el agua hacia el centro:
* Para una caída de apenas $H = 1.8\text{ m}$ y un caudal de acequia de $Q = 25\text{ L/s}$, con eficiencia global $\eta_{\text{vórtice}} \approx 0.42$:
  $$P_{\text{eléctrica}} = 9.81 \times 25 \times 1.8 \times 0.42 = \mathbf{185\text{ W continuos}} = \mathbf{4.44\text{ kWh/día}}$$

---

### 2.5 Refrigeración Nocturna Cero-Vatios (Balance Térmico de la Nevera + PCM Eutéctico)

#### A. Flujo de Infiltración de Calor a través de las Paredes de la Nevera ($Q_{\text{infiltración}}$)
Una nevera doméstica de $250\text{ L}$ tiene un área superficial externa $A_{\text{ext}} \approx 2.6\text{ m}^2$.
* **De fábrica:** Espesor de poliuretano $e_1 = 0.035\text{ m}$ ($3.5\text{ cm}$), conductividad térmica $k = 0.024\text{ W/(m}\cdot\text{K)}$. El coeficiente global de transferencia (incluyendo puentes térmicos en burletes de goma) es $U_1 \approx 0.85\text{ W/(m}^2\cdot\text{K)}$. Con temperatura exterior nocturna $T_{\text{amb}} = 22^\circ\text{C}$ e interior $T_{\text{int}} = 3^\circ\text{C}$ ($\Delta T = 19^\circ\text{C}$):
  $$Q_{\text{fábrica}} = U_1 \cdot A_{\text{ext}} \cdot \Delta T = 0.85 \times 2.6 \times 19 = \mathbf{42.0\text{ W térmicos continuos}}$$
* **Con chaqueta adicional en taller ($+5\text{ cm}$ de poliestireno extruido XPS en caras frías):** La resistencia térmica ($R_{\text{term}} = e / k$) sube de $1.18$ a $2.75\text{ m}^2\cdot\text{K/W}$, bajando el coeficiente global a $U_2 \approx 0.48\text{ W/(m}^2\cdot\text{K)}$:
  $$Q_{\text{mejorada}} = 0.48 \times 2.6 \times 19 = \mathbf{23.7\text{ W térmicos continuos}} \quad (\text{Reducción del } 43.5\% \text{ en ganancia de calor})$$

#### B. Masa de Salmuera Eutéctica ($\text{NaCl}$ al $9\%$) para 14 Horas de Apagado Nocturno
Durante las $14\text{ horas}$ de noche ($18:00\text{ a }08:00$), el calor total infiltrado dentro del gabinete mejorado es:

$$E_{\text{calor 14h}} = 23.7\text{ W} \times 14\text{ h} = \mathbf{331.8\text{ Wh térmicos}} \quad (+ 60\text{ Wh por 3 aperturas de puerta} = \mathbf{392\text{ Wh térmicos}})$$

Como $1\text{ kg}$ de nuestra solución eutéctica (agua + $9\%\text{ NaCl}$, punto de fusión $-6^\circ\text{C}$) absorbe al derretirse $L_{\text{fusión}} \approx 85\text{ Wh/kg}$ térmicos:

$$m_{\text{PCM necesaria}} = \frac{392\text{ Wh}}{85\text{ Wh/kg}} = \mathbf{4.61\text{ kg}} \quad \longrightarrow \quad \text{Instalamos }\mathbf{6.0\text{ kg}}\text{ (factor de seguridad } 1.3\times\text{)}$$

---

## 3. Algoritmos de Integración Numérica para tus Mediciones de Taller

Cuando registres datos en tu bitácora (cada $\Delta t$ minutos o segundos) donde tanto el voltaje $V(t)$ como la corriente $I(t)$ cambian con el fuego de leña o con el sol, aplica la **Regla del Trapecio** en tu hoja de cálculo para no sobreestimar la energía:

$$E_{\text{total}} \text{ (Wh)} = \sum_{k=1}^{n} \left( \frac{P_{k-1} + P_k}{2} \right) \cdot \left( \frac{t_k - t_{k-1}}{3600} \right)$$

Donde $P_k = V_k \cdot I_k - P_{\text{aux}, k}$ es la potencia neta en el instante $k$, y $(t_k - t_{k-1})$ es el intervalo de tiempo en segundos entre dos mediciones consecutivas.
* **Fórmula directa para pegar en Google Sheets:** Si la columna `A` tiene el tiempo en horas decimales (ej. `0.00`, `0.25`, `0.50` para cada 15 min) y la columna `B` tiene la Potencia Neta en Vatios (`W`), en la celda `C3` escribe:
  `=((B2+B3)/2)*(A3-A2)`
  Y suma toda la columna `C` para obtener los **$\text{Wh}$ reales entregados por el prototipo**.

---

## 4. Fuentes Científicas, Manuales Abiertos y Referencias Históricas Verificables

### 4.1 Física Termoeléctrica y Generadores de Biomasa (Rusia / URSS / Europa)
1. **Ioffe, A. F. (1957):** *Semiconductor Thermoelements and Thermoelectric Cooling*. Infosearch Ltd., London / Instituto Físico-Técnico Ioffe de Leningrado (San Petersburgo). Documento fundacional donde se demuestra la figura de mérito $ZT = \frac{\alpha^2 \sigma}{\kappa} T$ y el diseño de los generadores soviéticos *TGK-3* y *TGK-10* para alimentar radios en aldeas sin electricidad usando calor de combustión.
2. **Champier, D., Bédécarrats, J. P., Rivaletto, M., & Strub, F. (2010):** *Thermoelectric power generation from biomass cook stoves*. **Energy** (Elsevier), Vol. 35(2), pp. 935–942. DOI: `10.1016/j.energy.2009.07.015`. Demuestra experimentalmente el acoplamiento de módulos de bismuto-telururo enfriados por agua sobre estufas de leña, validando los rangos de $180\text{--}220^\circ\text{C}$ en la placa amortiguadora caliente.
3. **Montecucco, A., Siviter, J., & Knox, A. R. (2014):** *The effect of temperature mismatch on thermoelectric generators electrically connected in series and parallel*. **Applied Energy**, Vol. 123, pp. 47–54. Explica cómo cablear arreglos serie-paralelo ($4\text{S}4\text{P}$) para no perder potencia cuando un extremo de la placa caliente está $15^\circ\text{C}$ más frío que el centro.

### 4.2 Conversión Termoacústica y Stirling Sin Pistones (NASA / Los Álamos, EE. UU.)
4. **Swift, G. W. (2017):** *Thermoacoustics: A Unifying Perspective for Some Engines and Refrigerators* (2nd Edition). Acoustical Society of America / Springer. Manual completo con todas las ecuaciones de ondas acústicas, regeneradores de malla y diseño de resonadores desarrollados en el **Los Alamos National Laboratory (LANL)**.
5. **Backhaus, S., & Swift, G. W. (1999):** *A thermoacoustic Stirling heat engine*. **Nature**, Vol. 399, pp. 335–338. Demostración de eficiencia térmica del $30\%$ sin partes móviles en el núcleo caliente.
6. **Software Libre de Simulación Termoacústica (LANL):** **DeltaEC** (*Design Environment for Low-Amplitude Thermoacoustic Energy Conversion*). Disponible gratuitamente a través del Los Alamos National Laboratory: `https://www.lanl.gov/org/ddste/aldps/mpa/cond-mat-magnet-thermo/thermoacoustics.php`.

### 4.3 Solar Fotovoltaica-Térmica (PVT), Enfriamiento Radiativo y Clima (China / EE. UU. / UE)
7. **Comisión Europea — Joint Research Centre (JRC):** *PVGIS 5.2 / 5.3 (Photovoltaic Geographical Information System)*. Herramienta oficial abierta para obtener series horarias de radiación solar y simular baterías *Off-Grid* en cualquier coordenada del planeta: `https://re.jrc.ec.europa.eu/pvg_tools/es/`.
8. **Chow, T. T. (2010) — City University of Hong Kong / Tsinghua:** *A review on photovoltaic/thermal hybrid solar technology*. **Applied Energy**, Vol. 87(2), pp. 365–379. Documenta las ganancias eléctricas ($10\text{--}15\%$) y térmicas ($45\text{--}60\%$) al adherir colectores hidráulicos laminares detrás de paneles monocristalinos.
9. **Raman, A. P., Anoma, M. A., Zhu, L., Rephaeli, E., & Fan, S. (2014):** *Passive radiative cooling below ambient air temperature under direct sunlight*. **Nature**, Vol. 515, pp. 540–544. Fundamento físico del sub-enfriamiento radiativo hacia la ventana atmosférica de $8\text{--}13\text{ }\mu\text{m}$.

### 4.4 Microhidráulica, Vórtice Gravitacional, Ariete y Eólica de Taller
10. **Inversin, A. R. (1986 / Reimpresión NRECA):** *Micro-Hydropower Sourcebook: A Practical Guide to Design and Implementation in Developing Countries*. NRECA International Foundation, Washington D.C.
11. **Smith, N. (1994 / Practical Action Publishing):** *Motors as Generators for Micro-Hydro Power*. Guía técnica completa para dimensionar los capacitores de excitación ($C = \frac{Q_{\text{reactiva}}}{2 \pi f V^2}$) al usar motores trifásicos de jaula de ardilla como generadores hidroeléctricos.
12. **Mulligan, S., Casserly, J., & Sherlock, R. (2016):** *Hydrodynamic investigation of free-surface turbulent vortex flows with strong-air core in a gravitational water vortex power plant*. **Renewable Energy**, Elsevier. Ecuaciones de relación geométrica entre el diámetro del tanque y el orificio de descarga para turbinas de vórtice.
13. **Piggott, H. (2013):** *A Wind Turbine Recipe Book (Metric Edition)*. Scoraig Wind Electric (`https://scoraigwind.co.uk/`). Estándar mundial de referencia para bobinado de generadores axiales de imanes permanentes de neodimio en discos de freno.

---

## 5. Resumen de Límites de Seguridad y Fronteras Termodinámicas

1. **Primera Ley (Conservación de la Energía):** En cualquier prototipo del laboratorio se cumple estrictamente que $E_{\text{entrada}} = E_{\text{útil eléctrica}} + E_{\text{útil térmica}} + E_{\text{pérdidas}} + \Delta E_{\text{almacenada}}$. Cualquier medición donde la energía de salida parezca superar a la de entrada se debe a: (a) descarga no contabilizada de una batería o inercia previa, (b) medición de Voltiamperios reactivos ($\text{VA}$) en lugar de Vatios activos ($\text{W}$) en corriente alterna, o (c) multiplicación de voltaje en vacío ($V_{oc}$) por corriente de cortocircuito ($I_{sc}$) tomadas en instantes separados.
2. **Segunda Ley (Eficiencia de Carnot):** Ninguna máquina térmica conectada a tu fogón de leña ($T_H$) o a un colector solar térmico y enfriada a temperatura ambiente ($T_C$, ambas en Kelvin: $K = ^\circ\text{C} + 273.15$) puede superar la eficiencia ideal de Carnot ($\eta_{\text{Carnot}} = 1 - T_C / T_H$).
3. **Aislamiento de Seguridad en Banco de Pruebas:**
   * Todo experimento con agua hirviendo o aire presurizado en tubos cerrados (termoacústica) debe contar con una **válvula de alivio mecánico calibrada** o tapón fusible de estaño-bismuto, y probarse primero lleno de agua fría a $2\times$ la presión de trabajo (prueba hidrostática, donde el agua incompresible no almacena energía neumática explosiva) antes de calentar gas.
   * Toda línea de corriente continua de baterías ($\text{LiFePO}_4$ o plomo) debe llevar un **fusible en serie en el polo positivo a menos de $20\text{ cm}$ del borne**, ya que la corriente de cortocircuito de una batería de litio supera los $1,000\text{ A}$ y funde llaves metálicas en segundos.