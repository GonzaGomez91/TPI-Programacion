import csv  

ARCHIVO_CSV = 'paises_prueba.csv'


#=== Constantes de error y advertencia ===
ERROR_ARCHIVO_NO_ENCONTRADO = "Error: no se encontró el archivo {}."
ERROR_CSV_COLUMNA_FALTANTE = "Error: falta la columna {} en el archivo CSV."
ERROR_CSV_NUMERO_INVALIDO = "Error: el país {} tiene un valor numérico inválido en población o superficie."
ERROR_PAIS_CON_CAMPO_VACIO = "Error: el país {} tiene campos vacíos."
ADVERTENCIA_NO_HAY_PAISES = "Advertencia: no se cargaron países desde el archivo CSV."

#=== Funciones ===

def tiene_campos_vacios(fila):
    """
    Verifica si una fila del CSV tiene algún campo vacío o incompleto.
    """
    return (
        fila["nombre"] is None or fila["nombre"].strip() == "" or
        fila["poblacion"] is None or fila["poblacion"].strip() == "" or
        fila["superficie"] is None or fila["superficie"].strip() == "" or
        fila["continente"] is None or fila["continente"].strip() == ""
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
    
    if not paises:
        print(ADVERTENCIA_NO_HAY_PAISES)

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


def mostrar_menu():
    """
    Muestra el menú principal del sistema.
    """
    print("\n===== Gestión de Datos de Países =====")
    print("1. Agregar país")
    print("2. Actualizar país")
    print("3. Buscar país por nombre")
    print("4. Filtrar países")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas")
    print("7. Mostrar todos los países")
    print("0. Salir")


def main():
    paises = cargar_paises(ARCHIVO_CSV)

    opcion = ""

    while opcion != "0":
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            print("Funcionalidad pendiente: agregar país.")

        elif opcion == "2":
            print("Funcionalidad pendiente: actualizar país.")

        elif opcion == "3":
            print("Funcionalidad pendiente: buscar país por nombre.")

        elif opcion == "4":
            print("Funcionalidad pendiente: filtrar países.")

        elif opcion == "5":
            print("Funcionalidad pendiente: ordenar países.")

        elif opcion == "6":
            print("Funcionalidad pendiente: mostrar estadísticas.")

        elif opcion == "7":
            mostrar_paises(paises)

        elif opcion == "0":
            print("Saliendo del programa...")

        else:
            print("Opción inválida. Intente nuevamente.")

        if opcion != "0":
            input("\nPresione Enter para continuar...")


main()