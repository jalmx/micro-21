# from pyfirmata import Arduino, util
# from time import sleep

# board = Arduino('/tmp/ttyS1')
# print('Arranca la conexion')

# it = util.Iterator(board) # le pasamos la tarjeta al iterador
# it.start() #arrancamos a el iterador para poder leer entradas

# # configuro el pin como ENTRADA
# PIN = 2
# board.get_pin(f'd:{str(PIN)}:i')

# while True:
#     print(board.digital[PIN].read())
#     sleep(0.25)

from pyfirmata import Arduino, util
from time import sleep

try:
    PORT = '/tmp/ttyS1'
    board = Arduino(PORT)

    while True:
        board.digital[13].write(1)
        sleep(1)
        board.digital[13].write(0)
        sleep(1)
except:
    print('termino el programa')
    board.exit() # indicamos que cierre la conexion con la tarjeta
