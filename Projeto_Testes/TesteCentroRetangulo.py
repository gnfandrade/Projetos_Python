import unittest
from Projeto_Testes.CentroRetangulo import *



class TestPonto(unittest.TestCase):
    def testPontoConstrutor(self):
        pt = Ponto(2, 3)

        self.assertEqual(2, pt.x)
        self.assertEqual(3, pt.y)

    def testImprime(self):
        pt = Ponto(2, 4)

        self.assertEqual((2, 4), pt.imprime())


class TestRetangulo(unittest.TestCase):
    def testRetanguloConstrutor(self):
        pt = Ponto(2, 4)
        ret = Retangulo(pt.imprime())

        self.assertEqual(0, ret.altura)
        self.assertEqual(0, ret.largura)
        self.assertEqual((2, 4), ret.verticePartida)

    def testEncontraCentro(self):
        pt = Ponto(1, 2)
        ret = Retangulo(pt, 5, 6)

        self.assertEqual((3, 4), ret.encontraCentro().imprime())


if __name__ == '__main__':
    unittest.main()








