from pyfirmata import Arduino, util
from time import sleep

PORT = '/tmp/ttyS1'
board = Arduino(PORT)

util.Iterator(board).start()

# Configuro botones
DOWN = 8
UP = 9

down = board.get_pin(f'd:{str(DOWN)}:i')
up = board.get_pin(f'd:{str(UP)}:i')
# configuro la entrada del potenciometro
POT = 3
pot = board.get_pin(f'a:{str(POT)}:i')

# config Servo
SERVO = 3
servo = board.get_pin(f'd:{str(SERVO)}:s')

sleep(1) # time to wait

step = 18
angulo = 0

while True:

    if down.read():
        if angulo <= 0:
            continue
        angulo -= step
        print(f'Incremento angulo {angulo}')
        servo.write(angulo)
        sleep(0.25)

    if up.read():
        if angulo >= 180:
            continue

        angulo += step
        print(f'Decremento el angulo {angulo}')
        servo.write(angulo)
        sleep(0.25)
