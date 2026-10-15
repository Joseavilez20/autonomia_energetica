# 00 — Resumen Ejecutivo, Física de Conversión y Matriz de Decisión

> **Nota metodológica:** Este documento distingue estrictamente entre **fuentes primarias de energía** (sol, gravedad/agua, viento, biomasa), **sistemas de almacenamiento** (baterías químicas, estanques elevados, tanques térmicos) y **medidas de eficiencia/ahorro** (aislamiento, uso directo mecánico). El almacenamiento jamás genera energía; siempre introduce una pérdida neta por eficiencia de ciclo completo ($\eta_{round-trip} < 100\%$).

---

## 1. Desglose Físico de Alternativas Evaluadas

### 1.1 Solar Fotovoltaica (FV)
* **Fuente primaria:** Radiación electromagnética solar (fotones).
* **Conversión:** Efecto fotovoltaico en unión semiconductora P-N (corriente continua, DC) $\rightarrow$ Regulación MPPT/PWM $\rightarrow$ Almacenamiento electroquímico o Inversión a Corriente Alterna (AC).
* **Pérdidas típicas:** Sombreado y suciedad ($3\text{--}10\%$), coeficiente térmico por calentamiento del panel ($-0.35\%/^\circ\text{C}$ sobre $25^\circ\text{C}$, pérdida típica $8\text{--}15\%$), caída óhmica en cableado ($1\text{--}3\%$), controlador e inversor ($8\text{--}15\%$), ciclo de batería ($\text{LiFePO}_4$: $5\text{--}8\%$; Plomo-ácido: $15\text{--}25\%$).
* **Utilidad final:** Electricidad universal (iluminación, electrónica, motores DC/AC, refrigeración).

### 1.2 Solar Térmica (Calentamiento de agua y cocción/secado)
* **Fuente primaria:** Radiación solar global (directa + difusa).
* **Conversión:** Absorción fototérmica (cuerpo negro / superficie selectiva) $\rightarrow$ Transferencia por conducción y convección a un fluido (agua o aire).
* **Pérdidas típicas:** Reflexión óptica en cubierta ($5\text{--}12\%$), pérdidas convectivas y radiativas al ambiente según aislamiento ($15\text{--}40\%$), pérdidas en tuberías y tanque de almacenamiento ($10\text{--}20\%$ cada 24 h).
* **Utilidad final:** Agua caliente sanitaria (ducha, cocina), deshidratación de cosechas, cocción solar directa. **Ventaja física crítica:** Eficiencia bruta de captación del $45\text{--}70\%$ frente al $18\text{--}22\%$ de un panel fotovoltaico, a una fracción del costo por vatio térmico si se autoconstruye.

### 1.3 Microhidráulica y Picohidráulica (Flujo de agua gravitacional)
* **Fuente primaria:** Energía potencial gravitatoria del agua en movimiento ($P_{bruta} = \rho \cdot g \cdot Q \cdot H_{neta}$).
* **Conversión:** Energía potencial $\rightarrow$ Energía cinética (tobera/inyector) $\rightarrow$ Energía mecánica rotacional (rodete Pelton, Turgo o Michell-Banki) $\rightarrow$ Energía eléctrica mediante generador de imanes permanentes (PMG) o motor de inducción con capacitores (PAT/SEIG).
* **Pérdidas típicas:** Fricción hidráulica en tubería forzada o *penstock* ($5\text{--}15\%$), eficiencia mecánica de la turbina ($50\text{--}75\%$ en prototipos artesanales), eficiencia del generador y rectificación ($65\text{--}85\%$). Eficiencia global ($\eta_{total}$): $35\text{--}55\%$.
* **Utilidad final:** Generación eléctrica base 24/7. **Ventaja crítica:** Un sistema picohidráulico continuo de apenas $150\text{ W}$ entrega $3.6\text{ kWh/día}$, equivalente a instalar $\sim 1000\text{ Wp}$ en paneles solares, requiriendo un banco de baterías mínimo.

