
from pyfirmata import Arduino, util
from time import sleep

PORT = '/tmp/ttyS1'
board = Arduino(PORT)

# Configuramos el pin que sera utilizado como PWM
pin_analog = board.get_pin('d:3:p')

while True:

    for i in range(0, 101,3):
        pin_analog.write(i/100)
        sleep(0.2)
