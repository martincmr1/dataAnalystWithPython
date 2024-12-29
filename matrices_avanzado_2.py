import numpy as np

from numpy.linalg import det , inv

matriz = np.array([[1,2],
                  [3,4]])

#determinante 

print("determinante:")
print(det(matriz))

#inversa 

print("inversa")
print(inv(matriz))

matriz_2 = np.array([[10,20,30],
                     [40,50,60],
                     [70,80,90]])

#seleccionar multiples elementos 

print("seleccionar filas 0 y 2:")
print(matriz_2[[0,2]])

#seleccionar elemento mayores a 50

print("elementos mayores a 50")
print(matriz_2[matriz_2 > 50])
