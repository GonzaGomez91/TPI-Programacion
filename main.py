import csv  

ARCHIVO_CSV = 'paises_prueba.csv'


#=== Constantes de Mensajes ===
ERROR_ARCHIVO_NO_ENCONTRADO = "Error: no se encontró el archivo {}."
ERROR_CSV_COLUMNA_FALTANTE = "Error: falta la columna {} en el archivo CSV."
ERROR_CSV_NUMERO_INVALIDO = "Error: el país {} tiene un valor numérico inválido en población o superficie."
ERROR_PAIS_CON_CAMPO_VACIO = "Error: el país {} tiene campos vacíos."

ADVERTENCIA_NO_HAY_PAISES = "Advertencia: no se cargaron países desde el archivo CSV."

MENSAJE_NO_HAY_PAISES = "No hay países para mostrar."
MENSAJE_OPCION_INVALIDA = "Opción inválida. Intente nuevamente."
MENSAJE_SALIDA = "Saliendo del programa..."

#=== Funciones Auxiliares ===

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

def mostrar_pais(pais):
    """
    Muestra los datos de un país de forma ordenada.
    """

    print(f"Nombre: {pais['nombre']}")
    print(f"Población: {pais['poblacion']}")
    print(f"Superficie: {pais['superficie']} km²")
    print(f"Continente: {pais['continente']}")

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

def buscar_paises_por_nombre(paises, nombre_buscado):
    """
    Busca países por nombre.
    Permite coincidencias parciales y no distingue entre mayúsculas y minúsculas.
    """

    resultados = []

    # Se normaliza el texto buscado para comparar sin importar mayúsculas/minúsculas
    nombre_buscado = nombre_buscado.strip().lower()

    # Se recorren todos los países cargados
    for pais in paises:
        nombre_pais = pais["nombre"].lower()

        # Si el texto buscado aparece dentro del nombre del país, se agrega a resultados
        if nombre_buscado in nombre_pais:
            resultados.append(pais)

    return resultados

#=== Funciones Principales ===
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
    


def mostrar_paises(paises):
    """
    Muestra una lista de países.
    """

    if not paises:
        print(MENSAJE_NO_HAY_PAISES)
    else:
        for pais in paises:
            print("-" * 40)
            mostrar_pais(pais)

def opcion_buscar_pais(paises):
    """
    Solicita un nombre al usuario y muestra los países encontrados.
    """

    # Se pide al usuario el texto a buscar
    nombre_buscado = input("Ingrese el nombre del país a buscar: ").strip()

    # Se valida que el usuario no haya ingresado un texto vacío
    if nombre_buscado == "":
        print("Error: debe ingresar un nombre para buscar.")
        return

    # Se buscan coincidencias parciales o exactas
    resultados = buscar_paises_por_nombre(paises, nombre_buscado)

    # Se muestran los resultados encontrados
    if resultados:
        print("\nPaíses encontrados:")
        mostrar_paises(resultados)
    else:
        print("No se encontraron países con ese nombre.")




def main():
    """
    Ejecuta el programa principal.
    Carga los países desde el CSV y muestra el menú de opciones.
    """

    # Se cargan los países desde el archivo CSV al iniciar el programa
    paises = cargar_paises(ARCHIVO_CSV)

    # Se inicializa la opción con un valor distinto de "0" para entrar al bucle
    opcion = ""

    # El menú se repite hasta que el usuario elija salir
    while opcion != "0":
        mostrar_menu()

        # Se solicita una opción y se eliminan espacios innecesarios
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            print("Funcionalidad pendiente: agregar país.")

        elif opcion == "2":
            print("Funcionalidad pendiente: actualizar país.")

        elif opcion == "3":
            opcion_buscar_pais(paises)

        elif opcion == "4":
            print("Funcionalidad pendiente: filtrar países.")

        elif opcion == "5":
            print("Funcionalidad pendiente: ordenar países.")

        elif opcion == "6":
            print("Funcionalidad pendiente: mostrar estadísticas.")

        elif opcion == "7":
            mostrar_paises(paises)

        elif opcion == "0":
            print(MENSAJE_SALIDA)

        else:
            print(MENSAJE_OPCION_INVALIDA)

        # Pausa para que el usuario pueda leer el resultado antes de volver al menú
        if opcion != "0":
            input("\nPresione Enter para continuar...")

# Punto de entrada
main()