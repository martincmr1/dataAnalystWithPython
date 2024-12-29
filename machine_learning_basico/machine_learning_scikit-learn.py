import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import matplotlib.pyplot as plt

# Datos ficticios
data = {
    "Tamaño (m2)": [50, 60, 70, 80, 100, 120, 150],
    "Precio (miles)": [100, 120, 140, 160, 200, 240, 300]
}
df = pd.DataFrame(data)

# Variables independientes (X) y dependientes (y)
X = df[["Tamaño (m2)"]]
y = df["Precio (miles)"]

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo de regresión lineal
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Predecir precios en el conjunto de prueba
y_pred = modelo.predict(X_test)

# Evaluar el modelo
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Errores del modelo:")
print(f"MAE (Error Absoluto Medio): {mae:.2f}")
print(f"R2 (Coeficiente de determinación): {r2:.2f}")

# Visualizar el modelo
plt.scatter(df["Tamaño (m2)"], df["Precio (miles)"], color="blue", label="Datos reales")
plt.plot(df["Tamaño (m2)"], modelo.predict(X), color="red", label="Línea de regresión")
plt.xlabel("Tamaño (m2)")
plt.ylabel("Precio (miles)")
plt.title("Regresión Lineal: Tamaño vs Precio")
plt.legend()
plt.show()
