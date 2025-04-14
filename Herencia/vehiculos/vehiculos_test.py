import unittest
from moto import Moto
from colectivo import Colectivo


class TestVehiculos(unittest.TestCase):

    def test_moto_chofer(self):
        moto = Moto("Luis")
        self.assertEqual(moto.chofer, "Luis")
        moto.agregar_acompaniante("Ana")
        # moto.cambiar_chofer("Carlos")  # No debería cambiar
        self.assertEqual(moto.chofer, "Luis")  # Sigue siendo Luis
        moto.acompaniante = None
        moto.cambiar_chofer("Carlos")  # Ahora sí cambia
        self.assertEqual(moto.chofer, "Carlos")

    def test_colectivo_chofer(self):
        colectivo = Colectivo("Pedro", 100)
        colectivo.agregar_pasajero("Juan")
        # colectivo.cambiar_chofer("Mario")  # No debería cambiar
        self.assertEqual(colectivo.chofer, "Pedro")

        # Limpiar los pasajeros y ahora debería cambiar el chofer
        colectivo.pasajeros.clear()
        colectivo.cambiar_chofer("Mario")
        self.assertEqual(colectivo.chofer, "Mario")

    def test_kilometros(self):
        moto = Moto("Luis", 10)
        moto.recorrer(15)
        self.assertEqual(moto.kilometros, 25)


if __name__ == "__main__":
    unittest.main()
