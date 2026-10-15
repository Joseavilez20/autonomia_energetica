# Recuperación de calor y otras vías experimentales

Versión 0.1 • 2026-10-15 • Alcance principal: aprender y alimentar sensores; no se presupone autonomía doméstica.

## Termoelectricidad: mecanismo y frontera

Flujo: **fuente caliente → módulo TEG → sumidero frío**; una fracción sale como **electricidad → convertidor → sensor**. El calor debe atravesar el módulo continuamente. Dos objetos a igual temperatura no proporcionan generación continua por efecto Seebeck.

**demostrado:** existen convertidores para aprovechar pequeñas tensiones de TEG en sensores de muy baja potencia; [Analog Devices, preguntas técnicas LTC3108/LTC3109, 2014](https://www.analog.com/en/resources/technical-articles/2017/09/14/04/06/frequently-asked-questions-thermoelectric-energy-harvesting-with-the-ltc3108-ltc3109.html). Esa documentación no prueba que un TEG concreto entregue watts con cualquier diferencia térmica.

**Estimación:** si 50 W térmicos atravesaran el módulo y la eficiencia neta medida fuese 2%, saldría 1 W eléctrico. Un ventilador de 1,5 W volvería negativo el balance eléctrico neto. No inferir flujo térmico solo de ΔT.

## Fases 0–2: banco sin combustión

Material: 1 módulo TEG identificado (no asumir tolerancia de un TEC/Peltier desconocido), 2 placas/disipadores de borde seguro, 2 sondas de temperatura, 1 multímetro, resistencias conocidas y agua templada ≤45 °C en recipiente abierto. Fuente y sumidero separados de los terminales; ninguna llama. Provisión **USD 20–60**, instrumentos comunes aparte, compra minorista internacional estimada a 2026-10-15.

1. Registrar ficha del módulo, temperaturas máximas y condición de contacto. Montar según presión de contacto del fabricante, sin romper cerámica.
2. Poner una cara en contacto térmico indirecto con agua templada y la otra con disipador a ambiente; medir temperaturas EN LAS CARAS, no solo en agua y aire.
3. Medir voltaje bajo una resistencia alta y después con resistencias progresivamente menores dentro de límites. Calcular `P=V²/R`; registrar cada 5 s durante 10 minutos y repetir tres veces con igual condición inicial.
4. Comparar con ambas caras a igual temperatura. Anotar agua enfriándose y disipador calentándose: el almacenamiento térmico inicial alimenta el ensayo.
5. Sin calorímetro o balance térmico completo no reportar eficiencia. Sí reportar mW bajo carga y Wh integrados.

Aceptación: salida repetible superior al ruido del medidor y correlacionada con ΔT; el control próximo a cero descarta offset. Una tensión en vacío no prueba capacidad para encender un equipo real.

## Fase 3 y límite de escalamiento

Probar un sensor cuyo consumo medio se mida, incluidos convertidor, reposo y transmisión. Comparar costo y mantenimiento con una pequeña celda solar o batería de larga duración. Para 1 mW durante 24 h se necesitan 24 mWh; no usar consumo durante reposo como consumo total del sensor.

Antes de recuperar calor de estufa, motor o chimenea, exigir diseño profesional de transferencia y seguridad: puede afectar combustión, tiro, presión o refrigeración. No añadir combustible para obtener unos watts y llamarlo calor residual. Para vivienda/finca, evaluar primero el uso térmico directo del calor; detener el escalamiento eléctrico si los auxiliares consumen la salida o el costo por Wh resulta desproporcionado.

Mantenimiento: contacto térmico, corrosión, grietas y temperatura. Vida del banco usada para presupuesto: 2 años, sin garantía. Si cambia ΔT, no diagnosticar desgaste solo por bajar potencia.

## Otras ideas que pueden investigarse

| Idea | Entrada física que debe medirse | Prueba mínima razonable y límite |
|---|---|---|
| Piezoelectricidad en vibraciones | Energía mecánica de la máquina/estructura | Medir potencia en carga y cuánto cambia la vibración; útil potencial para sensor, sin proyección a vivienda |
| Generador manual/bicicleta | Trabajo metabólico humano | Medir Wh y tiempo; herramienta didáctica/emergencia, no energía gratuita sin esfuerzo |
| Agua de lluvia descendente | Masa, altura y frecuencia real de lluvia | Balance mgh antes de comprar: 1 m³ a 10 m tiene solo 27,25 Wh ideales |
| Hidrógeno producido con electricidad | Electricidad del electrolizador y auxiliares | Es almacenamiento/conversión, con pérdidas; fuera del laboratorio inicial por complejidad de gas/presión |
| Motor que acciona su propio generador | Electricidad inicial, batería, energía de giro y pérdidas | El balance de ciclo completo debe incluir ΔE de almacenamiento; no hay fuente primaria adicional |

No se han ejecutado estos experimentos ni encontrado evidencia que justifique usarlos como base de tu vivienda. Se mantienen como preguntas medibles cuando exista un recurso concreto y un objetivo pequeño.
