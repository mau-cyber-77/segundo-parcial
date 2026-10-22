from ejercicios import ejercicio1_cine as ej1
from ejercicios import ejercicio2_combustible as ej2


def ejecutar_ejercicio1():
    cantidad = ej1.leerCantidad()
    precio_unitario = 75.00
    subtotal = ej1.calcularSubtotal(cantidad, precio_unitario)
    descuento = ej1.calcularDescuento(subtotal, cantidad)
    ej1.mostrarCompra(cantidad, precio_unitario, subtotal, descuento)


def ejecutar_ejercicio2():
    distancia, litros = ej2.leerDatos()
    rendimiento = ej2.calcularRendimiento(distancia, litros)
    costo = ej2.calcularCosto(litros)
    ej2.mostrarResultados(distancia, litros, rendimiento, costo)


def mostrar_menu():
    print()
    print("Seleccione un ejercicio para ejecutar:")
    print("1. Ejercicio 1: Cine")
    print("2. Ejercicio 2: Combustible")
    print("3. Salir")

def menus():
    opcion=""
    while opcion != "3":
        mostrar_menu()
        opcion = input("Ingrese el número de la opción deseada: ")
        if opcion == "1":
            ejecutar_ejercicio1()
        elif opcion == "2":
            ejecutar_ejercicio2()
        elif opcion == "3":
            print("Saliendo del programa...")
        elif opcion != "0":
            print("Opción inválida. Por favor, seleccione una opción válida.")
