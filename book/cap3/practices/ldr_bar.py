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

# guardo en una lista los pines de los leds
LEDS_PIN = [2,3,4,5,6,7,8,9]

while True:

    lux = ligth_sensor.read()
    if lux == None:
        continue

    if lux < 0.2:
        for index, pin in enumerate(LEDS_PIN):
            board.digital[pin].write(1)
    elif lux >= 0.2 and lux < 0.5:
        for index, pin in enumerate(LEDS_PIN):
            if index <= 6:
                board.digital[pin].write(1)
            else:
                board.digital[pin].write(0)

    elif lux >= 0.5 and lux < 0.8:
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

    print(f'Valor: {lux}')
    sleep(2)
