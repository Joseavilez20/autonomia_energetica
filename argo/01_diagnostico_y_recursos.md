# 01 — Diagnóstico de Demanda, Inventario de Recursos y Prueba Inicial Cero-Desembolso

> **Advertencia de rigor:** Dado que los datos específicos de tu propiedad están pendientes de confirmación, este documento establece: (1) la metodología exacta de medición en campo, (2) un **Escenario Ilustrativo de Referencia** (explícitamente marcado como supuesto de trabajo para enseñar las ecuaciones y no como diseño definitivo de tu terreno), y (3) el primer experimento físico realizable hoy mismo con materiales cotidianos.

---

## 1. Supuestos del Escenario Ilustrativo de Referencia

Mientras completas los datos de tu sitio, modelaremos sobre dos escalas progresivas ubicadas en una topografía andina/intertropical típica (ej. $1,500\text{--}2,200\text{ m s. n. m.}$, radiación solar mínima en mes lluvioso de $3.8\text{ HSP}$ y media anual de $4.5\text{ HSP}$):

* **Escenario A (Vivienda Eficiente):** 3 habitantes. Iluminación LED, refrigerador eficiente tipo Inverter o compresor convencional optimizado, 2 computadores portátiles, router Wi-Fi, carga de celulares, licuadora/herramientas de uso corto. (Cocción y ducha separadas de la red eléctrica de baterías).
* **Escenario B (Finca Productiva):** Vivienda A + bombeo de agua ($3,000\text{ L/día}$ a $25\text{ m}$ de altura), cerca eléctrica ganadera/perimetral, taller mecánico ligero (taladro de banco, amoladora $800\text{ W}$, soldador inversor ocasional), picapasto o despulpadora ($1.5\text{ HP}$) y cuarto frío o congelador agrícola.

---

## 2. Metodología de Auditoría de Cargas (Fase 0)

Antes de comprar un solo panel o turbina, es obligatorio distinguir entre **Potencia Instantánea ($\text{W}$ o $\text{kW}$)** —que define el tamaño del inversor y el calibre de los cables— y **Energía Consumida en el Tiempo ($\text{Wh}$ o $\text{kWh}$)** —que define cuántos paneles, cuánta agua y cuántas baterías necesitas—.

$$\text{Energía Diaria } (E_d \text{ en Wh/día}) = \sum_{i=1}^{n} \left( P_{\text{nominal}, i} \times t_{\text{uso diario}, i} \times f_{\text{ciclo}, i} \right)$$

Donde $f_{\text{ciclo}}$ es el factor de trabajo (por ejemplo, $1.0$ para un bombillo encendido continuo, pero $0.30\text{--}0.40$ para el compresor de una nevera que arranca y para según su termostato).

### 2.1 Matriz de Cargas — Escenario A (Vivienda) y Escenario B (Finca)

