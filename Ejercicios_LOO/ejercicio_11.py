"""Escribir una función que calcule la suma de los múltiplos de 3 o 5, mayores o iguales que 0 y menores que un parámetro n. Por ejemplo la llamada:
sumaMultiplos(10); // devuelve 23 (3+5+6+9)
sumaMultiplos(16); // devuelve 60 (3+5+6+9+10+12+15)
"""

def sumarmultiplos(n):
    suma = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            suma += i
    return suma

numero = int(input("Ingrese un número: "))

print(sumarmultiplos(numero))

