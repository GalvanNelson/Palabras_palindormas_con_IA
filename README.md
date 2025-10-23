# Palíndromos API

Esta pequeña aplicación expone un endpoint HTTP para predecir si una palabra es válida (palíndromo) usando un modelo de ejemplo.

Requisitos:

- Python 3.8+
- dependencias en `requirements.txt`

Instalación:

```powershell
python -m pip install -r requirements.txt
```

Ejecutar API:

```powershell
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

Endpoint:

- POST /predict  -> JSON {"texto": "cadena"}

Ejemplo de petición (PowerShell):

```powershell
$body = '{"texto":"radar"}'
Invoke-RestMethod -Method Post -Uri http://127.0.0.1:8000/predict -Body $body -ContentType 'application/json'
```
