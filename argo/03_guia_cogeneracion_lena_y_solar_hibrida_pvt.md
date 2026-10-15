# 03A — Guía Constructiva: Cogeneración en Estufa de Leña (TEG/Termoacústica) y Solar Híbrida PVT

## 1. Objetivo y Resultado Esperado
Construir e integrar dos subsistemas complementarios que operan en sinergia climática:
1. **Módulo Solar Fotovoltaico-Térmico con Concentración Plana (PVT V-Trough):** Incrementar en un **$25\text{--}32\%$** la cosecha eléctrica diaria ($\text{Wh/día}$) de paneles solares estándar enfriándolos por la espalda con agua y añadiendo reflectores laterales a $120^\circ$, entregando simultáneamente **$150\text{ L/día}$ de agua caliente ($45\text{--}55^\circ\text{C}$)**.
2. **Módulo Cogenerador en Estufa de Leña Rocket (TEG por Termosifón + Resonador Termoacústico):** Extraer entre **$50\text{ W}$ y $120\text{ W}$ eléctricos continuos** en corriente continua ($12\text{ V}/24\text{ V}/48\text{ V DC}$) mientras cocinas con leña, garantizando el funcionamiento del router, iluminación y carga base durante temporales de lluvia de varios días sin sol.

---

## 2. Diagrama de Bloques y Flujo de Energía

```text
[SOL: Radiación Directa + Difusa]
       │
       ├──► (Alas Reflectoras Al/Mylar 1.4x) ──► [Cara Frontal Celda FV] ──► Electricidad DC (──► Regulador MPPT)
       │                                                  │
       │                                    (Calor residual ~75% del sol)
       │                                                  ▼
[Agua Fría Entrada] ───────────────────────► [Serpentín Trasero PVT] ──► Agua Precalentada (38-45°C)
                                                                                 │
                                                                                 ▼
[LEÑA: Combustión 650°C en Estufa Rocket]                               [Tanque Termosifón 120L]
       │                                                                         ▲
       ├──► (15-25% Calor en Hornilla) ──► Cocción de Alimentos                  │ (Agua a 65°C sube sin bomba)
       │                                                                         │
       ├──► (Placa Amortiguadora Fe/Al 200°C) ──► [Módulos TEG Seebeck] ──► [Bloque Agua Fría]
       │                                                  │
       │                                                  └──► Electricidad DC (──► Convertidor Boost/MPPT ──► Batería)
       │
       └──► (Tubo Inox 550°C en Brasas) ──► [Regenerador Malla #150] ──► [Onda Acústica 75 Hz] ──► [Diafragma + Imán N52] ──► AC ──► Rectificador DC```

---

## 3. Lista de Componentes (BOM), Especificaciones y Mercado de Referencia (Octubre 2026)

