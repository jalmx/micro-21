from pyfirmata import Arduino, util
from time import sleep

PORT = '/tmp/ttyS1'
board = Arduino(PORT)

util.Iterator(board).start()

# pines en donde estan los botones
POT = 0
# configuro la entrada del potenciometro
pot = board.get_pin(f'a:{str(POT)}:i')

# Configuramos el pin que sera utilizado como PWM
LED = 3
led = board.get_pin(f'd:{str(LED)}:p')

sleep(1) #se estabiliza la configuracion

while True:

    intensidad = pot.read()
    sleep(0.25)

    if intensidad == None:
        continue

    led.write(intensidad)
    print(intensidad)

