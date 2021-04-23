#Juego de adivina el numero
import random

number = random.randint(1,10)

print("Juego de adivina el numero")
print("El numero esta entre 1 y 10")
print("Tienes 5 intentos")
print("Mucha suerte!!!!")

intentos = 0
while True:
    nuevo = int(input("Dame un valor: "))

    if nuevo < number:
        print("El numero es MAYOR")
        intentos +=1
    elif nuevo > number:
        print("El numero es MENOR")
        intentos +=1
    else:
        print("Felicidades le has atinado")
        break

    print(f"Llevas {intentos} intentos")
    
    if intentos == 5:
        print("Perdiste, lastima margarito  T.T")
        break

