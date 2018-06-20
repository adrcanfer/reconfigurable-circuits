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
    
    
    if(i == 0):
        for j in range(n):
            puerta = circuito[i][j][0]
            conexiones_iniciales = circuito[i][j][1]
            if(puerta == 'AND'):
                if(vector_entrada2[conexiones_iniciales[0]] + vector_entrada2[conexiones_iniciales[1]] == 2):
                    vector_salida.append(1)
                else:
                    vector_salida.append(0)
                    
                
            if(puerta == 'OR'):
                if(vector_entrada2[conexiones_iniciales[0]] + vector_entrada2[conexiones_iniciales[1]] >= 1):
                    vector_salida.append(1)
                else:
                    vector_salida.append(0)
                  
            if(puerta == 'NOT'):
                if(vector_entrada2[conexiones_iniciales[0]] == 0):
                    vector_salida.append(1)
                else:
                    vector_salida.append(0)
                  
            if(puerta == 'NAND'):
                if(vector_entrada2[conexiones_iniciales[0]] + vector_entrada2[conexiones_iniciales[1]] == 2):
                    vector_salida.append(0)
                else:
                    vector_salida.append(1)
                
            if(puerta == 'XOR'):
                if(vector_entrada2[conexiones_iniciales[0]] + vector_entrada2[conexiones_iniciales[1]] == 1):
                    vector_salida.append(1)
                else:
                    vector_salida.append(0)
               
            if(puerta == '--'):
                    vector_salida.append(0)     
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
                    vector_salida.append(1)
                else:
                    vector_salida.append(0)
            
            if(puerta == '--'):
                    vector_salida.append(0)     
              
             
    return vector_salida;

def resultado_circuito (vector_entrada1, vector_entrada2, circuito, m, n):
    vector_salida = []
    for i in range(m):
       vector_salida = resultado_circuito_capas (vector_entrada1, vector_entrada2, circuito, i, n)
       vector_entrada1 = vector_entrada2
       vector_entrada2 = vector_salida
    return vector_entrada2


def resultado_circuito_defectuoso (vector_entrada1, vector_entrada2, puertas_defectuosas, circuito, m, n):
    vector_salida = []
    for i in range(len(puertas_defectuosas)):
        circuito[puertas_defectuosas[i][0]][puertas_defectuosas[i][1]][0] = '--'
        
    for i in range(m):
       vector_salida = resultado_circuito_capas (vector_entrada1, vector_entrada2, circuito, i, n)
       vector_entrada1 = vector_entrada2
       vector_entrada2 = vector_salida
    return vector_entrada2

print('Estructura de datos para la definición de un circuito')

#CON UNA NOT AL FINAL EL METODO NO FUNCIONA
#programacionPuertas = ['AND', 'OR', '--', 'OR', 'NOT', '--', 'NAND', 'AND', '--', 'XOR', 'AND', 'OR']
#conexiones = [[0,1], 
#          [1,2],
#          [],
#          [2,3],
#          [[0,0]],
#          [],
#          [[0,0], [0,1]],
#          [[0,1],[0,3]],
#          [],
#          [[0,0], [1,0]],
#          [[1,0],[1,2]],
#          [[1,2],[1,3]]]


#m = 3
#n = 4


programacionPuertas = ['AND', 'OR', '--', 'NOT', '--', 'NAND', '--', 'XOR', 'AND']
conexiones = [[0,1], 
          [1,2],
          [],
          [[0,0]],
          [],
          [[0,0], [0,1]],
          [],
          [[0,0], [1,0]],
          [[1,0],[1,2]]]


m = 3
n = 3


circuito = estructura_circuito(m,n, programacionPuertas, conexiones)

vector_entrada1 = [0,0,0]
#vector_entrada2 = [0,0,1]
puertas_defectuosas = [[0,1],
                       [1,2]]

#vector_salida = resultado_circuito (vector_entrada1, vector_entrada2, circuito, m, n)
#vector_salida_defectuoso = resultado_circuito_defectuoso(vector_entrada1, vector_entrada2, puertas_defectuosas, circuito, m, n)




#sprint("Vector de salida: ")
#print(vector_salida)
#print("Vector de salida defectuoso: ")
#print(vector_salida_defectuoso)





vectores_entrada_inicial= [[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]]

def f_vectores_salida(vectores_entrada,vector_entrada1,circuito,m,n):
    vec_salida=[]
    vectores_entrada_nuevo= calcula_vectores_entrada(vectores_entrada,n)
    for i in range(len(vectores_entrada_nuevo)):
        vec_salida.append(resultado_circuito(vector_entrada1,vectores_entrada_nuevo[i],circuito,m,n))
    return vec_salida

#para n mayor que tres, cada vector de entrada se le añadirá un cero, es decir, si n fuese 5, el primer vector de entrada
#seria [0,0,0,0,0] y el segundo seria [0,0,1,0,0]. Se le añade tantos ceros según la diferencia de n-3
def calcula_vectores_entrada(vectores_entrada,n):
    vectores_entrada_nuevo= vectores_entrada

    if(n<3):
        for i in range(len(vectores_entrada_nuevo)):
            vectores_entrada_nuevo.pop()
        vectores_entrada_nuevo.append([0,0])
        vectores_entrada_nuevo.append([0,1])
        vectores_entrada_nuevo.append([1,0])
        vectores_entrada_nuevo.append([1,1])
    elif (n>3):
        vectores_entrada_nuevo=vectores_entrada
        for i in range(len(vectores_entrada)):
            for j in range(3,n):
                vectores_entrada_nuevo[i].append(0)
    return vectores_entrada_nuevo


def calcula_vectores_salida_defectuosos(vectores_entrada):
    vectores_salida_defec=[]

    for i in range(len(vectores_entrada)):
        vectores_salida_defec.append(resultado_circuito_defectuoso(vector_entrada1, vectores_entrada[i], puertas_defectuosas,circuito,m,n))
    return vectores_salida_defec



def auto_diagnostico(vect_ent,vectores_entrada_inicial,vector_entrada1, circuito, puertas_defectuosas,m,n):
    res= True
    vectores_e=calcula_vectores_entrada(vectores_entrada_inicial,n)#Vectores entrada

    #Calculo el vector de salida defectuoso del vector de entrada que le pasamos por parametro
    #vector_sal_def= resultado_circuito_defectuoso(vector_entrada1,vect_ent,puertas_defectuosas,circuito,m,n)
    vectores_s= f_vectores_salida(vectores_entrada_inicial,vector_entrada1,circuito,m,n)#Vectores salida

    #Compruebo que el vector de salida defectuoso coincide con el vector de salida correcto


    for i in range(len(vectores_e)):
        for j in range(len(vectores_e[i])):
            if(vectores_e[i][j]==vect_ent[j]):
                vect_sal_aux_def= resultado_circuito_defectuoso(vector_entrada1,vect_ent,circuito,puertas_defectuosas,m,n)

                for z in range(len(vectores_s)):
                    for x in range(len(vectores_s[z])):
                        if(vectores_s[z][x] != vect_sal_aux_def[x]):
                            res=False
                            break
                        break
                    break
                break
            break
        break
    return res

print(calcula_vectores_entrada(vectores_entrada_inicial,n))
print(f_vectores_salida(vectores_entrada_inicial,vector_entrada1,circuito,m,n))
print(calcula_vectores_salida_defectuosos(vectores_entrada_inicial))
print(auto_diagnostico([0,0,0], vectores_entrada_inicial,vector_entrada1,circuito,puertas_defectuosas,m,n))


