import matplotlib.pyplot as plt

import numpy as np

#datos 

x = np.random.rand(50)
y = np.random.rand(50)

#crear un grafico de dispersion

plt.scatter(x , y , color='purple')

#agregar etiquetas y titulo

plt.xlabel("variable X")
plt.ylabel("variable y")
plt.title("grafico de dispersion")

#mostrar el grafico

plt.show()