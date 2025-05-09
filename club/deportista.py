from abc import ABCMeta, abstractmethod


class Deportista(metaclass=ABCMeta):
    _cuotabase = 10000

    def __init__(self, nsocio, diasentrenados):
        self.nsocio = nsocio
        self.diasentrenados = diasentrenados

    @classmethod
    def set_cuota_base(cls, nueva):
        cls._cuotabase = nueva

    @classmethod
    def get_cuota_base(cls):
        return cls._cuotabase

    @abstractmethod
    def calcularcuota(self):
        pass

    def getcuota_mensual(self):
        return self.calcularcuota()
