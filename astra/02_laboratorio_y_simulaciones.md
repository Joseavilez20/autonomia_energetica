# Laboratorio inicial y simulaciones

Versión 0.1 • 2026-10-15 • Bancos de mesa a 6–12 V DC, potencia limitada, sin conexión a la instalación de la vivienda.

## Instrumentos: comprar por necesidad

Los precios son **asignaciones estimadas de presupuesto**, USD minoristas internacionales a la fecha, sin impuestos/envío ni una oferta verificada. Si se prestan los instrumentos, el desembolso puede reducirse.

| Prioridad | Instrumento / cantidad | Prestación mínima deseada | Comprobación y limitación | Provisión USD |
|---|---|---|---|---:|
| Indispensable para carga | 1 medidor enchufable AC certificado, compatible con tensión/frecuencia/conector | Wh/kWh y W activos; error objetivo ≤2% en la carga real; registrar factor de potencia si lo ofrece | Comparar con equipo conocido durante 1 h; no mide bien arranques rápidos ni cargas por debajo de su umbral | 20–40 |
| Indispensable en banco DC | 1 multímetro; preferibles 2 prestados si se mide V e I simultáneamente | Voltaje DC ≤1%; corriente ≤2%; puntas y entradas protegidas | Cero, resistencia conocida y comparación con medidor de referencia; no usar entrada A en paralelo con fuente | 15–35 cada uno |
| Indispensable según prueba | Recipiente graduado 10–20 L, cinta y cronómetro | Volumen ±2%; tiempo ±0,2 s; duración de llenado preferible >10 s | Graduar por masa de agua aproximando 1 kg/L; medir cinco veces; no supone calibración acreditada | 0–15 |
| Indispensable térmico | 2 sondas, 1 báscula y reloj | ±0,5 °C, ±1% masa, tiempos comunes | Comparar sondas juntas en agua agitada a dos temperaturas moderadas; desvío persistente exige corrección | 10–25 si falta todo |
| Opcional DC | 1 registrador de Wh con shunt | ±2% objetivo; rango y corriente acordes, registra tensión y corriente | Verificar consumo del propio instrumento y resolución; no sirve para mW si su umbral es alto | 15–40 |
| Opcional de campo | Nivel de manguera / nivel óptico prestado | Desnivel acumulado objetivo ±5% | Eliminar burbujas; repetir en sentido inverso; GPS de teléfono puede ser inadecuado para saltos pequeños | 10–30 / préstamo |
| Alquilar o pedir prestado | Pinza con captura de arranque, analizador AC, medidor de aislamiento | Según motor y red; equipo apto para categoría de instalación | Operador competente, no improvisar mediciones dentro de tableros | Cotizar |
| Alquilar si se escala | Piranómetro, caudalímetro, anemómetro con registro, topografía | Radiación ~5% o mejor; caudal ~5%; viento ±0,2 m/s deseable | Certificado/rango y montaje importan más que pantalla; un luxómetro no mide irradiancia solar útil | Cotizar |

Un conjunto inicial de medidor AC, multímetro, sondas y recipiente se provisiona en **USD 45–115** si no se tiene nada. No es necesario adquirir todos los opcionales. Para diferencias pequeñas entre tratamientos, mejorar instrumentos o prolongar la medición en vez de declarar una mejora menor que el error.

## Primera prueba de recurso: agua y desnivel

**Objetivo:** obtener un dato de caudal puntual, sin modificar cauces. Material: recipiente graduado, cronómetro, libreta; salida existente de agua con permiso y acceso desde suelo firme. Si eso no existe, no forzar este método.

1. Colocar el recipiente sin entrar al agua ni acercarse a un borde inestable. Si la descarga desborda o es difícil de controlar, detener el ensayo.
2. Medir tiempo para un volumen conocido cinco veces. Registrar cada volumen y tiempo; calcular cada `Q = litros / segundos` y su dispersión.
3. Ejemplo **estimación**, no medición: 10 L en 5 s = 2 L/s. Mejor 20 L en 10 s para reducir error relativo de reacción.
4. Reconocer el desnivel por medios seguros; reservar topografía si se necesita bajar una ladera. No presurizar una manguera improvisada para medirlo.
5. Calcular una banda de potencia con altura neta y eta supuestas; marcarla como pendiente de validar. Repetir en estiaje.

**Conclusión permitida:** caudal aproximado en esa salida y ese momento. **No concluye:** producción anual, caudal legalmente derivable, estabilidad de ladera o potencia de una turbina concreta.

## Primera construcción: calor solar con control

Prueba propuesta de baja complejidad, **sin desembolso solo si ya existen** dos recipientes iguales de metal o material apto para la temperatura, 2 L de agua, soporte estable, cobertura exterior negra/removible, dos termómetros, báscula o jarra y cronómetro. No usar recipientes de químicos ni agua destinada a beber.

1. Poner 1,00 kg de agua en cada recipiente abierto, con igual temperatura inicial. Usar el mismo soporte y posición solar sin concentradores ni vidrio que pueda romperse.
2. Oscurecer solo el exterior de uno; mantener el otro como control. No cerrar herméticamente. No mezclar color de recipiente con distinta tapa, volumen o aislamiento.
3. Registrar temperatura ambiente y del agua cada 5 minutos durante 60–120 minutos; mezclar suavemente antes de cada lectura, de la misma manera en ambos.
4. Detener a 45 °C o si el recipiente se deteriora. No hay esterilización ni garantía sanitaria por esta prueba.
5. Repetir al menos tres pares de ensayos alternando posiciones y, si se puede, la cobertura entre recipientes.
6. Calcular `E_agua = m × 4,186 × ΔT / 3600` en kWh. Para 1 kg y 10 °C: 0,01163 kWh = 11,63 Wh térmicos. Restar el control si se busca la ganancia atribuible al tratamiento.

