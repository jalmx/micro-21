from pyfirmata import Arduino, util, INPUT
from time import sleep

def display(number):
    numbers = [number_0,number_1,number_2,number_3,number_4,number_5,number_6,number_7,number_8,number_9]

    for position,segments in enumerate(numbers):
        if position == number:
            segments()
            break

def number_0():
    set_segment(1,1,1,1,1,1,0)

def number_1():
    set_segment(0,1,1,0,0,0,0)

def number_2():
    set_segment(1,1,0,1,1,0,1)

def number_3():
    set_segment(1,1,1,1,0,0,1)

def number_4():
    set_segment(0,1,1,0,0,1,1)

def number_5():
    set_segment(1,0,1,1,0,1,1)

def number_6():
    set_segment(0,0,1,1,1,1,1)

def number_7():
    set_segment(1,1,1,0,0,0,0)

def number_8():
    set_segment(1,1,1,1,1,1,1)

def number_9():
    set_segment(1,1,1,1,0,1,1)

def set_segment(*segments):
    display_pins = [2,3,4,5,6,7,8]

    for pin, segment in enumerate(segments):
        print(f'Pin a encender{board.digital[display_pins[pin]]}')
        board.digital[display_pins[pin]].write(segment)

PORT = '/tmp/ttyS1'
# importamos los elementos necesarios
board = Arduino(PORT)

it = util.Iterator(board) # le pasamos la tarjeta al iterador
it.start() #arrancamos a el iterador para poder leer entradas

# configuro el pin como ENTRADA
BOTON = 12
board.digital[BOTON].mode = INPUT

count = 0
display(count)
sleep(0.1)

while True:
    boton = board.digital[BOTON].read()

    if boton:
        count += 1
        sleep(0.25)
        display(count)

        if count == 9: count = -1
