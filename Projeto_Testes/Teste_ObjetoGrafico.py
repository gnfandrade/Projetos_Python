import unittest
from Projeto_Testes.Objeto_Grafico import *


class TestObjetoGrafico(unittest.TestCase):
    def TestConstructor(self):
        og = ObjetoGrafico("Azul", True, "Azul Claro")

        self.assertEqual("Azul", og.cor_preenchimento)
        self.assertEqual(True, og.preenchido)
        self.assertEqual("Azul Claro", og.cor_contorno)

class TestRetangulo(unittest.TestCase):
    def TestConstructor(self):
        og = ObjetoGrafico()


if __name__ == '__main__':
    unittest.main()

