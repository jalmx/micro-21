from pyfirmata import Arduino
from time import sleep

def giro(pin, signal):
    board.digital[pin[0]].write(signal[0])
    board.digital[pin[1]].write(signal[1])

PORT = '/tmp/ttyS1'
board = Arduino(PORT)

MOTOR1_1 = 2
MOTOR1_2 = 3

while True:
    giro([MOTOR1_1, MOTOR1_2],[0,1])
    sleep(5)
    giro([MOTOR1_1, MOTOR1_2],[1,0])
    sleep(5)

