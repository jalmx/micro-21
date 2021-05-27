from pyfirmata import Arduino, util
from time import sleep

PORT = '/tmp/ttyS1'
board = Arduino(PORT)

util.Iterator(board).start()

# pines en donde estan los botones
DOWN = 4
UP = 5

up = board.get_pin(f'd:{str(UP)}:i')
down = board.get_pin(f'd:{str(DOWN)}:i')

# Configuramos el pin que sera utilizado como PWM
led = board.get_pin('d:3:p')

# variable me indica el valor del pwm
intensidad = 0

while True:

    if up.read():
        if not (intensidad >= 99):
            intensidad += 3
            led.write(intensidad/100)
            print(intensidad/100)
            sleep(0.25)

    if down.read():
        if not (intensidad <= 0):
            intensidad -= 3
            led.write(intensidad/100)
            print(intensidad/100)
            sleep(0.25)

