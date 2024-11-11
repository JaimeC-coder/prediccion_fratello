import pickle
import pandas as pd
from sklearn.linear_model import LinearRegression
import json

# Cargar los datos generados desde el archivo JSON
with open('product_data.json', 'r') as file:
    data = json.load(file)

# Convertir los datos a un DataFrame
df = pd.DataFrame(data)

# Separar las características y la variable objetivo
X = df[['currentPrice', 'competitorPrice', 'inventory']]  # Características
y = df['priceAdjustment']  # Variable objetivo (ajuste de precio)

# Entrenar un modelo de regresión lineal
model = LinearRegression()
model.fit(X, y)

# Guardar el modelo entrenado en un archivo
with open('price_adjustment_model1.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Modelo entrenado y guardado correctamente.")
