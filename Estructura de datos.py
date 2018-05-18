# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

def estructura_circuito(m,n, programacionPuertas, inputs):
    estructura = []
    for i in range (m):
        puertas = [];
        for j in range(n):
            puertas.append([programacionPuertas[(i*n)+j], inputs[(i*n)+j]]);
        estructura.append(puertas);
    return estructura;



def resultado_circuito_capas (vector_entrada1, vector_entrada2, circuito, i, n):
    vector_salida = []
    contador_entrada = 0;
    
    
    if(i == 0):
        for j in range(n):
            puerta = circuito[i][j][0]
            if(puerta == 'AND'):
                if(vector_entrada2[contador_entrada] + vector_entrada2[contador_entrada + 1] == 2):
                    vector_salida.append(1)
                else:
                    vector_salida.append(0)
                    contador_entrada += 2
           
                
            if(puerta == 'OR'):
                if(vector_entrada2[contador_entrada] + vector_entrada2[contador_entrada + 1] >= 1):
                    vector_salida.append(1)
                else:
                    vector_salida.append(0)
                    contador_entrada += 2
              
            if(puerta == 'NOT'):
                if(vector_entrada2[contador_entrada] == 0):
                    vector_salida.append(1)
                else:
                    vector_salida.append(0)
                    contador_entrada += 1
              
            if(puerta == 'NAND'):
                if(vector_entrada2[contador_entrada] + vector_entrada2[contador_entrada + 1] == 2):
                    vector_salida.append(0)
                else:
                    vector_salida.append(1)
                contador_entrada += 2 
              
            if(puerta == 'XOR'):
                if(vector_entrada2[contador_entrada] + vector_entrada2[contador_entrada + 1] == 1):
                    vector_salida.append(0)
                else:
                    vector_salida.append(1)
                contador_entrada += 2
                
    if(i > 0):
        for j in range(n):
            puerta = circuito[i][j][0]
            conexiones = circuito[i][j][1]
            valor1 = 0
            valor2 = 0
            if(puerta == 'AND'):
                if(conexiones[0][0] == i-2):
                    valor1 = vector_entrada1[conexiones[0][1]]
                else:
                    valor1 = vector_entrada2[conexiones[0][1]]
                if(conexiones[1][0] == i-2):
                    valor2 = vector_entrada1[conexiones[1][1]]
                else:
                    valor2 = vector_entrada2[conexiones[1][1]]
                if(valor1 + valor2 == 2):
                    vector_salida.append(1)
                else:
                    vector_salida.append(0)
           
                
            if(puerta == 'OR'):
                if(conexiones[0][0] == i-2):
                    valor1 = vector_entrada1[conexiones[0][1]]
                else:
                    valor1 = vector_entrada2[conexiones[0][1]]
                if(conexiones[1][0] == i-2):
                    valor2 = vector_entrada1[conexiones[1][1]]
                else:
                    valor2 = vector_entrada2[conexiones[1][1]]
                if(valor1 + valor2 >= 1):
                    vector_salida.append(1)
                else:
                    vector_salida.append(0)
                    
              
            if(puerta == 'NOT'):
                if(conexiones[0][0] == i-2):
                    valor1 = vector_entrada1[conexiones[0][1]]
                else:
                    valor1 = vector_entrada2[conexiones[0][1]]
                
                if(valor1 == 0):
                    vector_salida.append(1)
                else:
                    vector_salida.append(0)
                    contador_entrada += 1
                    
              
            if(puerta == 'NAND'):
                if(conexiones[0][0] == i-2):
                    valor1 = vector_entrada1[conexiones[0][1]]
                else:
                    valor1 = vector_entrada2[conexiones[0][1]]
                if(conexiones[1][0] == i-2):
                    valor2 = vector_entrada1[conexiones[1][1]]
                else:
                    valor2 = vector_entrada2[conexiones[1][1]]
                
                if(valor1 + valor2 == 2):
                    vector_salida.append(0)
                else:
                    vector_salida.append(1)
                contador_entrada += 2 
              
            if(puerta == 'XOR'):
                if(conexiones[0][0] == i-2):
                    valor1 = vector_entrada1[conexiones[0][1]]
                else:
                    valor1 = vector_entrada2[conexiones[0][1]]
                if(conexiones[1][0] == i-2):
                    valor2 = vector_entrada1[conexiones[1][1]]
                else:
                    valor2 = vector_entrada2[conexiones[1][1]]
                
                if(valor1 + valor2 == 1):
                    vector_salida.append(0)
                else:
                    vector_salida.append(1)
                contador_entrada += 2
              
             
    return vector_salida;

def resultado_circuito (vector_entrada1, vector_entrada2, circuito, m, n):
    vector_salida = []
    for i in range(m):
       vector_salida = resultado_circuito_capas (vector_entrada1, vector_entrada2, circuito, i, n)
       vector_entrada1 = vector_entrada2
       vector_entrada2 = vector_salida
    return vector_entrada2



print('Estructura de datos para la definición de un circuito')

programacionPuertas = ['NOT', 'OR', 'NOT', 'NAND', 'XOR', 'AND']
conexiones = [[], 
          [],
          [[0,0]],
          [[0,0], [0,1]],
          [[0,0], [1,0]],
          [[0,0], [1,1]]]


m = 3
n = 2

circuito = estructura_circuito(m,n, programacionPuertas, conexiones)

vector_entrada1 = [0,0,0]
vector_entrada2 = [0,0,0]

vector_salida = resultado_circuito (vector_entrada1, vector_entrada2, circuito, m, n)
print(vector_salida)

