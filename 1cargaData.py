import json
import random

# Lista de 10 nombres de productos únicos
product_names = [f"Product {chr(65 + i)}" for i in range(10)]


# Función para calcular el ajuste de precio
def calculate_price_adjustment(current_price, competitor_price, inventory):
    # Comparar precios y ajustar según inventario y diferencia con el precio de competencia
    adjustment = 0
    if current_price > competitor_price:
        # Si el precio actual es mayor que el de la competencia
        if inventory > 100:
            adjustment = -0.25 * current_price  # Disminuir 25%
        elif inventory > 10:
            adjustment = -0.10 * current_price  # Disminuir 10%
    else:
        # Si el precio actual es menor o igual al de la competencia
        if inventory > 100:
            adjustment = 0.20 * current_price  # Aumentar 20%
        elif inventory > 10:
            adjustment = 0.005 * current_price  # Aumentar 0.5%

    return round(adjustment, 2)


# Generar 800 registros con los atributos solicitados
data = []
for i in range(800):
    record = {
        "productName": random.choice(product_names),
        "currentPrice": round(random.uniform(50, 500), 2),
        "generationPrice": round(random.uniform(30, 400), 2),
        "salesQuantity": random.randint(0, 100),
        "competitorPrice": round(random.uniform(50, 500), 2),
        "inventory": random.randint(0, 200),
        "reviews": round(random.uniform(1.0, 5.0), 1),
        "seasonality": random.choice(["Winter", "Spring", "Summer", "Autumn"]),
    }
    # Asegurar que el generationPrice <= currentPrice
    if record["generationPrice"] > record["currentPrice"]:
        record["generationPrice"] = record["currentPrice"]

    # Calcular el ajuste de precio
    record["priceAdjustment"] = calculate_price_adjustment(
        record["currentPrice"],
        record["competitorPrice"],
        record["inventory"]
    )

    data.append(record)

# Guardar los datos generados en un archivo JSON para entrenamiento
with open("product_data.json", "w") as file:
    json.dump(data, file, indent=4)

print("Data generated and saved to product_data.json")
