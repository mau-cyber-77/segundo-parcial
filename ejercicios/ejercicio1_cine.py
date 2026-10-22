"""
Un cine necesita desarrollar un programa que permita determinar el importe de una compra de boletos. 
Cada boleto cuesta $75.00. El usuario deberá indicar cuántos boletos desea comprar. Cuando se adquieran 4 
boletos o más, se aplicará un descuento del 10% sobre el subtotal. Para compras menores a 4 boletos, no se 
aplicará descuento. 
El programa deberá realizar los cálculos necesarios y presentar la siguiente información: 
• Cantidad de boletos adquiridos. 
• Precio unitario del boleto. 
• Subtotal de la compra. 
• Descuento aplicado. 
• Total a pagar.

"""
#Funciones obligatorias: leerCantidad, calcularSubtotal, calcularDescuento, mostrarCompra.
#La función que presenta los resultados deberá utilizar tabulate.
#la única biblioteca externa permitida es tabulate. 


def leerCantidad():
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de boletos que desea comprar: "))
            if cantidad < 0:
                print("La cantidad de boletos no puede ser negativa. Intente nuevamente.")
            else:
                return cantidad
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

def calcularSubtotal(cantidad, precio_unitario):
    return cantidad * precio_unitario

def calcularDescuento(subtotal, cantidad):
    if cantidad >= 4:
        return subtotal * 0.1
    return 0

def mostrarCompra(cantidad, precio_unitario, subtotal, descuento):
    total = subtotal - descuento
    print("Detalles de la compra:")
    print(f"Cantidad de boletos: {cantidad}")
    print(f"Precio unitario: {precio_unitario}")
    print(f"Subtotal: {subtotal}")
    print(f"Descuento: {descuento}")
    print(f"Total a pagar: {total}")