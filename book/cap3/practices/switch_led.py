from pyfirmata import Arduino, util
from time import sleep

PORT = '/tmp/ttyS1'

board = Arduino(PORT)

it = util.Iterator(board) # le pasamos la tarjeta al iterador
it.start() #arrancamos a el iterador para poder leer entradas

# configuro el pin como ENTRADA
BOTON = 2
board.get_pin(f'd:{str(2)}:i')

LED = 3

status = False # me ayuuda a saber si el led esta encendido o apagado
while True:
    boton = board.digital[BOTON].read()
    sleep(0.1)

    if boton:
        print('boton presionado')
        status = not status
        board.digital[LED].write(status)
        sleep(0.1)

