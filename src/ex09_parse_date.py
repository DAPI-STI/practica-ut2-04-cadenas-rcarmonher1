"""
Ejercicio 9: leer una fecha (día, mes, año) introducida como "dd/mm/aaaa"
y mostrar cada componente por separado.

La función:

Recibe un string con formato "d/m/aaaa" o "dd/mm/aaaa".

Devuelve (dia, mes, año) como enteros.

Si el formato o los rangos son incorrectos, lanza ValueError.
"""

def parse_date(date_str: str) -> tuple[int, int, int]:
    """Devuelve (día, mes, año) como enteros a partir de una cadena d/m/aaaa."""
    # TODO: usa split("/"), convierte a int y valida rangos sencillos
    fecha = date_str.split('/')
    
    if len(fecha) != 3:
        raise ValueError("Introduce una fecha correcta")
        
    if not fecha[0].isdigit() or not fecha[1].isdigit() or not fecha[2].isdigit():
        raise ValueError("La fecha solo puede contener números y barras '/'")
    
        
    dia = int(fecha[0])
    mes = int(fecha[1])
    año = int(fecha[2])
    
    if dia > 31 or dia < 1:
        raise ValueError("Introduce una fecha correcta")
        
    
    if mes > 12 or mes < 1:
        raise ValueError("Introduce una fecha correcta")
    
    if len(fecha[2]) != 4:
        raise ValueError("Intoduce un año correcto")
    
    return dia, mes, año
    


    
    