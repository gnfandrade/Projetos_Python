# -*- coding: utf-8 -*-

# Title     : Exercícios com Listas
# Objective : Arquivo que contém algoritmos para treino da estrutura de listas em python.
# Created by: Gustavo Nunes
# Created on: 16/01/2018

lstVotos = []
lstPorcentagem = []
lstContagem = []
lstFiltVotos = []
lstFiltPorcent = []
lstFiltCont = []

def main():
    num = -1
    while num != 0:
        num = int(input("Digite um núnero entre 1 e 23 ou 0 para encerrar o programa: "))
        armazenaVotos(num)
    else:
        print("O número de votos computados foi de: {}").format(len(lstVotos))
        print()
        print("Votos dos Jogadores")


def armazenaVotos(*num):
    global lstVotos
    for i in num:
        lstVotos.append(i)
    return lstVotos

def votosNaoRepetidos():
    for i, j, k in zip(calculaPorcentagem()[0], calculaPorcentagem()[1], calculaPorcentagem()[2]):


def calculaPorcentagem():
    for i in lstVotos:
        valor = (lstVotos.count(i) / len(lstVotos)) * 100
        lstPorcentagem.append(valor)

    for j in lstVotos:
        valor = lstVotos.count(j)
        lstContagem.append(j)

    return lstPorcentagem, lstContagem, lstVotos

def imprimeFormatado():
    for k in lstPorcentagem:
        return print("O Jogador {} obteve {} votos, equivalente a {} dos votos").format()

main()

"""
# Código para testes
assert [3,3,4,4,6,7,5,7,6,5,3] == armazenaVotos(3,3,4,4,6,7,5,7,6,5,3)
print("OK")
assert [3,4,5,6,7] == votosNaoRepetidos(3,3,4,4,6,7,5,7,6,5,3)
print("OK")
assert 27.27272727272727 == calculaPorcentagem(3)
print("OK")
"""
