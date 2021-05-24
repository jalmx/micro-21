from pyfirmata import Arduino
from time import sleep

PORT = '/tmp/ttyS1'
board = Arduino(PORT)

try:
    print('inicio el blink')
    while True:
        print('enciendo el led')
        board.digital[13].write(1)
        sleep(1)
        print('apago el led')
        board.digital[13].write(0)
        sleep(1)
except:
    print('se cierra la conexion con la placa')
    board.exit() # indicamos que cierre la conexion con la tarjeta
