# -*- coding: utf-8 -*-
import unittest
# Classe que contém a lógica do software.
class Juros():
    def jurosimples(self):
        return self.capital * self.taxa * self.n_periodos

# Classe que realiza o teste sobre o objeto.
class MyCalcTest(unittest.TestCase):
    def testJuroSimples(self):
        calcJuros = Juros()
        calcJuros.capital = 16000
        calcJuros.taxa = 0.04
        calcJuros.n_periodos = 4

        self.assertEquals(2560, calcJuros.jurosimples())

if __name__ == '__main__':
    unittest.main()
