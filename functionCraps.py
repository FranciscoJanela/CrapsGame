# -*- coding: utf-8 -*-
"""
Funcionalidades para o jogo Craps

@author: Francisco Janela & Nicolas Queiroga
"""
import tipoAposta as tA
import essencialsCraps as eC


# Computação da fase Come Out
# Pergunta quais as apostas do jogador e quanto vai apostar
# Calcula as fichas no final do resultado das apostas
def fase_come_out(fichas,tipo_de_fase):
  Point = 0
  aposta_point = 0
  soma_co = eC.soma_dos_dados()
  print(eC.informa_fase(tipo_de_fase))
  apostas_do_usuario=eC.escolhe_apostas(fichas)  # registra um tuple de respostas que seram usadas no while, a linha 0 referente ao tipo de aposta e a linha 1 ao valor apostado
  i = 0  # índice de controle do while
  while i<len(apostas_do_usuario):  # computa os tipos de aposta feitos pelo jogador
      if apostas_do_usuario[i][0] == 'Pass Line Bet':
          fichas -= apostas_do_usuario[i][1]
          resultado = tA.pass_line_bet(soma_co,fichas,apostas_do_usuario[i][1],tipo_de_fase)
          fichas = resultado[0]
          tipo_de_fase = resultado[1]
          Point = resultado[2]
          aposta_point = resultado[3]
          vitoria = resultado[4]
          print(eC.resposta_da_aposta(fichas,vitoria,apostas_do_usuario[i][0]))
      elif apostas_do_usuario[i][0] == 'Field':
          fichas -= apostas_do_usuario[i][1]
          resultado = tA.field(soma_co, fichas, apostas_do_usuario[i][1])
          fichas = resultado[0]
          vitoria = resultado[1]
          print(eC.resposta_da_aposta(fichas,vitoria,apostas_do_usuario[i][0]))
      elif apostas_do_usuario[i][0] == 'Any Craps':
          fichas -= apostas_do_usuario[i][1]
          resultado = tA.any_craps(soma_co, fichas, apostas_do_usuario[i][1])
          fichas = resultado[0]
          vitoria = resultado[1]
          print(eC.resposta_da_aposta(fichas,vitoria,apostas_do_usuario[i][0]))
      elif apostas_do_usuario[i][0] == 'Twelve':
          fichas -= apostas_do_usuario[i][1]
          resultado = tA.twelve(soma_co,fichas,apostas_do_usuario[i][1])
          fichas = resultado[0]
          vitoria = resultado[1]
          print(eC.resposta_da_aposta(fichas,vitoria,apostas_do_usuario[i][0]))
      else:
          print('resposta inválida, tente novamente')
      i += 1
  resultado_come_out = [fichas,tipo_de_fase,Point,aposta_point]
  return resultado_come_out


# Computação da fase Point
# Pergunta quais as apostas do jogador e quanto vai apostar
# Calcula as fichas no final do resultado das apostas
def fase_point(fichas, tipo_de_fase, Point, aposta_point):         
  soma_p = eC.soma_dos_dados()
  print(eC.informa_fase(tipo_de_fase))
  apostas_do_usuario=eC.escolhe_apostas(fichas) 
  i = 0  # índice de controle do while
  while i<len(apostas_do_usuario):  # computa os tipos de aposta feitos pelo jogador
      if apostas_do_usuario[i][0] == 'Field':
          fichas -= apostas_do_usuario[i][1]
          resultado = tA.field(soma_p, fichas, apostas_do_usuario[i][1])
          fichas = resultado[0]
          vitoria = resultado[1]
          print(eC.resposta_da_aposta(fichas,vitoria,apostas_do_usuario[i][0]))
          resultado = tA.pointBet(Point,soma_p,fichas,aposta_point,tipo_de_fase)
          fichas = resultado[0]
          tipo_de_fase = resultado[1]
          vitoria = resultado[2]
          print(eC.resposta_da_aposta(fichas,vitoria,apostas_do_usuario[i][0]))
      elif apostas_do_usuario[i][0] == 'Any Craps':
          fichas -= apostas_do_usuario[i][1]
          resultado = tA.any_craps(soma_p, fichas, apostas_do_usuario[i][1])
          fichas = resultado[0]
          vitoria = resultado[1]
          print(eC.resposta_da_aposta(fichas,vitoria,apostas_do_usuario[i][0]))
          resultado = tA.pointBet(Point,soma_p,fichas,aposta_point,tipo_de_fase)
          fichas = resultado[0]
          tipo_de_fase = resultado[1]
          vitoria = resultado[2]
          print(eC.resposta_da_aposta(fichas,vitoria,apostas_do_usuario[i][0]))
      elif apostas_do_usuario[i][0] == 'Twelve':
          fichas -= apostas_do_usuario[i][1]
          resultado = tA.twelve(soma_p,fichas,apostas_do_usuario[i][1])
          fichas = resultado[0]
          vitoria = resultado[1]
          print(eC.resposta_da_aposta(fichas,vitoria,apostas_do_usuario[i][0]))
          resultado = tA.pointBet(Point,soma_p,fichas,aposta_point,tipo_de_fase)
          fichas = resultado[0]
          tipo_de_fase = resultado[1]
          vitoria = resultado[2]
          print(eC.resposta_da_aposta(fichas,vitoria,apostas_do_usuario[i][0]))
      elif apostas_do_usuario[i][0] == 'somente Point':
          fichas -= apostas_do_usuario[i][1]
          resultado = tA.pointBet(Point,soma_p,fichas,aposta_point,tipo_de_fase)
          fichas = resultado[0]
          tipo_de_fase = resultado[1]
          vitoria = resultado[2]
          print(eC.resposta_da_aposta(fichas,vitoria,apostas_do_usuario[i][0]))
      else:
          print('resposta inválida, tente novamente')
      i += 1
  resultado_pointbet = [fichas, tipo_de_fase]
  return resultado_pointbet
