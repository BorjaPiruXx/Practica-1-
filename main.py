# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 13:42:58 2019

@author: Yolanda Gomez Henche - Borja Martin Alonso
"""

from Puzzle import Puzzle
import numpy as np

def esMultiplo(movimientos,multiplo):
    return (movimientos%multiplo) == 0

print('Esta es la vista del puzzle resuelto')
print()
resultado = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
matrizResultado = Puzzle(resultado)
matrizResultado.toString()
explicacion = 'Usted debe generar ese mismo puzzle a partir de otro diferente cuyas posiciones estan colocadas aleatoriamente. ¿Desea resolver el puzzle? [s/n]: '
letra1 = input(explicacion)
nombreUsuario = 'Nombre de Usuario: '
usuario = input(nombreUsuario)
print()
partidas = 0
movimientosMejorPartida = 0
while letra1 == 's' or letra1 == 'S':
    partidas+=1
    aleatorios = np.random.choice(np.arange(16),16,replace=False)
    matriz = Puzzle(aleatorios)
    matriz.toString()
    matriz.mostrarHueco()
    matriz.mostrarAdyacentes()
    while not matriz.esSolucion():
        escogerNumero = 'De esos numeros adyacentes, ¿cual desea escoger?: '
        numero = int(input(escogerNumero))
        print()
        while not matriz.esAdyacente(numero):
            numero = int(input('El numero que has seleccionado no es adyacente, por favor introduzca un numero correcto: '))
        matriz.recolocarPiezas(numero,matrizResultado)
        if esMultiplo(matriz.getMovimientos(),10):
            rendirse = '¿Desea rendirse?[s/n]: '
            letra2 = input(rendirse)
            print()
            if letra2 == 's' or letra2 == 'S':
                letra1 = 'n'
                break
        matriz.toString()
        print('Numero de movimientos realizados:',matriz.getMovimientos())
        matriz.mostrarHueco()
        matriz.mostrarAdyacentes()
        if matriz.esSolucion():
            break
    if matriz.esSolucion():
        print('¡Genial has resuelto el puzzle en ',matriz.getMovimientos(),' movimientos!')
        if partidas == 1:
            archivo = open("ganadores.txt","w")
            archivo.writelines(usuario,' --> ',str((matriz.getMovimientos)))
            archivo.close()
        else:
            if matriz.getMovimientos < movimientosMejorPartida:
                movimientosMejorPartida = matriz.getMovimientos()
                archivo = open("ganadores.txt","a")
                archivo.writelines(usuario,' --> ',str((movimientosMejorPartida)))
                archivo.close()
        reintento = ', ¿quiere volver a reconstruir el puzzle?[s/n]: '
        letra1 = input(usuario,reintento)
        if letra1 == 'n' or 'N':
            break
print('¡Hasta la proxima!')
            



