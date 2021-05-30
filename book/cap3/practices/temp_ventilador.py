from pyfirmata import Arduino, util
from time import sleep
import math

def blink(board, pin, time):
    board.digital[pin].write(1)
    sleep(time)
    board.digital[pin].write(0)
    sleep(time)

# configuracion de la tarjeta
PORT = '/tmp/ttyS1'
board = Arduino(PORT)
print('Conexion lista')

util.Iterator(board).start()

# configuro la salida del PWM para el ventilador
MOTOR_PIN = 3
motor = board.get_pin(f'd:{str(MOTOR_PIN)}:p')

# configuro salida del LED
LED_PIN = 8
led = board.get_pin(f'd:{str(LED_PIN)}:o')

# configuracion SENSOR
SENSOR_CURRENT_PIN = 0
current_sensor = board.get_pin(f'a:{str(SENSOR_CURRENT_PIN)}:i')
sleep(1)


while True:

    value = current_sensor.read()

    if value == None:
        continue

    celsius = value * 500
    celsius = math.ceil(celsius)

    if celsius <= 50:
        blink(board=board, pin=LED_PIN,time=1)
        motor.write(0.00)
    elif celsius > 50 and celsius <= 100:
        motor.write(0.33)
        led.write(1)
    elif celsius > 100 and celsius <= 150:
        motor.write(0.6)
        led.write(1)
    elif celsius > 150:
        motor.write(0.999)
        blink(board=board,pin=LED_PIN,time=0.2)

    print(f'temperatura {celsius}')

