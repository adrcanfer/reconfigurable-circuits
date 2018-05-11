# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
print('Estructura de datos para la definición de un circuito')

programacionPuertas = ['AND', 'OR', 'NOT', 'NAND', 'XOR', 'AND']
inputs = [[], 
          [],
          [[0,0]],
          [[0,0], [0,1]],
          [[0,0], [1,0]],
          [[0,0], [1,1]]]




def estructura_circuito(m,n, programacionPuertas):
    estructura = []
    for i in range (m):
        puertas = [];
        for j in range(n):
            puertas.append([programacionPuertas[(i*n)+j], inputs[(i*n)+j]]);
        estructura.append(puertas);
    return estructura;

prueba1 = estructura_circuito(3,2, programacionPuertas)
print(prueba1[0])
