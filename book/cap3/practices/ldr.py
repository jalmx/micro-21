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

    if lux < 0.7:
        for index, pin in enumerate(LEDS_PIN):
            board.digital[pin].write(1)
    elif lux >= 0.7 and lux < 0.8:
        for index, pin in enumerate(LEDS_PIN):
            if index <= 6:
                board.digital[pin].write(1)
            else:
                board.digital[pin].write(0)

    elif lux >= 0.8 and lux < 0.9:
        for index, pin in enumerate(LEDS_PIN):
            if index <= 3:
                board.digital[pin].write(1)
            else:
                board.digital[pin].write(0)
    else:
        for index, pin in enumerate(LEDS_PIN):
            if index <= 1:
                board.digital[pin].write(1)
            else:
                board.digital[pin].write(0)

    lux = ((lux * 999)/0.83) - 87
    print(f'Valor: {lux}')
    sleep(2)
