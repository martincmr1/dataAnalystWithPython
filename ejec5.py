import numpy as np

matriz = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])

print("suma de todos los elementos de la matriz")
print(np.sum(matriz))

matriz_2 = np.array([[2,4],
                     [6,8]])

print(matriz_2.reshape(4,1))

matriz_3 = np.array([[3,6,9],
                     [12,15,18],
                     [21,24,27]])

#1: → Desde la segunda fila en adelante.
#1: → Desde la segunda columna en adelante.

print(matriz_3[1:,1:])

matriz_4= np.array([[1,2,3],
                    [4,5,6],
                    [7,8,9]])
print("matriz diagonal")
print(np.diag(matriz_4))

matriz_5 = np.array([[1,2],
                     [3,4]])

print("pregunta 9 mutiplicacion matricial")
print(np.dot(matriz_5,matriz_5))

matriz_6 = np.array([[1,2,3],
                     [4,5,6]])

print("pregunta 10 concatenacion horizontal")
print(np.stack((matriz_6,matriz_6)))



