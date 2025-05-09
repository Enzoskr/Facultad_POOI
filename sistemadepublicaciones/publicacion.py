class Publicacion:
    def __init__(self, titulo, precioBase):
        self._titulo = titulo
        self._precioBase = precioBase

    def get_datos(self):
        return f"titulo Título: {self._titulo}, Precio base: ${self._precioBase}"
