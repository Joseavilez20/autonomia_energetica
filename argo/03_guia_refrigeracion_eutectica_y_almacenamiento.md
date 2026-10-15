# 03C — Guía Constructiva: Nevera Solar de Consumo Nocturno Cero (PCM Eutéctico) y Almacenamiento Modular

## 1. Objetivo y Resultado Esperado
Transformar la carga más difícil de una vivienda desconectada (la nevera) y el banco de almacenamiento eléctrico[cite: 1]:
1. **Conversión de Nevera a Batería Térmica de Cambio de Fase (PCM Eutéctico):** Reducir el consumo eléctrico total de la nevera en un **$35\text{--}45\%$** y llevar su **consumo nocturno desde las baterías químicas a $0\text{ Wh}$** durante las 14 horas sin sol ($18:00\text{ a }08:00$), almacenando frío directamente como hielo salino eutéctico durante las horas de sol pleno ($10:00\text{ a }16:00$)[cite: 1].
2. **Arquitectura de Almacenamiento Eléctrico Reparable:** Integrar un banco de baterías $\text{LiFePO}_4$ con celdas prismáticas individuales y BMS reemplazable (más un respaldo mecánico/gravitacional en tanque de agua), eliminando cajas negras selladas que te aten a un fabricante[cite: 1].

---

## 2. Diagrama de Bloques y Lógica de Control Térmico-Eléctrico

```text
[BUS DC DEL SISTEMA (12V / 24V / 48V)]
       │
       ├──► [Sensor de Voltaje de Excedente Solar (V_bat > 13.6V / 27.2V / 54.4V)]
       │          │
       │          ├──► (SI HAY SOL PLENO: Relé 1 Activo) ──► [Termostato Solar T_baja = -8°C en Congelador]
       │          │                                                   │
       │          │                                                   ▼
       │          │                                    [Compresor Congela Placas Eutécticas NaCl al 10%]
       │          │
       │          └──► (NOCHE / LLUVIA: Relé 1 Abierto) ───► [Termostato Emergencia T_alta = +6.5°C en Gabinete]
       │                                                              │
       │                                                              ▼
       │                                               [Compresor APAGADO toda la noche (0 Wh)]
       │                                               (Las placas eutécticas a -6°C absorben el calor)
```

## 3. Formulación Química y Fabricación de los Acumuladores Eutécticos en Taller

Si pones botellas de agua pura en la nevera, el agua pura se congela a $0.0^\circ\text{C}$, lo cual es excelente para un enfriador simple, pero tiene poca diferencia de temperatura ($\Delta T$) para enfriar rápido el aire del gabinete a $+3^\circ\text{C}$. Al añadir una sal inorgánica en proporción exacta, creamos una **mezcla criohidratada / eutéctica** que cambia de fase a temperatura bajo cero constante:

### 3.1 Receta para Acumulador PCM de $-6^\circ\text{C}$ (Óptimo para Conservación en Nevera)

- **Proporción exacta por cada $1.0\text{ Litro}$ de mezcla:**
  - **Agua limpia (preferiblemente hervida o filtrada):** $900\text{ g}$ ($90\%$).
  - **Cloruro de Sodio ($\text{NaCl}$, sal de cocina o sal marina gruesa sin aditivos):** $90\text{ g}$ ($9\%$).
  - **Tetraborato de sodio (Bórax de ferretería/droguería):** $5\text{ g}$ ($0.5\%$ — actúa como agente nucleante para evitar el sub-enfriamiento líquido sin cristalizar).
  - **Espesante (Goma Xantana, CMC o Maicena cocida):** $5\text{ g}$ ($0.5\%$ — evita que la sal decante al fondo tras 100 ciclos de congelación y deshielo).
- **Receta alternativa para Ultracongelación ($-10.7^\circ\text{C}$, si tienes congelador agrícola):**
  - Agua ($80.5\%$) + **Cloruro de Potasio ($\text{KCl}$, fertilizante muriato de potasio blanco o sal dietética)** ($19.5\%$). Calor latente: $\sim 285\text{ kJ/kg}$ ($79\text{ Wh/kg}$).
