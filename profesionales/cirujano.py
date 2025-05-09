from medico import Medico


class Cirujano(Medico):

    def calcular_honorario(self):
        return super().calcular_honorario() * 1.25
