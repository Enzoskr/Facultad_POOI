"""Definir una clase que represente a un número complejo.
Sus atributos serán dos números reales que representarán
la parte real y la parte imaginaria del número complejo.
La clase deberá contener:

un constructor por defecto.
un constructor con parámetros.
los métodos set y get respectivos.
el método toString().
suma(), resta(), producto(), division() y conjugado()."""


class NumeroComplejo:
    # constructor por defecto
    def __init__(self, parte_real: float = 0.0, parte_imaginaria: float = 0.0):
        self.__parte_real = parte_real
        self.__parte_imaginaria = parte_imaginaria

    def set_parte_real(self, parte_real: float):
        """Establece la parte real del número complejo."""
        self.__parte_real = parte_real

    def set_parte_imaginaria(self, parte_imaginaria: float):
        """Establece la parte imaginaria del número complejo."""
        self.__parte_imaginaria = parte_imaginaria

    def get_parte_real(self) -> float:
        """Devuelve la parte real del número complejo."""
        return self.__parte_real

    def get_parte_imaginaria(self) -> float:
        """Devuelve la parte imaginaria del número complejo."""
        return self.__parte_imaginaria

    def to_string(self) -> str:
        """Devuelve una representación en cadena del número complejo."""
        if self.__parte_imaginaria >= 0:
            return f"{self.__parte_real} + {self.__parte_imaginaria}i"
        else:
            return f"{self.__parte_real} - {abs(self.__parte_imaginaria)}i"

    def suma(self, otro):
        """Devuelve la suma de dos números complejos."""
        return NumeroComplejo(
            self.__parte_real + otro.get_parte_real(),
            self.__parte_imaginaria + otro.get_parte_imaginaria()
        )

    def resta(self, otro):
        """Devuelve la resta de dos números complejos."""
        return NumeroComplejo(
            self.__parte_real - otro.get_parte_real(),
            self.__parte_imaginaria - otro.get_parte_imaginaria()
        )

    def producto(self, otro):
        """Devuelve el producto de dos números complejos."""
        return NumeroComplejo(
            self.__parte_real * otro.get_parte_real() - self.__parte_imaginaria *
            otro.get_parte_imaginaria(),
            self.__parte_real * otro.get_parte_imaginaria() + self.__parte_imaginaria *
            otro.get_parte_real()
        )

    def division(self, otro):
        """Devuelve la división de dos números complejos."""
        denominador = otro.get_parte_real() ** 2 + otro.get_parte_imaginaria() ** 2
        return NumeroComplejo(
            (self.__parte_real * otro.get_parte_real() +
             self.__parte_imaginaria * otro.get_parte_imaginaria()) / denominador,
            (self.__parte_imaginaria * otro.get_parte_real() -
             self.__parte_real * otro.get_parte_imaginaria()) / denominador
        )

    def conjugado(self):
        """Devuelve el conjugado del número complejo."""
        return NumeroComplejo(self.__parte_real, -self.__parte_imaginaria)


"""
# Ejemplo de uso:
"""
if __name__ == "__main__":
    num1 = NumeroComplejo(3, 4)
    num2 = NumeroComplejo(1, 2)

    print("Número 1:", num1.to_string())
    print("Número 2:", num2.to_string())

    suma = num1.suma(num2)
    print("Suma:", suma.to_string())

    resta = num1.resta(num2)
    print("Resta:", resta.to_string())

    producto = num1.producto(num2)
    print("Producto:", producto.to_string())

    division = num1.division(num2)
    print("División:", division.to_string())

    conjugado = num1.conjugado()
    print("Conjugado de Número 1:", conjugado.to_string())
    conjugado2 = num2.conjugado()
    print("Conjugado de Número 2:", conjugado2.to_string())
    print("Parte real de Número 1:", num1.get_parte_real())
    print("Parte imaginaria de Número 1:", num1.get_parte_imaginaria())
    print("Parte real de Número 2:", num2.get_parte_real())
    print("Parte imaginaria de Número 2:", num2.get_parte_imaginaria())
