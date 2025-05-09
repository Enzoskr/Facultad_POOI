from cirujano import Cirujano


class CirujanoCardiovascular(Cirujano):
    def calcular_honorario(self):
        return super().calcular_honorario() * 1.25
