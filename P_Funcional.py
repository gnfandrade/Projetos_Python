matriz = [[1,2,3],
          [5,9,1],
          [7,8,9]]

lstindice = []
lstcopia = matriz[1].copy()
matriz[1].sort()

# Pela iteração dos elementos da lista matriz na linha 1, usa-se tais elementos para obter-se os índices dos mesmos adicionando-os na variável valor. Posteriormente os índices são
# adicionados na lista lstindice.
for i in matriz[1]:
    valor = lstcopia.index(i)
    lstindice.append(valor)

matriz2 = [[],[],[]]

# Usa-se a lista lstindice para adicionar nas matrizes m"número do índice da lista matriz" os elementos da linha especificada da lista matriz conforme os índices anteriores da linha 1 da
# lista matriz.
for x in lstindice:
    matriz2[0].append(matriz[0][x])
    matriz2[1].append(lstcopia[x])
    matriz2[2].append(matriz[2][x])

print(matriz2)
print(lstindice)




