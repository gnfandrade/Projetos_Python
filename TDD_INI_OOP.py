# -*- coding: utf-8 -*-
import unittest

# Classe que contém a lógica do software.
class Calc():
    def dobro(self, num):
        return num * 2

# Testes
class MyCalcTest(unittest.TestCase):
    def testDobro(self):
        obj = Calc()
        self.assertEquals(16, obj.dobro(8))

if __name__ == '__main__':
    unittest.main()