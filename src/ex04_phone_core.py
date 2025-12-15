"""
Ejercicio 4: a partir de un teléfono con el formato "+34-<numero>-<extension>"
obtener solamente la parte central (el número), sin prefijo ni extensión.

Ejemplo: "+34-913724710-56" -> "913724710"
"""

def phone_core(s: str) -> str:
    """
    Recibe el teléfono como cadena y devuelve solo la parte central.
    Requisitos mínimos (si no se cumplen, lanza ValueError):
    - Debe haber exactamente 3 partes separadas por "-".
    - La primera parte debe comenzar por "+" (prefijo).
    - La parte central debe ser numérica.
    """
    # TODO: usa .strip(), .split("-") y validaciones con .isdigit() y startswith("+")
    cadena = s.strip()
    sep = cadena.split("-")
    centro = cadena
    if len(sep) != 3:
        raise ValueError("El número de teléfono debe estar separado en 3 partes por guiones")
    
    if not sep[0].startswith("+"): 
        raise ValueError("El número de teléfono debe empezar por '+'")
    
    if not sep[1].isdigit():
        raise ValueError("La parte central del número debe ser numérico")
    
    else:
        return sep[1]
