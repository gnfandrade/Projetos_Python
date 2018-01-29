# -*- coding: utf-8 -*-

def antecessor(numero):
    return numero - 1

def sucessor(numero):
    return numero + 1


#
# Testes
#
assert antecessor(10) == 9, "O antecessor de 10 deve ser igual a 9."
assert sucessor(10) == 11, "O sucessor de 10 deve ser igual a 11."

print("O Teste Passou !!!")
