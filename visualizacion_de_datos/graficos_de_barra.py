import matplotlib.pyplot as plt

#datos

categorias = ["A","B","C","D"]
valores = [5,7,3,8]

# crear un grafico de barras 

plt.bar(categorias,valores, color='skyblue')

# agregar estiquetas y título

plt.xlabel("categorias")
plt.ylabel("valores")
plt.title("Grafico de barras")

#mostrar el grafico

plt.show()

