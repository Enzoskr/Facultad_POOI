"""main"""
from elipse import Elipse
from circulo import Circulo
from triangulo import Triangulo
from rectangulo import Rectangulo
from cuadrado import Cuadrado


def main():
    c1 = Circulo(2)
    e1 = Elipse(8, 4)
    r1 = Rectangulo(4, 2)
    cu = Cuadrado(6)

    figuras = []

    figuras.append(c1)
    figuras.append(Rectangulo(6, 2))
    figuras.append(e1)
    figuras.append(r1)
    figuras.append(Triangulo(10, 20))
    figuras.append(Cuadrado(10))
    figuras.append(cu)

    for f in figuras:
        print(f.get_area())

    figuras.sort()

    print("\nOrdenados:\n")
    for f in figuras:
        # cada figura se muestra de acuerdo al str
        print(f)


# Esto asegura que `main()` solo se ejecute cuando este archivo sea ejecutado directamente
if __name__ == "__main__":
    main()
