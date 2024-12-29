import pandas as pd

#dataframes de ejemplo 

df1 = pd.DataFrame({"ID":[1,2,3],"Nombre":["ana","luis","maria"]})
df2 = pd.DataFrame({"ID":[1,2,4],"Edad":[25,30,40]})

#union (inner join por defecto)

unido= pd.merge(df1,df2, on="ID")

print("\nunion(INNER JOIN):\n",unido)

#union (left join)

unido_left = pd.merge(df1,df2, on="ID", how="left")

print("\nunion (left JOIN):\n", unido_left)

