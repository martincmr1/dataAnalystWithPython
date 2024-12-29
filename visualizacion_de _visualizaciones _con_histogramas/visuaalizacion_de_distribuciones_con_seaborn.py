import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Generar datos
datos = np.random.normal(loc=50, scale=10, size=1000)  # Cambiar 'local' por 'loc'

# Crear el histograma con Seaborn
sns.histplot(datos, bins=20, kde=True, color='purple')  # kde=True agrega la curva de densidad

# Etiquetas y título
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.title("Distribución con Seaborn")

# Mostrar el gráfico
plt.show()