| Equipo / Carga | Categoría (Prioridad) | Cantidad | Potencia Nominal ($P$, en $\text{W}$) | Factor de Arranque ($P_{\text{pico}} / P$) | Potencia de Pico ($P_{\text{pico}}$, en $\text{W}$) | Horas reales de operación al día ($t \cdot f_{\text{ciclo}}$) | Energía Diaria Requerida ($E_d$, en $\text{Wh/día}$) | Ventana Horaria / Gestión |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Iluminación LED (10W)** | 1 - Esencial | 6 | $60\text{ W}$ | $1.0$ | $60\text{ W}$ | $5.0\text{ h}$ | $300\text{ Wh}$ | Nocturna ($18:00\text{--}23:00$) |
| **Router Wi-Fi + ONT Fibra/4G** | 1 - Esencial | 1 | $15\text{ W}$ | $1.0$ | $15\text{ W}$ | $24.0\text{ h}$ | $360\text{ Wh}$ | Continua 24/7 (Apagable de madrugada para ahorrar $100\text{ Wh}$) |
| **Refrigerador doméstico (250 L)** | 1 - Esencial | 1 | $120\text{ W}$ | $6.0$ (Compresor AC) / $1.2$ (Inverter) | $720\text{ W}$ | $8.0\text{ h}$ (ciclo $33\%$) | $960\text{ Wh}$ | 24/7 (Aplazable de noche con acumulador de frío / eutéctico) |
| **Computadores portátiles** | 1 - Esencial | 2 | $90\text{ W}$ | $1.0$ | $90\text{ W}$ | $6.0\text{ h}$ | $540\text{ Wh}$ | Diurna preferente (Cargar baterías internas al mediodía) |
| **Carga móviles / Linternas / Radio** | 1 - Esencial | 4 | $40\text{ W}$ | $1.0$ | $40\text{ W}$ | $2.5\text{ h}$ | $100\text{ Wh}$ | Diurna ($10:00\text{--}15:00$) |
| **Licuadora / Procesador alimentos** | 2 - Confort | 1 | $400\text{ W}$ | $2.0$ | $800\text{ W}$ | $0.15\text{ h}$ ($9\text{ min}$) | $60\text{ Wh}$ | Diurna |
| **Lavadora (ciclo en frío, motor)** | 2 - Aplazable | 1 | $450\text{ W}$ | $3.0$ | $1,350\text{ W}$ | $0.5\text{ h}$ (promedio diario) | $225\text{ Wh}$ | **Estrictamente entre 10:00 y 14:00 en días soleados** |
| **SUBTOTAL VIVIENDA (Escenario A)** | — | — | **$1,175\text{ W}$ (Instalados)** | — | **$\sim 1,600\text{ W}$ (Simultáneo máx.)** | — | **$2,545\text{ Wh/día}$ ($2.55\text{ kWh/día}$)** | **Cargas esenciales (Cat 1): $2,260\text{ Wh/día}$** |
| **Cerca eléctrica rural** | 1 - Esencial Finca | 1 | $8\text{ W}$ | $1.0$ | $8\text{ W}$ | $24.0\text{ h}$ | $192\text{ Wh}$ | Continua 24/7 |
| **Bomba de agua ($0.5\text{ HP}$ / $370\text{ W}$)** | 2 - Aplazable (Tanque alto) | 1 | $450\text{ W}$ | $3.5$ | $1,575\text{ W}$ | $2.0\text{ h}$ | $900\text{ Wh}$ | **Solo con excedente solar directo** (Almacenamiento gravitacional) |
| **Congelador horizontal agrícola** | 1 - Esencial Finca | 1 | $150\text{ W}$ | $5.0$ | $750\text{ W}$ | $7.0\text{ h}$ | $1,050\text{ Wh}$ | Sobre-enfriar de $10:00\text{ a }15:00$ con termostato dual |
| **Herramientas taller (Taladro/Amoladora)** | 3 - Productiva diferible | 1 | $850\text{ W}$ | $2.5$ | $2,125\text{ W}$ | $0.8\text{ h}$ | $680\text{ Wh}$ | Horario de pico solar |
| **TOTAL FINCA + VIVIENDA (Escenario B)** | — | — | **$2,633\text{ W}$ (Instalados)** | — | **$\sim 3,200\text{ W}$ (Simultáneo gestionado)** | — | **$5,367\text{ Wh/día}$ ($5.37\text{ kWh/día}$)** | — |

---

## 3. Protocolo de Medición de Recursos Naturales (Datos Medidos vs. Históricos)

Nunca dimensiones un sistema definitivo usando únicamente el promedio anual de un mapa satelital. Los sistemas autónomos fallan durante el **peor mes del año (mes crítico)**.

### 3.1 Recurso Solar
* **Datos históricos (Línea base gratuita):** Consulta **PVGIS** (Photovoltaic Geographical Information System de la Comisión Europea, cobertura global) o **NASA POWER** ingresando latitud y longitud exactas. Extrae la irradiancia mensual en el plano inclinado óptimo y en un ángulo de $\text{Latitud} + 10^\circ$ (para favorecer el invierno/época de lluvias).
* **Medición física en sitio (Obligatoria para sombras):** Construye un goniómetro o usa la cámara del teléfono con superposición de trayectoria solar (ej. *SunSurveyor* o *SolarTopo*) en el punto exacto del techo o suelo para identificar obstáculos (árboles, montañas, edificios) entre las $08:00$ y las $16:00$ durante el solsticio de diciembre y de junio.
* **Duración de observación necesaria:** El análisis de obstrucción de horizonte se hace en **1 día**, pero debe cruzarse con al menos **10 años de serie histórica satelital** para identificar el percentil P10 de días consecutivos nublados.

