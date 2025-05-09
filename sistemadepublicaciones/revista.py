from publicacion import Publicacion


class Revista(Publicacion):
    def __init__(self, titulo, edicionesyear, precioBase):
        super().__init__(titulo, precioBase)
        self._edicionesyear = edicionesyear

    def calcular_precio_final(self):
        if self._edicionesyear > 12:
            return self._precioBase * 1.05
        else:
            return self._precioBase
