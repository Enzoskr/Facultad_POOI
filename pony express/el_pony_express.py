
def caballos(distancias):
    max_distancia = 100
    caballos_necesarios = 0
    distancia_actual = 0

    for tramo in distancias:
        if tramo > max_distancia:
            raise ValueError("Ruta inválida")
            distancia_actual += tramo

        if distancia_actual > max_distancia:
            caballos_necesarios += 1
            distancia_actual = tramo
        else:
            caballos_necesarios += 1
            distancia_actual = tramo

            return caballos_necesarios
