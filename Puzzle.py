# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 19:26:33 2019

@author: Yolanda Gomez Henche - Borja Martin Alonso
"""

import numpy as np

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
FILAS = 4
COLUMNAS = 4

def sonIguales(vector,lista):
        for i in range(16):
            if vector[i] != lista[i]:
                return False
        return True

def buscarHueco(matriz):
    hueco = (0,0)
    for i in range(FILAS):
        for j in range(COLUMNAS):
            if matriz[i][j] == 0:
                hueco = (i,j)
    return hueco

def dameAdyacentes(matriz,iHueco,jHueco):
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

def buscarAdyacente(matriz,numero,iHueco,jHueco):
    adyacente = (iHueco,jHueco)
    if iHueco == 0:
        if jHueco == 0:
            if matriz[iHueco][jHueco+1] == numero:
                adyacente = (iHueco,jHueco+1)
            else:
                adyacente = (iHueco+1,jHueco)
        elif jHueco > 0 and jHueco < 3:
            if matriz[iHueco][jHueco-1] == numero:
                adyacente = (iHueco,jHueco-1)
            elif matriz[iHueco][jHueco+1] == numero:
                adyacente = (iHueco,jHueco+1)
            else:
                adyacente = (iHueco+1,jHueco)
        else:
            if matriz[iHueco][jHueco-1] == numero:
                adyacente = (iHueco,jHueco-1)
            else:
                adyacente = (iHueco+1,jHueco)
    elif iHueco > 0 and iHueco < 3:
        if jHueco == 0:
            if matriz[iHueco-1][jHueco] == numero:
                adyacente = (iHueco-1,jHueco)
            elif matriz[iHueco][jHueco+1] == numero:
                adyacente = (iHueco,jHueco+1)
            else:
                adyacente = (iHueco+1,jHueco)
        elif jHueco > 0 and jHueco < 3:
            if matriz[iHueco-1][jHueco] == numero:
                adyacente = (iHueco-1,jHueco)
            elif matriz[iHueco][jHueco-1] == numero:
                adyacente = (iHueco,jHueco-1)
            elif matriz[iHueco][jHueco+1] == numero:
                adyacente = (iHueco,jHueco+1)
            else:
                adyacente = (iHueco+1,jHueco)
        else:
            if matriz[iHueco-1][jHueco] == numero:
                adyacente = (iHueco-1,jHueco)
            elif matriz[iHueco][jHueco-1] == numero:
                adyacente = (iHueco,jHueco-1)
            else:
                adyacente = (iHueco+1,jHueco)
    else:
        if jHueco == 0:
            if matriz[iHueco-1][jHueco] == numero:
                adyacente = (iHueco-1,jHueco)
            else:
                adyacente = (iHueco,jHueco+1)
        elif jHueco > 0 and jHueco < 3:
            if matriz[iHueco-1][jHueco] == numero:
                adyacente = (iHueco-1,jHueco)
            elif matriz[iHueco][jHueco-1] == numero:
                adyacente = (iHueco,jHueco-1)
            else:
                adyacente = (iHueco,jHueco+1)
        else:
            if matriz[iHueco-1][jHueco] == numero:
                adyacente = (iHueco-1,jHueco)
            else:
                adyacente = (iHueco,jHueco-1)
    return adyacente
    
class Puzzle:
    
    def __init__(self,vector):
        if sonIguales(vector,lista):
            self.matriz = np.array(lista).reshape(FILAS,COLUMNAS)
        else:
            self.matriz = np.array(vector).reshape(FILAS,COLUMNAS)
        self.filas = FILAS
        self.columnas = COLUMNAS
        self.movimientos = 0
        self.hueco = buscarHueco(self.matriz)
        self.adyacentes = dameAdyacentes(self.matriz,self.hueco[0],self.hueco[1])
    
    def getFilas(self):
        return self.filas
    
    def getColumnas(self):
        return self.columnas
    
    def getMovimientos(self):
        return self.movimientos
    
    def toString(self):
        print(self.matriz)
        print()
            
    def mostrarHueco(self):
        print('Posicion libre:',self.hueco)
            
    def mostrarAdyacentes(self):
        print('Numeros adyacentes al hueco:',end=' ')
        for i in self.adyacentes:
            print(i,end=' ')
        
    def esAdyacente(self,numero):
        for i in self.adyacentes:
            if numero == i:
                return True
        return False
    
    def esSolucion(self):
        k = 0
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.matriz[i][j] != lista[k] :
                    return False
                else:
                    k+=1
        return True
    
    def recolocarPiezas(self,numero,matrizResultado):
        adyacente = buscarAdyacente(self.matriz,numero,self.hueco[0],self.hueco[1])
        self.matriz[self.hueco[0]][self.hueco[1]] = self.matriz[adyacente[0]][adyacente[1]]
        self.matriz[adyacente[0]][adyacente[1]] = 0
        self.movimientos+=1
        self.hueco = buscarHueco(self.matriz)
        self.adyacentes = dameAdyacentes(self.matriz,self.hueco[0],self.hueco[1])
                

    