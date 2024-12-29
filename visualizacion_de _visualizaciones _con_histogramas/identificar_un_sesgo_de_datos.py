import matplotlib.pyplot as plt

import numpy as np

#generar datos con sesgo positivo

datos_sesgados = np.random.exponential(scale=10, size=1000)

#crear un histograma

plt.hist(datos_sesgados, bins=20, color='orange', edgecolor='black')
plt.xlabel("valor")
plt.ylabel("frecuencia")
plt.title("hisgrama con sesgo possitivo")
plt.show()
