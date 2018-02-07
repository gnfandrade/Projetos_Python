import unittest
from Projeto_Testes.ObjetoGrafico import *


class TestObjetoGrafico(unittest.TestCase):
    def testConstrutor(self):
        og = ObjetoGrafico("Azul", True, "Rosa")

        self.assertEqual("Azul", og.cor_preenchimento)
        self.assertEqual(True, og.preenchido)
        self.assertEqual("Rosa", og.cor_contorno)


class TestRetangulo(unittest.TestCase):
    def testConstructor(self):
        #og = ObjetoGrafico("Azul", True, "Rosa")
        ret = Retangulo("Vermelho", False, "Laranja", 3, 4)

        self.assertEqual("Vermelho", ret.cor_preenchimento)
        self.assertEqual(False, ret.preenchido)
        self.assertEqual("Laranja", ret.cor_contorno)
        self.assertEqual(3, ret.base)
        self.assertEqual(4, ret.altura)

    def testArea(self):
        ret = Retangulo("Vermelho", False, "Laranja", 3, 4)

        self.assertEqual(12, ret.area())

    def testPerimetro(self):
        ret = Retangulo("Vermelho", False, "Laranja", 3, 4)

        self.assertEqual(14, ret.perimetro())


class TestTriangulo(unittest.TestCase):
    def testConstructor(self):
        trg = Triangulo("Ciano", True, "Nenhuma", 6, 10)

        self.assertEqual("Ciano", trg.cor_preenchimento)
        self.assertEqual(True, trg.preenchido)
        self.assertEqual("Nenhuma", trg.cor_contorno)
        self.assertEqual(6, trg.base)
        self.assertEqual(10, trg.altura)

    def testArea(self):
        trg = Triangulo("Ciano", True, "Nenhuma", 6, 10)

        self.assertEqual(30, trg.area())


class TestCirculo(unittest.TestCase):
    def testConstructor(self):
        circ = Circulo("Verde", False, "roxo", 5)

        self.assertEqual(5, circ.raio)
        self.assertEqual("Verde", circ.cor_preenchimento)
        self.assertEqual(False, circ.preenchido)
        self.assertEqual("roxo", circ.cor_contorno)

    def testArea(self):
        circ = Circulo("Verde", False, "roxo", 5)

        self.assertEqual(78.53981633974483, circ.area())

    def testPerimetro(self):
        circ = Circulo("Verde", False, "roxo", 5)

        self.assertEqual(31.41592653589793, circ.perimetro())




if __name__ == '__main__':
    unittest.main()