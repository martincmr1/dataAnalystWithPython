import pandas as pd

#crear un dataframe

data = {
    "Nombre":["ana","luis","Maria","Pedro","juan"],
    "edad":[25,30,22,35,29],
    "ingresos":[2000,2500,2200,2700,2400],
    "horas trabajo":[40,45,38,50,42]
}

df = pd.DataFrame(data)

print(df)

print("resumen estadistico")
print(df.describe())

print("media de edad:", df["edad"].mean())

print("mediana de ingresos", df["ingresos"].median())

print("varianza de edad:", df["edad"].var())
print("desviacion estandar de edad", df["edad"].std())

print("filtrar columnas no numericas")
numericas = df.select_dtypes(include="number")
print(numericas.describe())
