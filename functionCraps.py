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
  tipo_de_aposta = eC.escolhe_tipo_aposta()
  aposta = eC.valor_da_aposta(tipo_de_aposta)
  i = 0  # índice de controle do while
  while i<len(tipo_de_aposta):  # computa os tipos de aposta feitos pelo jogador
      if tipo_de_aposta[i] == 'Pass Line Bet':
          fichas -= aposta[i]
          resultado = tA.pass_line_bet(soma_co,fichas,aposta[i],tipo_de_fase[i])
          fichas = resultado[0]
          tipo_de_fase = resultado[1]
          Point = resultado[2]
          aposta_point = resultado[3]
          vitoria = resultado[4]
          print(eC.resposta_da_aposta(fichas,vitoria,tipo_de_aposta[i]))
      elif tipo_de_aposta[i] == 'Field':
          fichas -= aposta[i]
          resultado = tA.field(soma_co, fichas, aposta[i])
          fichas = resultado[0]
          vitoria = resultado[1]
          print(eC.resposta_da_aposta(fichas,vitoria,tipo_de_aposta[i]))
      elif tipo_de_aposta[i] == 'Any Craps':
          fichas -= aposta[i]
          resultado = tA.any_craps(soma_co, fichas, aposta[i])
          fichas = resultado[0]
          vitoria = resultado[1]
          print(eC.resposta_da_aposta(fichas,vitoria,tipo_de_aposta[i]))
      elif tipo_de_aposta[i] == 'Twelve':
          fichas -= aposta[i]
          resultado = tA.twelve(soma_co,fichas,aposta[i])
          fichas = resultado[0]
          vitoria = resultado[1]
          print(eC.resposta_da_aposta(fichas,vitoria,tipo_de_aposta[i]))
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
  tipo_de_aposta = eC.escolhe_tipo_aposta()
  aposta = eC.valor_da_aposta(tipo_de_aposta)
  i = 0  # índice de controle do while
  while i<len(tipo_de_aposta):  # computa os tipos de aposta feitos pelo jogador
      if tipo_de_aposta[i] == 'Field':
          fichas -= aposta[i]
          resultado = tA.field(soma_p, fichas, aposta[i])
          fichas = resultado[0]
          vitoria = resultado[1]
          print(eC.resposta_da_aposta(fichas,vitoria,tipo_de_aposta[i]))
          resultado = tA.pointBet(Point,soma_p,fichas,aposta_point,tipo_de_fase)
          fichas = resultado[0]
          tipo_de_fase = resultado[1]
          vitoria = resultado[2]
          print(eC.resposta_da_aposta(fichas,vitoria,tipo_de_aposta))
      elif tipo_de_aposta[i] == 'Any Craps':
          fichas -= aposta[i]
          resultado = tA.any_craps(soma_p, fichas, aposta[i])
          fichas = resultado[0]
          vitoria = resultado[1]
          print(eC.resposta_da_aposta(fichas,vitoria,tipo_de_aposta[i]))
          resultado = tA.pointBet(Point,soma_p,fichas,aposta_point,tipo_de_fase)
          fichas = resultado[0]
          tipo_de_fase = resultado[1]
          vitoria = resultado[2]
          print(eC.resposta_da_aposta(fichas,vitoria,tipo_de_aposta))
      elif tipo_de_aposta[i] == 'Twelve':
          fichas -= aposta[i]
          resultado = tA.twelve(soma_p,fichas,aposta[i])
          fichas = resultado[0]
          vitoria = resultado[1]
          print(eC.resposta_da_aposta(fichas,vitoria,tipo_de_aposta[i]))
          resultado = tA.pointBet(Point,soma_p,fichas,aposta_point,tipo_de_fase)
          fichas = resultado[0]
          tipo_de_fase = resultado[1]
          vitoria = resultado[2]
          print(eC.resposta_da_aposta(fichas,vitoria,tipo_de_aposta))
      elif tipo_de_aposta[i] == 'somente Point':
          fichas -= aposta[i]
          resultado = tA.pointBet(Point,soma_p,fichas,aposta_point,tipo_de_fase)
          fichas = resultado[0]
          tipo_de_fase = resultado[1]
          vitoria = resultado[2]
          print(eC.resposta_da_aposta(fichas,vitoria,tipo_de_aposta))
      else:
          print('resposta inválida, tente novamente')
      i += 1
  resultado_pointbet = [fichas, tipo_de_fase]
  return resultado_pointbet
