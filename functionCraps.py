# -*- coding: utf-8 -*-
"""
Funcionalidades para o jogo Craps

@author: Francisco Janela & Nicolas Queiroga
"""
import tipoAposta as tA
import essencialsCraps as eC

def fase_come_out(fichas,tipo_de_fase):
  Point=0
  aposta_point=0
  soma_co = eC.soma_dos_dados()
  print(eC.informa_fase(tipo_de_fase))
  tipo_de_aposta =input('a aposta será: ')
  aposta=int(input('o valor da aposta será: '))
  fichas -= aposta
  if tipo_de_aposta=='Pass Line Bet':
      resultado=tA.pass_line_bet(soma_co,fichas,aposta,tipo_de_fase)
      fichas=resultado[0]
      tipo_de_fase=resultado[1]
      Point=resultado[2]
      aposta_point=resultado[3]
      vitoria=resultado[4]
      print(eC.resposta_da_aposta(fichas,vitoria,tipo_de_aposta))
  elif tipo_de_aposta == 'Field':
      resultado = tA.field(soma_co, fichas, aposta)
      fichas=resultado[0]
      vitoria=resultado[1]
      print(eC.resposta_da_aposta(fichas,vitoria,tipo_de_aposta))
  elif tipo_de_aposta == 'Any Craps':
      resultado = tA.any_craps(soma_co, fichas, aposta)
      fichas=resultado[0]
      vitoria=resultado[1]
      print(eC.resposta_da_aposta(fichas,vitoria,tipo_de_aposta))
  elif tipo_de_aposta=='Twelve':
      resultado = tA.twelve(soma_co,fichas,aposta)
      fichas=resultado[0]
      vitoria=resultado[1]
      print(eC.resposta_da_aposta(fichas,vitoria,tipo_de_aposta))
  else:
      print('resposta inválida, tente novamente')
  resultado_come_out=[fichas,tipo_de_fase,Point,aposta_point]
  return resultado_come_out

def fase_point(fichas, tipo_de_fase, Point, aposta_point):         
  soma_p = eC.soma_dos_dados()
  print(eC.informa_fase(tipo_de_fase))
  tipo_de_aposta =input('a aposta será: ')
  aposta=int(input('o valor da aposta será: '))
  fichas-=aposta
  if tipo_de_aposta=='Field':
      resultado = tA.field(soma_p, fichas, aposta)
      fichas=resultado[0]
      vitoria=resultado[1]
      print(eC.resposta_da_aposta(fichas,vitoria,tipo_de_aposta))
      resultado=tA.pointBet(Point,soma_p,fichas,aposta_point,tipo_de_fase)
      fichas=resultado[0]
      tipo_de_fase=resultado[1]
      vitoria=resultado[2]
      print(eC.resposta_da_aposta(fichas,vitoria,tipo_de_aposta))
  elif tipo_de_aposta == 'Any Craps':
      resultado = tA.any_craps(soma_p, fichas, aposta)
      fichas=resultado[0]
      vitoria=resultado[1]
      print(eC.resposta_da_aposta(fichas,vitoria,tipo_de_aposta))
      resultado=tA.pointBet(Point,soma_p,fichas,aposta_point,tipo_de_fase)
      fichas=resultado[0]
      tipo_de_fase=resultado[1]
      vitoria=resultado[2]
      print(eC.resposta_da_aposta(fichas,vitoria,tipo_de_aposta))
  elif tipo_de_aposta=='Twelve':
      resultado = tA.twelve(soma_p,fichas,aposta)
      fichas=resultado[0]
      vitoria=resultado[1]
      print(eC.resposta_da_aposta(fichas,vitoria,tipo_de_aposta))
      resultado=tA.pointBet(Point,soma_p,fichas,aposta_point,tipo_de_fase)
      fichas=resultado[0]
      tipo_de_fase=resultado[1]
      vitoria=resultado[2]
      print(eC.resposta_da_aposta(fichas,vitoria,tipo_de_aposta))
  elif tipo_de_aposta=='somente Point':
      resultado=tA.pointBet(Point,soma_p,fichas,aposta_point,tipo_de_fase)
      fichas=resultado[0]
      tipo_de_fase=resultado[1]
      vitoria=resultado[2]
      print(eC.resposta_da_aposta(fichas,vitoria,tipo_de_aposta))
  else:
      print('resposta inválida, tente novamente')
  resultado_pointbet=[fichas, tipo_de_fase]
  return resultado_pointbet
