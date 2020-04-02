# CrapsGame
Projeto para a disciplina de Design de Software.

Nós, alunos do Insper, desenvolvemos um jogo de Craps em Python.

************************************************************************************************************************
Bem vindo ao Craps:

Este jogo consiste em apostas sucessivas para o número da soma de dois dados de seis lados dentro de dois tipos de fase:
- Come Out
- Point

Na fase Come Out existem 4 tipos de apostas possíveis de serem feitas:
- Field:
  Se a soma for 5, 6, 7 ou 8 perde a aposta.
  Se a soma for 3, 4, 9, 10 ou 11 ganha o valor da aposta.
  Se for 2 ganha o doubro e 12 o triplo do que apostou.
- Any Craps:
  Se a soma for 2, 3 ou 12 ganha 7 vezes o q apostou.
  Se não perde a aposta.
- Twelve:
  Se a soma der 12 ganha 35 vezes o que apostou.
  Se não perde a aposta.
- Pass Line Bet:
  Se a soma der 7 ou 11, recebe a aposta.
  Se for 2, 3 ou 12, perde a aposta.
  Se a soma der outro número, entrará na fase Point e sua aposta ainda vale.

Na fase Point ainda pode apostar em Field, Any Craaps e Twelve, porém:
- Nesta fase, a soma na aposta do Pass Line Bet se torna o Point
e até a soma da rodada ser igual ao Point ou a 7, permanece na fase Point:
- Se a soma da rodada for igual ao Point, receberá a aposta feita no Pass Line Bet
- Se for igual a 7 perde essa aposta.

Você começará o jogo com 1000 fichas.

Boa sorte nas apostas!

*************************************************************************************************************************
