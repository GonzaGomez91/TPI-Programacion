import csv  

ARCHIVO_CSV = 'paises_prueba.csv'


#=== Constantes de Mensajes ===
ERROR_ARCHIVO_NO_ENCONTRADO = "Error: no se encontró el archivo {}."
ERROR_CSV_COLUMNA_FALTANTE = "Error: falta la columna {} en el archivo CSV."
ERROR_CSV_NUMERO_INVALIDO = "Error: el país {} tiene un valor numérico inválido en población o superficie."
ERROR_PAIS_CON_CAMPO_VACIO = "Error: el país {} tiene campos vacíos."
ERROR_CAMPO_INGRESADO_VACIO = "Error: el campo ingresado no puede estar vacío."
ERROR_NUMERO_INVALIDO = "Error: debe ingresar un número entero válido."
ERROR_NUMERO_NO_POSITIVO = "Error: el número debe ser mayor que cero."
ERROR_PAIS_EXISTENTE = "Error: ya existe un país registrado con ese nombre."
ERROR_PAIS_NO_ENCONTRADO = "Error: no se encontraron países con ese nombre."

ADVERTENCIA_NO_HAY_PAISES = "Advertencia: no se cargaron países desde el archivo CSV."

MENSAJE_NO_HAY_PAISES = "No hay países para mostrar."
MENSAJE_OPCION_INVALIDA = "Opción inválida. Intente nuevamente."
MENSAJE_SALIDA = "Saliendo del programa..."
MENSAJE_ACTUALIZACION_CANCELADA = "Actualización cancelada."
MENSAJE_PAIS_ACTUALIZADO = "País actualizado correctamente."



#=== Funciones Auxiliares ===
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

def pedir_texto_no_vacio(mensaje):
    """
    Solicita un texto al usuario y valida que no esté vacío.
    Devuelve el texto ingresado sin espacios innecesarios.
    """

    texto = input(mensaje).strip()

    # Se valida que el usuario no haya dejado el campo vacío
    while texto == "":
        print(ERROR_CAMPO_INGRESADO_VACIO)
        texto = input(mensaje).strip()

    return texto


def pedir_entero_positivo(mensaje):
    """
    Solicita un número entero positivo al usuario.
    Repite la solicitud hasta que el valor ingresado sea válido.
    """

    numero_valido = False
    numero = 0

    # Se repite hasta que el usuario ingrese un entero positivo
    while not numero_valido:
        try:
            numero = int(input(mensaje))

            # Se valida que el número sea mayor que cero
            if numero > 0:
                numero_valido = True
            else:
                print(ERROR_NUMERO_NO_POSITIVO)

        except ValueError:
            print(ERROR_NUMERO_INVALIDO)

    return numero

def existe_pais(paises, nombre):
    """
    Verifica si ya existe un país con el mismo nombre.
    La comparación no distingue entre mayúsculas y minúsculas.
    """

    # Se normaliza el nombre ingresado
    nombre = nombre.strip().lower()

    # Se recorre la lista de países para buscar coincidencia exacta
    for pais in paises:
        if pais["nombre"].lower() == nombre:
            return True

    return False

def seleccionar_pais(resultados):
    """
    Permite seleccionar un país de una lista de resultados.
    Devuelve el país seleccionado o None si el usuario cancela con 0.
    """

    print("\nSe encontraron varios países:")

    # Se muestran los países encontrados con un número de opción
    for i, pais in enumerate(resultados, start=1):
        print(f"{i}. {pais['nombre']} - {pais['continente']}")

    print("0. Cancelar")

    while True:
        try:
            # Se solicita al usuario que elija uno de los resultados
            opcion = int(input("Seleccione el número del país: "))

            # La opción 0 permite cancelar la selección
            if opcion == 0:
                return None

            # Si la opción está dentro del rango, se devuelve el país seleccionado
            if 1 <= opcion <= len(resultados):
                return resultados[opcion - 1]

            # Si el número está fuera del rango, se muestra mensaje general
            print(MENSAJE_OPCION_INVALIDA)

        except ValueError:
            # Si el usuario ingresa algo que no puede convertirse a entero
            print(MENSAJE_OPCION_INVALIDA)

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

def agregar_pais(paises):
    """
    Solicita los datos de un país y lo agrega a la lista de países.
    """

    print("\n=== Agregar país ===")

       # Se solicita el nombre del nuevo país
    nombre = pedir_texto_no_vacio("Ingrese el nombre del país: ")

    # Se verifica que no exista otro país con el mismo nombre
    if existe_pais(paises, nombre):
        print(ERROR_PAIS_EXISTENTE)
        return

    
    # Se solicitan los datos del nuevo país
    poblacion = pedir_entero_positivo("Ingrese la población: ")
    superficie = pedir_entero_positivo("Ingrese la superficie en km²: ")
    continente = pedir_texto_no_vacio("Ingrese el continente: ")

    # Se crea el diccionario que representa al país
    pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    # Se agrega el nuevo país a la lista principal
    paises.append(pais)

    print("País agregado correctamente.")

def actualizar_pais(paises):
    """
    Permite actualizar la población y la superficie de un país existente.
    La búsqueda permite coincidencias parciales.
    """

    print("\n=== Actualizar país ===")

    # Se solicita el nombre o parte del nombre del país a actualizar
    nombre_buscado = pedir_texto_no_vacio("Ingrese el nombre o parte del nombre del país a actualizar: ")

    # Se buscan países que coincidan parcial o totalmente con el texto ingresado
    resultados = buscar_paises_por_nombre(paises, nombre_buscado)

    # Si no se encontraron países, se informa el error y se termina la función
    if not resultados:
        print(ERROR_PAIS_NO_ENCONTRADO)
        return

    # Si hay un solo resultado, se selecciona automáticamente
    if len(resultados) == 1:
        pais = resultados[0]

    # Si hay varios resultados, se le pide al usuario que seleccione uno
    else:
        pais = seleccionar_pais(resultados)

        # Si el usuario cancela con 0, no se realiza ninguna modificación
        if pais is None:
            print(MENSAJE_ACTUALIZACION_CANCELADA)
            return

    # Se muestran los datos actuales antes de actualizarlos
    print("\nDatos actuales del país:")
    mostrar_pais(pais)

    # Se solicitan los nuevos valores usando la validación de enteros positivos
    nueva_poblacion = pedir_entero_positivo("Ingrese la nueva población: ")
    nueva_superficie = pedir_entero_positivo("Ingrese la nueva superficie en km²: ")

    # Se actualizan únicamente población y superficie, como pide la consigna
    pais["poblacion"] = nueva_poblacion
    pais["superficie"] = nueva_superficie

    print(MENSAJE_PAIS_ACTUALIZADO)

def opcion_buscar_pais(paises):
    """
    Solicita un nombre al usuario y muestra los países encontrados.
    """

   # Se solicita el nombre a buscar, validando que no esté vacío
    nombre_buscado = pedir_texto_no_vacio("Ingrese el nombre del país a buscar: ")

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
            agregar_pais(paises)

        elif opcion == "2":
            actualizar_pais(paises)

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