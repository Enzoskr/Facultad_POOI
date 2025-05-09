from dentista import Dentista


class Endodoncista(Dentista):
    def calcular_honorario(self):
        return super().calcular_honorario() * 1.25
