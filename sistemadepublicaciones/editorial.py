class Editorial:
    def mostrar_publicaciones(self, publicaciones):
        for pub in publicaciones:
            print(pub.get_datos())
            print(f"precio final: ${pub.calcular_precio_final()}\n")
