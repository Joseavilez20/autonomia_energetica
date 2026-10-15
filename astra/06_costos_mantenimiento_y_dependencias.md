# Costos, mantenimiento y dependencia externa

Versión 0.1 • 2026-10-15 • Moneda de planificación: USD; no se aplicó tasa de cambio.

## Cómo interpretar los importes

Separar **precio observado**, **estimación presupuestaria** y **costo aún desconocido**. No se conoce país/municipio del proyecto. Los presupuestos siguientes son escenarios de ingeniería para comparar alcances, con referencia a compra minorista internacional y mano de obra local por confirmar; no son cotizaciones de un mercado local.

Único precio comercial incorporado como referencia concreta: [PowerSpout PLT Cube](https://www.powerspout.com/products/powerspout-plt-cube), **NZD 2.329,75 sin GST**, mostrado el 2026-10-15. No incluye una instalación completa; transporte, importación, regulador y obra se verifican aparte. No se convirtió a USD ni se afirma que esa turbina sea adecuada a 12 m de salto. Se consultó un kit Renogy, pero la respuesta recuperada no permitió extraer un precio: no se inventa una cotización.

Para decidir una compra, solicitar al menos dos cotizaciones con misma frontera, prestaciones bajo Q/H o radiación comparables, repuestos, garantía y costo entregado en sitio.

## Presupuesto base de los dos escenarios

| Componente | Cantidad / alcance | Solar 2 kWp + 4 kWh, USD | Híbrido solar 0,8 kWp + hidro + 4 kWh, USD | Naturaleza |
|---|---|---:|---:|---|
| Módulos | 5 × 400 W / 2 × 400 W supuestos | 1.000 | 400 | Estimación, no producto elegido |
| MPPT solar | 1 compatible con el arreglo | 300 | 200 | Estimación |
| Banco de batería | 1 conjunto comercial de 4 kWh nominales con BMS | 1.400 | 1.400 | Estimación; corriente/vida por verificar |
| Inversor | 1, referencia 1,2 kW de simulación | 450 | 450 | Estimación; arranque real desconocido |
| Protección/cable/envolventes comunes | 1 conjunto | 500 | 450 | Provisión; no selección de protecciones |
| Estructura FV | 1 conjunto adecuado a área | 300 | 200 | Provisión |
| Integración eléctrica común | 1 servicio | 650 | 600 | Trabajo profesional supuesto |
| Turbina/generador | 1 de ~0,1–0,3 kW al recurso real | — | 1.200 | Reserva genérica, distinta del precio NZD citado |
| Control/desvío hidráulico | 1 conjunto | — | 500 | Provisión de controlador y carga segura |
| Conducción | 100 m supuestos × USD 10/m | — | 1.000 | Provisión; trazado/diámetro/presión pueden cambiarla mucho |
| Toma, retorno y obra sencilla | 1 conjunto | — | 1.000 | Provisión, no presupuesto de obra |
| Medición hidráulica adicional | 1 conjunto | — | 100 | Provisión básica |
| Integración/puesta en marcha hidro | 1 servicio | — | 700 | Trabajo profesional supuesto |
| **Total base** | | **4.600** | **8.200** | **Entradas del modelo económico** |

Sistema solar pequeño de 0,8 kWp con componentes comunes: USD 3.700. La hidráulica agrega USD 4.500 y produce el total híbrido de USD 8.200. No sumar el sistema solar de 2 kWp y el pequeño: son alternativas.

Los prototipos previos solo se descuentan si sus componentes sirven técnicamente en el sistema final. No recuperar celdas desconocidas para alcanzar artificialmente estos importes. Hacer soportes, registrar datos y preparar obra accesible puede reducir costos; los valores de esa sustitución deben anotarse como trabajo propio, no desaparecer del análisis.

**Exclusiones pendientes:** envío, aduana, impuestos locales, permisos, estudios, servidumbres, obra geotécnica, largas distribuciones, reparación de techo, respaldo, financiación, herramientas nuevas y retiro al final de vida. El costo base no es «llave en mano».

Usar inicialmente contingencia de planificación de 25%: solar USD 5.750 e híbrido USD 10.250, más las exclusiones que efectivamente apliquen. No se incluyó esa contingencia en el ejemplo de costo energético para que sea rastreable; mostrarlo evita dar apariencia de precisión. Sensibilidad de preestudio: ±50% en equipos/integración y hasta ±100% o más en obra hidráulica, hasta recibir cotizaciones. No son intervalos probabilísticos.

## Horizonte de 10 años: cálculo reproducible

**Estimación condicional**, tasa real de descuento elegida 5% anual, dólares constantes, sin deuda, impuestos, subsidios ni valor residual. Cada sistema se supone entregando el mismo servicio de **2,64 × 365 = 963,6 kWh AC/año**. Esa producción anual **NO** fue demostrada por la simulación corta; es un denominador común para explorar costos, que debe reemplazarse por energía útil anual validada.

Fórmula: `costo_por_kWh = [CAPEX + suma((O&M_y + reposición_y)/(1+r)^y)] / [suma(E_útil_y/(1+r)^y)]`.

Entradas: solar O&M USD 80/año; híbrido USD 200/año. Batería USD 1.400 al final del año 8 e inversor USD 450 al final del año 10 en ambos; repuestos hidráulicos USD 150 al final del año 5. Incluir la reposición del año 10 con valor residual cero es conservador para ese horizonte. Son hipótesis de costo; no predicción de falla.

| Métrica a 10 años | Solar 2 kWp | Híbrido 0,8 kWp + hidro |
|---|---:|---:|
| Inversión base | USD 4.600 | USD 8.200 |
| Costo total sin descuento, sin trabajo propio | USD 7.250 | USD 12.200 |
| Valor presente de costo, sin trabajo propio | USD 6.441,57 | USD 11.085,71 |
| Energía útil descontada, condición de igual servicio | 7.440,66 kWh | 7.440,66 kWh |
| **Costo condicional por kWh útil** | **USD 0,866** | **USD 1,490** |
| Horas propias presupuestadas/año | 12 | 52 |
| Valor elegido para comparar trabajo: USD 5/h | USD 60/año | USD 260/año |
| Costo condicional incluyendo trabajo recurrente | USD 0,928/kWh | USD 1,760/kWh |

El montaje propio inicial se registra aparte en bitácora; no se conoce aún. No contar todo el excedente como kWh útil vendido: se necesita consumo real, tarifa y autorización de exportación. Si solo se aprovecha 90% de la energía útil supuesta, el costo unitario sube aproximadamente 1/0,9 manteniendo igual costo.

Resultado de este escenario: el híbrido **no gana por costo**. Puede aportar energía nocturna, menor necesidad de reserva cotidiana o servicio de finca; esos beneficios deben medirse y compararse con su obra y trabajo. La hidráulica puede resultar mucho más favorable si ya existe conducción autorizada apta o hay cargas útiles para excedentes, pero esos hechos no se han confirmado.

## Acercarse al 100% de autonomía

- Aumentar batería de 4 a 8 kWh agrega 4 kWh nominales; usando la misma provisión lineal de USD 350/kWh serían USD 1.400 de batería más integración/protecciones si hacen falta. La linealidad es un supuesto de presupuesto, no precio de fabricante.
- En el evento simulado, esa ampliación reduce energía no atendida de 4,16 a 1,46 kWh durante los 30 días; aún no alcanza 100%. No dividir ese costo por una supuesta frecuencia anual de eventos que no conocemos.
- Gestionar cargas puede evitar parte de inversión sin reducir servicios esenciales. Respaldo de red o generador autorizado puede resolver eventos raros a menor inversión, pero tiene costo fijo/combustible/mantenimiento; falta definir aceptación y precios.
- Más generación puede recuperar batería más rápido, pero sirve poco durante un evento sin recurso y puede producir excedente habitual no utilizado.

No se calcula ahorro de factura ni amortización local sin tarifa, cargos fijos, consumo y costo instalado real. La razón para comprar instrumentos primero es evitar una inversión mal dirigida.

## Plan operativo

| Frecuencia inicial | Acción | Registro / criterio |
|---|---|---|
| Diaria al iniciar piloto | Energía, SOC, temperatura, alarmas y servicio | Déficits, cambios y consumo auxiliar |
| Según acumulación y tras eventos seguros | Revisar toma hidro, descarga y filtros | Minutos de trabajo, Q y potencia antes/después; no acercarse durante crecientes |
| Mensual | Inspección visual FV, cables accesibles, caseta, corrosión y ventilación | Fotos y deterioro; no abrir equipos energizados |
| Según fabricante / profesional | Aprietes, protecciones, lubricación, pruebas de corte y tierra | Responsable, medición y repuesto usado |
| Anual | Comparar energía útil, costos y tiempo de mantenimiento; revisar repuestos | Cobertura estacional y si merece ampliar |
| Por condición | Sustituir batería con capacidad/seguridad insuficientes, no solo por edad | Capacidad útil medida dentro de procedimiento permitido y diagnóstico |

## Dependencias y repuestos

Comprar localmente cuando haya equivalencia documentada: fusibles, conectores, cable, rodamientos y sellos identificados. Preferir tornillería estándar, documentación descargable, ajustes exportables y controles que mantengan funciones esenciales sin nube.

Fabricable/recuperable con inspección: cajas de banco, soportes no críticos, piezas mecánicas de prototipo y aislantes aptos. Para potencia: adquirir componentes certificados/apropiados y verificables en batería/BMS, corte, protección, red, presión y gas. Guardar manuales y lista de piezas, sin depender de una sola referencia difícil de importar.

Reservar dinero no equivale a una vida útil garantizada. Evaluar al año: kWh útiles, compras de energía/combustible, horas-persona, gasto total y duración de fallas. Esas métricas determinan la autonomía real.
