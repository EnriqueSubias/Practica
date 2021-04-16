#! /usr/bin/python3

import os
import sys 

f = open(sys.argv[1], "r")
result = f.readline()
print(result, end = '')

ejemplo_dir = '/Users/enriquesubias/Documents/GitHub/Practica'
with os.scandir(ejemplo_dir) as ficheros:
    ficheros = [fichero.name for fichero in ficheros if fichero.is_file() and fichero.name.endswith('.in')]
print(ficheros)

