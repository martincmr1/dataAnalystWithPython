import matplotlib.pyplot as plt

#Datos 

x = [1,2,3,4,5]
y = [2,4,6,8,10]

# crear un grafico de linea

plt.plot(x,y, label="Linea de ejemplo")

# agregar etiquetas y titulo

plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("grafico de linea simple")
plt.legend()

#mostrar el grafico 

plt.show() 
