import matplotlib.pyplot as plt

# Crear un gráfico simple
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 35]

plt.plot(x, y, label="Línea de ejemplo")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Gráfico simple")
plt.legend()
plt.show()
