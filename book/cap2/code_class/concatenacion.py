# Ejemplo de concatenacion y tipos de variables

nombre = 'Superman' # variable tipo str
edad = 30           #variable tipo int
altura = 1.70       #variable tipo float
conCarro = False    #variable tipo bool

print(nombre) # ***funcion*** print, manda mensajes a la terminal
print(edad)
print(altura)
print(conCarro)

#-------------------------------------

# Mi nombre es: Superman
frase = "Mi nombre es: " + nombre #Concatenacion

print(frase)

# Mi edad es: 30
edad_str = str(edad) # estoy convirtiendo la variable edad en tipo str

print("Mi edad es: " + edad_str + " anios")

# Funcion str()

altura_str = str(altura)
conCarro_str = str(conCarro)

print(altura_str + " --- " +conCarro_str)

# Mi nombre es Fulanito, tengo 200 anios, mido 1.7 metro, mi carro es: True

print("Mi nombre es " + nombre + ", tengo " + str(edad) + ", mido " + str(altura) +" mi carro es: " + str(conCarro))

