"""Se ingresa por teclado un conjunto de valores numéricos enteros positivos, se pide informar, por cada uno, si el valor ingresado es par o impar. Para indicar el final se ingresará un valor cero o negativo"""

# Ingreso de datos

numero = int(input("Ingrese un numero: "))

# Proceso y salida de datos

while numero > 0:
    if numero % 2 == 0:
        print("El numero es par")
    else:
        print("El numero es impar")
    numero = int(input("Ingrese un numero: "))
