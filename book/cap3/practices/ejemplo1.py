from pyfirmata import Arduino    #importamos la libreria que nos permite conectarnos por el protocolo de firmata
import time         # importamos la libreria de retardos

# Indicamos el puerto donde se encuentra conectada la tarjeta electronica
PORT = '/tmp/ttyS1'
board = Arduino(PORT) #es la conexion con la placa
print('Placa conectada')

PIN = 3

#se manda un nivel 1 a la salida del pin 3
board.digital[PIN].write(1)
print(f'Enciendo el pin {PIN}')
time.sleep(4)
board.digital[PIN].write(0)
print(f'Apago el pin {PIN}')

