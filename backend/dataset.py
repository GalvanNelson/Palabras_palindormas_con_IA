import pandas as pd

def cargar_dataset():
    """Devuelve un DataFrame con el dataset usado para entrenar."""
    data = {
        'cadena': [
            # Palíndromos verdaderos
            'oso', 'ana', 'radar', 'reconocer', 'level', 'madam', 'rotor',
            'a', 'anna', 'civic', 'kayak', 'racecar', 'noon', 'deed',
            'refer', 'sagas', 'solos', 'stats', 'tenet', 'wow',
            'bob', 'dad', 'mom', 'pop', 'aba', 'ece', 'iji',
            # No palíndromos
            'casa', 'hola', 'robot', 'python', 'proyecto', 'inteligencia',
            'palindromo', 'automata', 'lenguaje', 'aprendizaje',
            'computadora', 'algoritmo', 'programar', 'datos',
            'variable', 'funcion', 'clase', 'objeto', 'metodo',
            'codigo', 'software', 'hardware', 'tecnologia'
        ],
        'valido': [
            # Palíndromos (27)
            1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1,
            # No palíndromos (23)
            0, 0, 0, 0, 0, 0,
            0, 0, 0, 0,
            0, 0, 0, 0,
            0, 0, 0, 0, 0,
            0, 0, 0, 0
        ]
    }
    return pd.DataFrame(data)