### 1.4 Energía Eólica de Pequeña Escala (Autoconstrucción tipo Hugh Piggott)
* **Fuente primaria:** Energía cinética del viento ($P_{viento} = \frac{1}{2} \rho A v^3$).
* **Conversión:** Sustentación aerodinámica en palas $\rightarrow$ Par mecánico en rotor $\rightarrow$ Generador axial de flujo magnético con imanes de neodimio o alternador modificado.
* **Pérdidas típicas:** Límite teórico de Betz ($40.7\%$ mínimo perdido inevitablemente; límite máximo extraíble $59.3\%$), pérdidas aerodinámicas y mecánicas reales (coeficiente de potencia $C_p \approx 0.20\text{--}0.30$ en rotores caseros), pérdidas en rectificación y desacople de impedancia.
* **Utilidad final:** Complemento eléctrico en zonas de ventisca nocturna o estacional. **Advertencia física:** Como la potencia depende del **cubo de la velocidad** ($v^3$), reducir el viento a la mitad reduce la potencia a la **octava parte** ($12.5\%$). En vientos promedio menores a $4.0\text{ m/s}$, la producción energética real no amortiza el desgaste mecánico de rodamientos y torres.

### 1.5 Biogás (Digestión Anaerobia Mesofílica/Psicrofílica)
* **Fuente primaria:** Energía química almacenada en enlaces de carbono de materia orgánica biodegradable (estiércol, desechos agrícolas).
* **Conversión:** Hidrólisis, acidogénesis, acetogénesis y metanogénesis bacteriana sin oxígeno $\rightarrow$ Mezcla gaseosa ($55\text{--}70\%\text{ CH}_4$, $30\text{--}45\%\text{ CO}_2$, trazas de $\text{H}_2\text{S}$).
* **Pérdidas típicas:** Energía térmica requerida para mantener el biodigestor entre $25\text{--}35^\circ\text{C}$, pérdidas por conversión en motor de combustión interna si se busca electricidad ($75\text{--}85\%$ se pierde como calor; solo $15\text{--}25\%$ se vuelve electricidad).
* **Utilidad final:** **Uso directo en quemadores de cocina, hornos o calentadores de agua** (eficiencia térmica $\sim 55\text{--}60\%$), más producción de biol (fertilizante líquido rico en nitrógeno disponible). Convertir biogás a electricidad en pequeña escala es mecánicamente destructivo por la corrosión del ácido sulfhídrico ($\text{H}_2\text{S}$) a menos que se instale un filtro riguroso de óxido férrico y carbón activado.

### 1.6 Conversión Termoeléctrica (Efecto Seebeck / Celdas Peltier TEG)
* **Fuente primaria:** Gradiente térmico ($\Delta T = T_{caliente} - T_{fria}$) proveniente de fogones de leña, estufas Rocket o escapes.
* **Conversión:** Difusión de portadores de carga en materiales semiconductores disímiles ($\text{Bi}_2\text{Te}_3$) bajo diferencia de temperatura.
* **Pérdidas típicas:** Eficiencia termodinámica extremadamente baja ($\eta \approx 2\text{--}5\%$). El $95\text{--}98\%$ del calor cruza el módulo por conducción térmica sin generar electricidad. Requiere disipación activa o por termosifón de agua en la cara fría; si la cara fría se calienta, el voltaje cae a cero y la soldadura interna se funde ($>200^\circ\text{C}$ en celdas Peltier comerciales TEC1-12706).
* **Alcance real:** Exclusivamente para **microgeneración ($2\text{--}15\text{ W}$)** destinada a cargar teléfonos, linternas, alimentar sensores IoT o mover un ventilador que mejore la combustión de la misma estufa. **No escalable a vivienda ni finca.**

