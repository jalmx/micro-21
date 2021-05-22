from pyfirmata import Arduino
from time import sleep

PORT = '/tmp/ttyS1'
board = Arduino(PORT)

try:
    while True:
        board.digital[13].write(1)
        sleep(1)
        board.digital[13].write(0)
        sleep(1)
except:
    print('termino el programa')
    board.exit() # indicamos que cierre la conexion de la placa
