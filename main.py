# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 13:42:58 2019

@author: ECI ALCORCON
"""

from Puzzle import Puzzle
import numpy as np

aleatorios = np.random.choice(np.arange(16),16,replace=False)
matriz = Puzzle(aleatorios)
print("Matriz generada aleatoriamente")
matriz.toString()
print()

print("Matriz resultado")
resultado = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
matrizResultado = Puzzle(resultado)
matrizResultado.toString()
print()


