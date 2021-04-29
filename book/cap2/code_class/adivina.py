#Juego de adivina el numero
import random

num_random = random.randint(1,10) #genera un numero al azar en ese rango

print("JUEGO + ADIVINA EL NUMERO")
print("El numero esta entre 1 al 10")
print("Tienes solo 5 intentos")
print("Mucha suerte >:) ")

intentos = 0
while True:
    number = int(input("Dar el numero: "))

    if number < num_random:
        print("El numero es mayor")
        intentos +=1
    elif number > num_random:
        print("El numero es menor")
        intentos +=1
    else:
        print("Felicidades le atinaste :D")
        break

    if intentos == 5:
        print(f"Fallaste {intentos} veces")
        print(f"EL numero era: {num_random}")
        print(f"Lastima margarito")
        break


