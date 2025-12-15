"""
Ejercicio 6: pedir una frase y una vocal y mostrar la frase con la vocal en mayúsculas.

La función debe:

Recibir una frase y una vocal (a, e, i, o, u) en cualquier caso.

Devolver la frase sustituyendo esa vocal (mayúscula/minúscula) por su versión en mayúscula.

Si la vocal no es válida, lanzar ValueError.
"""

def emphasize_vowel(phrase: str, vowel: str) -> str:
    """
    Convierte a mayúscula todas las apariciones de vowel en la frase.
    Sugerencia:
    - Comprueba que vowel es un solo carácter y está en "aeiou" (en minúscula).
    - Recorre la frase carácter a carácter y construye una nueva cadena.
    """
    # TODO: validar y transformar
    minuscula = vowel.lower()
    validas = "aeiou"
    lista = []
    
    if len(vowel) != 1:
        raise ValueError("Solo debe introducirse 1 vocal")
    
    if minuscula not in validas:
        raise ValueError("La vocal debe ser una vocal válida y no una consonante, número o cualquier otro carcater")
    
    mayuscula = vowel.upper()
    
    for char in phrase:
        if char.lower() == minuscula:
            lista.append(mayuscula)
            
        else:
            lista.append(char)
            
    return "".join(lista)


