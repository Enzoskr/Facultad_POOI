"""Los soldados pueden atacar cuerpo a cuerpo a otras unidades si tienen suficiente energía.
Cada ataque les consume 10 puntos de energía, y comienzan con 100. Restauran energía si reciben
la ración de agua. Infringen un daño de 10 puntos y comienzan con 200 de salud"""


from unidades import Unidad


class Soldado(Unidad):
    def __init__(self, energia, salud, damage):
        super().__init__(salud, damage)
