from vehiculo import Vehiculo


class Colectivo(Vehiculo):
    def __init__(self, chofer, kilometros=0):
        super().__init__(chofer, kilometros)
        self.pasajeros = []

    def agregar_pasajero(self, pasajero):
        self.pasajeros.append(pasajero)

    def cambiar_chofer(self, chofer):
        if len(self.pasajeros) == 0:
            super().cambiar_chofer(chofer)
        else:
            raise ValueError(
                "No se puede cambiar el chofer mientras haya pasajeros")

    def __str__(self):
        return f"{super().__str__()}, pasajeros: {len(self.pasajeros)}"
