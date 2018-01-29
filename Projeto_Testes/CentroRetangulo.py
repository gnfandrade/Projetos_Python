# -*- coding: utf-8 -*-

class Ponto(object):
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def imprime(self):
        return self.x, self.y
        #print("Ponto ({},{})".format(self.x, self.y))

class Retangulo(object):
    def __init__(self, ponto = Ponto(), b = 0, h = 0):
        self.verticePartida = ponto
        self.largura = b
        self.altura = h
pt = Ponto()
ret = Retangulo(pt.imprime())

print(ret.verticePartida)



