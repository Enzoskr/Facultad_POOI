"""
Existen dos tipos de vehículos: las motos, que llevan un chofer y un
acompañante, y los colectivos, que llevan un chofer y varios pasajeros.

Los vehículos deben conocer la cantidad de kilómetros recorridos, asignar
y cambiar chofer.
Cada vehículo particular deberá poder agregar un acompañante o diversos pasajeros, respectivamente.
En caso del colectivo,no puede cambiar de chofer si hubiera pasajeros.
En el caso de la moto,no puede hacerlo si hubiera un acompañante
"""


class Vehiculo:
    def __init__(self, chofer, kilometros=0):
        self.chofer = chofer
        self.kilometros = kilometros

    def asignar_chofer(self, chofer):
        self.chofer = chofer

    def cambiar_chofer(self, chofer):
        if self.chofer != chofer:
            self.chofer = chofer
        else:
            raise ValueError("El chofer es el mismo que el actual")

    def kilometros_recorridos(self, kilometros):
        self.kilometros += kilometros
        return self.kilometros

    def __str__(self):
        return f"chofer: {self.chofer}, kilometros: {self.kilometros}"
