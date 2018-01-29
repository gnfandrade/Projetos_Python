class Pessoa():
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        if self.idade < 21:
            self.altura += 0.05

        self.idade += 1

        return self.idade, self.altura

    def engordar(self, peso):
         self.peso += peso
         return self.peso

    def emagrecer(self, peso):
        self.peso -= peso
        return self.peso

    def crescer(self, altura):
        self.altura += altura
        return self.altura
