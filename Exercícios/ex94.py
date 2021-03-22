galera = []
pessoa = {}
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Digite apenas M ou F.')
    galera.append(pessoa.copy())
    while True:
        resposta = str(input('Quer continuar? [S/N]? ')).upper()[0]
        if resposta in 'SN':
            break
        print('Erro! Digite apenas S ou N.')
    if resposta == 'N':
        break
print('-=' * 30)
print (f'A) Foram cadastradas {len(galera)} pessoas.')
média = soma / len(galera)
print(f'B) A média de idade é {média:.1f} anos.')
print(f'C) As mulheres cadastradas foram:',end=' ')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end=' ')
print()
print(f'D) Lista das pessoas acima da média: ')
for p in galera: #Analisa cada linha dentro da lista 'galera'
    if p['idade'] >= média:
        for key, value, in p.items(): #Analisa cada item dentro da linha e retorna os valores
            print(f'{key} = {value};', end=' ')
        print()