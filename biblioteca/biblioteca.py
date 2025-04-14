from libro import Libro
from genero import Genero


class Biblioteca:
    def __init__(self):
        self.__libros = []

    def cuantos_libros(self):
        return len(self.__libros)

    def agregar_libro(self, titulo: str, autor: str, genero, paginas):
        """Agrega un libro a la lista"""
        self.__libros.append(Libro(titulo, autor, genero, paginas))

    def obtener_libro(self, posicion: int):
        return self.__libros[posicion]

    def libro_en_la_posicion(self, posicion):
        """Devuelve el título del libro en la posición indicada (empezando desde 1)"""
        return self.__libros[posicion - 1].obtener_titulo()

    def libro_con_mas_paginas(self) -> Libro:
        """Devuelve el título del libro con más páginas"""
        if not self.__libros:
            return None

        pos_max = 0
        max_pag = self.__libros[0].obtener_paginas()

        for i in range(1, len(self.__libros)):
            if self.__libros[i].obtener_paginas() > max_pag:
                pos_max = i
                max_pag = self.__libros[i].obtener_paginas()

        return self.__libros[pos_max].obtener_titulo()


def main():
    l1 = Libro("El Principito", "Antoine de Saint-Exupéry", 1, 96)
    l2 = Libro("1984", "George Orwell", 2, 328)


if __name__ == "__main__":
    main()
