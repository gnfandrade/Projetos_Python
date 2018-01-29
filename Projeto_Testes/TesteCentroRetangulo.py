import unittest
from Projeto_Testes.CentroRetangulo import *


class TestPonto(unittest.TestCase):
    def testPontoConstrutor(self):
        pt = Ponto()

        self.assertEqual(1, 1, pt.__init__())

    def testImprime(self):
        pt = Ponto()

        self.assertEqual((0, 0), pt.imprime())


class TestRetangulo(unittest.TestCase):
    def testRetanguloConstrutor(self):
        pt = Ponto()
        ret = Retangulo(pt.imprime())

        self.assertEqual(0, ret.altura)
        self.assertEqual(0, ret.largura)
        self.assertEqual((0, 0), ret.verticePartida)


if __name__ == '__main__':
    unittest.main()








