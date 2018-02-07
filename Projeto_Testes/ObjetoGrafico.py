class ObjetoGrafico(object):
    def __init__(self, cor_preenchimento, preenchido, cor_contorno):
        self.cor_preenchimento = cor_preenchimento
        self.preenchido = preenchido
        self.cor_contorno = cor_contorno


class Retangulo(ObjetoGrafico):
    def __init__(self, cor_preenchimento, preenchido, cor_contorno, base, altura):
        super().__init__(cor_preenchimento, preenchido, cor_contorno)
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.altura + self.base)


class Triangulo(ObjetoGrafico):
    def __init__(self, cor_preenchimento, preenchido, cor_contorno, base, altura):
        super().__init__(cor_preenchimento, preenchido, cor_contorno)
        self.base = base
        self.altura = altura

    def area(self):
        return (self.altura * self.base) / 2

    def perimetro(self):
        pass

from math import pi


class Circulo(ObjetoGrafico):
    def __init__(self, cor_preenchimento, preenchido, cor_contorno, raio):
        super().__init__(cor_preenchimento, preenchido, cor_contorno)
        self.raio = raio

    def area(self):
        return pi * self.raio * self.raio

    def perimetro(self):
        return 2 * pi * self.raio
