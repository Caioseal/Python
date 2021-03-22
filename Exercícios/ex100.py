from random import randint

def sorteia(lista):
    print(f'Sorteando os números... ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')

def somapar(números):
    soma = 0
    for valor in números:
        if valor % 2 == 0:
            soma += valor
    print(f'\nA soma dos valores pares são: {soma}.')


números = []
sorteia(números)
somapar(números)