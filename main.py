# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 13:42:58 2019

@author: Yolanda Gomez Henche - Borja Martin Alonso
"""

from Puzzle import Puzzle
import numpy as np

print("Esta es la vista del puzzle resuelto")
print()
resultado = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
matrizResultado = Puzzle(resultado)
matrizResultado.toString()
print()

print('Usted debe generar ese mismo puzzle a partir de otro diferente',end='')
print('cuyas posiciones estan colocadas aleatoriamente',end='.')
print('¿Desea resolver el puzzle? [s/n]:')
letra = input()
if letra == 's' or letra == 'S':
    aleatorios = np.random.choice(np.arange(16),16,replace=False)
    matriz = Puzzle(aleatorios)
    matriz.toString()
    print()
    print('Posicion libre:',matriz.mostrarHueco())
    print('Numeros adyacentes al hueco:',matriz.mostrarAdyacentes())    
else:
    print('¡Hasta la proxima!')



