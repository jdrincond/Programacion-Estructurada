#8. Escribe un programa que pida al usuario un número y determine si es par o impar.

numero = int(input("Ingrese un número: ")) 
if numero % 2 == 0: 
    print("El número", numero, "es par.") 
else:    
    print("El número", numero, "es impar.")
