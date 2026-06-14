# Trabajo Práctico Integrador - Gestión de Datos de Países
Trabajo Práctico Integrador de **Programación 1**.

## Descripción del proyecto

Este proyecto consiste en una aplicación de consola desarrollada en Python para gestionar información sobre países.

El sistema permite cargar datos desde un archivo CSV, agregar nuevos países, actualizar información, realizar búsquedas, aplicar filtros, ordenar resultados y calcular estadísticas básicas.

El objetivo del trabajo es aplicar los contenidos vistos en Programación 1, especialmente:

- Listas
- Diccionarios
- Funciones
- Condicionales
- Estructuras repetitivas
- Manejo de archivos CSV
- Validaciones


## Integrantes

- Gonzalo Hernan Gómez
- Ana Laura Mansilla

## Tecnologías utilizadas

- Python 3.x
- Archivos CSV
- GitHub

## Estructura del proyecto

```text
tpi-programacion/
│
├── main.py
├── archivo_csv.py
├── busqueda.py
├── constantes.py
├── estadisticas.py
├── filtros.py
├── menus.py
├── opciones.py
├── ordenamiento.py
├── validaciones.py
├── visualizacion.py
├── paises.csv
├── README.md
└── informe.pdf
```

## Formato del archivo CSV

El archivo `paises.csv` debe estar ubicado en la raíz del proyecto y debe tener el siguiente formato:

```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
Japón,125800000,377975,Asia
Brasil,213993437,8515767,América
Alemania,83149300,357022,Europa
```

Cada país contiene los siguientes datos:

| Campo | Tipo de dato | Descripción |
|---|---|---|
| `nombre` | Texto | Nombre del país |
| `poblacion` | Entero | Cantidad de habitantes |
| `superficie` | Entero | Superficie del país en km² |
| `continente` | Texto | Continente al que pertenece |

## Funcionalidades principales

El programa permite:

- Cargar países desde un archivo CSV.
- Agregar un nuevo país.
- Actualizar la población y superficie de un país existente.
- Buscar países por nombre con coincidencia parcial.
- Filtrar países por continente.
- Filtrar países por rango de población.
- Filtrar países por rango de superficie.
- Ordenar países por nombre, población o superficie en orden ascendente o descendente.
- Mostrar estadísticas generales.
- Guardar cambios en el archivo CSV.
- Salir sin guardar cambios.

## Validaciones implementadas

El sistema incluye validaciones para evitar errores durante la ejecución:

- Archivo CSV inexistente.
- Columnas faltantes en el CSV.
- Campos vacíos en el CSV.
- Valores numéricos inválidos en población o superficie.
- Entradas vacías ingresadas por el usuario.
- Números inválidos.
- Números menores o iguales a cero al agregar o actualizar países.
- Países duplicados al agregar.
- Opciones inválidas en menús y submenús.
- Confirmación antes de guardar cuando el CSV original tenía errores.

## Cómo ejecutar el programa

1. Clonar o descargar el repositorio.

```bash
git clone URL_DEL_REPOSITORIO
```

2. Ingresar a la carpeta del proyecto.

```bash
cd tpi-programacion
```

3. Ejecutar el programa.

```bash
python main.py
```

También puede ejecutarse con:

```bash
python3 main.py
```

según la configuración del sistema operativo.

## Menú principal

Al iniciar el programa se muestra el siguiente menú:

```text
===== Gestión de Datos de Países =====
1. Agregar país
2. Actualizar país
3. Buscar país por nombre
4. Filtrar países
5. Ordenar países
6. Mostrar estadísticas
7. Mostrar todos los países
8. Guardar cambios y salir
0. Salir sin guardar
```

## Ejemplos de uso

### Buscar país por nombre

Entrada:

```text
Ingrese el nombre del país a buscar: arg
```

Salida esperada:

```text
Países encontrados:
----------------------------------------
Nombre: Argentina
Población: 45376763
Superficie: 2780400 km²
Continente: América
```

### Agregar país

Entrada:

```text
Ingrese el nombre del país: Perú
Ingrese la población: 33715471
Ingrese la superficie en km²: 1285216
Ingrese el continente: América
```

Salida esperada:

```text
País agregado correctamente.
```

### Actualizar país

Entrada:

```text
Ingrese el nombre o parte del nombre del país a actualizar: arg
Ingrese la nueva población: 46000000
Ingrese la nueva superficie en km²: 2780400
```

Salida esperada:

```text
País actualizado correctamente.
```

### Filtrar por continente

Entrada:

```text
Ingrese el continente a filtrar: América
```

Salida esperada:

