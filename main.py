import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import tkinter as tk
from tkinter import font

# Un dataset más variado con diferentes longitudes y casos
data = {
    'cadena': [
        'oso', 'ana', 'radar', 'reconocer', 'level', 'madam', 'rotor', # Válidos conocidos
        'a', 'anna', 'civic', 'kayak', 'racecar', # Más válidos
        'casa', 'hola', 'robot', 'python', 'proyecto', 'inteligencia', # Inválidos
        'palindromo', 'automata', 'lenguaje', 'aprendizaje' # Más inválidos
    ],
    'valido': [
        1, 1, 1, 1, 1, 1, 1, # Etiqueta 1 para válidos
        1, 1, 1, 1, 1,
        0, 0, 0, 0, 0, 0, # Etiqueta 0 para inválidos
        0, 0, 0, 0
    ]
}

# Crear el DataFrame
df = pd.DataFrame(data)

print("--- Dataset de Entrenamiento ---")
print(df)

# Función para convertir una cadena en un vector de características numéricas
def extraer_caracteristicas(cadena):
    """
    Extrae características de una cadena para el modelo de IA.
    - Característica 1: Longitud de la cadena.
    - Característica 2: Si es un palíndromo (1) o no (0).
    """
    es_palindromo = 1 if cadena == cadena[::-1] else 0
    return [len(cadena), es_palindromo]

# Aplicar la función a nuestro dataset
X = [extraer_caracteristicas(c) for c in df['cadena']] # Características (datos de entrada)
y = df['valido'] # Etiquetas (lo que queremos predecir)

print("\n--- Características Extraídas (Ejemplo) ---")
print(f"Cadena: 'radar' -> Características: {extraer_caracteristicas('radar')}")
print(f"Cadena: 'casa'  -> Características: {extraer_caracteristicas('casa')}")

# Dividir los datos para entrenar y para probar (buena práctica)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo
modelo = DecisionTreeClassifier()

# Entrenar el modelo con los datos de entrenamiento
modelo.fit(X_train, y_train)

# Evaluar el desempeño del modelo con los datos de prueba
y_pred = modelo.predict(X_test)
print(f"\n✅ El modelo fue entrenado con una precisión del: {accuracy_score(y_test, y_pred) * 100}%")

def clasificar_cadena(cadena):
    """
    Usa el modelo entrenado para clasificar una nueva cadena.
    """
    # 1. Limpiar la cadena (opcional, pero mejora el modelo)
    cadena_limpia = cadena.lower().replace(" ", "")
    
    # 2. Extraer sus características
    caracteristicas = extraer_caracteristicas(cadena_limpia)
    
    # 3. Predecir con el modelo
    prediccion = modelo.predict([caracteristicas])[0]
    
    # 4. Devolver un resultado legible
    return "✅ Aceptada (es un palíndromo)" if prediccion == 1 else "❌ Rechazada (no es un palíndromo)"

# --- Pruebas Finales ---
print("\n--- Probando el clasificador ---")
print(f"'reconocer' -> {clasificar_cadena('reconocer')}")
print(f"'amor' -> {clasificar_cadena('amor')}")
print(f"'Anita lava la tina' -> {clasificar_cadena('Anita lava la tina')}") # Prueba de originalidad

# Función que se ejecuta al presionar el botón
def on_classify_click():
    cadena_usuario = entry.get()
    if cadena_usuario:
        resultado = clasificar_cadena(cadena_usuario)
        result_label.config(text=resultado)
    else:
        result_label.config(text="Por favor, ingresa una palabra.")

# --- Configuración de la ventana ---
window = tk.Tk()
window.title("Clasificador de Palíndromos con IA")
window.geometry("500x250")
window.configure(bg="#f0f0f0")

# --- Creación de los componentes (widgets) ---
title_font = font.Font(family="Helvetica", size=14, weight="bold")
label_font = font.Font(family="Helvetica", size=11)
result_font = font.Font(family="Helvetica", size=12, weight="bold")

title_label = tk.Label(window, text="Introduce una palabra o frase", font=title_font, bg="#f0f0f0")
title_label.pack(pady=10)

entry = tk.Entry(window, width=40, font=label_font)
entry.pack(pady=5)

classify_button = tk.Button(window, text="Clasificar", command=on_classify_click, font=label_font, bg="#4CAF50", fg="white")
classify_button.pack(pady=15)

result_label = tk.Label(window, text="", font=result_font, bg="#f0f0f0")
result_label.pack(pady=10)

# --- Iniciar la aplicación ---
window.mainloop()