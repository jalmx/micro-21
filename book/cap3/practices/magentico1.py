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
MAGENTICO_INPUT = 2
board.get_pin(f'd:{str(MAGENTICO_INPUT)}:i')

# declaro en donde esta mi alarma
ALARM = [8]

while True:

    magnetico = board.digital[MAGENTICO_INPUT].read()

    if not magnetico:
        print('ventana abierta')
        secuencia(board=board,leds=ALARM,time=0.5)
