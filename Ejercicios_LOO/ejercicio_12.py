"""Dado un conjunto de valores numéricos que se ingresan por teclado determinar el valor promedio. El fin de datos se indicará ingresando un valor igual a cero"""

def promedio():
    suma = 0
    contador = 0
    while True:
        numero = int(input("Ingrese un número: "))
        if numero == 0:
            break
        suma += numero
        contador += 1
    return suma / contador


print(promedio())
