from pyfirmata import Arduino, util, INPUT
from time import sleep

def display(number):
    for segmento in segmentos:

def number_0():
    pass
def number_1():
    pass
def number_2():
    pass
def number_3():
    pass
def number_4():
    pass
def number_5():
    pass
def number_6():
    pass
def number_7():
    pass
def number_8():
    pass
def number_9():
    pass

PORT = '/tmp/ttyS1'
# importamos los elementos necesarios
board = Arduino(PORT)

it = util.Iterator(board) # le pasamos la tarjeta al iterador
it.start() #arrancamos a el iterador para poder leer entradas

BOTON1 = 2
BOTON2 = 4
# configuro el pin como ENTRADA
board.digital[BOTON].mode = INPUT

count = 0

while True:
    boton = board.digital[BOTON1].read()



