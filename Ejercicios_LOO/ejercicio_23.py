"""Determinar si una cadena es vacía (función esVacia)"""


def cadenavacia(cadena):
    if len(cadena) == 0:
        return True
    else:
        return False


cadena = input("Ingrese una cadena: ")
print(cadenavacia(cadena))
