from pyfirmata import Arduino
from time import sleep

PORT = '/tmp/ttyS1'
board = Arduino(PORT)

MOTOR1_1 = 2
MOTOR1_2 = 3

while True:
    print('Gira el motor en un sentido')
    board.digital[MOTOR1_1].write(1)
    board.digital[MOTOR1_2].write(0)
    sleep(5)
    print('Motor apagado')
    board.digital[MOTOR1_1].write(0)
    board.digital[MOTOR1_2].write(0)
    sleep(1)
    print('Gira el motor en sentido contrario')
    board.digital[MOTOR1_1].write(0)
    board.digital[MOTOR1_2].write(1)
    sleep(5)
    print('Motor apagado')
    board.digital[MOTOR1_1].write(0)
    board.digital[MOTOR1_2].write(0)
    sleep(1)
