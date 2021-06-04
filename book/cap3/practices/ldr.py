from pyfirmata import Arduino, util
from time import sleep

# configuracion de la tarjeta
PORT = '/tmp/ttyS1'
board = Arduino(PORT)
print('Conexion lista')

util.Iterator(board).start()

# configuracion SENSOR
SENSOR_LIGTH_PIN = 0
ligth_sensor = board.get_pin(f'a:{str(SENSOR_LIGTH_PIN)}:i')
sleep(1)

while True:

    sensor_light = ligth_sensor.read()
    print(f'Sensor: {sensor_light}')
    if sensor_light == None:
        continue

    lux = (1118.1 * sensor_light) - 79.83863

    print(f'Valor: {sensor_light}')
    print(f'Lux: {lux}')
    sleep(2)
