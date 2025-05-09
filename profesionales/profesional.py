#  clase base Profesional:
"""Dada la jerarquía que se aprecia en el diagrama UML,
considerando que solo la clase Profesional es abstracta y
las demás clases son concretas,. Todos los profesionales tienen
un honorario mensual básico de $500.000 (si se cambia el honorario
básico cambia para toda la jerarquía de clases). De todos los profesionales
se guarda su nombre y apellido. Médicos y Dentistas cobran honorarios
básicos. Se pide:
"""


from abc import ABCMeta, abstractmethod


class Profesional(metaclass=ABCMeta):
    _honorario_basico = 500000

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    @abstractmethod
    def calcular_honorario(self):
        pass

    @classmethod
    def set_honorario_basico(cls, nuevo_honorario):
        cls._honorario_basico = nuevo_honorario

    @classmethod
    def get_honorario_basico(cls):
        return cls._honorario_basico

    def __lt__(self, other):
        return self.calcular_honorario() > other.calcular_honorario()

    def __eq__(self, other):
        return self.calcular_honorario() == other.calcular_honorario()

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({type(self).__name__})"
