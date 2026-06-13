import constantes
import validaciones
import visualizacion

# ==============================
# Funciones de filtros
# ==============================


def filtrar_por_continente(paises):
    """
    Filtra países por continente.
    No distingue entre mayúsculas y minúsculas.
    """

    resultados = []

    # Se solicita el continente y se valida que no esté vacío
    continente_buscado = validaciones.pedir_texto_no_vacio("Ingrese el continente a filtrar: ").lower()

    # Se recorren los países para buscar coincidencias exactas de continente
    for pais in paises:
        if pais["continente"].lower() == continente_buscado:
            resultados.append(pais)

    # Se muestran los resultados encontrados
    if resultados:
        visualizacion.mostrar_paises(resultados)
    else:
        print(constantes.MENSAJE_SIN_RESULTADOS)

def filtrar_por_rango_poblacion(paises):
    """
    Filtra países cuya población esté dentro de un rango indicado por el usuario.
    """

    resultados = []

    print("\n=== Filtro por rango de población ===")

    # Se solicita un rango válido de población
    poblacion_minima, poblacion_maxima = validaciones.pedir_rango(
        "Ingrese la población mínima: ",
        "Ingrese la población máxima: "
    )

    # Se recorren los países y se agregan los que estén dentro del rango
    for pais in paises:
        if poblacion_minima <= pais["poblacion"] <= poblacion_maxima:
            resultados.append(pais)

    # Se muestran los resultados encontrados
    if resultados:
        visualizacion.mostrar_paises(resultados)
    else:
        print(constantes.MENSAJE_SIN_RESULTADOS)

def filtrar_por_rango_superficie(paises):
    """
    Filtra países cuya superficie esté dentro de un rango indicado por el usuario.
    """

    resultados = []

    print("\n=== Filtro por rango de superficie ===")

    # Se solicita un rango válido de superficie
    superficie_minima, superficie_maxima = validaciones.pedir_rango(
        "Ingrese la superficie mínima en km²: ",
        "Ingrese la superficie máxima en km²: "
    )

    # Se recorren los países y se agregan los que estén dentro del rango
    for pais in paises:
        if superficie_minima <= pais["superficie"] <= superficie_maxima:
            resultados.append(pais)

    # Se muestran los resultados encontrados
    if resultados:
        visualizacion.mostrar_paises(resultados)
    else:
        print(constantes.MENSAJE_SIN_RESULTADOS)
