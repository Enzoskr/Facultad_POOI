"""Determinar si un carácter es una letra mayúscula o minúscula (función esMayuscula(char c) y esMinuscula(char c))"""


def mayuscula(caracter):
    return caracter.isupper()


def minuscula(caracter):
    return caracter.islower()


caracter = input("Ingrese un caracter: ")
if mayuscula(caracter):
    print("Es una letra mayúscula")
elif minuscula(caracter):
    print("Es una letra minúscula")
else:
    print("No es una letra")
