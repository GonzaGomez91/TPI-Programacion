from constantes import MENSAJE_NO_HAY_PAISES

# ==============================
# Funciones de visualización
# ==============================

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
        print(MENSAJE_NO_HAY_PAISES)
    else:
        for pais in paises:
            print("-" * 40)
            mostrar_pais(pais)
