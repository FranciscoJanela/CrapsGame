import random

def soma_dos_dados():
    dado1=random.randint(1,6)
    dado2=random.randint(1,6)
    soma=dado1+dado2
    return soma

def resposta_da_aposta(fichas,vitoria,tipo_de_aposta):
    if vitoria==True:
        print('Parabéns!\nSua aposta em {0} rendeu!')
        print('Você agora tem {1} fichas.'.format(tipo_de_aposta,fichas))
    elif vitoria=='point':
        print('Você foi para a fase de Point!\nSua aposta ainda continua valendo.')
        print('Você agora tem {0} fichas.'.format(fichas))
    elif vitoria==False:
        print('Que pena...\nVocê perdeu a aposta em {0}.')
        print('Você agora tem {1} fichas.'.format(tipo_de_aposta,fichas))
    else:
        if vitoria=='point vitoria':
            print('Você ganhou no Point!\nvoltará para a fase Come Out, parabéns!')
            print(Você agora tem {0} fichas.'.format(fichas))
        elif vitoria=='point mantem':
            print('Você se mantem na fase Point.')
            print('Continua com {0} fichas.'.format(fichas))
        else:
            print('Que pena, você perdeu no Point...\nVoltará para a fase Come Out.')
            print('Você agora tem {0} fichas.'.format(fichas))
    fim_resposta='***'
    return fim_resposta

#print(resposta_da_aposta(fichas,vitoria,tipo_de_aposta))