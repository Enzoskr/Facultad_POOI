from deportista import Deportista


class Tenista(Deportista):
    def __init__(self, nrosocio, diasentrenados):
        super().__init__(nrosocio, diasentrenados)

    def calcularcuota(self):
        return self._cuotabase + (0.10 * self._cuotabase * self.diasentrenados)

    def getcuota_mensual(self):
        return super().calcularcuota()
