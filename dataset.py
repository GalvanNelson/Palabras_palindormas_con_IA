import pandas as pd

def cargar_dataset():
    """Devuelve un DataFrame con el dataset usado para entrenar."""
    data = {
        'cadena': [
            'oso', 'ana', 'radar', 'reconocer', 'level', 'madam', 'rotor',
            'a', 'anna', 'civic', 'kayak', 'racecar',
            'casa', 'hola', 'robot', 'python', 'proyecto', 'inteligencia',
            'palindromo', 'automata', 'lenguaje', 'aprendizaje'
        ],
        'valido': [
            1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1,
            0, 0, 0, 0, 0, 0,
            0, 0, 0, 0
        ]
    }
    return pd.DataFrame(data)