Una diferencia de 2 °C con sondas de ±0,5 °C requiere repetir y revisar sesgo. No calcular eficiencia solar sin medir irradiancia sobre el área durante el mismo intervalo. El calor del recipiente y las pérdidas al ambiente no están en la simple energía del agua.

## Medir energía correctamente

- DC: medir V e I simultáneos bajo carga; integrar `E_Wh = suma(P_W × Δt_h)`. Con muestras puntuales se puede usar la regla trapezoidal entre tiempos. Un registro cada 1–5 s sirve para bancos variables; ciclos lentos pueden registrarse por minuto si se justifica.
- AC: usar potencia activa. Para una carga monofásica `P = Vrms × Irms × factor_de_potencia_real`; con formas distorsionadas, no sustituirlo por solo coseno de desfase. El medidor debe medir W reales.
- Comparar entrada y salida en el mismo intervalo y en fronteras definidas: panel → regulador, regulador → batería, batería → inversor, inversor → carga. No atribuir toda caída a un componente sin medir sus dos extremos.
- Registrar ventiladores, bombas, controladores y consumo del registrador. La energía del bombeo de un banco de agua recirculada es una entrada.
- Anotar almacenamiento inicial/final. Para un sistema sin otras entradas: `E_generada = E_cargas + E_auxiliares + E_pérdidas + E_no_aprovechada + ΔE_almacenada`. Si la batería termina más descargada, parte del servicio vino de su energía inicial.
- Un voltaje alto en circuito abierto no prueba energía útil. Un LED iluminado tampoco cuantifica Wh.

## Herramientas gratuitas: una por necesidad

| Necesidad | Elección | Disponibilidad/licencia verificadas al 2026-10-15 | Requisitos y uso |
|---|---|---|---|
| Registro manual y cálculos simples | LibreOffice Calc, opcional; también sirve la bitácora Markdown | [LibreOffice: MPL 2.0](https://www.libreoffice.org/licenses/); [requisitos actuales](https://www.libreoffice.org/system-requirements/) | Windows 10/11, macOS 11+ o Linux compatible según distribución publicada; no requiere Java para cálculos ordinarios; sin instalación aquí |
| Radiación y producción por lugar | PVGIS del JRC, empezar con rama 5.3 documentada | [Acceso gratuito sin registro](https://joint-research-centre.ec.europa.eu/photovoltaic-geographical-information-system-pvgis_en); [condiciones de uso](https://joint-research-centre.ec.europa.eu/photovoltaic-geographical-information-system-pvgis/general-information/usage-conditions-data-protection_en?prefLang=mt): información gratuita sin restricciones de uso | Navegador e internet; registrar versión, coordenadas, base de datos, años y horizonte. Existe una rama 6/beta anunciada; no mezclar versiones sin anotarlo |
| Simulación de energía | Python 3, script incluido, sin paquetes externos | [Python y bibliotecas estándar bajo licencia Python/PSF](https://policies.python.org/python.org/Legal-Statements/); ejecución real aquí con **3.12.14** | Script requiere Python ≥3.10 y pocos MB; sin internet para reproducir las series sintéticas |
| Circuitos, solo cuando haga falta | ngspice | [Versión estable 47 publicada en descargas](https://ngspice.sourceforge.io/download.html); [licencia BSD modificada salvo componentes indicados](https://ngspice.sourceforge.io/devel.html) | Windows 64-bit 10+, Linux o macOS con paquete correspondiente; **no instalado aquí**, por lo que no se ejecutó SPICE |

No hace falta instalar los cuatro para empezar. Cuaderno y medidores bastan para el primer ensayo. PVGIS estima recurso histórico; no mide la sombra de un árbol que falte en el modelo del terreno. No se ha asignado una climatología a tu vivienda.

## Simulación realmente ejecutada

Ejecutar desde la carpeta del paquete:

```bash
python3 modelo/simular.py
```

En Windows con el lanzador instalado: `py -3 modelo/simular.py`. Alternativamente: `python modelo/simular.py`. El script acepta una ruta JSON de entradas y una carpeta de salida. No instala nada ni realiza peticiones externas.

Incluye 11 casos de despacho horario, balances de energía, sensibilidad por degradación de batería, pérdidas de conducción, costos condicionales a 10 años y un barrido de carga de un generador ideal de Thévenin. Este último usa fuente de 6 V y resistencia interna de 10 ohmios: máximo 0,9 W en 10 ohmios; no es un modelo validado de panel fotovoltaico.

La batería se inicia sin energía utilizable adicional a su reserva y se deja evolucionar durante 30 días previos; luego se evalúan otros 30. Se documentan las energías inicial y final. El script verifica conservación de energía y el caso límite sin generación ni energía inicial. Residuo máximo del balance observado: menos de 3×10^-12 kWh, redondeo numérico. Eso valida la contabilidad del modelo, **no el comportamiento físico**.

Limitaciones: intervalo de 1 h, perfil de nevera promediado, rendimientos constantes, sin tensión, corriente de arranque, temperatura, envejecimiento dinámico, tormentas, hidráulica transitoria ni estrategia real del BMS. Las guías de potencia requieren esas verificaciones por separado.
