lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    print('Valor adicionado com sucesso')
    resposta = str(input('Quer continuar: [S/N] ')).strip()
    if resposta in 'Nn':
        break
print('-=' * 30)
print(f'Foram digitados {len(lista)} números.')
lista.sort(reverse=True) #reverse em letra minúscula
print(f'Os números em ordem decrescente são: {lista}.')
if 5 in lista:
    print('O valor 5 faz parte da lista.')

else:
    print('O valor 5 não faz parte da lista.')