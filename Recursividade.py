#Função que imprime uma sequência de números a partir do parâmetro num1 até o parâmetro num2.

def intervalo(num1, num2):
    for i in range(num1, num2 + 1):
        print(i)

#Função que imprime uma sequência de números a partir do parâmetro num1 até o parâmetro num2 com recursividade.
def intervalo2(num1, num2):
    if num1 <= num2:
        print(num1)
        intervalo2(num1 + 1, num2)

#intervalo2(20, 59)

#Função que retorna a soma de uma sequência de númros a partir do parâmetro num1 até 0.
def somaN(num1):
    soma = 0
    for i in range(num1, 0, -1):
        soma += i
    return print(soma)

#Função que imprime um intervalo decrescente de núemros.
def soma0():
    for i in range(10, 0, -1):
        print(i)

#somaN(4)

def somaRegressiva(num1):
    if num1 == 1:
        return num1
    return num1 + somaRegressiva(num1 - 1)

print(somaRegressiva(4))