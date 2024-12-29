import numpy as np



matriz_a = np.array([[1,2],
                     [3,4]])

matriz_b= np.array([[5,6],
                    [7,8]])

print("suma")
print(matriz_a+matriz_b) 

print("multiplicacion elemento a elemento")

print(matriz_a*matriz_b)

#producto punto
print("multiplicacion matricial:")

print(np.dot(matriz_a,matriz_b))

#transposcion de matrices
matriz = np.array([[2, 4, 6],
                    [8, 10, 12],
                    [14,16,18]])


print("matriz transpuesta")
print(matriz.T)