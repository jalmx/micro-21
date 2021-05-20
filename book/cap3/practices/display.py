# importamos la libreria que nos permite conectarnos por el protocolo de firmata
from pyfirmata import Arduino
from display7 import display7

# Indicamos el puerto donde se encuentra conectada la tarjeta electronica
PORT = '/tmp/ttyS1'
board = Arduino(PORT)  # es la conexion con la placa
print('Placa conectada')

while True:
    # creo el digito 0
    print('digito 0')
    display7(1,1,1,1,1,1,0, board)
    print('digito 1')
    display7(0,1,1,0,0,0,0, board)
    print('digito 2')
    display7(1,1,0,1,1,0,1, board)
    print('digito 3')
    display7(1,1,1,1,0,0,1, board)
    print('digito F')
    display7(1,0,0,0,1,1,1, board)


