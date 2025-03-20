"""Leer tres valores numéricos enteros, indicar cual es el mayor, cuál es el del medio y cuál el menor. Considerar que los tres valores son diferentes   """

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

if num1  > num2 and num1 > num3:
    print("El mayor es el primer numero")
    if num2 > num3:
        print("El del medio es el segundo numero")
        print("El menor es el tercer numero")
    else:
        print("El del medio es el tercer numero")
        print("El menor es el segundo numero")

if num2 > num1 and num2 > num3:
    print("El mayor es el segundo numero")
    if num1 > num3:
        print("El del medio es el primer numero")
        print("El menor es el tercer numero")
    else:
        print("El del medio es el tercer numero")
        print("El menor es el primer numero")

if num3 > num1 and num3 > num2:
    print("El mayor es el tercer numero")
    if num1 > num2:
        print("El del medio es el primer numero")
        print("El menor es el segundo numero")
    else:
        print("El del medio es el segundo numero")
        print("El menor es el primer numero")


