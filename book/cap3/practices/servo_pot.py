from pyfirmata import Arduino, util
from time import sleep
from math import ceil

PORT = '/tmp/ttyS1'
board = Arduino(PORT)

util.Iterator(board).start()

# Config pot
POT = 0
# configuro la entrada del potenciometro
pot = board.get_pin(f'a:{str(POT)}:i')

# config Servo
SERVO = 3
servo = board.get_pin(f'd:{str(SERVO)}:s')

sleep(1) # time to wait

while True:

    value = pot.read()

    if value == None:
        continue

    ang = value * 180
    ang = ceil(ang) # redondeo para no generar falla
    servo.write(ang)
    print(f'angulo {ang}')

    sleep(0.25)
