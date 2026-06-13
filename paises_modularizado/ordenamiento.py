# ==============================
# Funciones de ordenamiento
# ==============================

def ordenar_paises(paises, criterio, descendente):
    """
    Ordena una lista de países según el criterio indicado.
    Devuelve una nueva lista ordenada sin modificar la lista original.
    """

    # sorted() genera una nueva lista ordenada.
    # key indica qué dato del diccionario se usa para ordenar.
    # reverse indica si el orden será ascendente o descendente.
    return sorted(paises, key=lambda pais: pais[criterio], reverse=descendente)
