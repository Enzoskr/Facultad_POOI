"""Dada la jerarquía de Figuras que se muestra debajo,
considerando que solo la clase Figura es abstracta y
las demás clases son concretas y que se puede calcular el área de todas las figuras concretas se pide:

a.Escribir las clases para almacenar el área como un atributo y  que sea calculada por
el constructor de la figura correspondiente. Los constructores de las clases concretas deberían calcular
un área y pasar el resultado al constructor del padre, en la invocación a super.
b.Definir un método getArea() en la clase Figura que devuelva el valor del atributo área.
Este método no se debe poder modificar en ninguna clase derivada de Figura.
c. Todas las figuras deben implementar la interfaz Comparable utilizando (aca supuestamente se utiliza el metodo sort)
el área de las mismas para determinar si una figura es mayor o menor que otra.
d.Implementar un demo dónde se creen distintas Figuras (una de cada tipo),
se almacenen en un arreglo, y se pueda calcular la suma de todas las áreas almacenadas.
"""

# clase base
from abc import ABC, abstractmethod


class Figura(ABC):
    def __init__(self, area: float):
        self._area = area

    
    def get_area(self) -> float:
        return self._area

    def __eq__(self, other) -> bool:
        return self.get_area() == other.get_area()

    def __lt__(self, other) -> bool:
        return self.get_area() < other.get_area()

    def __gt__(self, other) -> bool:
        return self.get_area() > other.get_area()

    def __le__(self, other) -> bool:
        return self.get_area() <= other.get_area()

    def __ge__(self, other) -> bool:
        return self.get_area() >= other.get_area()

    def __str__(self) -> str:
        return type(self).__name__ + f" (area={self.get_area()})"
