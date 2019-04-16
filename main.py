# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 13:42:58 2019

@author: Yolanda Gomez Henche - Borja Martin Alonso
"""

from Puzzle import Puzzle
import numpy as np

print('Esta es la vista del puzzle resuelto')
print()
resultado = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
matrizResultado = Puzzle(resultado)
matrizResultado.toString()
explicacion = 'Usted debe generar ese mismo puzzle a partir de otro diferente cuyas posiciones estan colocadas aleatoriamente. ¿Desea resolver el puzzle? [s/n]: '
letra = input(explicacion)
print()
if letra == 's' or letra == 'S':
    aleatorios = np.random.choice(np.arange(16),16,replace=False)
    matriz = Puzzle(aleatorios)
    matriz.toString()
    matriz.mostrarHueco()
    matriz.mostrarAdyacentes()
    while not matriz.esSolucion():
        escogerNumero = 'De esos numeros adyacentes, ¿cual desea escoger?: '
        numero = int(input(escogerNumero))
        while not matriz.esAdyacente(numero):
            numero = int(input('El numero que has seleccionado no es adyacente, por favor introduzca un numero correcto: '))
        print()
        matriz.recolocarPiezas(numero,matrizResultado)
        matriz.toString()
        print('Numero de movimientos realizados:',matriz.getMovimientos())
        matriz.mostrarHueco()
        matriz.mostrarAdyacentes()
        if matriz.esSolucion():
            break
    print('¡Genial has resuelto el puzzle en ',matriz.getMovimientos(),' movimientos!')
else:
    print('¡Hasta la proxima!')



