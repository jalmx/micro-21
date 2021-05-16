from pyfirmata import Arduino
from time import sleep

def pap(pin,signal):
    board.digital[pin['A']].write(signal[0])
    board.digital[pin['B']].write(signal[1])
    board.digital[pin['C']].write(signal[2])
    board.digital[pin['D']].write(signal[3])

PORT = '/tmp/ttyS1'
board = Arduino(PORT)

TIME = 0.25

PINS = {
'A': 2,
'B': 3,
'C': 4,
'D': 5
}

while True:
    pap(PINS,[1,0,0,0])
    sleep(TIME)
    pap(PINS,[0,1,0,0])
    sleep(TIME)
    pap(PINS,[0,0,1,0])
    sleep(TIME)
    pap(PINS,[0,0,0,1])
    sleep(TIME)

