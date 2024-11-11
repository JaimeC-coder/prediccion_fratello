import pickle
import pandas as pd

# Cargar el modelo entrenado desde el archivo .pkl
with open('price_adjustment_model1.pkl', 'rb') as file:
    model = pickle.load(file)

# Verifica que 'model' sea una instancia de LinearRegression
print(type(model))  # Debería mostrar: <class 'sklearn.linear_model._base.LinearRegression'>
print(model)
# Nuevos datos para predecir
new_data = {
    'currentPrice': [350],
    'competitorPrice': [300],
    'inventory': [120]
}

new_data_df = pd.DataFrame(new_data)

# Predecir el ajuste de precio con el modelo cargado
predicted_adjustment = model.predict(new_data_df)
print(f'Predicted price adjustment: {predicted_adjustment[0]}')
