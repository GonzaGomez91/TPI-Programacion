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
ERROR_RANGO_INVALIDO = "Error: el valor mínimo no puede ser mayor que el valor máximo."

ADVERTENCIA_NO_HAY_PAISES = "Advertencia: no se cargaron países desde el archivo CSV."
ADVERTENCIA_CSV_CON_ERRORES = "Advertencia: algunos países del CSV tenían errores y no fueron cargados."
ADVERTENCIA_GUARDADO_LIMPIEZA = "Si guarda los cambios, los países con errores serán eliminados del archivo CSV."

MENSAJE_NO_HAY_PAISES = "No hay países para mostrar."
MENSAJE_OPCION_INVALIDA = "Opción inválida. Intente nuevamente."
MENSAJE_SALIDA = "Saliendo del programa..."
MENSAJE_ACTUALIZACION_CANCELADA = "Actualización cancelada."
MENSAJE_PAIS_ACTUALIZADO = "País actualizado correctamente."
MENSAJE_SIN_RESULTADOS = "No se encontraron países con ese criterio."
MENSAJE_VOLVER_MENU = "Volviendo al menú principal..."
MENSAJE_ESTADISTICAS = "===== Estadísticas de países ====="
MENSAJE_CAMBIOS_GUARDADOS = "Cambios guardados correctamente."
MENSAJE_RECOMENDACION_CSV = "Puede corregir el CSV manualmente y volver a abrir el programa, o guardar para limpiar el archivo."
MENSAJE_GUARDADO_CANCELADO = "Guardado cancelado."

CONFIRMAR_GUARDADO_CON_ERRORES = "El CSV tenía errores. Si continúa, se guardarán solo los países válidos. ¿Desea continuar? (s/n): "

#=== Funciones de Menú ===

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
    print("8. Guardar cambios y salir")
    print("0. Salir sin guardar")

def mostrar_menu_filtros():
    """
    Muestra el submenú de filtros disponibles.
    """

    print("\n===== Filtrar países =====")
    print("1. Filtrar por continente")
    print("2. Filtrar por rango de población")
    print("3. Filtrar por rango de superficie")
    print("0. Volver al menú principal")

def mostrar_menu_ordenamientos():
    """
    Muestra el submenú de opciones de ordenamiento.
    """

    print("\n===== Ordenar países =====")
    print("1. Ordenar por nombre")
    print("2. Ordenar por población")
    print("3. Ordenar por superficie")
    print("0. Volver al menú principal")

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

def pedir_rango(mensaje_minimo, mensaje_maximo):
    """
    Solicita un rango numérico válido.
    Devuelve el mínimo y el máximo ingresados.
    """

    while True:
        # Se solicitan ambos valores usando la validación de enteros positivos
        minimo = pedir_entero_positivo(mensaje_minimo)
        maximo = pedir_entero_positivo(mensaje_maximo)

        # Se valida que el mínimo no sea mayor que el máximo
        if minimo <= maximo:
            return minimo, maximo

        print(ERROR_RANGO_INVALIDO)

def filtrar_por_continente(paises):
    """
    Filtra países por continente.
    No distingue entre mayúsculas y minúsculas.
    """

    resultados = []

    # Se solicita el continente y se valida que no esté vacío
    continente_buscado = pedir_texto_no_vacio("Ingrese el continente a filtrar: ").lower()

    # Se recorren los países para buscar coincidencias exactas de continente
    for pais in paises:
        if pais["continente"].lower() == continente_buscado:
            resultados.append(pais)

    # Se muestran los resultados encontrados
    if resultados:
        mostrar_paises(resultados)
    else:
        print(MENSAJE_SIN_RESULTADOS)

def filtrar_por_rango_poblacion(paises):
    """
    Filtra países cuya población esté dentro de un rango indicado por el usuario.
    """

    resultados = []

    print("\n=== Filtro por rango de población ===")

    # Se solicita un rango válido de población
    poblacion_minima, poblacion_maxima = pedir_rango(
        "Ingrese la población mínima: ",
        "Ingrese la población máxima: "
    )

    # Se recorren los países y se agregan los que estén dentro del rango
    for pais in paises:
        if poblacion_minima <= pais["poblacion"] <= poblacion_maxima:
            resultados.append(pais)

    # Se muestran los resultados encontrados
    if resultados:
        mostrar_paises(resultados)
    else:
        print(MENSAJE_SIN_RESULTADOS)

def filtrar_por_rango_superficie(paises):
    """
    Filtra países cuya superficie esté dentro de un rango indicado por el usuario.
    """

    resultados = []

    print("\n=== Filtro por rango de superficie ===")

    # Se solicita un rango válido de superficie
    superficie_minima, superficie_maxima = pedir_rango(
        "Ingrese la superficie mínima en km²: ",
        "Ingrese la superficie máxima en km²: "
    )

    # Se recorren los países y se agregan los que estén dentro del rango
    for pais in paises:
        if superficie_minima <= pais["superficie"] <= superficie_maxima:
            resultados.append(pais)

    # Se muestran los resultados encontrados
    if resultados:
        mostrar_paises(resultados)
    else:
        print(MENSAJE_SIN_RESULTADOS)

