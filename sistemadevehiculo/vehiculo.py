class Vehiculo():
    def __init__(self, marca, modelo, capacidadCarga):
        self._marca = marca
        self._modelo = modelo
        self._capacidadCarga = capacidadCarga

    def get_marca(self):
        return self._marca

    def get_modelo(self):
        return self._modelo

    def get_capacidadCarga(self):
        return self._capacidadCarga
