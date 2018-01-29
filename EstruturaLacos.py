#Segundo Teste Python
#Estruturas de Repetição em Python

#conta = 0

#while (conta <= 10):
    #print(conta)
    #conta += 1
#else:
    #print("Loop Encerrado com sucesso !!!")


array = [3, 4, 5, 6, 77, 88, 99, 0, 87, 66, 55, 44, 33, 22, 110, 100]

"""
for variavel in array:
    print(variavel)
    if(variavel > 99):
        print("Saindo do laço")
        break
else:
    print("Iteração do vetor executada com sucesso !!!")
"""
for item in range(0, 1000, 1):
    if(item%2 == 0):
        continue
    print(item)
else:
    print("Loop executado")