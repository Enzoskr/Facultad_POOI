import unittest
from el_pony_express import caballos


class TestCaballos(unittest.TestCase):
    def test_caballos_1(self):
        self.assertEqual(caballos([18, 15]), 1)
        self.assertEqual(caballos([18, 15, 20]), 2)
        self.assertEqual(caballos([18, 15, 20, 25]), 3)
        self.assertEqual(caballos([18, 15, 20, 25, 30]), 4)
        self.assertEqual(caballos([18, 15, 20, 25, 30, 35]), 5)


if __name__ == "__main__":
    unittest.main()
