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

    celsius = value * 500

    fahrenheint = (celsius * (9/5)) + 32
    print(f'Value: {value}')
    print(f'La temperatura Celsius {celsius}ºC')
    print(f'La temperatura Farenheit {fahrenheint}ºF')
    sleep(2)
