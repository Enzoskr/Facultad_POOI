from medico import Medico


class Dentista(Medico):
    def calcular_honorario(self):
        return super().calcular_honorario()
