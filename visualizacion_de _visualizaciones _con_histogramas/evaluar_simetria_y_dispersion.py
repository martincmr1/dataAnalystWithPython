from scipy.stats import skew, kurtosis
import numpy as np

#generar datos 

datos = np.random.normal(loc=50, scale=10, size=1000)

#calcular coeficiente de sesgo y curtosis

print("coeficiente de sesgo:", skew(datos))
print("cursosis:",kurtosis(datos))
