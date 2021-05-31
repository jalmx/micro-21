from pyfirmata import Arduino, util
from time import sleep

# configuracion de la tarjeta

PORT = '/tmp/ttyS1'
board = Arduino(PORT)
print('Conexion lista')

util.Iterator(board).start()

# configuracion SENSOR
SENSOR_OPTICO_PIN = 0
current_sensor = board.get_pin(f'a:{str(SENSOR_OPTICO_PIN)}:i')
sleep(1)

while True:

    value = current_sensor.read()

    if value == None:
        continue

    distancia = value * 50

    print(f'La distancia del objeto es: {distancia}cm')
    sleep(0.5)
