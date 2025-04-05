#5. Pide al usuario que ingrese su edad y determina si es mayor de edad (18 años o más).

edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Si tienes", edad, "años. Eres mayor de edad y puedes entrar")
else:
    print("Si tienes", edad, "años. Eres menor de edad y no puedes entrar")