### 1.7 Ariete Hidráulico (Bomba de golpe de ariete)
* **Fuente primaria:** Energía potencial gravitatoria de un caudal de agua con pequeña caída ($H_{motriz} \ge 1.5\text{ m}$).
* **Conversión:** Conversión directa de energía cinética del fluido en onda de sobrepresión (golpe de ariete por cierre súbito de válvula de ímpetu) $\rightarrow$ Elevación de una fracción del caudal a gran altura ($H_{descarga}$ hasta $10 \times H_{motriz}$).
* **Pérdidas típicas:** Entre el $70\%$ y el $90\%$ del agua que entra sale por la válvula de desagüe; eficiencia energética hidráulica $\eta \approx 40\text{--}60\%$.
* **Utilidad final:** **Ahorro directo de electricidad** al eliminar bombas eléctricas para riego o llenado de tanques altos. Se construye 100% con accesorios de plomería galvanizados o PVC de alta presión (Schedule 80) y válvulas de retención modificadas.

---

## 2. Tabla Comparativa de Alternativas (Bajo Supuestos Definidos)

* **Supuestos de base para comparación estandarizada:**
  * **Sitio tipo:** Finca / Vivienda periurbana-rural en zona intertropical o templada media ($4.5\text{ HSP}$ solares equivalentes a $4.5\text{ kWh/m}^2/\text{día}$; temperatura ambiente $18\text{--}26^\circ\text{C}$).
  * **Precios de referencia:** Dólares estadounidenses (USD) a valores de mercado minorista local / importación estándar en **octubre de 2026** (sin incluir mano de obra propia).

