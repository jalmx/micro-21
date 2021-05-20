from pyfirmata import Arduino
from time import sleep

PORT= '/tmp/ttyS1' #en window es COMx

board = Arduino(PORT)
print('Conexion creada')

# Luces
RED = 2
YELLOW = 3
GREEN = 4

while True:
    print('Enciendo Rojo')
    board.digital[RED].write(1)
    sleep(4)
    board.digital[RED].write(0)
    print('Apago Rojo')

    print('Enciendo Verder')
    board.digital[GREEN].write(1)
    sleep(2)
    board.digital[GREEN].write(0)
    sleep(0.4)
    board.digital[GREEN].write(1)
    sleep(0.4)
    board.digital[GREEN].write(0)
    sleep(0.4)
    board.digital[GREEN].write(1)
    sleep(0.4)
    board.digital[GREEN].write(0)
    sleep(0.4)
    board.digital[GREEN].write(1)
    sleep(0.4)
    board.digital[GREEN].write(0)
    print('Apago verde')

    print('Enciendo ambar')
    board.digital[YELLOW].write(1)
    sleep(2)
    board.digital[YELLOW].write(0)
    print('apago ambar')
