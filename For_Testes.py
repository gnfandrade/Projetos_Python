lista = [3,4,5,6,7,3,1,2,8,3,9,6,5,4,7,11,12,1,3,2]
lista2 = lista.copy()
lstindices = []
"""
tupla = (20,10,10,10,10,20,10,10,5,20,5,10,10,10,10,5,5,10,20,10)
for i, k in zip(lista, tupla):
    print(i, k)
"""
lstPorcentagem = []
lstContagem = []
lstFiltPorcent = []
lstFiltCont = []
lstIndexPorcent = []

def calcular():
    for i in lista:
        valor = (lista.count(i) / len(lista)) * 100
        lstPorcentagem.append(valor)

    for j in lista:
        contagem = lista.count(j)
        lstContagem.append(contagem)

    return lstPorcentagem, lstContagem, lista

#print(calcular())

for i, j, k in zip(calcular()[0], calcular()[1], calcular()[2]):
    rep = calcular()[2].count(k)
    for h in range(rep-1):
        lista.remove(k)

for i in lista:
    indices = lista2.index(i)
    lstindices.append(indices)


for i in lstindices:
    ele = calcular()[0][i]
    ele2 = calcular()[1][i]
    lstFiltPorcent.append(ele)
    lstFiltCont.append(ele2)

def imprimeMatriz():
    matriz = []
    matriz.append(lstFiltPorcent)
    matriz.append(lstFiltCont)
    matriz.append(lista)

    return matriz

"""
print(lista)
print(lstFiltPorcent)
print(lstFiltCont)

"""
for i, j, k in zip(imprimeMatriz()[0], imprimeMatriz()[1], imprimeMatriz()[2]):
    print(i, j, k)




