| Alternativa | Recurso Mínimo Requerido | Madurez Técnica | Potencia y Energía Útil (Módulo Base Definido) | Variabilidad e Intermitencia | Nivel de Autoconstrucción (DIY) | Dificultad Técnica | Inversión Inicial Estimada (USD, 2026) | Gastos Recurrentes y Mantenimiento | Vida Útil Estimada | Dependencia de Proveedores Externos | Aptitud para Vivienda / Finca |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Solar Fotovoltaica (FV)** | Irradiancia $\ge 3.5\text{ kWh/m}^2/\text{día}$; área libre de sombras $10\text{ m}^2$ | Comercial / Estándar global | **Módulo $1\text{ kWp}$:** Entrega **$\sim 3.4\text{ kWh/día}$** útiles (tras pérdidas de inversión y batería $\text{LiFePO}_4$) | Alta (ciclo diurno y nubosidad). Requiere batería para uso nocturno | **Baja en celdas / Alta en estructura**, cableado, protecciones y cajas de control | Baja - Media | **$750 - $1,200** ($1\text{ kWp}$ + inversor/regulador + $2.5\text{ kWh}$ batería) | Muy bajos ($15/año en limpieza, reapriete de bornes y fusibles) | Paneles: $25\text{+}$ años. Inversor: $7\text{--}10$ años. Batería $\text{LiFePO}_4$: $10\text{--}12$ años | **Alta en electrónica de potencia** y celdas; nula en operación diaria | **Excelente** (Eje central eléctrico para vivienda y finca) |
| **Solar Térmica (Termosifón)** | Irradiancia $\ge 3.5\text{ kWh/m}^2/\text{día}$; agua con baja dureza cálcica | Alta (Comercial y DIY muy probado) | **Colector $2\text{ m}^2$ ($150\text{ L}$):** Equivale a **$\sim 3.0\text{ kWh/día}$ térmicos** (agua a $50\text{--}65^\circ\text{C}$) | Media (el tanque aislado conserva calor por $24\text{--}36\text{ h}$) | **Muy Alta ($80\text{--}95\%$):** Parrilla de cobre/CPVC negro o polietileno en caja aislada | Baja | **$120 - $280** (Autoconstruido) vs. $450 - $700 (Tubos de vacío comercial) | Bajos ($10/año: purga de lodos, pintura negra mate, ánodo de sacrificio) | $15\text{--}20$ años (cobre/acero); $8\text{--}10$ años (polímeros expuestos) | **Muy Baja** (reparable con plomería local y soldadura blanda) | **Excelente** (Desplaza duchas eléctricas y gas en vivienda/finca) |
| **Picohidráulica (Pelton / Turgo)** | Quebrada con desnivel $H \ge 12\text{ m}$ y caudal continuo $Q \ge 2.5\text{ L/s}$ (con permiso/derecho) | Media - Alta | **Sistema $H=15\text{ m}, Q=3\text{ L/s}$:** Potencia eléctrica neta **$\sim 200\text{ W}$ continuos = $4.8\text{ kWh/día}$** | Muy Baja (generación continua 24/7; varía solo en estiaje severo) | **Alta ($70\text{--}85\%$):** Cucharas fundidas/impresas, carcasa, tobera y alternador modificado | Media - Alta (Mecánica, alineación e hidráulica) | **$400 - $950** (Incluida manguera de polietileno de alta densidad HDPE de $100\text{ m}$) | Moderados ($40/año: cambio de rodamientos cada $2\text{ años}$, limpieza de rejilla toma-agua) | Turbina y tubería: $20\text{+}$ años. Rodamientos: $1.5\text{--}3$ años | **Muy Baja** (rodamientos universales y alambre esmaltado estándar) | **Sobresaliente** donde exista el recurso hídrico con desnivel |
| **Eólica Pequeña Escala (Piggott)** | Viento medio anual medido a $10\text{ m}$ de altura $\ge 4.5\text{ m/s}$ libre de turbulencia | Media (Nicho técnico) | **Rotor $\varnothing 2.4\text{ m}$ a $5\text{ m/s}$ medios:** Entrega **$\sim 1.2\text{--}1.8\text{ kWh/día}$** (altamente racheado) | Extrema ($P \propto v^3$). Días enteros en $0\text{ W}$ seguidos de picos de tormenta | **Muy Alta ($90\%$):** Palas talladas en madera, bobinado manual e imanes en discos de freno | Alta (Equilibrado dinámico, torre arriostrada, freno de tormenta) | **$500 - $1,100** (El costo de la torre y cables tensores suele igualar al de la turbina) | Altos en fatiga mecánica ($50/año en inspección de palas, pintura de borde de ataque, tensores) | $10\text{--}15$ años con mantenimiento riguroso de torre y palas | **Baja** (salvo imanes de neodimio N42/N52 inicialmente) | **Condicional** (Solo viable en crestas, costas o cañones ventosos) |
| **Biogás (Biodigestor Tubular)** | Estiércol fresco $\ge 20\text{ kg/día}$ (ej. 2 vacas estabuladas o 6-8 cerdos) + $60\text{ L/día}$ de agua | Alta en sector rural | **Reactor de $6\text{ m}^3$ totales:** Produce $\sim 1.0\text{--}1.4\text{ m}^3\text{ biogás/día} \approx$ **$6.0\text{ kWh/día}$ térmicos** ($3\text{--}4\text{ h}$ de hornilla) | Baja (producción constante si se alimenta a diario y $T > 22^\circ\text{C}$) | **Muy Alta ($95\%$):** Geomembrana o polietileno tubular calibre 8, PVC sanitario y válvula de botella de agua | Baja - Media (Obra civil básica y hermeticidad de gases) | **$180 - $420** (Polietileno doble capa, tubería PVC, filtro de $\text{H}_2\text{S}$ con esponjilla de hierro) | Trabajo diario ($15\text{ min/día}$ para mezcla y carga; cambio de viruta de hierro cada $3\text{ meses}$) | Polietileno invernadero: $4\text{--}6$ años. Geomembrana HDPE/PVC: $12\text{--}15$ años | **Nula** (insumos de ferretería agrícola local) | **Inviable en urbano / Excelente en finca** con animales |
| **Ariete Hidráulico (Bombeo)** | Caída de agua $H \ge 1.5\text{ m}$ y flujo motriz $Q \ge 5\text{ L/min}$ constantes | Muy Alta (Mecánica clásica) | **Ariete de $1\text{''}$ ($H_{motriz}=3\text{ m}, Q=15\text{ L/min}$):** Eleva **$\sim 1,800\text{ L/día}$** a $20\text{ m}$ de altura sin electricidad | Baja (opera 24 h sin intervención humana mientras corra agua) | **Total ($100\%$):** Niples de hierro galvanizado, válvula de pie modificada con resorte/peso y cámara de aire | Baja | **$45 - $110** (Accesorios de plomería estándar de $1\text{''}$ a $1.5\text{''}$) | Muy bajos ($5/año: cambio de empaque de caucho de la válvula de ímpetu y purga de cámara de aire) | $20\text{+}$ años (cuerpo metálico) | **Nula** (reparable con caucho de neumático y llaves de tubo) | **Excelente en finca** para riego y agua doméstica en altura |
| **Termoeléctrica (Celdas Peltier/TEG)** | Fuente de calor constante ($150\text{--}250^\circ\text{C}$) y agua fría circulante ($20^\circ\text{C}$) | Experimental / Nicho | **Arreglo de 4 celdas en estufa de leña:** Entrega **$4\text{--}8\text{ W}$ ($\sim 0.03\text{ kWh/día}$)** durante tiempos de cocción | Alta (solo genera mientras el fogón está encendido y el agua permanece fría) | **Alta en montaje** (bloque disipador de aluminio, pasta térmica y control de sobretemperatura) | Media (Fácil destruir las celdas por exceso de calor $>200^\circ\text{C}$) | **$35 - $80** (Módulos TEC1-12706 o TEG SP1848, bloque de agua aluminio y convertidor DC-DC Boost) | Riesgo de degradación térmica rápida si falla el flujo de agua fría | $1\text{--}3$ años (fatiga térmica por ciclos de dilatación) | Media (módulos semiconductores importados) | **Solo Laboratorio / Emergencia** (Carga de baterías 5V/12V e IoT) |

