import csv  

ARCHIVO_CSV = 'paises.csv'

#=== Mensajes de error ===#
ERROR_ARCHIVO_NO_ENCONTRADO = f"Error: no se encontró el archivo {nombre_archivo}."
ERROR_CSV_NUMERO_INVALIDO = "Error: el archivo CSV contiene valores numéricos inválidos."
ERROR_CSV_COLUMNA_FALTANTE = "Error: el archivo CSV no contiene las columnas necesarias."

def cargar_paises(nombre_archivo):
    """
    Lee el archivo CSV y devuelve una lista de diccionarios.
    Cada diccionario representa un país.
    """
    
    paises = []

    try:
        
        with open(nombre_archivo, mode='r', encoding='utf-8') as archivo: # Abrir el archivo CSV en modo lectura con codificación UTF-8
            lector = csv.DictReader(archivo) # Crear un lector de CSV que devuelve cada fila como un diccionario
            for fila in lector: # Iterar sobre cada fila del CSV
                # Crear un diccionario para el país con los datos de la fila, convirtiendo los valores numéricos a enteros
                pais = {
                    "nombre": fila["nombre"],
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"]
                }
                paises.append(pais) # Agregar el diccionario del país a la lista de países
    
    except FileNotFoundError:
        print(ERROR_ARCHIVO_NO_ENCONTRADO)
    
    except ValueError:
        print(ERROR_CSV_NUMERO_INVALIDO)
    
    except KeyError as e:
        print(ERROR_CSV_COLUMNA_FALTANTE)
    
    return paises
    
