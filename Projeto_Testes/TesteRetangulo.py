import unittest

from Projeto_Testes.Retangulo import Retangulo

class MyRetanguloTest(unittest.TestCase):
    def testRetornaLados(self):
        ret = Retangulo()
        ret.ladoA = 3
        ret.ladoB = 4

        self.assertEqual((3,4), ret.RetornaLados())

    def testArea(self):
        ret = Retangulo()
        ret.ladoA = 3
        ret.ladoB = 4

        self.assertEqual(12, ret.area())

    def testPerimetro(self):
        ret = Retangulo()
        ret.ladoA = 3
        ret.ladoB = 4

        self.assertEqual(14, ret.perimetro())

if __name__ == "__main__":
    unittest.main()
