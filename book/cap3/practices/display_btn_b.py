from pyfirmata import Arduino, util, INPUT
from time import sleep


def display7(A,B,C,D,E,F,G,board,time=0):

    # segmentos del display
    SEGMENT_A = 2
    SEGMENT_B = 3
    SEGMENT_C = 4
    SEGMENT_D = 5
    SEGMENT_E = 6
    SEGMENT_F = 7
    SEGMENT_G = 8

    board.digital[SEGMENT_A].write(A)
    board.digital[SEGMENT_B].write(B)
    board.digital[SEGMENT_C].write(C)
    board.digital[SEGMENT_D].write(D)
    board.digital[SEGMENT_E].write(E)
    board.digital[SEGMENT_F].write(F)
    board.digital[SEGMENT_G].write(G)

    sleep(time)


PORT = '/tmp/ttyS1'
# importamos los elementos necesarios
board = Arduino(PORT)

util.Iterator(board).start() # arrancamos el hilo para poder leer datos de la tarjeta

# configuro el pin como ENTRADA
BOTON = 12
board.digital[BOTON].mode = INPUT

count = 0 # variable me ayuda a saber en la posicion en la que estoy
sleep(0.1) #estabilizar la comunicacion

display7(1,1,1,1,1,1,0,board) # coloco el cero en el display

while True:
    boton = board.digital[BOTON].read()
    sleep(0.25)

    if boton:
        count += 1

        if count >= 5:# el reset o el reinicio del conteo en el display
            count = 0
            sleep(0.1)

        if count == 0:
            print('muestro el 0')
            display7(1,1,1,1,1,1,0,board=board)
        elif count == 1:
            print('muestro el 1')
            display7(0,1,1,0,0,0,0,board=board)
        elif count == 2:
            print('muestro el 2')
            display7(1,1,0,1,1,0,1,board=board)
        elif count == 3:
            print('muestro el 3')
            display7(1,1,1,1,0,0,1,board=board)
        elif count == 4:
            print('muestro el 4')
            display7(1,0,0,0,1,1,1,board=board)
