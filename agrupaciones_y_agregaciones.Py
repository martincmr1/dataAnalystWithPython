import pandas as pd

data = {
    "Categoria":["A","B","A","B","A" ],
    "Valor":[10,20,30,40,50]
}

df = pd.DataFrame(data)

#agrupar por categoria y sumar valores

grupo = df.groupby("Categoria")["Valor"].sum()

print(grupo)


# Resultado:
# Categoría
# A    90
# B    60
# Name: Valor, dtype: int64