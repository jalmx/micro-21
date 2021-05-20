from time import sleep         # importamos la libreria de retardos

def display7(A,B,C,D,E,F,G,board,time=1 ):

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
