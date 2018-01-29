# -*- coding: utf-8 -*-

#
# Retorna o custo final da fabricação de um carro
#
def custoFinal(custoFabrica):
    custoProdutor = 0.28 * custoFabrica
    custoImposto = 0.45 * custoFabrica

    return custoFabrica + custoProdutor + custoImposto

#
# Teste
#
assert 17300 == custoFinal(10000), "'custoFinal' deve ser igual a 17300"

print("O Teste Passou !!!")
