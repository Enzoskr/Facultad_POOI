from club import Club
from futbolista import Futbolista
from tenista import Tenista


def main():
    club = Club()
    club.set_cuota_base(1000)

    f1 = Futbolista(112312, 4)

    club.agregarSocio(f1)

    print("Total de cuotas: ", club.getTotalcuotas())
    print("\nPlanilla de socios:")
    club.listarplanilladesocios()


if __name__ == "__main__":
    main()
