import unittest
from Projeto_Testes.Teste_Classes import Quadrado

# Classe de teste para a classe Quadrado.
class MyQuadradoTest(unittest.TestCase):
    def testRetornaLado(self):
        """
        Função que testa o método 'Retorna Lado' da classe Quadrado
        :return: sem retornos.
        """
        quadrado = Quadrado()# Recebe classe Quadrado.
        quadrado.lado = 4

        self.assertEquals(4, quadrado.RetornaLado())

    def testeCalcularArea(self):
        """
        Função que testa o método 'CalculaArea' da classe Quadrado
        :return: sem retornos.
        """
        quadrado = Quadrado()# Recebe classe Quadrado.
        quadrado.lado = 3

        self.assertEquals(9, quadrado.CalcularArea())

if __name__ == '__main__':
    unittest.main()