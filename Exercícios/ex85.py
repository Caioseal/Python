número = [[], []]
valor = 0
for contador in range (1, 8):
    valor = int(input(f'Digite o {contador}º valor: '))
    if valor % 2 == 0:
        número[0].append(valor)
    else:
        número[1].append(valor)
print('-=' * 30)
número[0].sort() #Ordem crescente na primeira lista
número[1].sort() #Ordem crescente na segunda lista
print(f'Todos os valores pares digitados foram {número[0]}')
print(f'Todos os valores ímpares digitados foram {número[1]}')