### 3.2 Recurso Hídrico (Micro/Picohidráulica y Ariete)
* **Advertencia:** Los mapas pluviométricos no sirven para saber cuánta agua lleva un arroyo pequeño en verano.
* **Medición de Caudal ($Q$):**
  1. **Método volumétrico (para $Q < 5\text{ L/s}$):** Desvía todo el chorro mediante un tubo o canaleta temporal hacia un balde de volumen conocido (ej. $20\text{ L}$). Mide el tiempo de llenado con cronómetro ($t$ en segundos). Repite 5 veces y saca el promedio:
     $$Q \text{ (L/s)} = \frac{V \text{ (Litros)}}{t \text{ (segundos)}}$$
  2. **Método del flotador o vertedero (para $Q > 5\text{ L/s}$):** Instala una tabla con una escotadura triangular ($90^\circ$, vertedero Thomson) o rectangular sellada con arcilla en el canal, y mide la altura de la lámina de agua ($h$) aguas arriba de la cresta.
* **Medición de Desnivel o Cabeza Bruta ($H_{bruta}$):**
  * **Método de la manguera transparente (Nivel de manguera):** Llena con agua (sin burbujas) una manguera transparente de jardín de $15\text{--}25\text{ m}$. Coloca un extremo en la cota de captación (a ras de suelo) y lleva el otro extremo pendiente abajo hasta que el menisco del agua llegue a la altura de tus ojos o de una vara graduada de $1.50\text{ m}$. Suma los tramos sucesivos hasta el punto donde iría la turbina. Es mucho más exacto que el GPS de un celular (cuyo error vertical supera los $\pm 10\text{ m}$).
* **Duración de observación necesaria:** Mínimo **1 ciclo hidrológico anual completo**, realizando mediciones puntuales cada 15 días durante los **2 meses más secos del año (estiaje)**. El sistema se dimensiona para el caudal mínimo garantizado en sequía (o respetando el caudal ecológico legal de al menos el $25\text{--}30\%$ del cauce).

### 3.3 Recurso Eólico
* **Por qué no usar datos satelitales directos:** El viento sufre cizalladura logarítmica cerca del suelo y turbulencia severa por árboles y techos. Un mapa macroclimático a $50\text{ m}$ de altura sobreestima enormemente lo que ocurre a $8\text{ m}$ en tu patio.
* **Duración de observación necesaria:** **Mínimo 3 a 6 meses continuos** con un anemómetro de cazoletas con registrador (*datalogger*) instalado en un mástil de bambú o tubo galvanizado a la altura real prevista ($8\text{--}12\text{ m}$).

---

## 4. Fase 1: Prueba Inicial Cero-Desembolso (Experimento 01)

Para inaugurar el laboratorio hoy mismo sin gastar dinero, realizaremos un **Calorímetro Solar e Hidráulico de Campo** y una **Auditoría de Potencia con Medidor Doméstico**.

### Experimento 1A: Medición Directa de Constante Solar Útil y Eficiencia Fototérmica por Calorimetría

* **Objetivo:** Medir experimentalmente cuántos vatios por metro cuadrado ($\text{W/m}^2$) de energía térmica útil puedes capturar en tu patio al mediodía solar y demostrar la ley de conservación de energía térmica sin usar piranómetros costosos.
* **Materiales y herramientas que debes tener previamente en casa (Cero desembolso):**
  1. Una bandeja metálica de hornear, sartén oscura, o una botella PET de $1.5\text{--}2.0\text{ L}$ pintada de negro mate (con hollín de vela o pintura acrílica negra que tengas sobrante) o forrada internamente con una bolsa plástica negra.
  2. Un trozo de cartón y plástico transparente (film de cocina o vidrio de un cuadro viejo) para crear una caja cerrada que reduzca el viento (efecto invernadero).
  3. Un termómetro disponible en casa (termómetro de cocina tipo punzón, termómetro clínico si trabajamos en el rango $35\text{--}42^\circ\text{C}$, o el sensor de temperatura de un multímetro económico).
  4. Una jarra medidora de cocina o balanza de cocina (sabiendo que $1\text{ L}$ de agua $\approx 1\text{ kg}$).
  5. Un reloj o cronómetro del teléfono y una regla o cinta métrica.
* **Fundamento Físico y Ecuación de Control:**
  La energía térmica absorbida por el agua ($Q_{term}$, en Joules o $\text{Wh}$) al subir su temperatura desde $T_{\text{inicial}}$ hasta $T_{\text{final}}$ está dada por el calor específico del agua ($c_p = 4,184\text{ J/(kg}\cdot^\circ\text{C)} = 1.162\text{ Wh/(kg}\cdot^\circ\text{C)}$):
  $$E_{\text{útil}} \text{ (Wh)} = m_{\text{agua}} \text{ (kg)} \times 1.162 \frac{\text{Wh}}{\text{kg}\cdot^\circ\text{C}} \times (T_{\text{final}} - T_{\text{inicial}})$$
  La potencia térmica media capturada ($P_{\text{captada}}$, en $\text{W}$) durante un intervalo de tiempo $\Delta t$ (en horas) es:
  $$P_{\text{captada}} \text{ (W)} = \frac{E_{\text{útil}} \text{ (Wh)}}{\Delta t \text{ (h)}}$$
  Dividiendo esta potencia por el área proyectada del colector expuesta al sol ($A = \text{largo} \times \text{ancho}$, en $\text{m}^2$), obtenemos el **Flujo de Potencia Térmica Neta ($\text{W/m}^2$)**:
  $$I_{\text{neta}} \left(\frac{\text{W}}{\text{m}^2}\right) = \frac{P_{\text{captada}}}{A}$$
