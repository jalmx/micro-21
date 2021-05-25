from pyfirmata import Arduino, util
from time import sleep

def sound(board,pin):
    time = 0.05

    board.digital[pin].write(1)
    sleep(time)
    board.digital[pin].write(0)
    sleep(time)


PORT = '/tmp/ttyS1'
# importamos los elementos necesarios
board = Arduino(PORT)

it = util.Iterator(board)  # le pasamos la tarjeta al iterador
it.start()  # arrancamos a el iterador para poder leer entradas

# configuro el pin como ENTRADA
FLAME_INPUT = 2

board.get_pin(f'd:{str(FLAME_INPUT)}:i')

# declaro mi lista de la posicion de los leds
BUZZER = 8

while True:

    flame = board.digital[FLAME_INPUT].read()

    if flame:
        print('existe flama')
        sound(board, BUZZER)
        print('FUEGOOOOOOOO!!!!!!!')