---

## 3. Selección Justificada de la Arquitectura Híbrida

Para cumplir tu objetivo de **máxima autonomía, reparabilidad con herramientas comunes y mínimo costo recurrente**, el error más costoso es intentar suplir todas las necesidades (especialmente el calor y el bombeo) mediante electricidad acumulada en baterías. 

Calentar agua o cocinar con resistencias eléctricas alimentadas por paneles solares y baterías multiplica por 4 el costo del sistema eléctrico. Por tanto, la estrategia óptima se basa en **desacoplar las cargas según su naturaleza física**:

1. **Pilar 1 — Reducción radical de demanda eléctrica por sustitución térmica y mecánica:**
   * Calentamiento de agua mediante **colector solar térmico por termosifón** autoconstruido.
   * En la etapa de finca, cocción mediante **biogás** (si hay estiércol/biomasa) y **cocina solar parabólica/caja aislada** en horas de sol, complementado con bombeo de agua por **ariete hidráulico** o **bombeo solar directo sin baterías** (acumulando agua en un tanque alto en lugar de electrones en una batería).
2. **Pilar 2 — Generación eléctrica modular y reparable:**
   * **Solar Fotovoltaica (FV)** como base escalable desde el día 1 (por su drástica caída de precios por vatio y ausencia de partes móviles).
   * **Picohidráulica autoconstruida** en la etapa de finca (siempre que el diagnóstico de la Fase 0 confirme una caída de agua viable), usando motores asincrónicos estándar o alternadores modificados que cualquier taller de bobinado local puede reparar.
3. **Pilar 3 — Experimentación educativa y de respaldo:**
   * Los generadores termoeléctricos (Peltier) y los rotores Savonius/axiales pequeños se ejecutarán en las **Fases 1 y 2 (Laboratorio)** para dominar la instrumentación, el rectificado trifásico, el acoplamiento de impedancias y el balance energético, pero no se les asignará la responsabilidad de sostener la vivienda a menos que las mediciones locales demuestren condiciones excepcionales.