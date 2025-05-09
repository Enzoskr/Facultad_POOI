class EmpresadeTransporte:
    def mostrar_Vehiculos(self, lista_vehiculos):
        for Vehiculo in lista_vehiculos:
            print(f"Marca: {Vehiculo.get_marca()}")
            print(f"Marca: {Vehiculo.get_modelo()}")
            Vehiculo.soporteCarga()
