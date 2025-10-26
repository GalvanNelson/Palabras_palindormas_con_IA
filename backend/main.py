from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from dataset import cargar_dataset
from features import extraer_caracteristicas
from model import PalindromoModelo

app = FastAPI(title="Palíndromos API", version="0.1")


class PredictRequest(BaseModel):
    texto: str


class PredictResponse(BaseModel):
    texto: str
    features: list
    prediccion: int


# Cargar y entrenar modelo al inicio (simple, pequeño dataset de ejemplo)
modelo = PalindromoModelo()
df = cargar_dataset()
X = df['cadena'].apply(lambda s: extraer_caracteristicas(s)).tolist()
y = df['valido'].tolist()

try:
    modelo.entrenar(X, y)
    print("Precisión del modelo:", modelo.entrenar(X, y))
    print("Modelo entrenado con éxito.")    
except Exception:
    # si falta scikit-learn en el entorno de edición, dejamos el modelo vacío
    pass


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predecir", response_model=PredictResponse)
def predict(req: PredictRequest):
    if req.texto is None:
        raise HTTPException(status_code=400, detail="`texto` requerido")
    try:
        resultado = modelo.predecir_desde_texto(req.texto, extraer_caracteristicas)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return resultado
