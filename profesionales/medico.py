from profesional import Profesional


class Medico(Profesional):

    def calcular_honorario(self):
        return super().get_honorario_basico()
