pessoas = []
dados = []
maiorpeso = menorpeso = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    print('Dados cadastrados com sucesso.')
    print('-='*30)
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    print('-='*30)
    if len(pessoas) == 0:
        maiorpeso = menorpeso = dados[1]
    else:
        if dados[1] > maiorpeso:
            maiorpeso = dados[1]
        if dados[1] < menorpeso:
            menorpeso = dados[1]
    pessoas.append(dados[:]) #Cria uma cópia dos 'dados' dentro de 'pessoas'
    dados.clear()
    if resposta in 'Nn':
        break
    while resposta not in 'Ss' :
        print('Opção inválida. Tente novamente')
        resposta = str(input('Quer continuar? [S/N] '))
print(f'Você cadastrou: {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maiorpeso}Kg. Peso de: ', end='')
for pessoa in pessoas:
    if pessoa[1] == maiorpeso:
        print(f'[{pessoa[0]}]', end=' ')
print(f'\nO menor peso foi {menorpeso}Kg. Peso de: ',end='')
for pessoa in pessoas:
    if pessoa[1] == menorpeso:
        print(f'[{pessoa[0]}]', end=' ')