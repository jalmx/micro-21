from pyfirmata import Arduino,util
from time import sleep

# Configuracion del puerto y la placa
PORT = '/tmp/ttyS1'
board = Arduino(PORT)

# activamos el iterador para poder leer datos de entrada de la tarjeta
util.Iterator(board).start()

# Activo el ADC 0 para que pueda leer su dato de entrada
board.analog[0].enable_reporting()

# damos un tiempo de estabilización al dato
sleep(1)

while True:
    # Leo el dato que exista en ese momento en el ADC
    valor_adc = board.analog[0].read()

    # imprimo el dato del ADC
    print(valor_adc)
    sleep(0.5)
