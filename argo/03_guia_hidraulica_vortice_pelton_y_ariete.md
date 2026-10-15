# 03B — Guía Constructiva: Picohidráulica (Pelton y Vórtice Gravitacional) y Ariete Hidráulico

## 1. Objetivo y Resultado Esperado
Aprovechar cualquier flujo de agua superficial disponible en el terreno que elijas para dos propósitos separados:
1. **Generación Eléctrica Base 24/7 (Turbina Pelton/Turgo o Vórtice de Baja Caída):** Producir entre **$150\text{ W}$ y $1,000\text{ W}$ continuos** ($3.6\text{ a }24.0\text{ kWh/día}$), reduciendo en un $70\%$ el tamaño de batería requerido para la vivienda y la finca.
2. **Bombeo Mecánico Directo sin Electricidad (Ariete Hidráulico Multiválvula):** Elevar entre **$1,500$ y $6,000\text{ L/día}$** de agua a un tanque elevado ($15\text{ a }40\text{ m}$ de altura) con $0\text{ Wh}$ de consumo eléctrico, usando solo tubería roscada y la energía cinética del agua.

---

## 2. Diagrama de Bloques y Flujo de Energía

```text
[CAUCE DE AGUA NATURAL (Quebrada / Canal)]
       │
       ├──► [Desarenador y Rejilla Coanda/Malla]
       │          │
       │          ├──► (Ruta A: Pequeño desnivel 1.5 - 4m, Tubo Rígido Galv/PVC Sch80)
       │          │            │
       │          │            ▼
       │          │    [ARIETE HIDRÁULICO] ──► (75% agua regresa al cauce)
       │          │            │
       │          │            └──► (Golpe de Ariete -> Válvula Check -> Cámara Aire) ──► Agua sube a Tanque Alto (30m)
       │          │
       │          └──► (Ruta B: Desnivel medio/alto 10 - 50m, Manguera Polietileno HDPE)
       │                       │
       │                       ▼
       │               [Tobera Inyectora Calibrada] ──► (Chorro alta velocidad: v = Cv * sqrt(2*g*H_neta))
       │                       │
       │                       ▼
       │               [Rodete Pelton / Turgo] ──► [Eje + Generador PMA / Motor Inducción Modificado]
       │                       │                                      │
       │            (Agua regresa limpia al río)                      ▼
       │                                            [Rectificador Trifásico + Controlador por Carga Balasto (Dump Load)]
       │                                                              │
       └──────────────────────────────────────────────────────────────┴──► Bus DC Baterías + Agua Caliente (Excedente)
```

---

## 3. Ecuaciones de Diseño para Taller

1. **Potencia eléctrica neta real ($P_e$):**

   $$
   P_e\ \text{(W)} = 9.81 \times Q\ \text{(L/s)} \times H_{\text{neta}}\ \text{(m)} \times \eta_{\text{turbina}} \times \eta_{\text{generador}}
   $$

   En prototipos de taller bien alineados, el producto $\eta_{\text{turbina}} \cdot \eta_{\text{generador}} \approx 0.45\text{ a }0.52$.

   **Regla rápida de campo:**

   $$
   P_e\ \text{(W)} \approx 4.8 \times Q\ \text{(L/s)} \times H_{\text{neta}}\ \text{(m)}
   $$

2. **Velocidad del chorro a la salida del inyector ($v_{\text{chorro}}$):**

   $$
   v_{\text{chorro}}\ \text{(m/s)} = 0.96 \times \sqrt{2 \times 9.81 \times H_{\text{neta}}}
   $$

3. **Diámetro exacto del orificio de la tobera ($d_{\text{tobera}}$, en milímetros):**

   Si haces el agujero demasiado grande, el tubo se vacía, cae la presión a cero y no generas nada. Debe estrangularse exactamente a:

   $$
   d_{\text{tobera}}\ \text{(mm)} = \sqrt{\frac{4{,}000 \times Q\ \text{(L/s)}}{\pi \times v_{\text{chorro}}\ \text{(m/s)}}}
   $$

4. **RPM óptimas de giro del rodete Pelton ($N_{\text{óptimo}}$):**

   La máxima transferencia de momento ocurre cuando la cuchara se mueve exactamente a la **mitad de la velocidad del chorro** ($u = 0.46 \cdot v_{\text{chorro}}$). Para un rodete de diámetro de paso $D_{\text{rodete}}$ (en metros):

   $$
   \text{RPM}_{\text{óptimo}} = \frac{60 \times 0.46 \times v_{\text{chorro}}}{\pi \times D_{\text{rodete}}}
   $$

## 4. Qué Fabricar / Recuperar en Taller vs. Qué Comprar

