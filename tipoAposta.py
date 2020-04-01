def pass_line_bet(soma,fichas,aposta,tipo_de_fase):
    if soma==7 or soma==11:
        fichas+=aposta*2
    elif soma==2 or soma==3 or soma==12:
        fichas=fichas
    else:
        tipo_de_fase='Point'
        fichas=ficha
        aposta_point=aposta
        point=soma
    resultado=[fichas,tipo_de_fase,point,aposta_point]
    return resultado

def pointBet(point,soma,fichas,aposta_point,tipo_de_fase):
    if soma==point:
        fichas+=2*aposta_point
        tipo_de_fase='Come out'
    elif soma==7:
        fichas=fichas
        tipo_de_fase='Come out'
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
