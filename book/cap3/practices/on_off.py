from pyfirmata import Arduino, util, INPUT
from time import sleep

PORT = '/tmp/ttyS1'

board = Arduino(PORT)

it = util.Iterator(board) # le pasamos la tarjeta al iterador
it.start() #arrancamos a el iterador para poder leer entradas

# configuro el pin como ENTRADA
BOTON = 2
board.digital[BOTON].mode = INPUT

LED = 8
status = False

while True:
    boton = board.digital[BOTON].read()

    if boton:
        status = not status
        board.digital[LED].write(status)
        sleep(0.25)
