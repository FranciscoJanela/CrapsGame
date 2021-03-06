# -*- coding: utf-8 -*-
"""
Craps!

@author: Francisco Janela & Nicolas Queiroga
"""
import functionCraps as fC
import essencialsCraps as eC

# Introdução do jogo
username = input('Username: ') 
print(eC.introducao_do_jogo(username))
fichas = 1000
tipo_de_fase = str('Come out')

# Fase de apostas:
# Pergunta se o jogador quer jogar ou sair e efetua a estrutura de apostas do jogo
# Sai do while se o jogador quisr parar ou se acabarem as fichas
while fichas > 0:
    in_out = input('deseja apostar ou sair?\n(digite "apostar" ou "sair")\nResposta: ')
    if in_out == 'apostar':
        if tipo_de_fase == 'Come out':
            resultado_come_out = fC.fase_come_out(fichas,tipo_de_fase)
            fichas = resultado_come_out[0]
            tipo_de_fase = resultado_come_out[1]
            Point = resultado_come_out[2]
            aposta_point = resultado_come_out[3]
        elif tipo_de_fase == 'Point':
            resultado_Point = fC.fase_point(fichas,tipo_de_fase,Point,aposta_point)
            fichas = resultado_Point[0]
            tipo_de_fase = resultado_Point[1]
            
    elif in_out == 'sair':
        print(eC.sair_do_jogo(username,fichas))
        break
    else:
        print('resposta inválida')
else:
    print(eC.fichas_acabaram(username))
