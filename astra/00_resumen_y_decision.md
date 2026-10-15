# Laboratorio de autonomía energética — decisión preliminar

Versión 0.1 • 15 de octubre de 2026 • Español • Estudio de prefactibilidad, no diseño de instalación.

## Decisión que podemos tomar ahora

**Medir primero el recurso hidráulico y la demanda; comparar después microhidráulica, solar y una combinación.** Has confirmado vivienda rural, corriente de agua durante todo el año y un primer alcance que incluye nevera y computador. No conocemos municipio, altitud, caudal aprovechable, desnivel, sombras, presupuesto ni consumo medido.

La microhidráulica merece prioridad de investigación porque puede aportar energía durante la noche. Su viabilidad económica depende especialmente de la conducción, el acceso al agua, la distancia a la vivienda y el mantenimiento. La solar es la alternativa modular que debe mantenerse en la comparación. El híbrido puede mejorar continuidad, pero no queda elegido como la opción más barata.

**No hay mediciones de tu propiedad en este paquete.** Los caudales, radiación, equipos y costos numéricos siguientes son supuestos. «Agua todo el año» no demuestra un caudal mínimo disponible para generación.

## Qué significa cada etiqueta

- **demostrado:** principio físico o funcionamiento documentado en una fuente identificada; no implica que se haya probado aquí.
- **estimación:** cálculo con entradas y límites declarados.
- **hipótesis:** mejora propuesta que debe contrastarse con un control.
- **pendiente de medición:** dato real del lugar que aún no tenemos.

## Comparación preliminar: recurso, conversión y utilidad

Las cifras son ejemplos independientes; no se suman entre sí. DC es corriente continua; AC, alterna. Un kWh térmico no equivale a un kWh eléctrico disponible para la nevera.

| Alternativa y función | Recurso y conversión | Madurez | Potencia / energía útil del ejemplo | Variabilidad y pérdidas | Aptitud y decisión |
|---|---|---|---|---|---|
| Microhidráulica; generación | Agua con desnivel → turbina → generador → bus DC | Comercial; adaptación local especializada | 2 L/s, 12 m netos, eficiencia total hasta DC 0,60: 141 W y 3,39 kWh DC/día; AC depende de inversor y batería | Caudal, sedimentos, obstrucciones, paradas; pérdidas de tubería separadas del rendimiento eléctrico | Investigar primero; posible base para vivienda y finca |
| Solar fotovoltaica; generación | Radiación → módulos → regulador → DC | Comercial | 0,8 kWp × 4 horas solares pico × 0,80 = 2,56 kWh DC/día; pico real no garantizado | Noche, nubes, sombra, temperatura y suciedad; almacenamiento e inversor después | Complemento o alternativa principal; 0,8 kWp solo resulta insuficiente en nuestro caso |
| Solar térmica; uso directo | Radiación → absorbedor → agua/aire caliente | Comercial y prototipable | Calentar 20 L en 15 °C almacena 0,349 kWh térmicos; si tarda 2 h, 174 W térmicos medios | Pérdidas térmicas y desajuste entre producción y uso | Reduce calentamiento eléctrico o combustible, si realmente se necesita |
| Eólica; generación | Viento → rotor → generador | Comercial; muy dependiente del sitio | Rotor de 2 m, densidad 1,1 kg/m³, viento constante 5 m/s, Cp 0,25 y eficiencia 0,8: 43 W; 0,346 kWh si esas condiciones duran 8 h | No extrapolar con velocidad media; turbulencia, arranque, frenado y densidad | Reservar hasta medir; no comprar por potencia nominal |
| Biogás; conversión de biomasa | Residuos → digestión → gas → calor o motor | Comercial; operación biológica exigente | Supuesto de 1 m³/día de biogás con 60% CH4 y 10 kWh/m³ CH4: 6 kWh químicos; 3 kWh térmicos con 50%, o 1,2 kWh eléctricos brutos con 20% | Producción, temperatura, composición, limpieza, auxiliares y fugas; las dos salidas son alternativas | Condicional a residuos y operador; priorizar calor antes de electricidad pequeña |
| Termoelectricidad; recuperación | Flujo de calor entre dos temperaturas → módulo TEG | Componentes maduros; aplicación particular experimental | Si se comprueban 50 W térmicos atravesando el módulo y 2% neto: 1 W eléctrico; 8 Wh en 8 h | Contactos, disipación, consumo de ventiladores; rendimiento supuesto | Sensores o enseñanza; no base para nevera/finca sin otra evidencia |
| Ariete / bombeo directo; servicio mecánico | Agua en caída → presión → agua elevada; o sol → bomba | Madura | Ariete supuesto: 0,5 L/s, caída 2 m, elevación 20 m, eficiencia 0,5 → 2,16 m³/día elevados; 4,9 W hidráulicos útiles | Descarga de parte del agua, pérdidas y disponibilidad | Muy pertinente para finca; ahorra bombeo eléctrico, no genera electricidad |
| Gestión de demanda; ahorro | Evitar energía innecesaria o mover horarios | Madura; resultado local por medir | Evitar 20 W durante 10 h reduce 0,20 kWh/día; no inventa energía | Efecto depende del hábito y servicio conservado | Primera inversión junto a medición |
| Batería / depósito; almacenamiento | Electricidad o agua previamente elevada → entrega posterior | Madura | Batería nominal 4 kWh, 80% utilizable, descarga 96%: 3,072 kWh al bus; depósito 1 m³ a 10 m: solo 0,0273 kWh potenciales antes de pérdidas | Capacidad, fugas, degradación y conversiones | Batería para continuidad; depósito sobre todo para servicio de agua |

