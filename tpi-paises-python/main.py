import csv  

ARCHIVO_CSV = 'paises.csv'


#=== Mensajes de error ===
ERROR_ARCHIVO_NO_ENCONTRADO = "Error: no se encontró el archivo {}."
ERROR_CSV_COLUMNA_FALTANTE = "Error: falta la columna '{}' en el archivo CSV."
ERROR_CSV_NUMERO_INVALIDO = "Error: el país '{}' tiene un valor numérico inválido en población o superficie."


#=== Funciones ===

def cargar_paises(nombre_archivo):
    """
    Lee el archivo CSV y devuelve una lista de diccionarios.
    Cada diccionario representa un país.
    """
    
    paises = []

    try:
        
        with open(nombre_archivo, mode='r', encoding='utf-8', newline='') as archivo: # Abrir el archivo CSV en modo lectura con codificación UTF-8
            lector = csv.DictReader(archivo) # Crear un lector de CSV que devuelve cada fila como un diccionario
            for fila in lector:
                try:
                    pais = {
                        "nombre": fila["nombre"],
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"]
                    }

                    paises.append(pais)

                except ValueError:
                    print(ERROR_CSV_NUMERO_INVALIDO.format(fila["nombre"]))
    
    except FileNotFoundError:
        print(ERROR_ARCHIVO_NO_ENCONTRADO.format(nombre_archivo))

    
    except KeyError as e:
        print(ERROR_CSV_COLUMNA_FALTANTE.format(e))
    
    return paises
    
