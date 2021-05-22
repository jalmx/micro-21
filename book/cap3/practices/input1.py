from pyfirmata import Arduino, util, INPUT
from time import sleep

PORT = '/tmp/ttyS1'
board = Arduino(PORT)

util.Iterator(board).start() # le pasamos la tarjeta al iterador

# configuro el pin como ENTRADA
PIN = 2
board.digital[PIN].mode = INPUT

while True:
    boton = board.digital[PIN].read() # leemos el valor del pin
    print(boton) # mandamos a imprimir el valor por la terminal
    sleep(0.5) # damos un tiempo entre pulsaciones
