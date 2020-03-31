# -*- coding: utf-8 -*-
"""
Craps!

@author: Francisco Janela & Nicolas Queiroga
"""
dinheiro = 100
while dinheiro>0:
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    soma = dado1 + dado2
    print('Você está na fase )
    aposta = int(input('Qual é a sua aposta? '))
    if soma == 7 or soma == 11:
        dinheiro += aposta
    elif soma == 2 or soma == 3 or soma == 12:
        dinheiro -= aposta
    else:
