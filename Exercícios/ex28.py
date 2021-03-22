from random import randint
from time import sleep
lista = randint(0,5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
n1 = int(input('Digite um número: '))
print('PROCESSANDO...')
sleep(2)
if n1 == lista:
    print('Parabéns! Você escolheu o mesmo número que o computador.')
else:
    print('Você não escolheu o mesmo número que o computador.')