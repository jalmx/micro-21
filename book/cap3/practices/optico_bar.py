from pyfirmata import Arduino, util
from time import sleep
from math import ceil

# configuracion de la tarjeta
PORT = '/tmp/ttyS1'
board = Arduino(PORT)
print('Conexion lista')

util.Iterator(board).start()

# configuracion SENSOR
SENSOR_OPTICO_PIN = 0
current_sensor = board.get_pin(f'a:{str(SENSOR_OPTICO_PIN)}:i')
sleep(1)

# configuracio de la salidas a los leds
LEDS_PINES = [2,3,4,5,6,7,8,9]

while True:

    value = current_sensor.read()

    if value == None:
        continue

    distance = value * 50
    distance = ceil(distance) # redondeo para evitar problemas en las comparaciones
    print(f'La distancia del objeto es: {distance}cm')

    if distance > 40:
        for index,pin in enumerate(LEDS_PINES):
            if index <= 0:
                board.digital[pin].write(1)
            else:
                board.digital[pin].write(0)

    elif distance <= 40 and distance > 30:
        for index,pin in enumerate(LEDS_PINES):
            if index <= 2:
                board.digital[pin].write(1)
            else:
                board.digital[pin].write(0)
    elif distance <= 30 and distance > 20:
        for index,pin in enumerate(LEDS_PINES):
            if index <= 4:
                board.digital[pin].write(1)
            else:
                board.digital[pin].write(0)
    elif distance <= 20 and distance > 10:
        for index,pin in enumerate(LEDS_PINES):
            if index <= 6:
                board.digital[pin].write(1)
            else:
                board.digital[pin].write(0)
    else:
        for pin in LEDS_PINES:
            board.digital[pin].write(1)

    sleep(0.5)