```text
----------------------------------------
Nombre: Argentina
Población: 45376763
Superficie: 2780400 km²
Continente: América
```

### Filtrar por rango de población

Entrada:

```text
Ingrese la población mínima: 10000000
Ingrese la población máxima: 100000000
```

Salida esperada:

```text
Se muestran los países cuya población está dentro del rango indicado.
```

### Ordenar por población descendente

Entrada:

```text
Ordenar por población
Tipo de orden: Descendente
```

Salida esperada:

```text
Países ordenados por población:
...
```

### Mostrar estadísticas

Salida esperada:

```text
===== Estadísticas de países =====

País con mayor población:
...

País con menor población:
...

Promedios:
Promedio de población: ...
Promedio de superficie: ...

Cantidad de países por continente:
América: ...
Europa: ...
Asia: ...
```

## Decisiones técnicas

El sistema utiliza una **lista de diccionarios** para representar el conjunto de países.

Cada país se almacena como un diccionario con la siguiente estructura:

```python
pais = {
    "nombre": "Argentina",
    "poblacion": 45376763,
    "superficie": 2780400,
    "continente": "América"
}
```

La lista completa de países tiene esta forma:

```python
paises = [
    {
        "nombre": "Argentina",
        "poblacion": 45376763,
        "superficie": 2780400,
        "continente": "América"
    },
    {
        "nombre": "Japón",
        "poblacion": 125800000,
        "superficie": 377975,
        "continente": "Asia"
    }
]
```

Los datos se cargan desde un archivo CSV al iniciar el programa. Durante la ejecución, los cambios se mantienen en memoria.

Si el usuario selecciona **Guardar cambios y salir**, la lista actual de países se escribe nuevamente en el archivo CSV. Si selecciona **Salir sin guardar**, los cambios realizados durante la ejecución se descartan.

Cuando el CSV contiene registros inválidos, el programa informa al usuario que esos países no fueron cargados. Si luego se decide guardar, el sistema solicita confirmación porque el archivo será sobrescrito únicamente con los países válidos. Esta decisión permite usar el guardado como una forma de limpiar registros inválidos del CSV, pero siempre avisando al usuario antes de hacerlo.

## Organización del código

El programa está organizado en módulos según sus responsabilidades:

- `main.py`: función principal `main()` y punto de entrada del programa.
- `constantes.py`: constantes de mensajes y nombre del archivo CSV.
- `menus.py`: funciones de menú.
- `validaciones.py`: funciones de validación y entrada.
- `visualizacion.py`: funciones para mostrar países.
- `busqueda.py`: funciones de búsqueda y selección.
- `archivo_csv.py`: funciones de carga y guardado CSV.
- `filtros.py`: funciones de filtros.
- `ordenamiento.py`: funciones de ordenamiento.
- `estadisticas.py`: funciones de estadísticas.
- `opciones.py`: funciones asociadas a las opciones del menú.

Esta organización permite que cada función mantenga una responsabilidad clara y facilita la lectura, mantenimiento y prueba del código.

## Capturas de pantalla

Las capturas de pantalla se encuentran en la carpeta `capturas/`.

Capturas por agregar:

- Menú principal.
- Búsqueda por nombre.
- Agregar país.
- Actualizar país.
- Filtro por continente.
- Filtro por rango de población.
- Ordenamiento.
- Estadísticas.
- Validación de error.

## Video demostrativo

Link al video demostrativo:

```text
URL_DEL_VIDEO
```

El video debe tener una duración de entre 10 y 15 minutos y mostrar el funcionamiento del sistema en consola.

## Informe PDF

Link o ubicación del informe:

```text
informe.pdf
```

## Participación de los integrantes

- Gonzalo Hernan Gómez: desarrollo de funcionalidades, validaciones,documentación y video demostrativo.

- Ana Laura Mansilla:  pruebas y revisión del código, capturas, informe, pruebas y video demostrativo.

## Estado del proyecto

Funcionalidades implementadas:

- [x] Carga de datos desde CSV
- [x] Validaciones de CSV
- [x] Agregar país
- [x] Actualizar país
- [x] Buscar país por nombre
- [x] Filtrar países
- [x] Ordenar países
- [x] Mostrar estadísticas
- [x] Guardar cambios
- [x] Salir sin guardar
- [x] Manejo básico de errores

## Enlaces

- Repositorio: [Repositorio GitHub](https://github.com/GonzaGomez91/TPI-Programacion)
- Video demostrativo: [Video demostrativo](https://youtu.be/BZjPmeeAa7I)
- Informe PDF: [Informe PDF](informe/informe.pdf)