# -*- coding: utf-8 -*-
"""
Definição dos tipos de aposta
Recebe as fichas que o jogador tem e a aposta feita e devolve o resultado da aposta

@author: Francisco Janela & Nicolas Queiroga
"""

# Computação do tipo de aposta Pass Line Bet
def pass_line_bet(soma,fichas,aposta,tipo_de_fase):
    point = 0
    aposta_point = 0
    if soma == 7 or soma == 11:
        fichas += aposta*2
        vitoria=True
    elif soma == 2 or soma == 3 or soma == 12:
        vitoria = False
    else:
        tipo_de_fase = 'Point'
        aposta_point = aposta
        point=soma
        vitoria = 'point'
    resultado = [fichas,tipo_de_fase,point,aposta_point,vitoria]
    return resultado

# Computação do tipo de aposta Point Bet
def pointBet(point,soma,fichas,aposta_point,tipo_de_fase):
    if soma == point:
        fichas += 2*aposta_point
        vitoria = 'point vitoria'
        tipo_de_fase = 'Come out'
    elif soma == 7:
        vitoria = 'point perda'
        tipo_de_fase = 'Come out'
    else:
        vitoria = 'point mantem'
    resultado = [fichas,tipo_de_fase,vitoria]
    return resultado

def field(soma, fichas, aposta):
    if soma == 5 or soma == 6 or soma == 7 or soma == 8:
        vitoria = False
    elif soma == 3 or soma == 4 or soma == 9 or soma == 10 or soma == 11:
        fichas += aposta*2
        vitoria = True
    elif soma == 2:
        fichas += aposta*3
        vitoria = True
    elif soma == 12:
        fichas += aposta*4
        vitoria = True
    resultado = [fichas,vitoria]
    return resultado

# Computação do tipo de aposta Any Craps
def any_craps(soma, fichas, aposta):
    if soma == 2 or soma == 3 or soma == 12:
        fichas += aposta*8
        vitoria = True
    else:
        vitoria = False
    resultado = [fichas,vitoria]
    return resultado

# Computação do tipo de aposta Twelve
def twelve(soma,fichas,aposta):
    if soma == 12:
        fichas += aposta*31
        vitoria = True
    else:
        vitoria = False
    resultado = [fichas,vitoria]
    return resultado
