from pyfirmata import Arduino
from time import sleep

PORT = '/tmp/ttyS1'
board = Arduino(PORT)

# Configuramos el pin que sera utilizado como PWM
servo = board.get_pin('d:3:s') # el tercer parametro define que tipo sera la salida
sleep(1)

while True:
    angulo = 0
    servo.write(angulo)
    print(angulo)
    sleep(2)
    angulo = 30
    servo.write(angulo)
    print(angulo)
    sleep(2)
    angulo = 60
    servo.write(angulo)
    print(angulo)
    sleep(2)
    angulo = 90
    servo.write(angulo)
    print(angulo)
    sleep(2)
    angulo = 120
    servo.write(angulo)
    print(angulo)
    sleep(2)
    angulo = 160
    servo.write(angulo)
    print(angulo)
    sleep(2)
    angulo = 180
    servo.write(angulo)
    print(angulo)
    sleep(2)

