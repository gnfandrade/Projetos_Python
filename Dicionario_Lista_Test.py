import un

nomes = []
agenda = {}

while True:
    ordem = input("Deseja Adicionar novo Contato(add) ou Parar Programa(stop)?").lower()

    if not ordem.isalpha():
        print("Somente Letras !")

    elif ordem.startswith('a'):
        contato = {}

        nome = input("Digite o Nome do Contato: ")
        if not nome[0].isupper():
            nome = nome[0].upper() + nome[1:]

        nomes.append(nome)

        tel = input("Digite o Telefone do Contato: ")
        contato["Telefone"] = tel

        end = input("Dogite o Endereço do Contato: ")
        contato["Endereco"] = end

        email = input("Digite o Email do Contato: ")
        contato["Email"] = email

        agenda[nome] = contato

    elif ordem.startswith('s'):
        break



print(nomes)
print()
print(agenda)