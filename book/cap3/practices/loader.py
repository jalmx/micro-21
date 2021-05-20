# importamos la libreria que nos permite conectarnos por el protocolo de firmata
from pyfirmata import Arduino
from time import sleep


# Indicamos el puerto donde se encuentra conectada la tarjeta electronica
PORT = '/tmp/ttyS1'
board = Arduino(PORT)  # es la conexion con la placa
print('Placa conectada')

while True:
    # creo el digito 0
    for PIN in range(2,9):
        board.digital[PIN].write(1)
        sleep(1)

    for PIN in range(2,9):
        board.digital[PIN].write(0)
    sleep(1)
