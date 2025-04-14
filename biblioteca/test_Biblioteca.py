import unittest
from biblioteca import Biblioteca
from genero import Genero


class TestBiblioteca(unittest.TestCase):
    def test_agregar_libro(self):
        mi_biblioteca = Biblioteca()
        mi_biblioteca.agregar_libro(
            "El Principito", "Antoine de Saint-Exupéry", Genero.AVENTURA, 96
        )

        self.assertEqual(1, mi_biblioteca.cuantos_libros())
        self.assertEqual(
            "El Principito", mi_biblioteca.libro_en_la_posicion(1))

    def test_libro_en_la_posicion(self):
        mi_biblioteca = Biblioteca()
        mi_biblioteca.agregar_libro(
            "El Principito", "Antoine de Saint-Exupéry", Genero.AVENTURA, 98)
        mi_biblioteca.agregar_libro(
            "1984", "George Orwell", Genero.CIENCIAFICCION, 328)

        self.assertEqual("1984", mi_biblioteca.libro_en_la_posicion(2))

    def test_libro_con_mas_paginas(self):
        mi_biblioteca = Biblioteca()
        mi_biblioteca.agregar_libro(
            "Libro corto", "Autor A", Genero.AVENTURA, 50)
        mi_biblioteca.agregar_libro(
            "Libro largo", "Autor B", Genero.CIENCIAFICCION, 500
        )

        self.assertEqual("Libro largo", mi_biblioteca.libro_con_mas_paginas())

    """contador de libros"""


if __name__ == "__main__":
    unittest.main()
