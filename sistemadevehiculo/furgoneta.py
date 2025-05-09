from vehiculo import Vehiculo


class Furgoneta(Vehiculo):
    def __init__(self, marca, modelo, capacidadCarga):
        super().__init__(marca, modelo, capacidadCarga)

    def soporteCarga(self):
        if self._capacidadCarga > 3:
            print("es apta para reparto urbano")
        else:
            print("no es apta para reparto urbano")
