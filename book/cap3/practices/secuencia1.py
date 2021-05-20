from pyfirmata import Arduino
from time import sleep

PORT= '/tmp/ttyS1' #en window es COMx

board = Arduino(PORT)
print('Conexion creada')

while True:

    for PIN_LED in range(2,7):
        board.digital[PIN_LED].write(1)
        sleep(1)

    for PIN_LED in range(2,7):
        board.digital[PIN_LED].write(0)
    sleep(1)
