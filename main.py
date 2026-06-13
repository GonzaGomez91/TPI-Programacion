import archivo_csv
import constantes
import menus
import opciones
import validaciones

# ==============================
# Programa principal
# ==============================

def main():
    """
    Ejecuta el programa principal.
    Carga los países desde el CSV y muestra el menú de opciones.
    """
    
    # Se cargan los países desde el archivo CSV al iniciar el programa
    paises, hubo_errores_csv = archivo_csv.cargar_paises(constantes.ARCHIVO_CSV)

    # Se inicializa la opción con un valor distinto de "0" para entrar al bucle
    opcion = ""

    # El menú se repite hasta que el usuario elija salir
    while opcion != "0" and opcion != "8":
        menus.mostrar_menu()

        # Se solicita una opción y se eliminan espacios innecesarios
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            opciones.opcion_agregar_pais(paises)

        elif opcion == "2":
            opciones.opcion_actualizar_pais(paises)

        elif opcion == "3":
            opciones.opcion_buscar_pais(paises)

        elif opcion == "4":
            opciones.opcion_filtrar_paises(paises)

        elif opcion == "5":
            opciones.opcion_ordenar_paises(paises)

        elif opcion == "6":
            opciones.opcion_mostrar_estadisticas(paises)

        elif opcion == "7":
            opciones.opcion_mostrar_paises(paises)

        elif opcion == "8":
            # Si el CSV tenía errores, se pide confirmación antes de sobrescribir el archivo
            if hubo_errores_csv:
                confirmar = validaciones.confirmar_guardado_con_errores()

                if confirmar:
                    guardado_correcto = archivo_csv.guardar_paises(constantes.ARCHIVO_CSV, paises)
                    if guardado_correcto:
                        print(constantes.MENSAJE_SALIDA)
                    else:
                        opcion = ""


                else:
                    print(constantes.MENSAJE_GUARDADO_CANCELADO)
                    opcion = ""
                
            else:
                # Si no hubo errores en la carga, se guarda normalmente
                guardado_correcto = archivo_csv.guardar_paises(constantes.ARCHIVO_CSV, paises)
                if guardado_correcto:
                    print(constantes.MENSAJE_SALIDA)
                else:
                    opcion = ""

        elif opcion == "0":
            print(constantes.MENSAJE_SALIDA)

        else:
            print(constantes.MENSAJE_OPCION_INVALIDA)

        # Pausa para que el usuario pueda leer el resultado antes de volver al menú
        if opcion != "0" and opcion != "8":
            input("\nPresione Enter para continuar...")

# Punto de entrada
if __name__ == "__main__":
    main()