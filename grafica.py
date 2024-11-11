# visualizations.py

import json
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error

# Cargar los datos desde el archivo JSON
with open("product_data.json", "r") as file:
    data = json.load(file)

# Convertir los datos en un DataFrame de pandas
df = pd.DataFrame(data)
df = pd.get_dummies(df, columns=["seasonality"])

# Separar las características (X) de la variable objetivo (y)
X = df.drop(columns=["priceAdjustment", "productName"])
y = df["priceAdjustment"]

# Cargar el modelo entrenado
model = joblib.load("price_adjustment_model2.pkl")

# Realizar predicciones
y_pred = model.predict(X)

# Gráfica de Importancia de Características
feature_importances = model.feature_importances_
features = X.columns
importance_df = pd.DataFrame({"Feature": features, "Importance": feature_importances}).sort_values(by="Importance", ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x="Importance", y="Feature", data=importance_df)
plt.title("Importancia de las Características")
plt.show()

# Gráfica de Dispersión: Valores Reales vs. Predicciones
plt.figure(figsize=(8, 8))
plt.scatter(y, y_pred, alpha=0.5)
plt.xlabel("Valores Reales")
plt.ylabel("Valores Predichos")
plt.title("Comparación de Valores Reales y Predichos")
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=2)
plt.show()

# Histograma de Errores
errors = y - y_pred
plt.figure(figsize=(10, 6))
sns.histplot(errors, kde=True, bins=30)
plt.xlabel("Error")
plt.title("Distribución de Errores")
plt.show()
