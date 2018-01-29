# -*- coding: utf-8 -*-

# Title     : Exercícios com variáveis globais.
# Objective : Arquivo que contém algoritmos para treino das variáveis globais em python.
# Created by: Gustavo Nunes
# Created on: 16/01/2018

import random

meu = [5, 10, 31, 32, 42, 60]

mega = list(range(1,61))

n = int(input("Número de testes: "))

soma = 0

for i in range(n):
    sorteado = []

    cont = 0

    while meu != sorteado:
        mega_sort = mega.copy()

        sorteado = []

        for j in range(6):
            num_sorteado = random.choice(mega_sort)
            sorteado.append(num_sorteado)
            mega_sort.remove(num_sorteado)

        sorteado.sort()

        cont +=1

    soma += cont

    print("Resultado do teste {}: {} tentativas".format(i+1, cont))

soma /= n

print("Média dos resultador: {}".format(soma))














