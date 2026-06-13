from constantes import (
    ARCHIVO_CSV,
    MENSAJE_SALIDA,
    MENSAJE_OPCION_INVALIDA,
    MENSAJE_GUARDADO_CANCELADO
)

from menus import mostrar_menu
from archivo_csv import cargar_paises, guardar_paises
from validaciones import confirmar_guardado_con_errores

from opciones import (
    opcion_agregar_pais,
    opcion_actualizar_pais,
    opcion_buscar_pais,
    opcion_filtrar_paises,
    opcion_ordenar_paises,
    opcion_mostrar_estadisticas,
    opcion_mostrar_paises
)

# ==============================
# Programa principal
# ==============================

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
                    guardado_correcto = guardar_paises(ARCHIVO_CSV, paises)
                    if guardado_correcto:
                        print(MENSAJE_SALIDA)
                    else:
                        opcion = ""

                else:
                    print(MENSAJE_GUARDADO_CANCELADO)
                    opcion = ""

            else:
                # Si no hubo errores en la carga, se guarda normalmente
                guardado_correcto = guardar_paises(ARCHIVO_CSV, paises)
                if guardado_correcto:
                    print(MENSAJE_SALIDA)
                else:
                    opcion = ""

        elif opcion == "0":
            print(MENSAJE_SALIDA)

        else:
            print(MENSAJE_OPCION_INVALIDA)

        # Pausa para que el usuario pueda leer el resultado antes de volver al menú
        if opcion != "0" and opcion != "8":
            input("\nPresione Enter para continuar...")

# Punto de entrada
if __name__ == "__main__":
    main()
