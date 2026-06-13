import csv

from constantes import (
    ERROR_ARCHIVO_NO_ENCONTRADO,
    ERROR_CSV_COLUMNA_FALTANTE,
    ERROR_CSV_NUMERO_INVALIDO,
    ERROR_PAIS_CON_CAMPO_VACIO,
    ERROR_GUARDADO_ARCHIVO,
    ADVERTENCIA_NO_HAY_PAISES,
    ADVERTENCIA_CSV_CON_ERRORES,
    ADVERTENCIA_GUARDADO_LIMPIEZA,
    MENSAJE_RECOMENDACION_CSV,
    MENSAJE_CAMBIOS_GUARDADOS
)

from validaciones import tiene_campos_vacios

# ==============================
# Funciones de archivos CSV
# ==============================

def cargar_paises(nombre_archivo):
    """
    Lee el archivo CSV y devuelve una lista de diccionarios.
    Cada diccionario representa un país.
    """

    paises = []
    hubo_errores_csv = False

    try:
        # Abrir el archivo CSV en modo lectura con codificación UTF-8
        with open(nombre_archivo, mode='r', encoding='utf-8', newline='') as archivo:

            # Crear un lector de CSV que devuelve cada fila como un diccionario
            lector = csv.DictReader(archivo)

            for fila in lector:
                try:
                    if tiene_campos_vacios(fila):
                        print(ERROR_PAIS_CON_CAMPO_VACIO.format(fila["nombre"]))
                        hubo_errores_csv = True
                        continue

                    pais = {
                        "nombre": fila["nombre"].strip(),
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"].strip()
                    }

                    paises.append(pais)

                except ValueError:
                    hubo_errores_csv = True
                    print(ERROR_CSV_NUMERO_INVALIDO.format(fila["nombre"]))

    except FileNotFoundError:
        hubo_errores_csv = True
        print(ERROR_ARCHIVO_NO_ENCONTRADO.format(nombre_archivo))

    except KeyError as e:
        hubo_errores_csv = True
        print(ERROR_CSV_COLUMNA_FALTANTE.format(e))

    if not paises:
        print(ADVERTENCIA_NO_HAY_PAISES)

    if hubo_errores_csv:
        print("=" * 100)
        print(ADVERTENCIA_CSV_CON_ERRORES)
        print(ADVERTENCIA_GUARDADO_LIMPIEZA)
        print(MENSAJE_RECOMENDACION_CSV)
        print("=" * 100)

    return paises, hubo_errores_csv

def guardar_paises(nombre_archivo, paises):
    """
    Guarda la lista de países en el archivo CSV.
    Sobrescribe el contenido anterior del archivo.
    """

    try:
        # Se abre el archivo en modo escritura para guardar todos los países actuales
        with open(nombre_archivo, mode='w', encoding='utf-8', newline='') as archivo:

            # Se definen los nombres de las columnas del CSV
            campos = ["nombre", "poblacion", "superficie", "continente"]

            # DictWriter permite escribir diccionarios en formato CSV
            escritor = csv.DictWriter(archivo, fieldnames=campos)

            # Se escribe la fila de encabezados
            escritor.writeheader()

            # Se escriben todos los países de la lista
            escritor.writerows(paises)

        print(MENSAJE_CAMBIOS_GUARDADOS)
        return True

    except PermissionError:
        # Este error puede ocurrir si el archivo CSV está abierto en Excel u otro programa
        print(ERROR_GUARDADO_ARCHIVO)
        return False
