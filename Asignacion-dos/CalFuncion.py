#3-Crear una calculadora usando funciones.
print("Bienvenido a la calculadora de Domin Rincon")

# Definición de funciones   
def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multiplicacion(x, y):
        return x * y
        
def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Operacion no permitida."
        
def potencia(x, y):
    return x ** y

def raiz(x):
    if x >= 0:
        return x ** (1/2)
    else:
        return "Error: Operacion no permitida."

def raiznesima(x, y):
    if x >= 0 and y != 0:
        return x ** (1/y)
    else:
        return "Error: Operacion no permitida."


while True:        
    while True:
        try:
            operacion = int(input("Selecione la operación que desea realizar:" 
                            "\n1. Suma\n2. Resta\n3. Multiplicacion\n4. Division\n5. Potencia\n6. Raiz cuadrada\n7. Raiz n-ésima\n8. Salir\n"))
            if operacion == 7:
                print("Saliendo de la calculadora...")
                exit()            
                break        
            
            if 1 <= operacion <= 6:
                break        
                        
            else:
                print("Error: Selección no válida.")
        except ValueError:
            print("Error: Debe ingresar una opcion valida del 1 a 6.")

    operadores = {
        1: "suma",
        2: "resta",
        3: "multiplicacion",
        4: "division",
        5: "potencia",
        6: "raiz cuadrada",
        7: "raiz n-ésima"
    }

    x = float(input("Ingrese el primer número de la "+ operadores[operacion]+": "))
    y = float(input("Ingrese el segundo número de la "+ operadores[operacion]+": ")) 

    def calculadora(x, y, operacion):
        if operacion == 1:
            return suma(x, y)
        elif operacion == 2:
            return resta(x, y)
        elif operacion == 3:
            return multiplicacion(x, y)
        elif operacion == 4:
            return division(x, y)
        elif operacion == 5:
            return potencia(x, y)
        elif operacion == 6:
            return raiznesima(x, y)     
        else:
            return "Error: Operación no válida."    
    
    print("El resultado de la", operadores[operacion], "de", x, "y", y, "es:", calculadora(x, y, operacion))
    
    continuar = input("¿Desea realizar otra operación? (s/n): ").lower()
    if continuar != 's':
        print("Saliendo de la calculadora...")
        break