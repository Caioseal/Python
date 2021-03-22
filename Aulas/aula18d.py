galera = []
dados = []
totalmaior = totalmenor = 0
for contador in range (0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])#Dois pontos serve para gerar uma cópia
    dados.clear() #Limpa a lista 'dados'

for pessoa in galera:
    if pessoa[1] >= 18: #O nome da variável não importa. O que importa é que vai pegar o segundo dado da lista, ou seja, idade
        print(f'{pessoa[0]} é maior de idade.')
        totalmaior += 1
    else:
        print(f'{pessoa[0]} é menor de idade.')
        totalmenor += 1
print(f'Há {totalmaior} pessoas maiores de idade e {totalmenor} menores de idade.')