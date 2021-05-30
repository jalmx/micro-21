from pyfirmata import Arduino, util
from time import sleep

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
    sleep(0.25)

    if value == None:
        continue

    ang = value * 180
    servo.write(ang)
