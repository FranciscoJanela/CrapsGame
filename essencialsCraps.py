# -*- coding: utf-8 -*-
"""
Funções essenciais para jogo Craps

@author: Francisco Janela & Nicolas Queiroga
"""
import random
import time

#função que imprime as regras do jogo para o usuário
def introducao_do_jogo(username):
    print('{0}'.format(str('*')*40))
    print('Bem vindo ao Craps, {0}'.format(username))
    print('Este jogo consiste em apostas sucessivas para o número da soma de dois dados de seis lados dentro de dois tipos de fase:')
    print('-Come Out\n-Point\n')
    print('Na fase Come Out existem 4 tipos de apostas possíveis de serem feitas:')
    print('- Field:\n  Se a soma for 5, 6, 7 ou 8 perde a aposta\n  Se a soma for 3, 4, 9, 10 ou 11 ganha o valor da aposta\n  Se for 2 ganha o doubro e 12 o triplo do que apostou')
    print('- Any Craps:\n   Se a soma for 2, 3 ou 12 ganha 7 vezes o q apostou\n  Se não perde a aposta')
    print('- Twelve:\n  Se a soma der 12 ganha 35 vezes o que apostou\n  Se não perde a aposta')
    print('- Pass Line Bet:\n  Se a soma der 7 ou 11, recebe a aposta\n  Se for 2, 3 ou 12, perde a aposta\n  Se a soma der outro número, entrará na fase Point e sua aposta ainda vale\n')
    print('Na fase Point ainda pode apostar em Field, Any Craps e Twelve, porém:')
    print('Nesta fase, a soma na aposta do Pass Line Bet se torna o Point\nE até a soma da rodada ser igual ao Point ou a 7, permanece na fase Point')
    print('Se a soma da rodada for igual ao Point, receberá a aposta feita no Pass Line Bet\nSe for igual a 7 perde essa aposta.\n')
    print('Você começará o jogo com 1000 fichas.')
    print('Boa sorte nas apostas, {0}!\n'.format(username))
    fim_da_introdução = 40*str('*')
    return fim_da_introdução


#função que imprime resposta caso o usuário não queira mais apostar
def sair_do_jogo(username,fichas):
    print('\n{0}'.format(str('*')*40))
    print('Obrigado por jogar, {0}'.format(username))
    print('Saiu do jogo com {0} fichas.'.format(fichas))
    print('Volte sempre!')
    fim_do_jogo = 40*str('*')
    return fim_do_jogo


#função que imprime a resposta ao usuário caso acabem suas fichas
def fichas_acabaram(username):
    print('\n{0}'.format(str('*')*40))
    print('Que pena... Suas fichas acabaram.')
    print('Volte sempre!')
    fim_do_jogo = 40*str('*')
    return fim_do_jogo


#função que calcula a soma de dois dados de seis lados
def soma_dos_dados():
    print('A soma dos dados é...\n')
    time.sleep(2)
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    soma = dado1 + dado2
    print(soma)
    return soma


#função que informa ao usuário a fase em que está e suas possíveis apostas
def informa_fase(tipo_de_fase):
    if tipo_de_fase == 'Come out':
        print('Está na fase Come Out,\ntem disponível os seguintes tipos de aposta')
        print(' - Pass Line Bet\n - Field\n - Any Craps\n - Twelve')
    else:
        print('Está na fase Point,\ntem disponível os seguintes tipos de aposta')
        print(' - Field\n - Any Craps\n - Twelve\n - Somente Point')
    fim_informa_fase = '(para escolher digite exatamente o nome do tipo de aposta)\n'
    return fim_informa_fase


#Integra o sistema de mais de uma aposta por rodada
#leva em consideração se a resposta do usuário é adequada e se pode apostar o valor escrito comparando com as fichas que tem
def escolhe_apostas(fichas):
    print('Que tipo de aposta deseja fazer?\n(caso não queira mais digite terminei)')
    tipo_de_aposta = str('')
    apostas_do_usuario = []
    tipo_de_aposta_valido = ['Pass Line Bet','Field','Any Craps','Twelve','Somente Point','terminei']  # Lista dos tipos de aposta possíveis
    total_apostado = 0
    while tipo_de_aposta != 'terminei':
        tipo_de_aposta = input('Tipo da aposta: ')
        if tipo_de_aposta in tipo_de_aposta_valido:
            if not any(aposta_ja_feita for aposta_ja_feita in apostas_do_usuario if aposta_ja_feita[0] == tipo_de_aposta):  # Garante que o tipo de aposta ainda não foi feito
                if tipo_de_aposta != 'terminei':
                    print('\nVocê tem {0} fichas'.format(fichas-total_apostado))
                    valor_da_aposta = input('Valor da aposta: ')
                    if not valor_da_aposta.isdigit() or '.' in valor_da_aposta or ',' in valor_da_aposta:  # Garante que o valor apostado seja um número
                        print('Aposta recusada,\nO valor da aposta tem de ser inteiro')
                    else:
                        valor_da_aposta = int(valor_da_aposta)
                        if total_apostado + valor_da_aposta <= fichas:
                            apostas_do_usuario.append((tipo_de_aposta,valor_da_aposta))
                            total_apostado += valor_da_aposta
                        else:
                            print('\nAposta recusada,\nNão tem fichas suficientes')
                else:
                    break
            else:
                print('\nTipo de aposta já feita\nNão pode repetir o tipo de aposta')
        else:
            print('\nTipo de aposta inválido')
    return apostas_do_usuario # A linha 0 leva o valor do tipo de aposa e a linha 1 o valor apostado
            
    
#função que computa e imprime o resultado da aposta feita pelo usuário
def resposta_da_aposta(fichas,vitoria,tipo_de_aposta):
    if vitoria == True:
        print('\nParabéns!\nSua aposta em {0} rendeu!'.format(tipo_de_aposta))
        print('Você agora tem {0} fichas.'.format(fichas))
    elif vitoria == False:
        print('\nQue pena...\nVocê perdeu a aposta em {0}.'.format(tipo_de_aposta))
        print('Você agora tem {0} fichas.'.format(fichas))
    elif vitoria == 'point':
        print('\nVocê foi para a fase de Point!\nSua aposta ainda continua valendo.')
        print('Você agora tem {0} fichas.'.format(fichas))
    elif vitoria == 'point vitoria':
        print('\nVocê ganhou no Point!\nvoltará para a fase Come Out, parabéns!')
        print('Você agora tem {0} fichas.'.format(fichas))
    elif vitoria == 'point mantem':
        print('\nVocê se mantem na fase Point.')
        print('Continua com {0} fichas.'.format(fichas))
    else:
        print('\nQue pena, você perdeu no Point...\nVoltará para a fase Come Out.')
        print('Você agora tem {0} fichas.'.format(fichas))
    fim_resposta = '***'
    return fim_resposta
