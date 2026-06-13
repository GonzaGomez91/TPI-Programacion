# ==============================
# Funciones de menú
# ==============================

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
