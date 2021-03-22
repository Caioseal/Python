time = [] #Cada jogador ficará cadastrado em uma lista
jogador = {} #O nome, total de gols e gols de cada partida ficarão em um dicionário
partidas = [] #Os gols de cada partida ficarão em uma lista

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: ')) #Cria uma varíavel nome dentro do dicionário 'jogador e recebe o input
    total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for contador in range (0, total): #Faz um contador de acordo com o número que o usuário digitar
        partidas.append(int(input(f'Quantos gols na {contador+1}ª partida? '))) #Insere as informações dentro da lista.
    jogador['gols'] = partidas[:] #Cria uma cópia da lista 'partidas' dentro do dicionário 'jogador'
    jogador['total'] = sum(partidas) 
    time.append(jogador.copy()) #Comando para copiar o dicionário 'jogador' dentro da lista 'time'.
    while True:
        resposta = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! Responda apenas "S" ou "N".') #Essa linha será executada como um ELSE.
    if resposta == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for indice in jogador.keys(): #Para cada índice no dicionário 'jogador':
    print(f'{indice:<15}', end='') #Irá mostrar as os indices em 15 caracteres, alinhado a esquerda.
print() #Terminar de mostrar os itens na mesma linha
print("-" * 40)
for key, valor in enumerate(time): #Para cada chave e valor dentro da lista time
    print(f'{key:>4} ', end='')
    for dado in valor.values(): #Para cada dado em valor.values
        print(f'{str(dado):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time): #Se o número digitado for maior que o tamanho da lista.
        print(f'ERRO! Não há jogador com o código {busca}.')
    else:
        print(f' -- DADOS DO JOGADOR {time[busca]["nome"]}: ') #Buscar o nome do jogador na lista, de acordo com o número que o usuário digitou
        for indice, gols in enumerate(time[busca]['gols']): #Função enumerate faz um contado primeiro e irá mostrar os dados da lista gols
            print(f'     No jogo {indice+1} fez {gols} gols.')
    print('-' * 40)
print('Encerrando...')