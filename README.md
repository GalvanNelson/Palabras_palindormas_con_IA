# Clasificador de Palíndromos con IA

Proyecto refactorizado en módulos:

- `dataset.py` - carga el DataFrame de entrenamiento
- `features.py` - funciones para extraer características de cadenas
- `model.py` - clase que encapsula el modelo (DecisionTreeClassifier)
- `gui.py` - interfaz gráfica con Tkinter
- `main.py` - punto de entrada que inicia la GUI

Requisitos:
- Python 3.8+
- Instalar dependencias desde `requirements.txt` (pandas, scikit-learn, etc.)

Cómo ejecutar:

1. Crear un entorno virtual (opcional pero recomendado).
2. Instalar dependencias:

```powershell
pip install -r requirements.txt
```

3. Ejecutar la aplicación:

```powershell
python main.py
```

Notas:
- El modelo se entrena al iniciar la app. Para mejorar la detección de frases con espacios y signos, se pueden añadir pasos de limpieza adicionales en `features.py`.
