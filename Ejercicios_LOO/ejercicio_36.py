# ejercicio 36
"""Escribir una función consonantes que recibe una cadena de caracteres
y devuelve la cadena que resulta de eliminar todas las vocales de la cadena recibida.
Por ejemplo: consonantes("hola como estas"); // devuelve "hl cm sts"""

def consonantes(cadena) -> str:
    """devuelve la cadena que resulta de eliminar todas las vocales de la cadena recibida"""
    vocales = "aeiouAEIOU"
    for letra in cadena:
        if letra in vocales:
            cadena = cadena.replace(letra, "")
    return cadena

print(consonantes("hola como estas"))
print(consonantes("Hola cómo estás"))
