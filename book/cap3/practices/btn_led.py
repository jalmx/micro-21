from pyfirmata import Arduino, util, INPUT
from time import sleep

PORT = '/tmp/ttyS1'
board = Arduino(PORT)

it = util.Iterator(board) # le pasamos la tarjeta al iterador
it.start() #arrancamos a el iterador para poder leer entradas

# configuro el pin como ENTRADA
BTN = 2
BTN2 = 4
board.get_pin(f'd:{str(BTN)}:i')
board.get_pin(f'd:{str(BTN2)}:i')

LED = 3
LED2 = 5

while True:
    boton = board.digital[BTN].read()
    boton2 = board.digital[BTN2].read()
    sleep(0.1)

    # configuracion pull-down
    if boton:
        board.digital[LED].write(1)
    else:
        board.digital[LED].write(0)

    #configuracion pull-up
    if not boton2:
        board.digital[LED2].write(1)
    else:
        board.digital[LED2].write(0)
