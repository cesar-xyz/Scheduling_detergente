# Scheduling para Planta de Embotellado de Detergente

Este proyecto implementa un modelo de scheduling para una planta de embotellado de detergente, gestionando la secuencia de producción a través de varias estaciones de trabajo (lavado, llenado, sellado, etiquetado y empaquetado).

## Estructura del Proyecto

El proyecto está dividido en las siguientes clases y archivos:

1. `Estacion`: Representa una estación de trabajo en la planta.
2. `Demanda`: Representa una demanda de producción.
3. `Planificador`: Gestiona la programación de la producción en las estaciones.
4. `main.py`: Contiene la ejecución principal del programa.

## Clases y Métodos

### Clase `Estacion`

Esta clase representa una estación de trabajo en la planta y contiene los métodos para procesar y desprocesar botellas.

#### Atributos:
- `id`: Identificador único de la estación.
- `nombre`: Nombre de la estación.
- `capacidad`: Capacidad de procesamiento de la estación.
- `tiempo_procesamiento`: Tiempo de procesamiento por botella (en segundos).
- `ocupacion`: Número de botellas procesadas actualmente.

#### Métodos:
- `procesar_botellas(cantidad, fecha_inicio)`: Procesa una cantidad específica de botellas, comenzando en `fecha_inicio`. Devuelve si fue posible procesar todas las botellas, la cantidad procesada y la fecha de finalización del procesamiento.
- `desprocesar_botellas(cantidad)`: Desprocesa una cantidad específica de botellas.

### Clase `Demanda`

Esta clase representa una demanda de producción.

#### Atributos:
- `producto`: Producto a ser producido.
- `cantidad`: Cantidad de producto a ser producido.
- `fecha_inicio`: Fecha y hora de inicio de la producción.

### Clase `Planificador`

Esta clase gestiona la programación de la producción a través de las estaciones disponibles.

#### Métodos:
- `agregar_estacion(estacion)`: Agrega una estación a la lista de estaciones del planificador.
- `programar_manual(demanda, estacion_id)`: Programa manualmente una demanda en una estación específica.
- `desprogramar_manual(demanda, estacion_id)`: Desprograma manualmente una demanda en una estación específica.
- `programar_automatico(lista_demandas)`: Programa automáticamente una lista de demandas en las estaciones disponibles y devuelve una secuencia de producción.

### Ejecución Principal (`main.py`)

El archivo `main.py` contiene la ejecución principal del programa. Realiza lo siguiente:

1. Crea las estaciones de trabajo.
2. Inicializa el planificador y agrega las estaciones.
3. Crea una demanda de producción.
4. Programa manualmente y desprograma la demanda.
5. Programa automáticamente una lista de demandas y muestra la secuencia de producción.

