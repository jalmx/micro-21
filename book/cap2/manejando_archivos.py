def agregar_contenido():
    ruta = 'archivo.txt'
    mi_archivo = open(ruta,mode='a', encoding='utf-8')

    mi_archivo.write('\nestamos con el grupo mas chido de mecatronica del cbtis 85')

    mi_archivo.close()

def creando_archivo():
    ruta = 'archivo.txt'
    mi_archivo = open(ruta,mode='w', encoding='utf-8')

    mi_archivo.write('\nestamos con el grupo mas chido de mecatronica del cbtis 85')

    mi_archivo.close()

def leyendo_archivo():
    # ruta = 'archivo.txt'
    # ruta = '/home/xizuth/Downloads/School/micro/antologia/book/cap3/practices/adc1.py'
    ruta = '../cap3/practices/adc1.py'
    mi_archivo = open(ruta, 'r', encoding='utf-8')
    contenido = mi_archivo.readlines()
    print(type(contenido))
    print(len(contenido))
    mi_archivo.close()
    print(contenido)
    print('=======')
    for renglon in contenido:
        print(f'Renglon: {renglon}')

def main():
    leyendo_archivo()

if __name__ == '__main__':
    main()