def pedir_tipo_orden():
    """
    Solicita al usuario el tipo de ordenamiento.
    Devuelve False para ascendente y True para descendente.
    """

    while True:
        print("\nSeleccione el tipo de orden:")
        print("1. Ascendente")
        print("2. Descendente")

        # Se solicita la opción y se eliminan espacios innecesarios
        opcion = input("Seleccione una opción: ").strip()

        # En sorted(), reverse=False indica orden ascendente
        if opcion == "1":
            return False

        # En sorted(), reverse=True indica orden descendente
        elif opcion == "2":
            return True

        else:
            print(MENSAJE_OPCION_INVALIDA)

def ordenar_paises(paises, criterio, descendente):
    """
    Ordena una lista de países según el criterio indicado.
    Devuelve una nueva lista ordenada sin modificar la lista original.
    """

    # sorted() genera una nueva lista ordenada.
    # key indica qué dato del diccionario se usa para ordenar.
    # reverse indica si el orden será ascendente o descendente.
    return sorted(paises, key=lambda pais: pais[criterio], reverse=descendente)


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

def obtener_pais_extremo(paises, campo, buscar_maximo=True):
    """
    Devuelve el país con el valor máximo o mínimo de un campo numérico.
    """

    # Si buscar_maximo es True, se devuelve el país con el valor más alto
    if buscar_maximo:
        return max(paises, key=lambda pais: pais[campo])

    # Si buscar_maximo es False, se devuelve el país con el valor más bajo
    return min(paises, key=lambda pais: pais[campo])

def calcular_promedio(paises, campo):
    """
    Calcula y devuelve el promedio de un campo numérico de los países.
    Por ejemplo: población o superficie.
    """

    total = 0

    # Se recorre la lista de países acumulando el valor del campo indicado
    for pais in paises:
        total += pais[campo]

    # Se divide el total por la cantidad de países
    return total / len(paises)

def contar_paises_por_continente(paises):
    """
    Cuenta cuántos países hay por cada continente.
    Devuelve un diccionario con el continente como clave y la cantidad como valor.
    """

    cantidades = {}

    # Se recorre la lista de países
    for pais in paises:
        continente = pais["continente"]

        # Si el continente no existe en el diccionario, se inicializa en 0
        if continente not in cantidades:
            cantidades[continente] = 0

        # Se suma un país al continente correspondiente
        cantidades[continente] += 1

    return cantidades

def confirmar_guardado_con_errores():
    """
    Solicita confirmación al usuario antes de guardar cuando el CSV tenía errores.
    Devuelve True si el usuario confirma y False si cancela.
    """

    while True:
        # Se pide confirmación porque guardar eliminará los registros inválidos del CSV
        respuesta = input(CONFIRMAR_GUARDADO_CON_ERRORES).strip().lower()

        if respuesta == "s":
            return True

        elif respuesta == "n":
            return False

        else:
            print(MENSAJE_OPCION_INVALIDA)


#=== Funciones Principales ===


def cargar_paises(nombre_archivo):
    """
    Lee el archivo CSV y devuelve una lista de diccionarios.
    Cada diccionario representa un país.
    """
    
    paises = []
    hubo_errores_csv = False
    try:
        
        with open(nombre_archivo, mode='r', encoding='utf-8', newline='') as archivo: # Abrir el archivo CSV en modo lectura con codificación UTF-8
            lector = csv.DictReader(archivo) # Crear un lector de CSV que devuelve cada fila como un diccionario
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
    
def opcion_agregar_pais(paises):
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

def opcion_actualizar_pais(paises):
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

def opcion_filtrar_paises(paises):
    """
    Permite elegir y ejecutar un filtro sobre la lista de países.
    """

    opcion = ""

    # El submenú se repite hasta que el usuario elija volver
    while opcion != "0":
        mostrar_menu_filtros()

        # Se solicita la opción del submenú
        opcion = input("Seleccione una opción de filtro: ").strip()

        if opcion == "1":
            filtrar_por_continente(paises)

        elif opcion == "2":
            filtrar_por_rango_poblacion(paises)

        elif opcion == "3":
            filtrar_por_rango_superficie(paises)

        elif opcion == "0":
            print(MENSAJE_VOLVER_MENU)

        else:
            print(MENSAJE_OPCION_INVALIDA)

        # Pausa para leer el resultado antes de volver al submenú
        if opcion != "0":
            input("\nPresione Enter para continuar...")

