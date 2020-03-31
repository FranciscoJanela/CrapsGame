# -*- coding: utf-8 -*-
"""
Craps!

@author: Francisco Janela & Nicolas Queiroga
"""
import random

def pass_line_bet(soma,fichas,aposta,tipo_de_fase):
    if soma==7 or soma==11:
        fichas+=aposta*2
    elif soma==2 or soma==3 or soma==12:
        ficha=ficha
    else:
        tipo_de_fase='Point'
        fichas=ficha
        aposta_point=aposta
        point=soma
    resultado[fichas,tipo_de_fase,point,aposta_point]
    return resultado

def pointBet(point,soma,fichas,aposta_point,tipo_de_fase):
    if soma==point:
        fichas+=2*aposta_point
        tipo_de_fase='Come out'
    elif soma==7:
        ficha=ficha
        tipo_de_fase='Come out'
    else:
    resultado=[fichas,tipo_de_fase]
    return resultado

def field(soma, fichas, aposta):
    if soma == 5 or soma == 6 or soma == 7 or soma == 8:
        fichas = fichas
    elif soma == 3 or soma == 4 or soma == 9 or soma == 10 or soma == 11:
        fichas += aposta*2
    elif soma == 2:
        fichas += aposta*3
    elif soma == 12:
        fichas += aposta*4
    return fichas

def any_craps(soma, fichas, aposta):
    if soma == 2 or soma == 3 or soma == 12:
        fichas += aposta*8
    else:
        fichas = fichas
    return fichas

def twelve(soma,fichas,aposta):
    if soma==12:
        fichas+=aposta*31
    else:
        fichas=fichas
    return fichas

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
            print('(para escolher digite exatamente o nome do tipo de aposta)')
            tipo_de_aposta =input('a aposta será: ')
            aposta=int(input('o valor da aposta será: '))
            fichas-=aposta
            if tipo_de_aposta=='Pass Line Bet':
                
            elif tipo_de_aposta == 'Field':
                
            elif tipo_de_aposta == 'Any Craps':
                
            elif tipo_de_aposta=='Twelve':
                
            else:
                print('resposta inválida, tente novamente')
        elif tipo_de_fase=='Point':
            dado1p = random.randint(1, 6)
            dado2p = random.randint(1, 6)
            soma_p = dado1p + dado2p
            print('Está na fase Point,\ntem disponível os seguintes tipos de aposta')
            print(' - Field\n - Any Craps\n - Twelve')
            print('(para escolher digite exatamente o nome do tipo de aposta)')
            tipo_de_aposta =input('a aposta será: ')
            valor_da_aposta=int(input('o valor da aposta será: '))
            fichas-=aposta
            if tipo_de_aposta=='Field':
                
            elif tipo_de_aposta == 'Any Craps':
                
            elif tipo_de_aposta=='Twelve':

            else:
                print('resposta inválida, tente novamente')
            
    elif in_out=='sair':
        break
    else:
        print('resposta inválida')
    
        
