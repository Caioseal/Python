from random import randint
computador = randint(0, 10)
print('Sou seu computador. Acabei de pensar em um número entre 0 e 10.')
print('Consegue advinhar qual foi? ')
acertou = False
tentativas = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite: '))
    tentativas += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...tente de novo.')
        elif jogador > computador:
            print('Menos...tente de novo.')
print(f'Acertou com {tentativas} tentativas')