import pandas as pd  

data = {
    "Nombre": ["Ana","Luis","Maria"],
    "Edad":[25,30,22],
    "Ciudad":["Madrid","Barcelona","Sevilla"]
}

df = pd.DataFrame(data)

print("\nDataframe completo")
print(df)

print("primeras filas")
print(df.head()) #primeras 5 filas

print("\nInformacion del dataframe")
print(df.info())

 # df = pd.read_csv("datos.csv")
# print(df.head()) #mostrar las primeras filas

#df.to_csv("archivo_salida2.csv", index=False)

#seleccionar columnas
print(df["Nombre"]) #una columna

print(df[["Nombre","Ciudad"]])

#selecionar filas por indice

print("fila cero por etiqueta")
print(df.loc[0]) #fila 0 por etiqueta

print("fila 0 por posicion")
print(df.iloc[0])

print("filtrar personas mayores de 25 años")
mayores_25 = df[df["Edad"] > 25]
print(mayores_25)

print("agregar una columna")
df["Saludo"] = "hola"
print(df)

print("modificar valores")

df.loc[0, "Edad"] = 26

df.loc[0, "Ciudad"] = "Berlin"

print(df)

