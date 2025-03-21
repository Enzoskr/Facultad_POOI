"""Se ingresa un valor numérico de 8 dígitos que representa una fecha con el siguiente formato aaaammdd.
Se pide informar por separado el día, el mes y el año de la fecha ingresada """


fecha = int(input("Ingrese una fecha en formato aaaammdd: "))

print("El año es: ", fecha // 10000)
print("El mes es: ", (fecha % 10000) // 100)
print("El día es: ", fecha % 100)

"""explicación:"""
# Se pide al usuario que ingrese una fecha en formato aaaammdd
# Se almacena en la variable fecha
# Se imprime el año, mes y día por separado
# Para obtener el año se divide la fecha por 10000
# Para obtener el mes se divide el resto de la fecha por 10000 y se divide por 100
# Para obtener el día se obtiene el resto de la fecha por 100
# Se imprime el año, mes y día
# Se finaliza el programa
