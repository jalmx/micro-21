# -*- coding: utf-8 -*-
# script para cambiar los nombres de los archivos
# eliminando los espacios y colocando un guion bajo
import os
from pathlib import Path

ipynb = '.ipynb_checkpoints'
path = '../book/'  # ruta que va analizar y obtener todos los archivos

# Con la funcion rglob busca todos los archivos con la extension .ipynb
for element in Path(path).rglob('**/*.ipynb'):

    # se brinca todos los archivos que estan carpertas "checkpoints"
    if not str(element).find(ipynb) > 0:
        path_full_old = os.path.abspath(element)
        name_old = str(element).split('/')[-1]
        name_new = name_old.replace(' ', '_')
        path_full_new = path_full_old.replace(name_old, name_new)
        os.rename(path_full_old, path_full_new)
        print(f"cambiando el nombre del archivo '{name_old}' por '{name_new}'")
