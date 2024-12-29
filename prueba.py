import pandas as pd

# Leer el archivo CSV
df = pd.read_csv('datos.csv')

# Mostrar los datos
print("\nDatos del archivo CSV:")
print(df)

# Operaciones básicas
print("\nResumen estadístico:")
print(df.describe())

# Filtrar datos
print("\nFiltrar personas mayores de 30 años:")
print(df[df['Edad'] > 30])

# Agregar una nueva columna
df['Años de experiencia'] = [2, 5, 10, 3, 8]
print("\nDataFrame con nueva columna:")
print(df)
