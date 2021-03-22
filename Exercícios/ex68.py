from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint (0, 10)
    total = jogador + computador
    parimpar = ' '
    while parimpar not in 'PpIi':
        parimpar = str(input('Par ou Ímpar [P/I]:')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total deu: {total}.', end=' ')
    print(f'DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if parimpar == 'P':
        if total % 2 == 0:
            print('Você ganhou!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif parimpar == 'I':
        if total % 2 != 0:
            print('Você ganhou!')
            v += 1
        else:
            print('Você perdeu')
            break
    print('Vamos jogar novamente.')
    print('-=-' * 10)
print(f'Você ganhou {v} vezes.')