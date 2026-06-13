import constantes

# ==============================
# Funciones de búsqueda y selección
# ==============================

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
            print(constantes.MENSAJE_OPCION_INVALIDA)

        except ValueError:
            # Si el usuario ingresa algo que no puede convertirse a entero
            print(constantes.MENSAJE_OPCION_INVALIDA)
