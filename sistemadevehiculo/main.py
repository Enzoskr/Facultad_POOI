from camion import Camion
from furgoneta import Furgoneta
from empresadetransporte import EmpresadeTransporte

camion1 = Camion("scania", "optacore", 15)
Furgoneta1 = Furgoneta("fiat", "toro", 3)


vehiculos = []


vehiculos.append(camion1)
vehiculos.append(Furgoneta1)

empresa = EmpresadeTransporte()


empresa.mostrar_Vehiculos(vehiculos)
