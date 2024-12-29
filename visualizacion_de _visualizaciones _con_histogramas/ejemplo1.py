import matplotlib.pyplot as plt

import numpy as np

#generar datos

datos = np.random.normal(loc=50, scale=10, size=1000)   #distribucion nomal 

#crear un histograma 

plt.hist(datos, bins=20 , color='skyblue', edgecolor='black')

#etiquetas y titulo

plt.xlabel("valor")
plt.ylabel("frecuencia")
plt.title("histograma de la distribucion")

#mostrar el grafico

plt.show()