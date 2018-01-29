# -*- coding: utf-8 -*-

# Title     : Exercícios com Listas
# Objective : Arquivo que contém algoritmos para treino da estrutura de listas em python.
# Created by: Gustavo Nunes
# Created on: 12/01/2018

# 1 - Lesson: Algoritmo que obtêm 4 notas, calcula a média das mesmas e as imprime na tela.
"""
lstNotas = []

def main():
    for k in range(1,5):
        notasAlunos = int(input("Digite sua {} nota: ".format(k)))
        armazenaNotas(notasAlunos)
    print("Suas notas foram: {} e sua média é de: {}".format(armazenaNotas(), calculaMedia()))

def armazenaNotas(*notas):
    global lstNotas
    for i in notas:
        lstNotas.append(i)
    return lstNotas

def calculaMedia():
    global lstNotas
    soma = 0
    for j in lstNotas:
        soma += j
    return soma / len(lstNotas)

#main()

# Código de Testes para aa funções "calculaMedia" e "armazenaNotas"

assert [6,7,8,9] == armazenaNotas(6,7,8,9)
print("Ok")
assert 7.5 == calculaMedia([6,7,8,9])
print("OK")

"""
#---------------------------------------------------------------------------------------------------------------------------------------------------#

"""
# Algoritmo que verifica se um número é par ou ímpar e separa-os de acordo com as classificações dos mesmos em listas separadas.
lstPar = []
lstImpar = []

def main():
    for i in range(1,9):
        numeros = int(input("Digite o {} número: ".format(i)))
        numPar(numeros)
        numImpar(numeros)

    print("O vetor par é: {} e o vetor ímpar é: {}".format(numPar(), numImpar()))

def numPar(*numeros):
    global lstPar
    for i in numeros:
        if i % 2 == 0:
            lstPar.append(i)
    return lstPar

def numImpar(*numeros):
    global lstImpar
    for j in numeros:
        if j % 2 != 0:
            lstImpar.append(j)
    return lstImpar

main()


# Código para testes das Funções "numPar" e "numImpar"
#assert [2,4,6,8] == numPar(1,2,3,4,5,6,7,8)
#print("OK")
#assert [1,3,5,7] == numImpar(1,2,3,4,5,6,7,8)
#print("OK")

"""

#----------------------------------------------------------------------------------------------------------------------------------------------------------#


#lstacima10 = []

# Função Principal: Execução do Software
#def main():
#    num = 0
#    while num != -1:
#        try:
#            num = int(input("Digite um número. (-1 aborta o programa.): "))
#            acima10(num)
#        except ValueError:
#            print("Número Inválido, Digite Novamente!")
#    else:
#        print(acima10())

#def acima10(*numeros):
#    """
#    Função que verifica se um número é maior do que 10 e armazena-os em uma lista.
#    :param numeros: Parâmetro que recebe "n" números de entrada para serem verificados pela função.
#    :return: Lista lstacima10
#    """
    
#    global lstacima10
#    for i in numeros:
#        if i > 10:
#            lstacima10.append(i)
#    return lstacima10

#main()

# Código para testar a função "acima10".
#assert [11,22,33,44,55] == acima10(1,3,6,10,11,22,33,44,55)
#print("OK")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#

"""
lstPar = []

# Função Principal: Execução do Software
def main():
    num = 0
    while num != -1:
        num = int(input("Digite um Número: "))
        filtraPar(num)
    else:
        print(filtraPar())

# Função que verifica se um número é par e caso seja, armazena-os em uma lista.
def filtraPar(*numeros):
    global lstPar
    for i in numeros:
        if i % 2 == 0:
            lstPar.append(i)
    return lstPar

# Codigo para testar a função "filtraPar"
#assert [2,4,6,8] == filtraPar(1,2,3,4,5,6,7,8,9)
#print("OK")

main()

"""

#----------------------------------------------------------------------------------------------------------------------------------#
lstValores = []

def main():
    num = 0
    while num != -1:
        num = int(input("Digite um número: "))
        mostrarValores(num)
    else:
        print("A Quantidade de valores informados foi de: {}, \nos valores digitados são: {}, os valores em ordem inversa são: {}. \nA soma dos valores é: {}."
              "\nA média dos valores informados é: {}. \nOs valores acima da média são: {}. \nOs valores menores do que 7 são: {} ".format
              (contaValores(), lstValores, mostraInvertido(), somaValores(), mediaValores(), acimaMedia(), abaixoSete()))

def mostrarValores(*lista):
    global lstValores
    for i in lista:
        lstValores.append(i)

def mostraInvertido():
    global lstValores
    lstInvertido = []
    for i in lstValores:
        lstInvertido.append(i)
    lstInvertido.reverse()
    return lstInvertido

def contaValores():
    return len(lstValores)

def somaValores():
    global lstValores
    soma = 0
    for i in lstValores:
        soma += i
    return soma

def mediaValores():
    return somaValores() / len(lstValores)

def acimaMedia():
    global lstValores
    lstAcimaMedia = []
    for i in lstValores:
        if i > mediaValores():
            lstAcimaMedia.append(i)
    return lstAcimaMedia

def abaixoSete():
    global lstValores
    lst7 = []
    for i in lstValores:
        if i < 7:
            lst7.append(i)
    lst7.sort()
    return lst7

main()

"""
assert [4,5,6,7,8,9,1,2,3] == mostrarValores(4,5,6,7,8,9,1,2,3)
print("OK")
assert [3,2,1,9,8,7,6,5,4] == mostraInvertido(4,5,6,7,8,9,1,2,3)
print("OK")
assert 9 == contaValores(4,5,6,7,8,9,1,2,3)
print("OK")
assert 45 == somaValores(4,5,6,7,8,9,1,2,3)
print("OK")
assert 5 == mediaValores(4,5,6,7,8,9,1,2,3)
print("OK")
assert [6,7,8,9] == acimaMedia(4,5,6,7,8,9,1,2,3)
print("OK")
assert [1,2,3,4,5,6] == abaixoSete(4,5,6,7,8,9,1,2,3)
print("OK")
"""











































































