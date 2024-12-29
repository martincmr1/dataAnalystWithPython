import pandas as pd
import matplotlib.pyplot as plt
# Crear el DataFrame con un diccionario




lubricantes= {
    'Producto': ['Aceite', 'Grasa', 'Lubricante'],
    'Cantidad': [10, 15, 8],
    'Precio': [2.5, 1.8, 3.0]

}
df = pd.DataFrame(lubricantes)

print('lista de lubricantes creada')
print(df)

# calcular total (precio*cantidad) 

df ['total'] = df ['Cantidad'] * df ['Precio']

print ("\nDataframe con columna total ")

print (df)

df = df.sort_values(by='total', ascending=False)

print ("\nDataframe ordenado por total (de mayor a menor):")

print(df)

df = df[df['Precio'] >2.0]

print("\nPrecios mayores a 2.0")

print(df['Precio'])

print("\nDataFrame después de filtrar por precio mayor a 2.0:")
print(df)


df.to_csv('lubricantes_filtrados.csv',index=False)

print("\nDataframe exportado a csv")



plt.bar(df['Producto'],df['Precio'],color=['red','green'])
plt.title('Precios de Productos')
plt.xlabel('Producto')
plt.ylabel('Precio')
plt.show()


for i, precio in enumerate(df['Precio']):
    plt.text(i, precio + 0.1, f'{precio}', ha='center')


plt.savefig('grafico_precios.png')
