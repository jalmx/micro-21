from pyfirmata import Arduino, util
from time import sleep

PORT = '/tmp/ttyS1'
# importamos los elementos necesarios
board = Arduino(PORT)


def control_output(board, pin, value):
    board.digital[pin].write(value)


it = util.Iterator(board)  # le pasamos la tarjeta al iterador
it.start()  # arrancamos a el iterador para poder leer entradas

# configuro el pin como ENTRADA
FLAME_INPUT = 2
PIR_INPUT = 3

board.get_pin(f'd:{str(FLAME_INPUT)}:i')
board.get_pin(f'd:{str(PIR_INPUT)}:i')

# declaro mis salidas
SOLENOIDE = 8
EXTRACTOR = 9

status_extractor = False
count_time_extractor = 0

while True:

    flame = board.digital[FLAME_INPUT].read()
    pir = board.digital[PIR_INPUT].read()

    if flame and not pir:
        control_output(board, SOLENOIDE, 0)
        control_output(board, EXTRACTOR, 1)
        status_extractor = True
        sleep(0.25)
    elif pir:
        control_output(board, SOLENOIDE, 1)
        control_output(board, EXTRACTOR, 0)
        status_extractor = False
        sleep(0.25)

    if status_extractor:
        if count_time_extractor >= 10:
            control_output(board, EXTRACTOR, 0)
            status_extractor = False
            count_time_extractor = 0
        else:
            count_time_extractor += 1
            sleep(1)
