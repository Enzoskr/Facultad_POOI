"""
Se ingresa por consola un número entero que representa un sueldo que se debe pagar.
Considerando que existen billetes de las denominaciones que se indican más abajo; informar,
que cantidad de billetes de cada denominación se deberá utilizar, dando prioridad a los de valor nominal más alto. Denominaciones ($) = {100, 50, 20, 10, 5, 2, 1}
"""


def billetes(sueldo):
    tipodecambio = [100, 50, 20, 10, 5, 2, 1]
    for i in tipodecambio:
        cantidad = sueldo // i
        sueldo = sueldo % i
        print(f"Se necesitan {cantidad} billetes de {i}")
    return sueldo


sueldo = int(input("Ingrese un sueldo: "))
billetes(sueldo)
