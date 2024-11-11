import json
import pandas as pd
import joblib

# Cargar el modelo entrenado
loaded_model = joblib.load("price_adjustment_model2.pkl")

# Verificar el tipo de modelo cargado
print(f"Tipo de modelo cargado: {type(loaded_model)}")

# Nuevos datos para hacer la predicción (asegurarse de que todas las características estén presentes)
new_data = {
    'currentPrice': [350],
    'generationPrice': [300],  # Asegurarse de incluir 'generationPrice'
    'salesQuantity': [80],  # Asegurarse de incluir 'salesQuantity'
    'competitorPrice': [300],
    'inventory': [120],
    'reviews': [4.5],
    'seasonality_Autumn': [1],
    'seasonality_Spring': [0],
    'seasonality_Summer': [0],
    'seasonality_Winter': [0]
}

# Crear el DataFrame con los datos de entrada
new_data_df = pd.DataFrame(new_data)

# Verificar las columnas que el modelo espera para la predicción
expected_columns = loaded_model.feature_importances_.shape[0]  # Este es el número de columnas que el modelo espera
print("Columnas esperadas en el modelo:", expected_columns)

# Asegurarse de que las columnas de entrada coincidan con las del entrenamiento
missing_columns = [col for col in loaded_model.feature_importances_ if col not in new_data_df.columns]
print("Columnas faltantes:", missing_columns)

# Si todo está en orden, realizar la predicción
predicted_adjustment = loaded_model.predict(new_data_df)

# Mostrar el ajuste de precio predicho
print(f'Predicted price adjustment: {predicted_adjustment[0]}')
