contas = []
depositos = []
saldo = 0

def main():
    opcao = bool(int(input("Deseja criar conta(1) ou fechar o programa(0)? ")))
    while opcao:
        criaConta()
        verSaldo()
        opcao = bool(int(input("Deseja criar conta(1) ou fechar o programa(0)? ")))

def criaConta():
    global contas, depositos, saldo
    numConta = int(input("Digite um número para a criação da conta: "))

    while numConta in contas:
        print("Conta já existente! Por favor, digite outro número de conta.")
        numConta = int(input("Digite um número para criação da conta: "))

    contas.append(numConta)

    deposito = float(input("Digite o valor do seu primeiro depósito: "))

    while deposito < 0:
        print("Valor de Depósito inválido! Por favor, Digite novamente o valor do depósito.")
        deposito = float(input("Digite o valor do seu primeiro depósito: "))

    depositos.append(deposito)
    saldo += deposito

def verSaldo():
    global saldo
    opcao = bool(int(input("Deseja ver o saldo bancário? (1 = SIM / 0 = NÃO): ")))
    if opcao:
        print("O saldo do banco é R$", saldo)

main()