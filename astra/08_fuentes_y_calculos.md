# Fuentes, cálculos reproducibles y limitaciones

Versión 0.1 • Fecha de investigación y ejecución: 2026-10-15.

## Registro de fuentes primarias

Fuentes consultadas mediante búsqueda web y apertura de páginas/documentos oficiales. Fecha de consulta común: **15 de octubre de 2026**. Se distingue antigüedad del documento de disponibilidad actual. No se usaron videos, patentes o marketing como demostración de rendimiento.

| ID | Fuente y enlace | Fecha/contexto | Uso concreto y límite |
|---|---|---|---|
| S01 | [DOE/NREL, Small Hydropower Systems](https://docs.nlr.gov/docs/fy01osti/29065.pdf) | Julio 2001, ficha técnica, 8 páginas | Relación entre caudal, altura y conversión; no se reutilizan precios/estadísticas antiguas |
| S02 | [PowerSpout, índice documental](https://www.powerspout.com/pages/document-index) | Página actual con manuales y entradas de mayo 2026 | Disponibilidad de guías de turbinas, control, mantenimiento y repuestos; no prueba nuestro rendimiento supuesto |
| S03 | [PowerSpout PLT Cube](https://www.powerspout.com/products/powerspout-plt-cube) | Oferta web observada, NZD 2.329,75 ex GST | Referencia comercial concreta, sin conversión de moneda ni selección de ese equipo |
| S04 | [JRC, PVGIS](https://joint-research-centre.ec.europa.eu/photovoltaic-geographical-information-system-pvgis_en) | Servicio actual; página anuncia versiones nuevas de prueba y rama 6 | Herramienta de recurso solar, gratuita y sin registro; no se obtuvo serie del sitio |
| S05 | [JRC, Using PVGIS 5](https://joint-research-centre.ec.europa.eu/photovoltaic-geographical-information-system-pvgis/using-pvgis-5_en) | Documentación de 5.3, septiembre 2024, cobertura histórica declarada hasta 2023 | Elegir versión y conservar metadatos; la rama nueva anuncia otra cobertura y no debe mezclarse |
| S06 | [JRC, manual PVGIS 5](https://joint-research-centre.ec.europa.eu/photovoltaic-geographical-information-system-pvgis/using-pvgis-5/pvgis-5-user-manual_en) | Manual web consultado | Método temporal de evaluación aislada y perfiles horarios; nuestro script es independiente y simplificado |
| S07 | [JRC, condiciones de uso](https://joint-research-centre.ec.europa.eu/photovoltaic-geographical-information-system-pvgis/general-information/usage-conditions-data-protection_en?prefLang=mt) | Información web vigente consultada | Uso libre de información según la página; al descargar capas verificar también condiciones específicas y atribución |
| S08 | [DOE, Small Wind Guidebook](https://www.energy.gov/cmei/systems/windexchange/small-wind-guidebook) | Guía oficial actual | Medición a altura de buje, turbulencia y evaluación de sitio; no usar reglas estadounidenses como permisos locales |
| S09 | [EPA AgSTAR, Operator Guidebook](https://www.epa.gov/agstar/anaerobic-digesterbiogas-system-operator-guidebook) | Manual noviembre 2020; página actualizada 2026-10-14 | Operación, mantenimiento, gas y riesgos; no reemplaza diseño del digestor ni normativa del país |
| S10 | [ENERGY STAR, Solar Water Heaters](https://www.energystar.gov/products/solar_water_heaters) | Programa estadounidense, página actual | Tecnología y necesidad de instalación/mantenimiento apropiados; no trasladar porcentajes de ahorro u orientación al sitio desconocido |
| S11 | [Analog Devices, FAQ sobre LTC3108/LTC3109](https://www.analog.com/en/resources/technical-articles/2017/09/14/04/06/frequently-asked-questions-thermoelectric-energy-harvesting-with-the-ltc3108-ltc3109.html) | Artículo técnico de 6 de octubre de 2014 | Recuperación termoeléctrica de baja potencia, sensores; no evidencia de kW domésticos |
| S12 | [NC State Extension, Hydraulic Ram Pumps](https://content.ces.ncsu.edu/hydraulic-ram-pumps) | Revisión electrónica marzo 1996 | Principio de ariete y servicio de agua; no tomar proveedores/precios como actuales |
| S13 | [Victron, instalación SmartSolar](https://www.victronenergy.com/media/pg/Manual_SmartSolar_MPPT_75-10_up_to_100-20/es/installation.html) | Manual oficial vigente recuperado | Ejemplo de instrucciones específicas del controlador y verificación de sistema; no universalizar |
| S14 | [Victron, especificaciones SmartSolar](https://www.victronenergy.com/media/pg/Manual_SmartSolar_MPPT_75-10_up_to_100-20/es/technical-specifications.html) | Familia 75/10 a 100/20 | Comprobar límites concretos de tensión/corriente; no se selecciona equipo definitivo |
| S15 | [ngspice, descargas](https://ngspice.sourceforge.io/download.html) | Página identifica versión estable 47 | Disponibilidad actual de simulador opcional; no instalado ni ejecutado aquí |
| S16 | [ngspice, licencias](https://ngspice.sourceforge.io/devel.html) | Página del proyecto | BSD modificada salvo componentes indicados |
| S17 | [LibreOffice, licencias](https://www.libreoffice.org/licenses/) | Página del proyecto | MPL 2.0 y componentes bajo otras licencias |
| S18 | [LibreOffice, requisitos](https://www.libreoffice.org/system-requirements/) | Página actual | Sistemas soportados y requisitos; herramienta opcional no ejecutada |
| S19 | [Python, declaraciones legales](https://policies.python.org/python.org/Legal-Statements/) | Página PSF | Python y biblioteca estándar bajo licencia Python; script ejecutado con Python 3.12.14 |

El índice de PowerSpout incluye contenido público y comercial; no se afirma que todo su diseño tenga licencia de hardware abierto. El programa local entregado está escrito para este estudio y puede modificarse para los experimentos; no contiene código copiado de esas fuentes. Las guías y fuentes permiten reproducir el razonamiento, pero no sustituyen ensayos físicos.

## Constantes y unidades

| Símbolo | Valor usado | Significado |
|---|---:|---|
| g | 9,81 m/s² | Aceleración gravitacional aproximada |
| rho agua | 1.000 kg/m³ | Aproximación para cálculos de banco |
| c agua | 4,186 kJ/(kg·°C) | Calor específico aproximado |
| 1 kWh | 3.600.000 J | Conversión de energía |
| 1 Wh | 3.600 J | Conversión de energía |
| 1 L/s | 0,001 m³/s | Conversión de caudal |
| rho aire del ejemplo | 1,1 kg/m³ | Supuesto, no derivado de altitud medida |

## Fórmulas y ejemplos auditables

1. **Energía eléctrica:** `E_Wh = suma(P_W × dt_h)`. Ejemplo: 12 W × 24 h = 288 Wh.
2. **Potencia hidráulica:** `P_W = rho g Q_m3s H_m eta = 9,81 Q_Ls H_m eta`. Con 2 L/s, 12 m y 0,6: 141,264 W; 24 h → 3,390336 kWh DC.
3. **Conducción:** `v = Q/A`; `h_f = f (L/D) v²/(2g)`; `h_m = K v²/(2g)`. El script calcula 32/50/63 mm interiores con f constante supuesto. No resuelve caudal de equilibrio si el salto neto calculado es negativo.
4. **FV simplificada:** `E_bus = P_kWp × HSP × factor_bus`. Factor_bus no incluye batería ni inversor en este estudio.
5. **Demanda DC para AC:** `E_bus = E_AC/eta_inv + P_idle×24 + E_aux_hidro`.
6. **Batería:** `C_util_quimica = C_nom × fraccion_util × salud`; `E_entregable_bus = C_util_quimica × eta_descarga`. Para autonomía, no multiplicar además por eficiencia de carga.
7. **Carga de batería:** energía guardada `ΔC = E_carga_bus × eta_carga`; descarga extrae `E_descarga_bus/eta_descarga` de capacidad química.
8. **Calor:** `E_kWh = masa_kg × 4,186 × ΔT / 3600`. 20 kg, 15 °C → 0,348833 kWh térmicos.
9. **Almacenamiento gravitacional:** `E_kWh = m g H / 3.600.000`. 1 m³ de agua a 10 m → 0,02725 kWh ideales.
10. **Bombeo:** `E_electrica = m g H_total /(3.600.000 eta_total)`. 5 m³, 20 m, 0,45 → 0,605556 kWh.
11. **Ariete:** `q_elevado ≈ Q_entrada × H_caida × eta / H_elevacion`, usando alturas netas/frontera definida. Ejemplo: 0,025 L/s → 2,16 m³/día.
12. **Viento:** `P = 0,5 rho A v³ Cp eta`; integrar con curva real, no solo velocidad media. Ejemplo de 2 m de diámetro descrito en guía: 43,197 W a 5 m/s constante.
13. **Biogás:** `E_quimica = volumen_normalizado × fraccion_CH4 × PCI_CH4`. El PCI 10 kWh/m³ y rendimientos del ejemplo son supuestos redondeados; no se convierten en rendimiento garantizado por kg de estiércol.
14. **Generador de Thévenin:** `I = Vs/(Ri+R)`; `P_carga = I²R`. Vs=6 V, Ri=10 ohmios, R=10 ohmios → 0,9 W. Es un modelo lineal genérico, no simula el punto de máxima potencia de un panel real.
15. **Costo útil descontado:** fórmula y entradas en `06`; script calcula ambos escenarios a 10 años. Energía servida anual es una condición económica, no una predicción de la simulación.

## Reproducción exacta

Desde la carpeta del paquete:

```bash
python3 modelo/simular.py
```

Para conservar la salida original y ensayar entradas propias, copiar `entradas.json`, cambiar solo datos documentados y ejecutar:

```bash
python3 modelo/simular.py mis_entradas.json mis_resultados
```

Escribir JSON con punto decimal y sin comentarios. El script solo requiere biblioteca estándar y Python ≥3.10. Ejecución verificada: 3.12.14. Los números de salida usan punto decimal para compatibilidad; los documentos usan coma decimal en español.

### Entradas temporales y casos

Se usan 30 días de calentamiento y 30 de evaluación, pasos de una hora y energía inicial utilizable cero antes del calentamiento. Ventana solar sintética de 6 a 18 h con forma senoidal normalizada; factores diarios [1; 0,9; 1,1; 1; 0,7; 1,3; 1]. El perfil no procede de PVGIS ni de observación climática.

Hidro se calcula con Q/H/eta constantes por escenario. Escenarios: conservador 0,8 L/s–10 m–0,5 y 2,5 HSP–factor FV 0,75; central 2 L/s–12 m–0,6 y 4 HSP–0,8; favorable 3 L/s–15 m–0,65 y 5,5 HSP–0,85. No son probabilidades ni percentiles del sitio.

Los casos adversos fijan Q=0 durante días 12–14 y sol=0,8 HSP/día. No contradice que exista corriente todo el año: representa parada de captación/equipo, no necesariamente desaparición del agua. La batería degradada conserva solo 80% de capacidad original; no se cambia resistencia interna, dato que falta para simular arranques.

### Orden del despacho

Generación disponible abastece demanda AC convertida a DC y auxiliares. Excedentes cargan con límite de potencia/capacidad; el resto se clasifica como no aprovechado. Déficit se extrae de batería dentro de límites; lo no cubierto queda como energía AC no atendida. Auxiliares tienen prioridad contable. En un sistema real se necesitan desconexiones discretas y calidad eléctrica adecuada.

En hidro, energía no aprovechada debe evitarse o derivarse de forma segura; no desaparece físicamente por llamarla «curtailment». El modelo no diseña el controlador de desvío.

### Salidas y verificación

- `resultados.json`: versión, cálculos, 11 casos, pérdidas, energía útil, déficit, capacidad inicial/final y residual.
- `series_horarias.json`: 720 muestras por caso, generación, demanda, déficit y estado de batería.
- `resultados.md`: tabla legible generada por el script.

Se verificaron límites de capacidad y balance: `generacion + almacenamiento_inicial = AC_util + auxiliares + perdidas_inversor + perdidas_bateria + no_aprovechada + almacenamiento_final`. Residuo máximo en esta ejecución ~2,37×10^-12 kWh. Prueba límite: sin generación ni energía inicial utilizable, la salida útil es cero. No se ejecutó una validación experimental.

## Incertidumbres y bloqueos reales

- No hay consumo, recurso ni climatología local medidos; faltan ubicación, estacionalidad y restricciones. Esto limita personalización, no impide los cálculos ilustrativos.
- No hay datos locales para decidir permisos, tarifa, certificación o cambio de moneda. No se verificó legislación de un país supuesto.
- **ngspice no está instalado**: no se ejecutó una simulación SPICE. El barrido eléctrico entregado es cálculo analítico en Python, no una ejecución encubierta de esa herramienta.
- Antiguas rutas de Energy Saver devolvieron 404; se sustituyeron por documentos oficiales accesibles. Un PDF canadiense devolvió 403 y otro PDF de PPA superó el límite de lectura del servicio; no se usaron como evidencia detallada.
- Los precios de la mayoría de componentes son provisiones explícitas. Falta cotización del lugar y costo de obra. No se puede demostrar amortización con ellos.
- No se ejecutó modelo meteorológico anual, hidráulica transitoria, cálculo estructural, cortocircuito, coordinación de protecciones ni análisis microbiológico.

La siguiente versión requiere datos del sitio y mediciones, no más precisión decimal en los supuestos. El propósito de esta versión es permitir decidir qué medir y qué ensayar con un límite de gasto.
