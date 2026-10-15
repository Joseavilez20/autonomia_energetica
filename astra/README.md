# Laboratorio de autonomía energética — paquete v0.1

Preparado el **15 de octubre de 2026** para iniciar un laboratorio en una **vivienda rural con corriente de agua todo el año**, con la meta inicial de atender también **nevera y computador**. Esos tres datos fueron aportados por el usuario; los demás valores de cálculo son ilustrativos.

## Por dónde comenzar

1. Leer [00_resumen_y_decision.md](00_resumen_y_decision.md).
2. Completar el diagnóstico y medir demanda/agua con [01_diagnostico_y_recursos.md](01_diagnostico_y_recursos.md).
3. Usar [02_laboratorio_y_simulaciones.md](02_laboratorio_y_simulaciones.md) para instrumentos, primera prueba y ejecución.
4. Empezar por la [guía hidráulica](03_guia_microhidraulica.md) y comparar con la [solar fotovoltaica](03_guia_solar_fotovoltaica.md).

## Contenido completo

| Documento | Contenido |
|---|---|
| `00_resumen_y_decision.md` | Comparación, madurez, energía, costos, dependencia y decisión preliminar |
| `01_diagnostico_y_recursos.md` | Preguntas y respuestas, supuestos, demanda y campaña de medición |
| `02_laboratorio_y_simulaciones.md` | Instrumentos, primeras pruebas, software y reproducción |
| `03_guia_microhidraulica.md` | Banco, conducción, prototipo, piloto y escalamiento condicionado |
| `03_guia_solar_fotovoltaica.md` | Panel pequeño bajo carga, piloto y dimensionamiento inicial |
| `03_guia_solar_termica.md` | Calor solar, control experimental y usos térmicos |
| `03_guia_bombeo_y_almacenamiento.md` | Bombeo, ariete y almacenamiento de agua |
| `03_guia_eolica.md` | Medición y límites antes de considerar turbina |
| `03_guia_biogas.md` | Disponibilidad de residuos, ensayo y requisitos de piloto profesional |
| `03_guia_recuperacion_termica_y_experimentales.md` | TEG, sensores y otras ideas con límites físicos |
| `04_escalamiento_vivienda_y_finca.md` | Arquitectura, ocho fases, compatibilidad, autonomía y límites |
| `05_hipotesis_y_experimentos.md` | Cuatro hipótesis, controles, predicciones y topes de gasto/tiempo |
| `06_costos_mantenimiento_y_dependencias.md` | Presupuesto y comparación condicional a 10 años |
| `07_bitacora_y_resultados.md` | Plantillas listas para registrar datos reales |
| `08_fuentes_y_calculos.md` | Fuentes primarias, fórmulas, método y limitaciones |
| `modelo/simular.py` | Modelo escrito para el estudio, ejecutado con Python 3.12.14 |
| `modelo/entradas.json` | Entradas modificables, con unidades en los nombres |
| `modelo/salida/` | Resultados completos y series horarias de 11 casos |

## Reproducir

```bash
python3 modelo/simular.py
```

Sin paquetes adicionales ni acceso a internet. En Windows puede usarse `py -3 modelo/simular.py` con Python instalado.

## Estado de entrega

Los documentos solicitados se incluyen completos para una **prefactibilidad con experimentos iniciales**. No hay documentos narrativos pendientes. La bitácora contiene campos vacíos de forma intencional para capturar mediciones futuras.

**No son resultados obtenidos en tu propiedad:** caudal de 2 L/s, salto de 12 m, consumo de 2,64 kWh/día, radiación y precios del presupuesto. No se ha construido ningún prototipo ni validado una instalación.

Pendientes para una versión adaptada: país/municipio/altitud, sombras y distancias; caudal de estiaje y desnivel neto; medición de carga/arranque; presupuesto/herramientas; autonomía y respaldo aceptables; cotizaciones y requisitos locales. El diseño ejecutivo de potencia, obra, presión y gas corresponde a profesionales del lugar.
