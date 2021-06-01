from pyfirmata import Arduino, util
from time import sleep
import math

from pyfirmata.pyfirmata import DIGITAL

# configuracion de la tarjeta
PORT = '/tmp/ttyS1'
board = Arduino(PORT)
print('Conexion lista')

util.Iterator(board).start()

# configuracion SENSOR
SENSOR_LIGTH_PIN = 0
ligth_sensor = board.get_pin(f'a:{str(SENSOR_LIGTH_PIN)}:i')
sleep(1)

LEDS_PIN = [2,3,4,5,6,7,8,9]

while True:

    lux = ligth_sensor.read()
    print(f'Sensor: {lux}')
    if lux == None:
        continue

    lux = ((lux * 999)/0.83) - 87
    print(f'Valor: {lux}')
    sleep(2)
