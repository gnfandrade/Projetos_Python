def main():
    try:
        quadrilatero = Retangulo()
        quadrilatero.ladoA = int(input("Insira o valor do Lado A do Retângulo: "))
        quadrilatero.ladoB = int(input("Insira o lado B do Retângulo: "))

        print("O lado A é: {}, e o lado B é: {}".format(quadrilatero.RetornaLados()[0], quadrilatero.RetornaLados()[1]))
        print("A área do retângulo é igual a: {}".format(quadrilatero.area()))
        print("O perímetro do retângulo é de: {}".format(quadrilatero.perimetro()))
        
    except ValueError:
        print("Número inválido ! Por Favor, digite um número inteiro.")

class Retangulo:
    def RetornaLados(self):
        return self.ladoA, self.ladoB

    def area(self):
        return self.ladoA * self.ladoB

    def perimetro(self):
        return 2*(self.ladoA + self.ladoB)

if __name__ == '__main__':
    main()