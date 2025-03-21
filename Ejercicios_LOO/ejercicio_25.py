""" Comparar cadenas (función comparaCadenas)"""


def cadenas(cadena1, cadena2):
    if cadena1 == cadena2:
        return True
    else:
        return False


cadena1 = input("Ingrese una cadena: ")
cadena2 = input("Ingrese otra cadena: ")
print(cadenas(cadena1, cadena2))
