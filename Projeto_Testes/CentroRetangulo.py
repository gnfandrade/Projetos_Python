# -*- coding: utf-8 -*-

class Ponto(object):
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def imprime(self):
        #return self.x, self.y
        print("Ponto ({},{})".format(self.x, self.y))

class Retangulo(object):
    def __init__(self, ponto = Ponto(), b = 0, h = 0):
        self.verticePartida = ponto
        self.largura = b
        self.altura = h

    def encontraCentro(self):
        x = self.verticePartida.x + self.largura/2
        y = self.verticePartida.y + self.altura/2

        return Ponto(x, y)


def main():
    verticePartida = Ponto()
    ret = Retangulo()

    while True:
        cmd = menu()

        if cmd.startswith('m'):
            mudaValores(ret)
        elif cmd.startswith('i'):
            ret.encontraCentro().imprime()
        else:
            break


def menu():
    while True:
        cmd = input("Deseja alterar os valores do retângulo(m), imprimir o valor do centro(i) ou fechar o programa(f)?\n")
        cmd.lower()

        if not cmd.isalpha():
            print("Digite apenas Letras!!!")
        else:
            if cmd.startswith('m') or cmd.startswith('i') or cmd.startswith('f'):
                return cmd
            else:
                print("Não entendi o seu comando, por favor digite novamente!")

def mudaValores(ret):
    ret.largura = float(input("Digite o valor da largura do retângulo: "))
    ret.altura = float(input("Digite o valor da altura do retângulo: "))
    ret.verticePartida.x = float(input("Digite o valor de x do vértice do retângulo: "))
    ret.verticePartida.y = float(input("Digite o valor de y do vértice do retângulo: "))

if __name__ == '__main__':
    main()
