lista3 = [4,5,6,7,1,9,8]

# Neste caso index será uma Tupla.
for index in enumerate(lista3):
    print(index)

# Neste caso index percorrerá os índices da lista3 e item os elementos da lista3.
for index, item in enumerate(lista3):
    print(index)

print()
print(len(lista3))
print()

for i in range(len(lista3)):
    print(i)

