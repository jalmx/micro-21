from pyfirmata import Arduino, util
from time import sleep, time

def blink(board, pin, time):
    '''
    genera el blink en un led para indicar su estado
    '''
    board.digital[pin].write(1)
    sleep(time)
    board.digital[pin].write(0)
    sleep(time)

# configuracion de la tarjeta

PORT = '/tmp/ttyS1'
board = Arduino(PORT)
print('Conexion lista')

util.Iterator(board).start()

# configurando salidas
LED_PIN = 4
RELAY_PIN = 2

led = board.get_pin(f'd:{str(LED_PIN)}:o')
relay = board.get_pin(f'd:{str(RELAY_PIN)}:o')

# configuracion SENSOR
SENSOR_CURRENT_PIN = 0
current_sensor = board.get_pin(f'a:{str(SENSOR_CURRENT_PIN)}:i')
sleep(1)

# defino varibles auxiliares
ON = 1
OFF = 0

while True:
# vamos a simular 3 niveles del sensor
# apagado < 0.2
# normal 0.2 >= hasta 0.8
# overload (sobrecarga) >0.8

    value = current_sensor.read()

    if value == None:
        continue

    if value >= 0.8:
        relay.write(OFF)
        blink(board=board,pin=LED_PIN,time=0.2)

    elif value < 0.8 and value >= 0.2:
        relay.write(ON)
        led.write(ON)

    else:
        relay.write(ON)
        blink(board=board,pin=LED_PIN,time=0.5)

