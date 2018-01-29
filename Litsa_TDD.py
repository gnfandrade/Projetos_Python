# -*-coding: utf-8 -*-

"""
# Código que adiciona numéros no intervalo de 1 a 5 (inclusive) no vetor de nome lista.
lista = []

for i in range(1, 6):
    lista.append(i)

# Teste Unitário para a lógica de inserção de números na lista.
assert 1 == lista[0]
assert 2 == lista[1]
assert 3 == lista[2]
assert 4 == lista[3]
assert 5 == lista[4]

print("OK !!!")
"""
#------------------------------------------------------------------#
"""
# -*-coding: utf-8 -*-

# Função que Soma os itens da lista (vetor)
def somarLista(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma

lista = [10, 20, 30, 0]

# Código que testa a função "somarLista".
assert 60 == somarLista(lista)


print("OK !!!")
"""
#------------------------------------------------------------------------#

"""
# -*- coding: utf-8 -*-
# Função que copia os elementos de uma lista e adiciona-os em uma outra lista independente.
def copiaLista(lista):
    lst2 = []
    for i in lista:
        lst2.append(i)

    return lst2

# Código que Testa a lógica da função "copiaLista".
assert [20,21,22,4,5,6,7,8,9] == copiaLista([20,21,22,4,5,6,7,8,9])

print("OK !!!")
"""

#----------------------------------------------------------------------------#

"""
#-*- coding: utf-8 -*-

lista = [1,4,5,2,3,10,9]
menor = 0
maior = 0

# Função que retorna o menor índice da lista.
def indiceMenor(lst):
    global menor #Global indica que tal variável não se dá apenas no escopo da função indiceMenor
    for index in range(len(lista)):
        if index <= menor:
            menor = index
    return menor
# Função que retorna o maior índice da lista
def indiceMaior(lst):
    global maior #Global indica que tal variável não se dá apenas no escopo da função indiceMaior.
    for index in range(len(lista)):
        if index > maior:
            maior = index
    return maior

# Código que testa as lógicas das funções indiceMenor e indiceMaior.
assert 0 == indiceMenor(lista)
print("OK")
assert 6 == indiceMaior(lista)
print("OK")
"""

#------------------------------------------------------------------------------------------------------------------#

#-*-coding: utf-8 -*-

def haDuplicata(lst):
   return len(lst) != len(set(lst))

assert 1 == haDuplicata([100,200,300,300,500])
print("SIM")
assert 0 == haDuplicata([100,200,300,400,500])
print("NÃO")









































