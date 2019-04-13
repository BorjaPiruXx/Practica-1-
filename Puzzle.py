# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 19:26:33 2019

@author: ECI ALCORCON
"""

import numpy as np

aleatorios = np.random.choice(np.arange(16),16,replace=False)

class Puzzle:
    
    def __init__(self): 
        self.matriz = np.array(aleatorios).reshape(4,4)
        self.filas = 4
        self.columnas = 4
    def toString(self):
        print(self.matriz)
                

    