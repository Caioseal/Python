jogador = {}
partidas = [] #Os gols de cada partida ficarão em uma lista, dentro do dicionário
jogador['nome'] = str(input('Nome do jogador: '))
total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for contador in range (0, total):
    partidas.append(int(input(f'Quantos gols na {contador+1}ª partida? '))) #Insere as informações dentro da lista.
jogador['gols'] = partidas[:] #Cria uma cópia da lista 'partidas' dentro do dicionário
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for key, value in jogador.items(): #Para cada chave e valor no dicionário, mostra o print abaixo.
    print(f'O campo {key} tem o valor {value}.')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for índice, value in enumerate(jogador['gols']):
    print(f'Na {índice+1}ª partida fez {value} gols.')
print(f'Total de {jogador["total"]} gols.')