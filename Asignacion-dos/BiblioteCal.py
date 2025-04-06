# 4-Crear una calculadora usando bibliotecas.

#Importar la biblioteca math para realizar las operaciones matemáticas.
import math

#definir funciones:
def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multiplicacion(x, y):
    return x * y

def division(x, y):
    if y == 0:
        raise ValueError("No se puede dividir por cero.")
    return x / y
    
def potencia(x, y):
    return math.pow(x, y)

def raiz(x):
    if x < 0:
        raise ValueError("No se permite Raiz cuadrada de numeros negativos.")
    return math.sqrt(x)

def raiznesima(x, y):
    if x < 0 and y % 2 == 0:
        raise ValueError("No se permite Raiz n-ésima de numeros negativos.")
    return math.pow(x, 1/y)

# Función para hacer que el usuario ingrese un número del 1 a 7.
def conseguir_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: Debe ingresar un número válido.")

# Función principal
def main():
    print("Bienvenido a la calculadora de Domin Rincon")
    print("Seleccione la operación que desea realizar:")    
    print("1. suma")
    print("2. resta")
    print("3. multiplicacion")
    print("4. division")
    print("5. raiz Cuadrada")
    print("6. raiz n-ésima")
    print("7. potencia")
    print("8. salir")

    while True:
        seleccionar = int(input("Seleccione una opción (1|2|3|4|5|6|7|8): "))
        
        if seleccionar == 8:
            print("Saliendo de la calculadora...")
            break

        if seleccionar in [1, 2, 3, 4]:
            x = conseguir_numero("Ingrese el primer número: ")
            y = conseguir_numero("Ingrese el segundo número: ")
            
            try:
                if seleccionar == 1:
                    print(f"{x} + {y} = {suma(x, y)}")
                elif seleccionar == 2:
                    print(f"{x} - {y} = {resta(x, y)}")
                elif seleccionar == 3:
                    print(f"{x} * {y} = {multiplicacion(x, y)}")
                elif seleccionar == 4:
                    print(f"{x} / {y} = {division(x, y)}")
            except ValueError as e:
                print(e)
        
        elif seleccionar == 5:
            x = conseguir_numero("Ingrese un número: ")
            try:
                print(f"La raíz cuadrada de {x} = {raiz(x)}")
            except ValueError as e:
                print(e)
        
        elif seleccionar == 6:
            x = conseguir_numero("Ingrese el radicando: ")
            y = conseguir_numero("Ingrese el índice: ")
            try:
                print(f"La raíz {y}-ésima de {x} = {raiznesima(x, y)}")
            except ValueError as e:
                print(e)
        
        elif seleccionar == 7:
            x = conseguir_numero("Ingrese la base: ")
            y = conseguir_numero("Ingrese el exponente: ")
            print(f"{x} ^ {y} = {potencia(x, y)}")
        
        else:
            print("Error: Selección no válida. Por favor, elija una opción de 1 a 8.")
    
if __name__ == "__main__":
    main()
