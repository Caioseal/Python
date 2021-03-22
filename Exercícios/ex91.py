from random import randint
from time import sleep
from operator import itemgetter
print('-='*30)
print(f'{"JOGO DE DADOS":^60}')
print('-='*30)
ranking = []
jogo = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),    
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6)}
print('Valores sorteados:')
print()
for key, values in jogo.items():
    print(f'- {key} tirou {values} no dado')
    sleep(1)
print('=-='*20)
print('RANKING DOS JOGADORES')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for índice, valor in enumerate(ranking):
    print(f'{índice+1}º lugar: {valor[0]} com {valor[1]}')
    sleep(1)