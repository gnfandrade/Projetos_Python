import unittest
from Projeto_Testes.Pessoa import Pessoa

class TestPessoa(unittest.TestCase):

    def testConstrutor(self):
        ps = Pessoa("Gustavo", 20, 50, 1.78)

        self.assertEqual(20, ps.idade)
        self.assertEqual("Gustavo", ps.nome)
        self.assertEqual(50, ps.peso)
        self.assertEqual(1.78, ps.altura)

    def testEnvelhecer(self):
        ps = Pessoa("Gustavo", 20, 50, 1.78)

        self.assertEqual((21, 1.83), ps.envelhecer())

    def testEngordar(self):
        ps = Pessoa("Gustavo", 20, 50, 1.78)

        self.assertEqual(80, ps.engordar(30))

    def testEmagrecer(self):
        ps = Pessoa("Gustavo", 20, 50, 1.78)

        self.assertEqual(47, ps.emagrecer(3))

    def testCrescer(self):
        ps = Pessoa("Gustavo", 20, 50, 1.78)

        self.assertEqual(1.8, ps.crescer(0.02))


if __name__ == '__main__':
    unittest.main()