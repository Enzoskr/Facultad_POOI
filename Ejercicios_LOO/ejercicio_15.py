"""Dado un conjunto de valores numéricos indicar cuál es el mayor. El ingreso de datos finaliza con la llegada de un cero"""

def mayor():
    mayor = 0
    while True:
        numero = int(input("Ingrese un número: "))
        if numero == 0:
            break
        if numero > mayor:
            mayor = numero
    return mayor

print(mayor())
