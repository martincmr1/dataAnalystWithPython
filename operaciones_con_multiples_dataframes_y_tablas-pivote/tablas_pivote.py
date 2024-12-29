import pandas as pd


#dataframe de ejemplo 

data = {
    "Mes":["Enero","Enero","Febrero","Febrero"],
    "Categoria":["A","B","A","B"],
    "Ventas":[100,150,200,250]
}
df = pd.DataFrame(data)

# crear tabla pivote 

pivot = df.pivot(index="Mes",columns="Categoria", values="Ventas")

#print("\nTabla pivote:\n",pivot)

# Crear tabla pivote con suma
pivot_table = df.pivot_table(index="Mes", columns="Categoria", values="Ventas", aggfunc="sum")
print("\nTabla pivote con suma:\n", pivot_table)






