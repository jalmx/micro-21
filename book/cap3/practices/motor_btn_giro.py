from pyfirmata import Arduino, util
from time import sleep

# Funcion para el giro del motor
def giro(board, pins=[2, 3], values=[0, 0]):
    board.digital[pins[0]].write(values[0])
    board.digital[pins[1]].write(values[1])
    sleep(0.5)  # estabilizar la salida al motor


PORT = '/tmp/ttyS1'
# importamos los elementos necesarios
board = Arduino(PORT)

it = util.Iterator(board)  # le pasamos la tarjeta al iterador
it.start()  # arrancamos a el iterador para poder leer entradas

# configuro el pin como ENTRADA
BOTON_R = 8
BOTON_L = 9

board.get_pin(f'd:{str(BOTON_R)}:i')
board.get_pin(f'd:{str(BOTON_L)}:i')

# Configuro los pines del motor
MOTOR_1 = 2
MOTOR_2 = 3

# variables que me indican el estado del motor y su sentido
status_r = False
status_l = False

while True:

    boton_r = board.digital[BOTON_R].read()
    boton_l = board.digital[BOTON_L].read()

    if boton_r:
        if not status_r and not status_l:
            giro(board, [MOTOR_1, MOTOR_2], [1, 0])
            status_r = True
        elif status_l:
            giro(board, [MOTOR_1, MOTOR_2], [0, 0])
            sleep(0.25)
            giro(board, [MOTOR_1, MOTOR_2], [1, 0])
            status_r = True
            status_l = False
        else:
            giro(board, [MOTOR_1, MOTOR_2], [0, 0])
            status_r = False

    if boton_l:
        if not status_l and not status_r:
            giro(board, [MOTOR_1, MOTOR_2], [0, 1])
            status_l = True
        elif status_r:
            giro(board, [MOTOR_1, MOTOR_2], [0, 0])
            sleep(0.25)
            giro(board, [MOTOR_1, MOTOR_2], [0, 1])
            status_l = True
            status_r = False
        else:
            giro(board, [MOTOR_1, MOTOR_2], [0, 0])
            status_l = False


