#7. Escribe un programa que pida al usuario un número y determine si es positivo, negativo o cero.
Numero = float(input("Ingrese un número: ")) # Asignar el número a la variable Numero

if Numero > 0: 
    print("El número es positivo.") 
elif Numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")