import busqueda
import constantes
import estadisticas
import filtros
import menus
import ordenamiento
import validaciones
import visualizacion

# ==============================
# Funciones de opciones del menú
# ==============================

def opcion_agregar_pais(paises):
    """
    Solicita los datos de un país y lo agrega a la lista de países.
    """

    print("\n=== Agregar país ===")

       # Se solicita el nombre del nuevo país
    nombre = validaciones.pedir_texto_no_vacio("Ingrese el nombre del país: ")

    # Se verifica que no exista otro país con el mismo nombre
    if busqueda.existe_pais(paises, nombre):
        print(constantes.ERROR_PAIS_EXISTENTE)
        return

    
    # Se solicitan los datos del nuevo país
    poblacion = validaciones.pedir_entero_positivo("Ingrese la población: ")
    superficie = validaciones.pedir_entero_positivo("Ingrese la superficie en km²: ")
    continente = validaciones.pedir_texto_no_vacio("Ingrese el continente: ")

    # Se crea el diccionario que representa al país
    pais = {
        "nombre": nombre.capitalize(),
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente.capitalize()
    }

    # Se agrega el nuevo país a la lista principal
    paises.append(pais)

    print(constantes.MENSAJE_PAIS_AGREGADO)

def opcion_actualizar_pais(paises):
    """
    Permite actualizar la población y la superficie de un país existente.
    La búsqueda permite coincidencias parciales.
    """

    print("\n=== Actualizar país ===")

    # Se solicita el nombre o parte del nombre del país a actualizar
    nombre_buscado = validaciones.pedir_texto_no_vacio("Ingrese el nombre o parte del nombre del país a actualizar: ")

    # Se buscan países que coincidan parcial o totalmente con el texto ingresado
    resultados = busqueda.buscar_paises_por_nombre(paises, nombre_buscado)

    # Si no se encontraron países, se informa el error y se termina la función
    if not resultados:
        print(constantes.ERROR_PAIS_NO_ENCONTRADO)
        return

    # Si hay un solo resultado, se selecciona automáticamente
    if len(resultados) == 1:
        pais = resultados[0]

    # Si hay varios resultados, se le pide al usuario que seleccione uno
    else:
        pais = busqueda.seleccionar_pais(resultados)

        # Si el usuario cancela con 0, no se realiza ninguna modificación
        if pais is None:
            print(constantes.MENSAJE_ACTUALIZACION_CANCELADA)
            return

    # Se muestran los datos actuales antes de actualizarlos
    print("\nDatos actuales del país:")
    visualizacion.mostrar_pais(pais)

    # Se solicitan los nuevos valores usando la validación de enteros positivos
    nueva_poblacion = validaciones.pedir_entero_positivo("Ingrese la nueva población: ")
    nueva_superficie = validaciones.pedir_entero_positivo("Ingrese la nueva superficie en km²: ")

    # Se actualizan únicamente población y superficie, como pide la consigna
    pais["poblacion"] = nueva_poblacion
    pais["superficie"] = nueva_superficie

    print(constantes.MENSAJE_PAIS_ACTUALIZADO)

def opcion_buscar_pais(paises):
    """
    Solicita un nombre al usuario y muestra los países encontrados.
    """

   # Se solicita el nombre a buscar, validando que no esté vacío
    nombre_buscado = validaciones.pedir_texto_no_vacio("Ingrese el nombre del país a buscar: ")

    # Se buscan coincidencias parciales o exactas
    resultados = busqueda.buscar_paises_por_nombre(paises, nombre_buscado)

    # Se muestran los resultados encontrados
    if resultados:
        print("\nPaíses encontrados:")
        visualizacion.mostrar_paises(resultados)
    else:
        print(constantes.ERROR_PAIS_NO_ENCONTRADO)

def opcion_filtrar_paises(paises):
    """
    Permite elegir y ejecutar un filtro sobre la lista de países.
    """

    opcion = ""

    # El submenú se repite hasta que el usuario elija volver
    while opcion != "0":
        menus.mostrar_menu_filtros()

        # Se solicita la opción del submenú
        opcion = input("Seleccione una opción de filtro: ").strip()

        if opcion == "1":
            filtros.filtrar_por_continente(paises)

        elif opcion == "2":
            filtros.filtrar_por_rango_poblacion(paises)

        elif opcion == "3":
            filtros.filtrar_por_rango_superficie(paises)

        elif opcion == "0":
            print(constantes.MENSAJE_VOLVER_MENU)

        else:
            print(constantes.MENSAJE_OPCION_INVALIDA)

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
        menus.mostrar_menu_ordenamientos()

        # Se solicita la opción del submenú
        opcion = input("Seleccione una opción de ordenamiento: ").strip()

        if opcion == "1":
            # Se pide si el orden será ascendente o descendente
            descendente = validaciones.pedir_tipo_orden()

            # Se ordenan los países por nombre
            paises_ordenados = ordenamiento.ordenar_paises(paises, "nombre", descendente)

            print("\nPaíses ordenados por nombre:")
            visualizacion.mostrar_paises(paises_ordenados)

        elif opcion == "2":
            # Se pide si el orden será ascendente o descendente
            descendente = validaciones.pedir_tipo_orden()

            # Se ordenan los países por población
            paises_ordenados = ordenamiento.ordenar_paises(paises, "poblacion", descendente)

            print("\nPaíses ordenados por población:")
            visualizacion.mostrar_paises(paises_ordenados)

        elif opcion == "3":
            # Se pide si el orden será ascendente o descendente
            descendente = validaciones.pedir_tipo_orden()

            # Se ordenan los países por superficie
            paises_ordenados = ordenamiento.ordenar_paises(paises, "superficie", descendente)

            print("\nPaíses ordenados por superficie:")
            visualizacion.mostrar_paises(paises_ordenados)

        elif opcion == "0":
            print(constantes.MENSAJE_VOLVER_MENU)

        else:
            print(constantes.MENSAJE_OPCION_INVALIDA)

        # Pausa para que el usuario pueda leer los resultados antes de volver al submenú
        if opcion != "0":
            input("\nPresione Enter para continuar...")

def opcion_mostrar_estadisticas(paises):
    """
    Muestra estadísticas generales sobre los países cargados.
    """

    # Si no hay países cargados, no se pueden calcular estadísticas
    if not paises:
        print(constantes.MENSAJE_NO_HAY_PAISES)
        return

    # Se obtienen los datos estadísticos usando funciones auxiliares

    pais_mayor_poblacion = estadisticas.obtener_pais_extremo(paises, "poblacion", True)
    pais_menor_poblacion = estadisticas.obtener_pais_extremo(paises, "poblacion", False)
    promedio_poblacion = estadisticas.calcular_promedio(paises, "poblacion")
    promedio_superficie = estadisticas.calcular_promedio(paises, "superficie")
    cantidades_por_continente = estadisticas.contar_paises_por_continente(paises)

    print(f"\n{constantes.MENSAJE_ESTADISTICAS}")

    print("\nPaís con mayor población:")
    visualizacion.mostrar_pais(pais_mayor_poblacion)

    print("\nPaís con menor población:")
    visualizacion.mostrar_pais(pais_menor_poblacion)

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
    visualizacion.mostrar_paises(paises)