def opcion_ordenar_paises(paises):
    """
    Permite elegir un criterio de ordenamiento y muestra los países ordenados.
    """

    opcion = ""

    # El submenú se repite hasta que el usuario elija volver
    while opcion != "0":
        mostrar_menu_ordenamientos()

        # Se solicita la opción del submenú
        opcion = input("Seleccione una opción de ordenamiento: ").strip()

        if opcion == "1":
            # Se pide si el orden será ascendente o descendente
            descendente = pedir_tipo_orden()

            # Se ordenan los países por nombre
            paises_ordenados = ordenar_paises(paises, "nombre", descendente)

            print("\nPaíses ordenados por nombre:")
            mostrar_paises(paises_ordenados)

        elif opcion == "2":
            # Se pide si el orden será ascendente o descendente
            descendente = pedir_tipo_orden()

            # Se ordenan los países por población
            paises_ordenados = ordenar_paises(paises, "poblacion", descendente)

            print("\nPaíses ordenados por población:")
            mostrar_paises(paises_ordenados)

        elif opcion == "3":
            # Se pide si el orden será ascendente o descendente
            descendente = pedir_tipo_orden()

            # Se ordenan los países por superficie
            paises_ordenados = ordenar_paises(paises, "superficie", descendente)

            print("\nPaíses ordenados por superficie:")
            mostrar_paises(paises_ordenados)

        elif opcion == "0":
            print(MENSAJE_VOLVER_MENU)

        else:
            print(MENSAJE_OPCION_INVALIDA)

        # Pausa para que el usuario pueda leer los resultados antes de volver al submenú
        if opcion != "0":
            input("\nPresione Enter para continuar...")

def opcion_mostrar_estadisticas(paises):
    """
    Muestra estadísticas generales sobre los países cargados.
    """

    # Si no hay países cargados, no se pueden calcular estadísticas
    if not paises:
        print(MENSAJE_NO_HAY_PAISES)
        return

    # Se obtienen los datos estadísticos usando funciones auxiliares

    pais_mayor_poblacion = obtener_pais_extremo(paises, "poblacion", True)
    pais_menor_poblacion = obtener_pais_extremo(paises, "poblacion", False)
    promedio_poblacion = calcular_promedio(paises, "poblacion")
    promedio_superficie = calcular_promedio(paises, "superficie")
    cantidades_por_continente = contar_paises_por_continente(paises)

    print(f"\n{MENSAJE_ESTADISTICAS}")

    print("\nPaís con mayor población:")
    mostrar_pais(pais_mayor_poblacion)

    print("\nPaís con menor población:")
    mostrar_pais(pais_menor_poblacion)

    print("\nPromedios:")
    print(f"Promedio de población: {promedio_poblacion:.2f}")
    print(f"Promedio de superficie: {promedio_superficie:.2f} km²")

    print("\nCantidad de países por continente:")

    # Se recorre el diccionario de cantidades para mostrar cada continente
    for continente, cantidad in cantidades_por_continente.items():
        print(f"{continente}: {cantidad}")


def opcion_mostrar_paises(paises):
    """
    Muestra todos los países cargados en el sistema.
    """

    print("\n=== Lista de países ===")
    mostrar_paises(paises)


def opcion_guardar_salir(nombre_archivo, paises):
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

    except PermissionError:
        # Este error puede ocurrir si el archivo CSV está abierto en Excel u otro programa
        print("Error: no se pudo guardar el archivo. Verifique que no esté abierto en otro programa.")



def main():
    """
    Ejecuta el programa principal.
    Carga los países desde el CSV y muestra el menú de opciones.
    """
    
    # Se cargan los países desde el archivo CSV al iniciar el programa
    paises, hubo_errores_csv = cargar_paises(ARCHIVO_CSV)

    # Se inicializa la opción con un valor distinto de "0" para entrar al bucle
    opcion = ""

    # El menú se repite hasta que el usuario elija salir
    while opcion != "0" and opcion != "8":
        mostrar_menu()

        # Se solicita una opción y se eliminan espacios innecesarios
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            opcion_agregar_pais(paises)

        elif opcion == "2":
            opcion_actualizar_pais(paises)

        elif opcion == "3":
            opcion_buscar_pais(paises)

        elif opcion == "4":
            opcion_filtrar_paises(paises)

        elif opcion == "5":
            opcion_ordenar_paises(paises)

        elif opcion == "6":
            opcion_mostrar_estadisticas(paises)

        elif opcion == "7":
            opcion_mostrar_paises(paises)

        elif opcion == "8":
            # Si el CSV tenía errores, se pide confirmación antes de sobrescribir el archivo
            if hubo_errores_csv:
                confirmar = confirmar_guardado_con_errores()

                if confirmar:
                    opcion_guardar_salir(ARCHIVO_CSV, paises)
                else:
                    print(MENSAJE_GUARDADO_CANCELADO)
                    opcion = ""

            else:
                # Si no hubo errores en la carga, se guarda normalmente
                opcion_guardar_salir(ARCHIVO_CSV, paises)

        elif opcion == "0":
            print(MENSAJE_SALIDA)

        else:
            print(MENSAJE_OPCION_INVALIDA)

        # Pausa para que el usuario pueda leer el resultado antes de volver al menú
        if opcion != "0" and opcion != "8":
            input("\nPresione Enter para continuar...")

# Punto de entrada
main()