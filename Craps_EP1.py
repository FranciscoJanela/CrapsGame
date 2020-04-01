# -*- coding: utf-8 -*-
"""
Craps!

@author: Francisco Janela & Nicolas Queiroga
"""
import random
import functionCraps.py as fC

fichas = int(input('Quantas fichas você quer? '))
point=0
soma=0
tipo_de_fase=str('Come out')
while fichas>0:
    in_out=input('deseja apostar ou sair?\n(digite "apostar" ou "sair")\nResposta:')
    if in_out=='apostar':
        if tipo_de_fase=='Come out':
            resultado_come_out=fC.come_out(fichas,tipo_de_fase)
            fichas=resultado_come_out[0]
            tipo_de_fase=resultado_come_out[1]
        elif tipo_de_fase=='Point':
            dado1p = random.randint(1, 6)
            dado2p = random.randint(1, 6)
            soma_p = dado1p + dado2p
            print('Está na fase Point,\ntem disponível os seguintes tipos de aposta')
            print(' - Field\n - Any Craps\n - Twelve\n - somente Point')
            print('(para escolher digite exatamente o nome do tipo de aposta)')
            tipo_de_aposta =input('a aposta será: ')
            valor_da_aposta=int(input('o valor da aposta será: '))
            fichas-=aposta
            if tipo_de_aposta=='Field':
                fichas = field(soma_p, fichas, aposta)
                resultado=pointBet(point,soma,fichas,aposta_point,tipo_de_fase)
                fichas=resultado[0]
                tipo_de_fase=resultado[1]
            elif tipo_de_aposta == 'Any Craps':
                fichas = any_craps(soma_p, fichas, aposta)
                resultado=pointBet(point,soma,fichas,aposta_point,tipo_de_fase)
                fichas=resultado[0]
                tipo_de_fase=resultado[1]
            elif tipo_de_aposta=='Twelve':
                fichas=twelve(soma_p,fichas,aposta)
                resultado=pointBet(point,soma,fichas,aposta_point,tipo_de_fase)
                fichas=resultado[0]
                tipo_de_fase=resultado[1]
            elif tipo_de_aposta=='somente Point':
                resultado=pointBet(point,soma,fichas,aposta_point,tipo_de_fase)
                fichas=resultado[0]
                tipo_de_fase=resultado[1]
            else:
                print('resposta inválida, tente novamente')
            
    elif in_out=='sair':
        print('Você saiu do jogo')
        break
    else:
        print('resposta inválida')
    
        
