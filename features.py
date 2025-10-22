def extraer_caracteristicas(cadena: str):
    """Extrae características numéricas de una cadena.

    - Característica 1: longitud de la cadena (int)
    - Característica 2: si es palíndromo (1) o no (0)
    """
    if cadena is None:
        cadena = ""
    es_palindromo = 1 if cadena == cadena[::-1] else 0
    return [len(cadena), es_palindromo]
