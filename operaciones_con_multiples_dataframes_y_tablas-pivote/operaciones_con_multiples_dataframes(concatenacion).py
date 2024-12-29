import pandas as pd

#dataframes de ejemplo 

df1 = pd.DataFrame({"ID":[1,2,3],"Nombre":["Ana","luis","Maria"]})
df2 = pd.DataFrame({"ID":[4,5,6],"Nombre":["Pedro","Juan","Sofia"]})

#concatenar verticalmente

vertical = pd.concat([df1,df2],ignore_index=True)

print("cocatenacion vertical:\n",vertical)

#cocantenar horizontalmente 

df3= pd.DataFrame({"Edad":[25,30,22]})

horizontal = pd.concat([df1,df3], axis=1)

print("\nconcatenacion horizontal:\n",horizontal)