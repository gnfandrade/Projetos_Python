# Função que retorna "N" parâmetros.
"""
lista = 0

def operacaoMat(num1, num2):
    return num1 + num2, num1 - num2, num1 * num2, num1 / num2, num1 % num2

lista = list(operacaoMat(4, 3))

print(lista)

for i in lista:
    print(i)

"""
"""

#Algoritmo que retorna a média de notas conforme o peso das mesmas dada pela soma processada pela função "somar".
def somar(*nums):
    somaNum = 0
    for num in nums:
        somaNum += num

    return somaNum

def media(p1, p2, p3, peso1 = 1, peso2 = 1, peso3 = 1):
    return (p1 * peso1 + p2 * peso2 + p3 * peso3) / somar(peso1, peso2, peso3)

print(media(6, 4, 5, 2))

"""

"""
def multiplica(*multi):
    multiNum = 1
    for i in multi:
        multiNum *= i

    return multiNum

print(multiplica(3,4,2,5,6,7,8))

"""
"""
def maiorNum(*nums):
    maior = nums [0] #índice da tupla.
    for i in nums:
        if(i > maior):
            maior = i

    return maior

print(maiorNum(3,4,5,6,77,99,100,-1,-2,44))

"""

