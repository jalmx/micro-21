from pyfirmata import Arduino, util
from time import sleep

def control_led(board,pin,value):
    board.digital[pin].write(value)

PORT = '/tmp/ttyS1'
# importamos los elementos necesarios
board = Arduino(PORT)

it = util.Iterator(board)  # le pasamos la tarjeta al iterador
it.start()  # arrancamos a el iterador para poder leer entradas

# configuro el pin como ENTRADA
PIR_INPUT = 2
SWICTH_INPUT = 3
board.get_pin(f'd:{str(PIR_INPUT)}:i')
board.get_pin(f'd:{str(SWICTH_INPUT)}:i')

# declaro mi lista de la posicion de los leds
FOCO = 8

status_foco = False

count = 0 # contador del temporizador

while True:

    pir = board.digital[PIR_INPUT].read()
    switch = board.digital[SWICTH_INPUT].read()

    if pir and switch and not status_foco :
        control_led(board, FOCO, 1)
        status_foco = True
        sleep(0.25) # estabilizamos el presionar el boton
    elif switch and status_foco:
        control_led(board, FOCO, 0)
        status_foco = False
        sleep(1)

    if status_foco and not pir:
        if count >= 10:
            control_led(board, FOCO, 0)
            status_foco = False
            count = 0
        sleep(1)
        count += 1
    else:
        count = 0


