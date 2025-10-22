import tkinter as tk
from tkinter import font

from dataset import cargar_dataset
from features import extraer_caracteristicas
from model import PalindromoModelo


def crear_y_ejecutar_app():
    # Cargar y preparar datos
    df = cargar_dataset()
    X = [extraer_caracteristicas(c) for c in df['cadena']]
    y = df['valido']

    # Entrenar modelo
    modelo = PalindromoModelo()
    precision = modelo.entrenar(X, y)
    print(f"\n✅ El modelo fue entrenado con una precisión del: {precision * 100}%")

    def clasificar_cadena(cadena):
        cadena_limpia = cadena.lower().replace(" ", "")
        caracteristicas = extraer_caracteristicas(cadena_limpia)
        pred = modelo.predecir(caracteristicas)
        return "✅ Aceptada (es un palíndromo)" if pred == 1 else "❌ Rechazada (no es un palíndromo)"

    # --- GUI ---
    window = tk.Tk()
    window.title("Clasificador de Palíndromos con IA")
    window.geometry("500x250")
    window.configure(bg="#f0f0f0")

    title_font = font.Font(family="Helvetica", size=14, weight="bold")
    label_font = font.Font(family="Helvetica", size=11)
    result_font = font.Font(family="Helvetica", size=12, weight="bold")

    title_label = tk.Label(window, text="Introduce una palabra o frase", font=title_font, bg="#f0f0f0")
    title_label.pack(pady=10)

    entry = tk.Entry(window, width=40, font=label_font)
    entry.pack(pady=5)

    result_label = tk.Label(window, text="", font=result_font, bg="#f0f0f0")
    result_label.pack(pady=10)

    def on_classify_click():
        cadena_usuario = entry.get()
        if cadena_usuario:
            resultado = clasificar_cadena(cadena_usuario)
            result_label.config(text=resultado)
        else:
            result_label.config(text="Por favor, ingresa una palabra.")

    classify_button = tk.Button(window, text="Clasificar", command=on_classify_click, font=label_font, bg="#4CAF50", fg="white")
    classify_button.pack(pady=15)

    window.mainloop()
