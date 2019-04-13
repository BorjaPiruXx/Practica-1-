# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 19:26:33 2019

@author: ECI ALCORCON
"""

import numpy as np

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]

def sonIguales(vector,lista):
        for i in range(16):
            if vector[i] != lista[i]:
                return False
        return True

class Puzzle:
    
    def __init__(self,vector):
        if sonIguales(vector,lista):
            self.matriz = np.array(lista).reshape(4,4)
        else:
            self.matriz = np.array(vector).reshape(4,4)
        self.filas = 4
        self.columnas = 4
    def toString(self):
        print(self.matriz)
                

    