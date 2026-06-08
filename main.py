import csv  

ARCHIVO_CSV = 'paises_prueba.csv'


#=== Mensajes de error ===
ERROR_ARCHIVO_NO_ENCONTRADO = "Error: no se encontró el archivo {}."
ERROR_CSV_COLUMNA_FALTANTE = "Error: falta la columna {} en el archivo CSV."
ERROR_CSV_NUMERO_INVALIDO = "Error: el país {} tiene un valor numérico inválido en población o superficie."
ERROR_PAIS_CON_CAMPO_VACIO = "Error: el país {} tiene campos vacíos."

#=== Funciones ===

def tiene_campos_vacios(fila):
    """
    Verifica si una fila del CSV tiene algún campo vacío.
    """

    return (
        fila["nombre"].strip() == "" or
        fila["poblacion"].strip() == "" or
        fila["superficie"].strip() == "" or
        fila["continente"].strip() == ""
    )


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
                    if tiene_campos_vacios(fila):
                        print(ERROR_PAIS_CON_CAMPO_VACIO.format(fila["nombre"]))
                        continue

                    pais = {
                        "nombre": fila["nombre"].strip(),
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"].strip()
                    }

                    paises.append(pais)

                except ValueError:
                    print(ERROR_CSV_NUMERO_INVALIDO.format(fila["nombre"]))
    
    except FileNotFoundError:
        print(ERROR_ARCHIVO_NO_ENCONTRADO.format(nombre_archivo))

    
    except KeyError as e:
        print(ERROR_CSV_COLUMNA_FALTANTE.format(e))
    
    return paises
    
def mostrar_pais(pais):
    """
    Muestra los datos de un país de forma ordenada.
    """

    print(f"Nombre: {pais['nombre']}")
    print(f"Población: {pais['poblacion']}")
    print(f"Superficie: {pais['superficie']} km²")
    print(f"Continente: {pais['continente']}")


def mostrar_paises(paises):
    """
    Muestra una lista de países.
    """

    if not paises:
        print("No hay países para mostrar.")
    else:
        for pais in paises:
            print("-" * 40)
            mostrar_pais(pais)


paises = cargar_paises(ARCHIVO_CSV)
mostrar_paises(paises)