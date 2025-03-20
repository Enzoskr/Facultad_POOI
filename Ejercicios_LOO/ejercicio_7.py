"""Leer un valor numérico que representa un día de la semana.
Se pide mostrar por pantalla el nombre del día considerando que el lunes es el día 1,
el martes es el día 2 y así, sucesivamente"""

# Ingreso de datos
dia = int(input("Ingrese un dia de la semana: "))

# Proceso y salida de datos
if dia == 1:
    print("Lunes")
elif dia == 2:
    print("Martes")
elif dia == 3:
    print("Miercoles")
elif dia == 4:
    print("Jueves")
elif dia == 5:
    print("Viernes")
elif dia == 6:
    print("Sabado")
elif dia == 7:
    print("Domingo")
else:
    print("El valor ingresado no es valido")
