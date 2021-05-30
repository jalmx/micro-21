from pyfirmata import Arduino, util
from time import sleep

# configuracion de la tarjeta

PORT = '/tmp/ttyS1'
board = Arduino(PORT)
print('Conexion lista')

util.Iterator(board).start()

# configuracion SENSOR
SENSOR_CURRENT_PIN = 0
current_sensor = board.get_pin(f'a:{str(SENSOR_CURRENT_PIN)}:i')
sleep(1)

while True:

    value = current_sensor.read()

    if value == None:
        continue

    current_value = value * 1000.0

    print(f'Value: {value}')
    print(f'La corriente es {current_value}mA')
    sleep(0.3)
