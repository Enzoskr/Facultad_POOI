from vehiculo import Vehiculo


class Moto(Vehiculo):
    def __init__(self, chofer, kilometros=0):
        super().__init__(chofer, kilometros)
        self.acompaniante = None

    def agregar_acompaniante(self, acompaniante):
        if self.acompaniante is None:
            self.acompaniante = acompaniante
        else:
            raise ValueError("Ya hay un acompañante asignado")

    def cambiar_chofer(self, chofer):
        if self.acompaniante is None:
            super().cambiar_chofer(chofer)
        else:
            raise ValueError(
                "No se puede cambiar el chofer mientras haya un acompañante")

    def recorrer(self, kilometros):
        self.kilometros_recorridos(kilometros)

    def __str__(self):
        return f"Moto {super().__str__()}, acompañante: {self.acompaniante}"
