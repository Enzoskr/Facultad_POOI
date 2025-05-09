from publicacion import Publicacion


class Libro(Publicacion):
    def __init__(self, titulo, nropaginas, precioBase):
        super().__init__(titulo, precioBase)
        self._nropaginas = nropaginas

    def calcular_precio_final(self):
        if self._nropaginas > 300:
            return self._precioBase * 1.10
        else:
            return self._precioBase

    def get_datos(self):
        return f"{super().get_datos()}"
