import tipoAposta.py as tA

def come_out(fichas,tipo_de_fase):
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
  resultado=[fichas,tipo_de_fase]
  return resultado
