from genero import Genero


class Libro:

    def __init__(self, titulo: str, autor: str, genero: Genero, paginas: int):
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__paginas = paginas

    def obtener_titulo(self):
        """devuelve el titulo del libro"""
        return self.__titulo

    def obtener_paginas(self):
        """devuelve la cantidad de paginas del libro"""
        return self.__paginas

    def obtener_genero(self):
        """devuelve el genero del libro"""
        return self.__genero

    def __eq__(self, other):
        return (
            self.__titulo == other.__titulo and
            self.__autor == other.__autor and
            self.__genero == other.__genero and
            self.__paginas == other.__paginas
        )
