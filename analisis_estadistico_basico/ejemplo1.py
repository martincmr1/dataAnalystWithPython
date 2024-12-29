import numpy as np

import pandas as pd

#datos

datos = [5,7,8,9,10,11,13,15]

#media 

media = np.mean(datos)
print("media", media)

#mediana 

mediana = np.median(datos)
print("mediana",mediana)

#moda (con pandas)

moda = pd.Series(datos).mode()[0]
print("moda con pandas",moda)

#varianza

varianza = np.var(datos)
print("varianza",varianza)

#desviacion estandar 

desviacion = np.std(datos)
print("desviacion estandar",desviacion)
