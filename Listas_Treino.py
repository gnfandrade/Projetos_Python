n = int(input("Digite um número inteiro: "))

lista = []
lstaux = []


for i in range(n):
    elemento = int(input("Digite o elemento %i de %i: "%(i+1, n)))
    lista.append(elemento)
    lstaux.append(elemento)

print(lista)
print()

for ele in lstaux:
    aparicoes = lista.count(ele)
    print(aparicoes)
    for i in range(aparicoes-1): # Esta parte do loop For serve para remover todos os n-1 elementos da lista que estamos iterando.
       lista.remove(ele)

print(lista)