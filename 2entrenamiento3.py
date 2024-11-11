import json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Cargar los datos de entrenamiento desde el archivo JSON
with open("product_data.json", "r") as file:
    data = json.load(file)

# Convertir los datos en un DataFrame de pandas
df = pd.DataFrame(data)

# Codificar la variable categórica 'seasonality' usando One-Hot Encoding
df = pd.get_dummies(df, columns=["seasonality"])

# Separar las características (X) de la variable objetivo (y)
X = df.drop(columns=["priceAdjustment", "productName"])
y = df["priceAdjustment"]

# Dividir los datos en conjuntos de entrenamiento y prueba (80% entrenamiento, 20% prueba)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializar y entrenar el modelo RandomForestRegressor
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = model.predict(X_test)

# Evaluación del modelo
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R-squared:", r2)

# Guardar el modelo entrenado si los resultados son satisfactorios
joblib.dump(model, "price_adjustment_model2.pkl")

print("Modelo entrenado y guardado como 'price_adjustment_model.pkl'")
