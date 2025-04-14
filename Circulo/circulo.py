"""
Desafío Círculos
1. Para construir un círculo se requiere un punto, que será su centro, y un radio.
Nuestro pequeño programa nos permitirá verificar si hay o no intersección entre dos
círculos.
Se te pide programar las clases Punto, Circulo, y una
prueba que te permita verificar el correcto funcionamiento del método especificado.

Ejemplo de funcionamiento:

Circulo c1 = new Circulo(new Punto(0, 0), 1);
Circulo c2 = new Circulo(new Punto(1, 1), 1.5);
System.out.println(c1.intersectaCon(c2)); // true
"""


class circulo:
    def __init__(self, centro, radio):
        self.radio = radio
        self.centro = centro

    def interseccion(self, otro_circulo):
        distancia_centros = self.centro.distancia(otro_circulo.centro)
        suma_radios = self.radio + otro_circulo.radio
        return distancia_centros <= suma_radios

    def __str__(self):
        return f"Circulo(centro=({self.centro.x}, {self.centro.y}), radio={self.radio})"


class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, otro_punto):
        x = self.x - otro_punto.x
        y = self.y - otro_punto.y
        return (x**2 + y**2)**0.5


p1 = Punto(0, 0)
p2 = Punto(1, 1)

c1 = circulo(p1, 1)
c2 = circulo(p2, 1.5)

print(c1)
print(c2)
