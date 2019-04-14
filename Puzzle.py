# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 19:26:33 2019

@author: Yolanda Gomez Henche - Borja Martin Alonso
"""

import numpy as np

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]

def sonIguales(vector,lista):
        for i in range(16):
            if vector[i] != lista[i]:
                return False
        return True

"""def esSolucion(matriz,solucion):
    for i in range(matriz):
        for j in range(matriz[0]):
            if matriz[i][j] != solucion[i][j]:
                return False
    return True"""

def buscarHueco(matriz):
    hueco = (0,0)
    for i in range(4):
        for j in range(4):
            if matriz[i][j] == 0:
                hueco = (i,j)
    return hueco

def numAdyacentes(adyacentes):
    cont = 0
    for i in range(adyacentes):
        cont+=1
    return cont

def buscarAdyacentes(matriz,iHueco,jHueco):
    adyacentes = []
    if iHueco == 0:
        if jHueco == 0:
            adyacentes.append(matriz[iHueco][jHueco+1])
            adyacentes.append(matriz[iHueco+1][jHueco])
        elif jHueco > 0 and jHueco < 3:
            adyacentes.append(matriz[iHueco][jHueco-1])
            adyacentes.append(matriz[iHueco][jHueco+1])
            adyacentes.append(matriz[iHueco+1][jHueco])
        else:
            adyacentes.append(matriz[iHueco][jHueco-1])
            adyacentes.append(matriz[iHueco+1][jHueco])
    elif iHueco > 0 and iHueco < 3:
        if jHueco == 0:
            adyacentes.append(matriz[iHueco-1][jHueco])
            adyacentes.append(matriz[iHueco][jHueco+1])
            adyacentes.append(matriz[iHueco+1][jHueco])
        elif jHueco > 0 and jHueco < 3:
            adyacentes.append(matriz[iHueco-1][jHueco])
            adyacentes.append(matriz[iHueco][jHueco-1])
            adyacentes.append(matriz[iHueco][jHueco+1])
            adyacentes.append(matriz[iHueco+1][jHueco])
        else:
            adyacentes.append(matriz[iHueco-1][jHueco])
            adyacentes.append(matriz[iHueco][jHueco-1])
            adyacentes.append(matriz[iHueco+1][jHueco])
    else:
        if jHueco == 0:
            adyacentes.append(matriz[iHueco-1][jHueco])
            adyacentes.append(matriz[iHueco][jHueco+1])
        elif jHueco > 0 and jHueco < 3:
            adyacentes.append(matriz[iHueco-1][jHueco])
            adyacentes.append(matriz[iHueco][jHueco-1])
            adyacentes.append(matriz[iHueco][jHueco+1])
        else:
            adyacentes.append(matriz[iHueco-1][jHueco])
            adyacentes.append(matriz[iHueco][jHueco-1])
    return adyacentes

class Puzzle:
    
    def __init__(self,vector):
        if sonIguales(vector,lista):
            self.matriz = np.array(lista).reshape(4,4)
        else:
            self.matriz = np.array(vector).reshape(4,4)
        self.filas = 4
        self.columnas = 4
        self.movimientos = 0
        self.hueco = buscarHueco(self.matriz)
        self.adyacentes = buscarAdyacentes(self.matriz,self.hueco[0],self.hueco[1])
        
    def toString(self):
        print(self.matriz)
        
    def getMovimientos(self):
        return self.movimientos
    
    def mostrarHueco(self):
            print(self.hueco[0],'',self.hueco[1])
            
    def mostrarAdyacentes(self):
        tamAdyacentes = numAdyacentes(self.adyacentes)
        for i in range(tamAdyacentes):
            print(i,end='')
        
    """def recolocarPiezas(self,solucion):
        while not esSolucion(self.matriz,solucion):
            self.matriz.buscarHueco()
            print('El hueco está situado en la posicion',hueco[0],'',hueco[1])
            
            
        print('Se ha completado el puzzle')"""
        
                

    