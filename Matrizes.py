import random
matriz = []

def geraMatriz(matriz):
    lista = list(range(16))
    for i in range(4):
        linha = []
        for j in range(4):
            x = random.choice(lista)
            linha.append(x)
            lista.remove(x)
        matriz.append(linha)

for i in range(1):
    matriz = []
    geraMatriz(matriz)
    print(matriz)