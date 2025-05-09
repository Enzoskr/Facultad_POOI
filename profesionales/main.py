from cirujano import Cirujano
from cirujanocardiovascular import CirujanoCardiovascular
from dentista import Dentista
from endodoncista import Endodoncista
# from medico import Medico


def main():
    ciruja = Cirujano("martin", "perez")
    c1 = CirujanoCardiovascular("juanjo", "zuñiga")
    c2 = CirujanoCardiovascular("alejo", "sergio")
    d1 = Dentista("mario", "gonzalez")
    panchoconpapitas = Endodoncista("pancho", "con papitas")
    
    

    profesionales = []

    profesionales.append(ciruja)
    profesionales.append(c1)
    profesionales.append(d1)
    profesionales.append(panchoconpapitas)
    profesionales.append(c2)

    for f in profesionales:
        print(f"{f.nombre} {f.apellido} cobra: {f.calcular_honorario()}")

    profesionales.sort()

    print("\nOrdenados:\n")
    for f in profesionales:
        # cada figura se muestra de acuerdo al str
        print(f)


if __name__ == "__main__":
    main()
