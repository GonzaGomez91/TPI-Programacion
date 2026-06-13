from constantes import (
    ERROR_CAMPO_INGRESADO_VACIO,
    ERROR_NUMERO_INVALIDO,
    ERROR_NUMERO_NO_POSITIVO,
    ERROR_RANGO_INVALIDO,
    MENSAJE_OPCION_INVALIDA,
    CONFIRMAR_GUARDADO_CON_ERRORES
)

# =================================
# Funciones de validación y entrada
# =================================

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
