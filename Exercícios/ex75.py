lista = (int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')))
print(f'Você digitou os valores {lista}')
if 9 in lista:
    print(f'Você digitou o número 9: {lista.count(9)} vezes')
else:
    print('O valor 9 não foi digitado')
if 3 in lista:
    print(f'O valor 3 apareceu na {lista.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado')
print('Os valores pares são:',end=' ')
for n in lista: # Para cada número na variável lista, veja se o número é divisiel por 2 e mostre.
    if n % 2 == 0:
        print(n, end=' ')