from deportista import Deportista


class Futbolista(Deportista):
    def __init__(self, nsocio, diasentrenados):
        super().__init__(nsocio, diasentrenados)

    def calcularcuota(self):
        return self._cuotabase + (0.10 * self._cuotabase * self.diasentrenados)

    def getcuota_mensual(self):
        return super().calcularcuota()
