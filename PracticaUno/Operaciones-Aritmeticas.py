#6. Escribe un programa que pida al usuario dos números y muestre la suma, resta, multiplicación y división de esos números.

numero1 = float(input("Ingrese un primer número del tipo real: ")) # Asignar el primer número a la variable numero1
numero2 = float(input("Ingrese el segundo número del tipo real: ")) # Asignar el segundo número a la variable numero2

suma = numero1 + numero2 # Realizar la suma de los dos números  
resta = numero1 - numero2 # Realizar la resta de los dos números
multiplicacion = numero1 * numero2 # Realizar la multiplicación de los dos números
division = numero1 / numero2 # Realizar la división de los dos números

print("La suma de:", numero1, "+", numero2, "=", suma) # Mostrar el resultado de la suma
print("La resta de:", numero1, "-", numero2, "=", resta) # Mostrar el resultado de la resta
print("La multiplicación de:", numero1, "x", numero2, "=", multiplicacion) # Mostrar el resultado de la multiplicación
print("La división de:", numero1, "/", numero2, "=", division) # Mostrar el resultado de la división
print("¡Gracias por usar la calculadora de coma flotante!")