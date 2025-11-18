def extraer_caracteristicas(cadena: str):
    """Extrae características numéricas de una cadena sin revelar si es palíndromo.
    
    Características extraídas:
    1. Longitud de la cadena
    2. Primera y última letra son iguales (1/0)
    3. Número de vocales
    4. Número de consonantes
    5. Ratio de letras únicas vs total
    6. Número de caracteres en posiciones pares que coinciden con posiciones impares espejadas
    7. Simetría de vocales (vocales en primera mitad vs segunda mitad)
    """
    if cadena is None or cadena == "":
        return [0, 0, 0, 0, 0, 0, 0]
    
    cadena_lower = cadena.lower()
    longitud = len(cadena_lower)
    
    # 1. Longitud
    feature_longitud = longitud
    
    # 2. Primera y última letra iguales
    primera_ultima_igual = 1 if cadena_lower[0] == cadena_lower[-1] else 0
    
    # 3 y 4. Contar vocales y consonantes
    vocales = 'aeiouáéíóúü'
    num_vocales = sum(1 for c in cadena_lower if c in vocales)
    num_consonantes = sum(1 for c in cadena_lower if c.isalpha() and c not in vocales)
    
    # 5. Ratio de letras únicas
    letras_unicas = len(set(cadena_lower))
    ratio_unicas = letras_unicas / longitud if longitud > 0 else 0
    
    # 6. Coincidencias espejadas (sin revisar si es palíndromo completo)
    mitad = longitud // 2
    coincidencias = 0
    for i in range(mitad):
        if cadena_lower[i] == cadena_lower[-(i+1)]:
            coincidencias += 1
    ratio_coincidencias = coincidencias / mitad if mitad > 0 else 0
    
    # 7. Simetría de vocales
    primera_mitad = cadena_lower[:mitad]
    segunda_mitad = cadena_lower[-mitad:]
    vocales_primera = sum(1 for c in primera_mitad if c in vocales)
    vocales_segunda = sum(1 for c in segunda_mitad if c in vocales)
    diferencia_vocales = abs(vocales_primera - vocales_segunda)
    
    return [
        feature_longitud,
        primera_ultima_igual,
        num_vocales,
        num_consonantes,
        round(ratio_unicas, 3),
        round(ratio_coincidencias, 3),
        diferencia_vocales
    ]