| Ítem | Componente | Cant. | Especificación Crítica | Fabricar / Recuperar vs. Comprar Certificado | Costo Est. (USD, 2026) |
| ---: | --- | --- | --- | --- | --- |
| 1 | Paneles Solares Monocristalinos | 2 a 4 | $400\text{--}550\text{ Wp}$ (o $100\text{ Wp}$ para prototipo Fase 2), celda partida (*Half-Cut*), marco aluminio. | **Comprar Certificado** (IEC 61215 / UL 61730). Imposible igualar eficiencia y encapsulado EVA en taller. | USD 65–85 c/u ($450\text{ Wp}$) |
| 2 | Intercambiador Trasero PVT | $2\text{ m}^2$ | Tubo de cobre flexible recocido $\varnothing 3/8\text{''}$ ($9.5\text{ mm}$) soldado a chapa de aluminio de $0.8\text{ mm}$ + aislamiento poliuretano XPS $30\text{ mm}$. | **100% Fabricar en Taller** (prensado en canaletas sobre lámina de aluminio y pasta térmica de óxido de zinc casera). | USD 35 / panel |
| 3 | Reflectores Laterales V-Trough | 4 | Bastidor de ángulo de hierro o aluminio con lámina de aluminio anodizado espejo ($0.5\text{ mm}$) o película Mylar metalizada pegada sobre chapa galvanizada. | **100% Fabricar en Taller** (con bisagras para plegar sobre el vidrio del panel en caso de granizo). | USD 25 / par |
| 4 | Módulos Termoeléctricos (TEG) | 16 | Alta temperatura: **TEG1-12611-6.0** o **SP1848-27145** (soportan $230\text{--}300^\circ\text{C}$ continuos con grafito térmico). *Nota: Usar TEC1-12706 solo para Fase 1 a $<165^\circ\text{C}$.* | **Comprar Módulos** (importación / distribuidor electrónico). El bloque colector se fabrica en taller. | USD 48 (16x SP1848) o USD 190 (16x TEG1 alta pot.) |
| 5 | Placa Caliente y Bloque Frío (Cogenerador Leña) | 1 jgo. | **Lado caliente:** Placa de aluminio rectificado $300 \times 200 \times 12\text{ mm}$. **Lado frío:** Cajetín estanco de cobre/aluminio con tabiques internos en zig-zag y racores de $3/4\text{''}$ para termosifón. | **100% Fabricar en Taller** (fresado/rectificado con lija al agua grano 400 sobre vidrio plano para planitud $<0.05\text{ mm}$). | USD 30 (chatarra de aluminio/cobre) |
| 6 | Núcleo Termoacústico (Prototipo Avanzado) | 1 | Tubo acero inox 304 Sch. 40 $\varnothing 1.5\text{''}$ ($L=450\text{ mm}$), regenerador de 120 discos de malla inox #150 ($40\text{ mm}$ largo), membrana bronce fosforoso + Imán Neodimio N52 $\varnothing 30 \times 15\text{ mm}$. | **Fabricar en Taller** (soldadura TIG o autógena con varilla de plata al $45\%$ en encamisado de agua) + **Comprar Imán N52**. | USD 75 |
| 7 | Controlador MPPT Solar + Convertidor DC-DC TEG | 1 + 1 | Solar: MPPT real $100\text{ V}/30\text{--}40\text{ A}$. Fogón: Convertidor DC-DC Buck-Boost con control de corriente constante ($CC/CV$) de entrada $8\text{--}60\text{ V}$. | **Comprar Electrónica Base** (o armar con topología síncrona TL494/XL4016 con inductores toroidales recuperados de fuentes ATX). | USD 75 (MPPT) + USD 12 (DC-DC) |
| 8 | Protecciones DC | 1 lote | Fusibles DC en portafusible cerámico ($15\text{ A}$ por rama), disyuntor termomagnético **polarizado DC** ($32\text{ A}$) y descargador de sobretensiones (SPD Tipo 2). | **Comprar Certificado obligatoriamente** (un disyuntor AC común no apaga el arco eléctrico en DC y se incendia). | USD 35 |

---

## 4. Evolución Paso a Paso por Fases Constructivas

### Fase 1 y 2: Prototipo Instrumentado en Banco (Bajo Riesgo)

1. **Pasta térmica de taller en volumen:** Para acoplar el serpentín trasero del panel PVT necesitas unos $300\text{ g}$ de compuesto térmico (comprarlo en jeringas de computación sería carísimo). **Fórmula de taller:** Mezcla un $60\%$ en peso de silicona neutra transparente o aceite mineral espeso con un $40\%$ de polvo de **óxido de zinc ($\text{ZnO}$, vendido en droguerías/químicas por kilo a bajo costo)** y polvo de aluminio fino hasta obtener una pasta homogénea sin grumos.

2. **Montaje del bloque TEG de prueba (4 módulos en serie $4\text{S}$):**
   - Rectifica la cara de la placa de aluminio caliente ($12\text{ mm}$ de espesor) y la cara del bloque de agua sobre un vidrio grueso usando lija al agua grano 240 y luego 400 con queroseno o agua jabonosa, verificando con regla metálica a contraluz que no pase luz.
   - Inserta un termopar Tipo K en un orificio lateral taladrado a $1.5\text{ mm}$ de la superficie donde apoyan las celdas.
   - Aplica una capa finísima de pasta térmica o lámina de grafito flexible ($0.2\text{ mm}$). Coloca las celdas asegurándote de que todas tengan la cara con letras (generalmente cara fría) mirando hacia el bloque de agua.
   - Une el conjunto con 4 pernos M6 que pasen **por fuera del perímetro de las celdas**, usando bujes aislantes de fibra de vidrio o arandelas de mica para no transferir calor por el tornillo, y resortes de compresión o arandelas cónicas Belleville para mantener la presión cuando el aluminio se dilate.

