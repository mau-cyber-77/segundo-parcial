"""
Un conductor necesita conocer el rendimiento de combustible de su vehículo y el costo de un recorrido. El 
usuario deberá proporcionar la distancia recorrida en kilómetros y la cantidad de litros consumidos. El 
precio por litro será de $24.00. 
El programa deberá realizar los cálculos necesarios y presentar la siguiente información: 
• Distancia recorrida en kilómetros. 
• Cantidad de litros consumidos. 
• Precio por litro de combustible. 
• Rendimiento del vehículo en kilómetros por litro. 
• Costo total del combustible consumido. 
"""
#Funciones obligatorias: leerDatos, calcularRendimiento, calcularCosto, mostrarResultados.
# La función que presenta los resultados deberá utilizar tabulate.
#la única biblioteca externa permitida es tabulate.



def leerDatos():
    while True:
        try:
            distancia = float(input("Ingrese la distancia recorrida en kilómetros: "))
            if distancia < 0:
                print("La distancia no puede ser negativa. Intente nuevamente.")
                continue
            litros = float(input("Ingrese la cantidad de litros consumidos: "))
            if litros < 0:
                print("La cantidad de litros no puede ser negativa. Intente nuevamente.")
                continue
            return distancia, litros
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")

def calcularRendimiento(distancia, litros):
    if litros == 0:
        return 0
    return distancia / litros   

def calcularCosto(litros):
    precio_por_litro = 24.00
    return litros * precio_por_litro

def mostrarResultados(distancia, litros, rendimiento, costo):
    print("Resultados del cálculo de combustible:")
    print(f"Distancia recorrida: {distancia} km")
    print(f"Litros consumidos: {litros} L")
    print(f"Rendimiento: {rendimiento} km/L")
    print(f"Costo total: ${costo:.2f}")