Fundamento hidráulico: [DOE/NREL, ficha técnica de julio de 2001](https://docs.nlr.gov/docs/fy01osti/29065.pdf), utilizada por sus principios, no por sus antiguos precios o estadísticas. Evaluación solar horaria: [JRC, manual PVGIS 5](https://joint-research-centre.ec.europa.eu/photovoltaic-geographical-information-system-pvgis/using-pvgis-5/pvgis-5-user-manual_en). Viento: [DOE, Small Wind Guidebook](https://www.energy.gov/cmei/systems/windexchange/small-wind-guidebook). Los ejemplos numéricos son cálculos propios.

## Construcción, costos y dependencia

**Estimación presupuestaria**, USD de planificación a 2026-10-15, compra minorista internacional genérica y trabajo local por cotizar. No son ofertas ni precios colombianos. Las vidas indicadas son supuestos para planificar reposiciones, no garantías universales. Gastos excluyen el valor del trabajo propio salvo donde se dice.

| Opción / alcance del presupuesto | Qué fabricar o recuperar | Dificultad | Inversión de referencia | Gastos y mantenimiento | Vida usada para planificar | Dependencia externa |
|---|---|---|---:|---|---|---|
| Hidráulica de 0,1–0,3 kW, recorrido ilustrativo de 100 m | Banco, soportes, rejilla y partes mecánicas verificadas; profesional valida conducción | Alta | USD 4.500 adicionales al sistema solar pequeño común; contingencia aparte | USD 120/año incrementales; inspección de toma, filtros, rodamientos | Obra 20 años; mecánica mayor 10; rodamientos se revisan por condición, reserva a 5 años | Rodamientos, sellos, electrónica; obra y disponibilidad de agua |
| Solar 2 kWp + batería 4 kWh, cargas esenciales | Bastidor validado, registro y gestión; comprar módulos y protecciones | Media/alta en potencia | USD 4.600 de base | USD 80/año; limpieza según suciedad, aprietes profesionales y registros | Módulos 20 años, batería 8 e inversor 10 para el modelo | Celdas, inversor, controlador, conectores |
| Solar térmica abierta de laboratorio | Caja, aislante, absorbedor, soporte | Baja en mesa; alta en agua sanitaria | USD 0–40 si existen recipientes y termómetros; sistema real requiere cotización | Prueba: limpieza y control; piloto profesional: reserva de 2% del costo/año como hipótesis | Banco 1–3 años; sistema real 10 sujeto a ficha | Tubería sanitaria, válvulas y aislante |
| Eólica: medición / piloto de 0,5 kW | Banco pequeño y registro; rotor y torre de potencia requieren validación | Alta | Medición USD 150–500; piloto asignación USD 3.000–6.000 sin batería | Reserva inicial 3% del piloto/año; inspección mecánica y de torre | Supuesto 10 años con reposiciones | Rodamientos, freno, controlador y elevación |
| Biogás: diagnóstico / servicio térmico de 1 m³/día supuesto | Clasificación, pesaje y manejo diseñado del residuo | Alta | Diagnóstico USD 0–100 con báscula disponible; piloto profesional USD 1.000–3.000 de provisión | Trabajo diario, agua, manejo del digestato; reserva 5%/año | 5 años membranas y 10 obra como hipótesis de costo | Materiales para gas, análisis y repuestos; residuo constante |
| TEG: banco pequeño | Contactos y disipador recuperado verificado | Media | USD 20–60 sin instrumentos comunes | Inspección de contacto; auxiliares pueden anular producción | Banco 2 años de supuesto | Módulo semiconductor y convertidor |
| Bombeo directo / ariete pequeño | Soportes y tanque apto; conjunto de presión certificado | Media/alta | Banco eléctrico USD 20–60; ariete instalado provisión USD 300–1.000, sin tanque y grandes conducciones | Válvulas, sedimentos; reserva 5% del conjunto/año | Conjunto 5 años; tanque según material/ficha | Válvulas y empaques; servidumbre de agua |
| Ahorro / programación | Hábitos, sombras pasivas y registro | Baja | USD 0–50 para cambios operativos | Revisar que se conserve el servicio | Reevaluación anual | Baja; medidor prestado reduce gasto |

Los porcentajes de mantenimiento son reservas de presupuesto, no estadísticas de fabricantes. La comparación económica completa está en [06_costos_mantenimiento_y_dependencias.md](06_costos_mantenimiento_y_dependencias.md).

## Qué mostraron los cálculos ejecutados

Se asumieron 2,64 kWh AC/día, batería nominal de 4 kWh y un perfil horario sintético. Se evaluaron 30 días después de 30 de calentamiento numérico. No se descargó una serie climática local porque falta ubicación.

| Caso | Energía demandada en 30 días | Energía AC no atendida | Interpretación |
|---|---:|---:|---|
| Híbrido conservador: 0,8 L/s, 10 m, 0,8 kWp, 2,5 HSP | 79,20 kWh | 19,23 kWh | Falta generación habitual; una batería mayor solo aplaza el déficit |
| Híbrido central: 2 L/s, 12 m, 0,8 kWp, 4 HSP | 79,20 kWh | 0,00 kWh | Funciona en esta serie; no prueba continuidad anual |
| Central con 3 días sin hidro y 0,8 HSP/día | 79,20 kWh | 4,16 kWh | Necesita respaldo, gestión o redimensionamiento |
| Mismo evento, batería de 8 kWh | 79,20 kWh | 1,46 kWh | Duplicar almacenamiento aún no cubre el evento supuesto |
| Solo solar 2 kWp, escenario conservador sin evento extremo | 79,20 kWh | 0,00 kWh | Alternativa que merece comparación económica con la hidráulica |

Resultados íntegros: [modelo/salida/resultados.md](modelo/salida/resultados.md). Que ambos sistemas logren 100% en una serie corta no establece igual fiabilidad anual. En los presupuestos supuestos, el híbrido cuesta más: puede justificarse por servicio nocturno, resiliencia o cargas productivas, no por asumir automáticamente ahorro monetario.

## Próximo paso realizable

1. Medir el consumo de la nevera durante siete días y registrar computador y otras cargas.
2. Medir una salida de agua accesible con recipiente y cronómetro; levantar desnivel con nivelación. No entrar al cauce ni alterar una captación.
3. Hacer la prueba solar térmica de recipientes descrita en `02` si se desea construir desde hoy.
4. No comprar turbina, batería grande ni inversor hasta disponer de consumo, altura neta, caudal de estiaje y requisitos locales.

Faltan dos grupos de información para adaptar la siguiente revisión: **país/municipio/altitud y datos del terreno**; **consumo real/presupuesto/herramientas/autonomía y respaldo aceptable**. El detalle está en `01`.
