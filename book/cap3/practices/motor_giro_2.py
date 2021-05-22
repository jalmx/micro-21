from pyfirmata import Arduino
from time import sleep

import lib_motor as motor

PORT = '/tmp/ttyS1'
board = Arduino(PORT)

while True:
    motor.giro(board, tipo='derecha')
    sleep(2)
    motor.parar(board)
    sleep(2)
    motor.giro(board, tipo='izquierda')
    sleep(2)
    motor.parar(board)
    sleep(2)

    motor.polarizacion(board, polar=[1,0])
    sleep(2)
    motor.polarizacion(board, polar=[0,0])
    sleep(2)
    motor.polarizacion(board, polar=[0,1])
    sleep(2)
    motor.parar(board)
    sleep(2)