| **Componente** | **Estrategia de Autoconstrucción y Recuperación con tus Herramientas** | **Qué Comprar** |
| --- | --- | --- |
| **Generador eléctrico (3 opciones de taller)** | Recuperar y adaptar un motor de lavadora *Direct Drive*, modificar un motor industrial trifásico o construir un generador axial Piggott. Las opciones se detallan debajo. | Imanes N42/N52 (si modificas motor), rodamientos sellados SKF/NTN 2RS y puente rectificador trifásico de $50\text{ A}$ y $1000\text{ V}$ con disipador ($8\text{ USD}$). |
| **Rodete Pelton o Turgo** | **En taller:** Fundición en arena verde usando aluminio de pistones automotrices fundidos (aleación rica en silicio que fluye excelente) a partir de una cuchara maestra tallada en madera o impresa en 3D, empernada individualmente a un disco de acero torneado. **Alternativa rápida para Fase 1 ($<150\text{ W}$):** Cucharones soperos de acero inoxidable grueso soldados con plantilla de ángulo a un cubo central y equilibrados estáticamente sobre dos cuchillas niveladas. | Pernos Allen de acero inoxidable A2/A4 con tuercas autofrenantes Nyloc. |
| **Vórtice gravitacional (para caídas de solo $1.2\text{ a }2.5\text{ m}$)** | Si el terreno elegido tiene un canal caudaloso ($>20\text{ L/s}$) pero casi plano, rola en tu taller un tanque cilíndrico de chapa de acero de $3\text{ mm}$ ($\varnothing\,1.2\text{ m}$) con entrada tangencial y un agujero central en el fondo ($\varnothing\,20\text{ cm}$). El agua forma un torbellino potente que mueve un rotor de 4 palas verticales a $80\text{--}120\text{ RPM}$ acoplado por polea dentada (relación $1:4$) al generador de lavadora. | Correas y poleas síncronas o cadena de motocicleta con piñones para multiplicar RPM. |
| **Ariete hidráulico** | **100% en taller:** Cuerpo en "T" de hierro galvanizado de $1.5\text{''}$. **Válvula de ímpetu:** Válvula de pie (*check* de bronce con colador retirado) a la cual le sueldas un vástago roscado de bronce/inox con tuercas y arandelas como contrapeso ajustable y un tope de carrera. **Cámara de amortiguación:** Niple vertical de hierro o PVC Sch. 80 de $3\text{''} \times 60\text{ cm}$ de alto con una cámara de neumático de bicicleta inflada a media presión adentro (evita que el aire se disuelva en el agua y el ariete se detenga a los pocos días). | Válvula de retención de chapaleta (*swing check*) y válvula de asiento en bronce ($25\text{ USD}$). |

### 4.1. Generador eléctrico: tres opciones de taller

**Opción 1 (mejor rendimiento a bajas RPM):** Motor de lavadora *Direct Drive* (LG/Samsung Inverter de chatarra). Ya trae $36$ bobinas de cobre y rotor con imanes permanentes de ferrita/neodimio. Re-cableando las fases en serie-estrella o serie-delta entrega $24\text{ V}$ a $48\text{ V}$ entre $300\text{ y }600\text{ RPM}$ con $\sim 80\%$ de eficiencia.

**Opción 2 (enorme robustez):** Motor industrial trifásico de jaula de ardilla ($1\text{ a }3\text{ HP}$) de chatarra. **Modificación en tu torno:** Tornea $3\text{ a }5\text{ mm}$ del diámetro exterior del rotor laminado e incrusta hileras de imanes de neodimio N42 pegados con resina epoxi y zunchados con hilo de fibra de vidrio (inclinados un ángulo *skew* de 1 ranura para eliminar el *cogging*), o úsalo sin abrir conectándole 3 capacitores de marcha AC en triángulo (**Generador de Inducción Autoexcitado — SEIG**).

**Opción 3 (disco axial Piggott):** Dos discos de freno automotrices con 12 imanes de neodimio c/u y estator de bobinas encapsulado en resina poliéster con talco industrial.

## 5. Regla Crítica de Operación Hidráulica: El Controlador por Desvío (*Dump Load*)

- **Peligro físico:** A diferencia de un panel solar (que puedes desconectar en circuito abierto sin que se rompa), **jamás debes desconectar en vacío una turbina hidráulica bajo chorro pleno**. Si la batería se llena y un controlador solar normal abre el circuito, la turbina pierde el freno electromagnético del generador y se embala al doble de su velocidad nominal ($v_{\text{embalamiento}} \approx 1.8 \times \text{RPM}_{\text{nominal}}$), disparando el voltaje al doble y destruyendo inversores y rodamientos.
- **Solución obligatoria:** El generador hidroeléctrico se conecta siempre a un **controlador por derivación (*Dump Load / Shunt Controller*)** (o un controlador tipo Morningstar TriStar configurado en modo *Diversion*). Cuando la batería llega al $100\%$ ($56.0\text{ V}$ en sistema de $48\text{ V}$), un MOSFET de potencia modulado por PWM desvía exactamente los vatios sobrantes hacia una **resistencia sumergida en el tanque de agua caliente de la casa o un radiador de aire**, manteniendo la carga y las RPM de la turbina constantes las 24 horas.

## 6. Procedimiento de Prueba en Fase 1 y 2 (Sin Río Todavía)

Si aún estás en tu taller actual antes de mudarte al terreno definitivo, puedes construir y caracterizar tu turbina Pelton y tu generador en un **circuito cerrado de banco**:

1. Usa un tambor plástico de $200\text{ L}$ y una bomba centrífuga o periférica que tengas en el taller ($0.5\text{ a }1\text{ HP}$) conectada a la tobera inyectora con un manómetro de $0\text{--}60\text{ PSI}$ justo antes de la tobera.
2. **Equivalencia exacta de altura:** Cada **$14.22\text{ PSI}$ ($1\text{ bar}$)** que marque el manómetro antes de la tobera equivale exactamente a tener una montaña con una caída neta de **$10.0\text{ metros}$ de columna de agua**. Si la bomba levanta $28.4\text{ PSI}$, estás simulando en tu taller una caída real de $20\text{ metros}$ en la finca.
3. Mide el caudal recirculado con un balde y cronómetro, mide las RPM con el tacómetro láser variando la carga resistiva conectada al puente rectificador, y traza la curva de eficiencia real ($\eta = P_{\text{eléctrica DC}} / P_{\text{hidráulica manómetro}}$) antes de ir al campo.
