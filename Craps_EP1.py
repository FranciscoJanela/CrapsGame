# -*- coding: utf-8 -*-
"""
Craps!

@author: Francisco Janela & Nicolas Queiroga
"""
import random

fichas = int(imput('Quantas fichas você quer? '))
tipo_de_fase=str('Come out')
while fichas>0:
    in_out=input('deseja apostar ou sair?\n(digite "apostar" ou "sair")\nResposta:')
    if in_out=='apostar':
        if tipo_de_fase=='Come out':
            print('Você está na fase Come Out')
            dado1co = random.randint(1, 6)
            dado2co = random.randint(1, 6)
            soma_co = dado1co + dado2co
            print('Está na fase Come Out,\ntem disponível os seguintes tipos de aposta')
            print(' - Pass Line Bet\n - Field\n - Any Craps\n - Twelve')
            print('(para escolher digite exatamente o nome da aposta)')
            tipo_de_aposta =input('a aposta será: ')
            valor_da_aposta
            if tipo_de_aposta=='Pass Line Bet':
                if soma_co==7 or soma_co==11:
                    fichas+=
                elif soma_co==2 or soma_co==3 or soma_co==12:
                    
                else:
                    
            if tipo_de_aposta == 'Field':
                if soma_co == 5 or soma_co == 6 or soma_co == 7 or soma_co == 8:
                    fichas -= fichas
                elif soma_co == 3 or soma_co == 4 or soma_co == 9 or soma_co == 10 or soma_co == 11:
                    fichas += aposta
                elif soma_co == 2:
                    fichas = fichas + aposta*2 + aposta
                elif soma_co == 12:
                    ficahs = fichas + aposta*3 + aposta
        elif tipo_de_fase=='Point':
            dado1p = random.randint(1, 6)
            dado2p = random.randint(1, 6)
            somap = dado1p + dado2p
    elif in_out=='sair':
        break
    else:
        print('resposta inválida')
    
        
