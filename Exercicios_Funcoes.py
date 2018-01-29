# Exercício para praticar a declaração de funções em Python.

# Programa que realiza o cálculo do custo final de um produto por meio da entrada do preço de fabricação e do valor do imposto.

custo = float(input("Insira o Valo do Custo do Produto: "))
imposto = float(input("Digite o valor do Imposto a ser Adicionado ao Valor do Produto: "))

def somaImposto(custo, imposto):
    return custo + imposto

print("O valor do Produto Final será de:",somaImposto(custo, imposto),"Reais")