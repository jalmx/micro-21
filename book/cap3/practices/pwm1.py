
from pyfirmata import Arduino
from time import sleep

PORT = '/tmp/ttyS1'
board = Arduino(PORT)

# Configuramos el pin que sera utilizado como PWM
pwm = board.get_pin('d:3:p')

while True:

    for i in range(0, 101,3):
        value = i/100
        print(value)
        pwm.write(value)
        sleep(0.2)
