#10. Escribe un programa que sume números ingresados por el usuario hasta que ingrese 0.

sumador = 0
sumandos = 0

while True:
    numero = int(input("Ingrese un número (0 para salir): "))
    if numero == 0:
        break
    sumador += numero
    sumandos=sumandos+1
    print(sumador)
print("El resultado total de la suma es:", sumador)
print("El numero de sumandos fue:", sumandos)