3. **Circuito de agua por termosifón (Cero bombas):**
   - Conecta la entrada inferior del bloque enfriador mediante manguera de $3/4\text{''}$ a la salida inferior de un tanque/tambor situado al menos $60\text{ cm}$ más alto que el fogón.
   - Conecta la salida superior del bloque enfriador (con pendiente **siempre ascendente $\ge 15^\circ$**, sin sifones ni curvas hacia abajo donde pueda atraparse aire) a la parte media-alta del mismo tanque.

### Fase 3: Piloto para Carga Real (Alimentación Continua del Router Wi-Fi y Luces LED)

- **Objetivo de Fase 3:** Mantener encendido el router ($15\text{ W}$) y 3 luces LED ($30\text{ W}$) usando exclusivamente el bloque de la estufa de leña durante un día lluvioso simulado (desconectando los paneles solares).
- **Criterio de aceptación:** Durante una cocción de $2.5\text{ horas}$, el bloque de 16 módulos TEG ($4\text{S}4\text{P}$) debe inyectar al menos **$45\text{ W}$ constantes ($112\text{ Wh}$ integrados en el medidor PZEM-017)** manteniendo la temperatura del bloque frío $\le 55^\circ\text{C}$ y la placa caliente entre $185^\circ\text{C}$ y $210^\circ\text{C}$.
- **Regulación mecánica pasiva contra sobretemperatura:** En una estufa de leña el fuego puede descontrolarse. No pegues jamás el bloque TEG directo a la llama viva: instálalo en la **pared exterior del conducto ascendente (*riser*)** separado por una placa difusora de hierro de $6\text{ mm}$ montada sobre una bisagra con un **resorte bimetálico (recuperado de plancha eléctrica o termostato viejo)** que separe la placa unos $5\text{ mm}$ cuando supere los $220^\circ\text{C}$.

---

## 5. Diagnóstico de Fallos, Mantenimiento y Límites de Escalamiento

| Síntoma Medido | Causa Física Probable | Solución en Taller |
| --- | --- | --- |
| Voltaje en vacío ($V_{oc}$) alto, pero al conectar carga cae casi a $0\text{ V}$. | 1) Una celda del arreglo en serie se abrió o fisuró por apriete desigual. 2) Conexión con polaridad invertida de una celda (resta voltaje). | Mide la resistencia interna ($\Omega$) de cada celda individual desconectada a temperatura ambiente (debe ser uniforme, aprox. $1.8\text{ a }3.2\text{ }\Omega$). |
| El tubo superior del termosifón da golpes y la cara fría sube a $95^\circ\text{C}$. | Estrangulamiento por burbuja de aire/vapor (*airlock*) en el punto alto de la manguera o manguera demasiado delgada ($<1/2\text{''}$). | Aumenta el diámetro interior a $3/4\text{''}$ ($19\text{ mm}$) e instala un tubo vertical de venteo abierto por encima del nivel máximo del tanque. |
| El panel PVT con reflectores da la misma corriente que sin reflectores. | Uno de los bordes del panel queda sin recibir reflejo (sombra parcial relativa), limitando la corriente de toda la serie de celdas. | Ajusta el ángulo de los espejos a $115\text{--}120^\circ$ respecto al plano del panel y haz los espejos un $20\%$ más largos que el panel. |

- **Límite físico de escalamiento:** La cogeneración termoeléctrica en fogón de leña tiene su techo práctico en **$100\text{--}200\text{ W}$ eléctricos** (porque al ~4% de eficiencia, extraer $500\text{ W}$ eléctricos exigiría transferir $12{,}500\text{ W}$ térmicos a través de los módulos, hirviendo cientos de litros de agua por hora). Si necesitas más de $300\text{ W}$ a partir de leña, el escalamiento pasa obligatoriamente a un **Gasificador de Leña de Tiro Invertido (*Imbert Downdraft Gasifier*)** alimentando un motor estacionario de 4 tiempos o un generador Stirling/Vapor con certificación de recipientes a presión.
