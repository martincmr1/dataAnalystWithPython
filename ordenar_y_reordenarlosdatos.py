import pandas as pd

data = {
    "Nombre": ["Ana","Luis","Maria"],
    "Edad":[25,30,22]
}

df = pd.DataFrame(data)

#ordenar la columna por edad 

df_shorted = df.sort_values("Edad")

print(df_shorted)


#aplicar funciones a los datos 

df["Edad en 5 años"] = df["Edad"].apply(lambda x:x+5)

print(df)