* **Procedimiento paso a paso:**
  1. Mide el área rectangular de tu bandeja o la sección longitudinal proyectada de la botella ($A = \text{diámetro} \times \text{altura llena}$, en $\text{m}^2$). *Ejemplo: Bandeja de $0.30\text{ m} \times 0.20\text{ m} = 0.06\text{ m}^2$.*
  2. Vierte exactamente $1.0\text{ kg}$ ($1.0\text{ L}$) de agua a temperatura ambiente dentro del recipiente, colócalo dentro de la caja de cartón aislada, mide su temperatura inicial ($T_i$, ej. $20.0^\circ\text{C}$) tras agitar suavemente y cúbrelo con el plástico transparente o vidrio.
  3. Orienta el recipiente perpendicular a los rayos del sol exactamente entre las $11:30$ y las $12:30$ en un día despejado ($\Delta t = 1.0\text{ h}$).
  4. Al cumplirse los $60\text{ minutos}$ ($\Delta t = 1.0\text{ h}$), agita el agua para homogeneizar estratos térmicos y mide inmediatamente la temperatura final ($T_f$).
* **Ejemplo de cálculo e interpretación de resultados:**
  * Si $m = 1.0\text{ kg}$, $A = 0.06\text{ m}^2$, $\Delta t = 1.0\text{ h}$, $T_i = 20.0^\circ\text{C}$ y al cabo de una hora mides $T_f = 48.0^\circ\text{C}$ ($\Delta T = 28.0^\circ\text{C}$):
    $$E_{\text{útil}} = 1.0 \times 1.162 \times 28.0 = 32.54\text{ Wh}$$
    $$P_{\text{captada}} = \frac{32.54\text{ Wh}}{1.0\text{ h}} = 32.54\text{ W}$$
    $$I_{\text{neta}} = \frac{32.54\text{ W}}{0.06\text{ m}^2} = 542.3\text{ W/m}^2$$
* **Qué conclusión permite obtener:**
  Si bajo pleno sol de mediodía obtienes una captación térmica neta superior a $450\text{ W/m}^2$, habrás demostrado físicamente que un colector casero de apenas **$2.0\text{ m}^2$** en ese mismo techo te entregará más de **$900\text{ W}$ de potencia térmica gratuita** (equivalente a tener una parrilla eléctrica encendida sin pagar factura), suficiente para calentar $120\text{ L}$ de agua para las duchas de toda la vivienda.

### Experimento 1B: Auditoría de Consumo Oculto ("Cargas Fantasma") con el Medidor de la Empresa Eléctrica

* **Materiales:** El contador/medidor de luz de tu vivienda actual y el cronómetro de tu celular (costo $0).
* **Procedimiento:**
  1. Apaga o desconecta las cargas grandes cíclicas (nevera y bombas) durante $15\text{ minutos}$, dejando conectado únicamente lo que suele quedar "en espera" (televisores apagados, cargadores enchufados, microondas, router, regletas con bombillo).
  2. Ve al medidor de la calle/entrada:
     * Si es digital, observa los impulsos del LED rojo (la carcasa indica la constante, usualmente $1000\text{ imp/kWh}$ o $1600\text{ imp/kWh}$). Cuenta cuántos segundos ($t$) transcurren entre 10 parpadeos.
     * La potencia instantánea exacta en vatios ($\text{W}$) es:
       $$P \text{ (W)} = \frac{3,600,000 \times N_{\text{parpadeos}}}{K_{\text{imp/kWh}} \times t \text{ (segundos)}}$$
* **Conclusión accionable:** Cada $25\text{ W}$ de consumo fantasma que descubras y elimines con un simple interruptor representan **$0.6\text{ kWh/día}$ ahorrados**, lo que equivale a **ahorrarte comprar e instalar $200\text{ Wp}$ en paneles solares y $700\text{ Wh}$ en baterías**.