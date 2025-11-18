from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class PalindromoModelo:
    def __init__(self):
        # self.model se inicializa sólo si se entrena o se carga desde disco
        self.model = None

    def entrenar(self, X, y, test_size=0.2, random_state=42):
        """Entrena el modelo con X (lista de features) y y (etiquetas)."""

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
        self.model = DecisionTreeClassifier(max_depth=10, min_samples_split=2, random_state=random_state)
        self.model.fit(X_train, y_train)
        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        
        # También entrenar con todos los datos para mejor predicción en producción
        self.model.fit(X, y)
        
        return accuracy

    def predecir(self, caracteristicas):
        """Predice usando el modelo entrenado; si no hay modelo, retorna error."""
        if self.model is None:
            raise ValueError("El modelo no ha sido entrenado aún")

        return int(self.model.predict([caracteristicas])[0])

    def guardar(self, ruta):
        """Guarda el modelo en disco usando joblib."""
        try:
            import joblib
        except Exception:
            raise
        joblib.dump(self.model, ruta)

    def cargar(self, ruta):
        """Carga el modelo desde disco usando joblib."""
        try:
            import joblib
        except Exception:
            raise
        self.model = joblib.load(ruta)

    def predecir_desde_texto(self, texto, extractor_de_caracteristicas):
        """Extrae características usando la función proporcionada y predice."""
        features = extractor_de_caracteristicas(texto)
        pred = self.predecir(features)
        return {'texto': texto, 'features': features, 'prediccion': pred}
