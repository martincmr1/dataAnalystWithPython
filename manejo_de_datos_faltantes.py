import numpy as np
import pandas as pd

data = {"Col":[1,2,np.nan],"Col2":[4,np.nan,6]}

df = pd.DataFrame(data)

# Identificar valores faltantes 

print(df.isnull())

#contar valores faltantes

print(df.isnull().sum)


#rellenar los faltantes con un numero 

df_filled = df.fillna(0)

print(df_filled)

#elimina filas con valores faltantes

df_dropped = df.dropna()

print(df_dropped)


