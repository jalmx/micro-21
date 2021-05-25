from pyfirmata import Arduino,util
from time import sleep

def bar(board, leds=[], value=[]):
    for position,led in enumerate(leds):
        board.digital[led].write(value[position])

# Configuracion del puerto y la placa
PORT = '/tmp/ttyS1'
board = Arduino(PORT)

# activamos el iterador para poder leer datos de entrada de la tarjeta
util.Iterator(board).start()

# Activo el ADC 0 para que pueda leer su dato de entrada
board.analog[0].enable_reporting()

# damos un tiempo de estabilización al dato
sleep(1)

LEDs = [2,3,4,5,6,7,8,9]

while True:
    # Leo el dato que exista en ese momento en el ADC
    valor_adc = board.analog[0].read()

    # checamos primero que exista un numero, en caso que aun no tenga un valor disponible se lo brica
    if valor_adc == None:
        continue

    #hago las comparaciones para encender la barra de leds
    if valor_adc < 0.1:
        bar(board, LEDs, [1,0,0,0,0,0,0,0])
    elif valor_adc < .25:
        bar(board, LEDs, [1,1,1,0,0,0,0,0])
    elif valor_adc > .25 and valor_adc < 0.5:
        bar(board, LEDs, [1,1,1,1,1,0,0,0])
    elif valor_adc > .5 and valor_adc < 0.75:
        bar(board, LEDs, [1,1,1,1,1,1,0,0])
    elif valor_adc > .75:
        bar(board, LEDs, [1,1,1,1,1,1,1,1])
    sleep(0.25)


