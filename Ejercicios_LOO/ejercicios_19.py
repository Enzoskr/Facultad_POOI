""" Determinar si un carácter es un dígito numérico (función esDigito(char c)) """


def esDigito(caracter):
    return caracter.isdigit()


caracter = input("Ingrese un caracter: ")

if esDigito(caracter):
    print("Es un dígito")
else:
    print("No es un dígito")
