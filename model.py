from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class PalindromoModelo:
    def __init__(self):
        self.model = DecisionTreeClassifier()

    def entrenar(self, X, y, test_size=0.2, random_state=42):
        """Entrena el modelo con X (lista de features) y y (etiquetas)."""
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
        self.model.fit(X_train, y_train)
        y_pred = self.model.predict(X_test)
        return accuracy_score(y_test, y_pred)

    def predecir(self, caracteristicas):
        return int(self.model.predict([caracteristicas])[0])
