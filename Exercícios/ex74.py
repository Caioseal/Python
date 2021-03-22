from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print ('Os valores sorteados foram: ',end='')
for n in numeros: #Leia: Para cada número na variável 'números' mostrará o pint da linha de baixo
    print(f'{n}',end=' ')
print(f'\nO maior valor foi {max(numeros)}') #O comando 'max' e 'min' vale para tuplas e outros formatos
print(f'O menor valor foi {min(numeros)}')