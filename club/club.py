from deportista import Deportista


class Club:

    def __init__(self):
        self.socios = []

    def agregarSocio(self, socio):
        self.socios.append(socio)

    def set_cuota_base(self, nueva):
        Deportista.set_cuota_base(nueva)

    def getTotalcuotas(self):
        total = 0
        for socio in self.socios:
            total += socio.calcularcuota()
        return total

    def listarplanilladesocios(self):
        for socio in self.socios:
            print(f"Socio: {socio.nsocio} - Cuota: {socio.calcularcuota()}")
