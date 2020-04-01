import tipoAposta as tA
import random
import essencialCraps as eC

def come_out(fichas,tipo_de_fase):
  print('Você está na fase Come Out')
  soma_co = eC.soma_dos_dados()
  print('Está na fase Come Out,\ntem disponível os seguintes tipos de aposta')
  print(' - Pass Line Bet\n - Field\n - Any Craps\n - Twelve')
  print('(para escolher digite exatamente o nome do tipo de aposta)')
  tipo_de_aposta =input('a aposta será: ')
  aposta=int(input('o valor da aposta será: '))
  fichas -= aposta
  if tipo_de_aposta=='Pass Line Bet':
      resultado=tA.pass_line_bet(soma_co,fichas,aposta,tipo_de_fase)
      fichas=resultado[0]
      tipo_de_fase=resultado[1]
      Point=resultado[2]
      aposta_point=resultado[3]
  elif tipo_de_aposta == 'Field':
      fichas = tA.field(soma_co, fichas, aposta)
  elif tipo_de_aposta == 'Any Craps':
      fichas = tA.any_craps(soma_co, fichas, aposta)
  elif tipo_de_aposta=='Twelve':
      fichas=tA.twelve(soma_co,fichas,aposta)
  else:
      print('resposta inválida, tente novamente
  resultado=[fichas,tipo_de_fase,Point,aposta_point]
  return resultado

def fase_point(fichas, tipo_de_fase, Point, aposta_point)           
  soma_p = eC.soma_dos_dados()
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
  return fichas, tipo_de_fase
