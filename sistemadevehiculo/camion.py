from vehiculo import Vehiculo


class Camion(Vehiculo):

    def __init__(self, marca, modelo, capacidadCarga):
        super().__init__(marca, modelo, capacidadCarga)

    def soporteCarga(self):
        if self._capacidadCarga > 10:
            print("puede transportar mas de 10 toneladas carga")
        else:
            print("no puede transportar mas de 10 toneladas de carga")
