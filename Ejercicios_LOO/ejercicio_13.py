"""Se ingresa un valor numérico por consola, determinar e informar si se trata de un número primo o no"""

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

numero = int(input("Ingrese un número: "))
if es_primo(numero):
    print("El número es primo")
else:
    print("El número no es primo")
