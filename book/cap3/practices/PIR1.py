from pyfirmata import Arduino, util
from time import sleep

def secuencia(board,leds=[],time=0.1):
    for led in leds:
        board.digital[led].write(1)
    sleep(time)
    for led in leds:
        board.digital[led].write(0)
    sleep(time)

PORT = '/tmp/ttyS1'
# importamos los elementos necesarios
board = Arduino(PORT)

it = util.Iterator(board)  # le pasamos la tarjeta al iterador
it.start()  # arrancamos a el iterador para poder leer entradas

# configuro el pin como ENTRADA
PIR_INPUT = 2
board.get_pin(f'd:{str(PIR_INPUT)}:i')

# declaro mi lista de la posicion de los leds
LEDS = [8,9,10,11,12,13]

while True:

    pir = board.digital[PIR_INPUT].read()

    if pir:
        print('deteccion de persona')
        secuencia(board=board,leds=LEDS,time=0.25)
    else:
        secuencia(board=board,leds=LEDS,time=1)
