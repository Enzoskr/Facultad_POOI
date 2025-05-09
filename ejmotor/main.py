from motor import Motor
from auto import Auto


auto1 = Auto("Ford", Motor("naftero"))
auto2 = Auto("Chevrolet", Motor("gasolero"))
auto3 = Auto("Fiat", Motor("naftero"))
auto4 = Auto("Peugeot", Motor("naftero"))
auto5 = Auto("Renault", Motor("naftero"))
auto6 = Auto("Toyota", Motor("diesel"))

autos = []

autos.append(auto1)
autos.append(auto2)
autos.append(auto3)
autos.append(auto4)
autos.append(auto5)
autos.append(auto6)


for auto in autos:
    print(f"Marca: {auto.get_marca()}")
    print(f"Tipo de motor: {auto.get_tipo_motor()}\n")
