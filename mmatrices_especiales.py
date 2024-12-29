import numpy as np

print("matriz identidad")
print(np.eye(3))

print("matriz de ceros")
print(np.zeros((2,3)))

print("matriz de unos:")
print(np.zeros((2,3)))

print("matriz de unos")
print(np.ones((3,2)))

matriz_a = np.array([[1,2],
                     [3,4]])

matriz_b = np.array([[5,6],
                     [7,8]])

#concatenar horizontalmente

print("concatenacion horizontal")
print(np.hstack((matriz_a,matriz_b)))

print("concatenacion vertical")
print(np.vstack((matriz_a,matriz_b)))

matriz_3 = np.array([1,2,3,4,5,6])

#convertir a matriz 2x3 
print("reorganizar a 2x3:")

print(matriz_3.reshape(2,3))
