# ==============================
# Funciones de estadísticas
# =============================

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