- **Envase de taller:** Usa envases rectangulares planos de **Polietileno de Alta Densidad (HDPE, símbolo reciclaje #2)**, como bidones planos de aceite nuevos o galones gruesos lavados, llenándolos **solo al $88\%$ de su volumen** y aplastándolos levemente antes de sellar la tapa con teflón y silicona para absorber la expansión volumétrica del $9\%$ del hielo sin reventar el plástico.

## 4. Modificación Física y Eléctrica de la Nevera Paso a Paso

### Paso 1: Enfriamiento Mejorado del Condensador (Reducción de Presión de Cabeza)

1. Identifica dónde disipa calor tu nevera:
   - **Si tiene parrilla negra trasera expuesta:** Sepárala al menos $12\text{ cm}$ de la pared e instala en la base de la parrilla 2 ventiladores silenciosos de PC de $120\text{ mm}$ ($12\text{ V}$, consumo total apenas $2.4\text{ W}$) conectados en paralelo con la alimentación del compresor (para que solo giren cuando el compresor está encendido). El flujo de aire forzado baja la temperatura de condensación en $10\text{--}14^\circ\text{C}$, reduciendo la corriente del motor entre un $15\%$ y un $22\%$.
   - **Si es de condensador embutido en las chapas laterales:** No cubras la zona caliente lateral; ponle un disipador o asegúrate de que corra aire fresco alrededor, y aplica aislamiento rígido XPS únicamente en la puerta, el techo, el piso y la espalda fría.

### Paso 2: Chaqueta de Super-Aislamiento (XPS de $50\text{ mm}$)

- Los fabricantes comerciales usan apenas $30\text{--}40\text{ mm}$ de espuma para ganar volumen interno de venta.
- Adhiere con cinta doble faz o espuma de poliuretano en aerosol paneles de **Poliestireno Extruido de alta densidad (XPS, $50\text{ mm}$ de espesor)** sobre el techo, la puerta frontal y las caras que no tengan tubos calientes embutidos, y sella los bordes con cinta de aluminio. Verifica con una hoja de papel que el burlete magnético de la puerta apriete firme en todo el perímetro.

### Paso 3: Automatización con Doble Termostato Digital ($8 USD)

Para no tener que conectar y desconectar la nevera a mano todos los días:

1. Adquiere un módulo de **doble termostato digital STC-3008** o dos módulos **W1209 ($12\text{ V}$)** más un relé de estado sólido o contactor de $20\text{ A}$, y un módulo **detector de voltaje de batería (XY-CD60 o comparador LM393)**.
2. **Modo Día (cuando el banco de baterías supera los $13.6\text{ V} / 27.2\text{ V} / 54.4\text{ V}$, indicando que los paneles o la turbina están produciendo fuerte):** El relé activa el **Termostato 1**, cuyo bulbo sensor está pegado a los paquetes eutécticos del congelador, forzando al compresor a trabajar hasta enfriar los paquetes a **$-8^\circ\text{C}$** y el gabinete a **$+1.5^\circ\text{C}$**.
3. **Modo Noche / Lluvia (cuando la tensión baja del umbral de flotación solar):** El relé pasa el control al **Termostato 2**, cuyo bulbo está en el estante medio de la nevera configurado para encender el compresor **únicamente si la temperatura sube de $+6.0^\circ\text{C}$**. Gracias a los $6\text{ a }8\text{ kg}$ de placas eutécticas congeladas arriba y al super-aislamiento XPS, el compresor no arrancará ni una sola vez en toda la noche[cite: 1].

## 5. Construcción y Gestión del Banco de Almacenamiento Eléctrico (Fases 3 a 6)

- **Por qué ensamblar celdas prismáticas $\mathrm{LiFePO}_4$ con BMS externo en vez de baterías selladas o plomo-ácido:**
  - Las baterías de plomo-ácido (incluso AGM o Gel) solo permiten usar el $50\%$ de su capacidad sin sulfatarse rápidamente ($500\text{--}800$ ciclos reales = $2\text{ a }3\text{ años}$) y desperdician el $20\%$ de la energía en calor al cargar.
  - Las celdas prismáticas de **Litio-Ferrofosfato ($\mathrm{LiFePO}_4$, $3.2\text{ V}$ nominales por celda, ej. EVE/CATL de $100\text{ Ah}$ o $280\text{ Ah}$)** no se incendian por fuga térmica como el litio-cobalto de celulares, duran **$4,000\text{ a }6,000$ ciclos ($12\text{ a }15\text{ años}$)**, tienen terminales roscados M6/M8 que armas con una llave dinamométrica en tu taller, y si en 8 años falla el controlador electrónico (**BMS — Battery Management System**, ej. JK-BMS con balanceador activo de $2\text{ A}$), cambias solo el BMS con 4 tornillos o reemplazas una sola celda de $3.2\text{ V}$ sin tirar todo el banco[cite: 1].
- **Requisitos de seguridad no negociables para el banco de baterías**[cite: 1]:
  1. **Compresión mecánica de celdas:** Las celdas prismáticas de aluminio se agrupan dentro de una prensa hecha en taller con dos placas de madera fenólica o acero aisladas con lámina de fibra de vidrio/caucho EPDB y 4 varillas roscadas revestidas en manguera plástica (apriete moderado para evitar que se hinchen al ciclar).
  2. **Fusible de alta capacidad de ruptura (Clase T o Mega/ANL con cámara apaga-chispas):** Conectado a menos de $20\text{ cm}$ del borne positivo principal de la batería[cite: 1].
  3. **Puesta a tierra y transferencia**[cite: 1]: Aunque estés 100% desconectado de la red comercial, el lado de Corriente Alterna ($120\text{ V}/240\text{ V AC}$) de tu inversor debe contar con una jabalina de cobre enterrada en el suelo, vínculo Neutro-Tierra único en el inversor (para que funcione el interruptor diferencial salvavidas **GFCI / RCD de $30\text{ mA}$**) y seccionadores bipolares certificados[cite: 1].
