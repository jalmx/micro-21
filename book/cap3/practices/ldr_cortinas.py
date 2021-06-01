from pyfirmata import Arduino, util
from time import sleep
import math

from pyfirmata.pyfirmata import DIGITAL

# configuracion de la tarjeta
PORT = '/tmp/ttyS1'
board = Arduino(PORT)
print('Conexion lista')

util.Iterator(board).start()

# configurar el servo
SERVO_PIN = 3
servo = board.get_pin(f'd:{str(SERVO_PIN)}:s')

# configuracion SENSOR
SENSOR_LIGTH_PIN = 0
ligth_sensor = board.get_pin(f'a:{str(SENSOR_LIGTH_PIN)}:i')
sleep(1)

while True:

# menos luz abre cortina (angulo mayor)
# mas luz cierra cortina (angulo menor)

    lux = ligth_sensor.read()

    if lux == None:
        continue

    if lux < 0.7:
        servo.write(180)
    elif lux >= 0.7 and lux < 0.8:
        servo.write(100)
    elif lux >= 0.8 and lux < 0.9:
        servo.write(60)
    else:
        servo.write(0)
