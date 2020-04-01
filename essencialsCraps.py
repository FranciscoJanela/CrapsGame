import random

def soma_dos_dados():
    dado1=random.randint(1,6)
    dado2=random.randint(1,6)
    soma=dado1+dado2
    return soma

def resposta_da_aposta(fichas,vitoria):
    if vitoria:
        print('parabéns! Sua aposta rendeu!\n você agora tem {0} fichas.'.format(fichas))
    else:
        print('Que pena... Você perdeu a aposta.\n você agora tem {0} fichas.'.format(fichas))
    return vitoria

    