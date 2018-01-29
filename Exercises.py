"""
num = 20

vetorPar = []
vetorImpar = []


for i in range(1, num+1):
    n = int(input('Digite um número: '))

    if(n % 2 == 0):
        vetorPar.append(n)
    else:
        vetorImpar.append(n)

print('Números Pares:', vetorPar)
print('Números Ímpares', vetorImpar)
print(vetorPar + vetorImpar)
"""

"""
vetor = []
for seq in range(1,7):
    num = int(input("Digite o número %i de 6: "%seq))
    vetor.append(num)

print(vetor)
"""

print("Enquete: Quem foi o melhor jogador?")
print()

lstj = []
lstaux = []
lstaux2 = []

num = int(input("Digite um número entre 1 e 23 ou 0 para encerrar a enquete: "))
lstj.append(num)
lstaux.append(num)

while(num != 0):
    if(num >= 1 and num <= 23):
        num = int(input("Digite um número entre 1 e 23 ou 0 para encerrar a enquete: "))
        if(num == 0):
            print("FIM")
        else:
            lstj.append(num)
            lstaux.append(num)
    else:
        num = int(input("Número Inválido!, por favor, digite um número entre 1 e 23 ou 0 para encerrar a enquete: "))
print()
print("Resultado da Enquete")
print()
print("Foram Computados: ", len(lstj))
print()
print("Votos dos Jogadores")
print()

for i in lstaux:
    rep = lstj.count(i)
    for j in range(rep-1): # Esta parte do loop For serve para remover todos os n-1 elementos da lista que estamos iterando.
        lstj.remove(i)

for l in lstj:
    rep2 = lstaux.count(i)
    for m in rep2:
        lstaux2.append(m)

lstaux2.sort()





for k in lstj:
    print("O Jogador %i obteve %i votos, equivalente a %.2f%% dos totais de votos" %(
    k, lstaux.count(k), (lstaux.count(k) / len(lstaux)) * 100))




