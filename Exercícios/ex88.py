from random import randint
from time import sleep
lista = [] #Lista menor com o gurpo de 6 números
jogos = [] #Lista maior que vai conter todos os jogos que o usuário quiser
print('-='*30)
print(f'{"JOGO DA MEGA-SENA":^60}')
print('-='*30)
quantidade = int(input('Quantos jogos você quer sortear: '))
total = 1 #Contador para a quantidade de jogos que o usuário quiser
while total <= quantidade:
    contador = 0 #Contador que irá sortear os números. 6x
    while True:
        número = randint(1,60) #Sorteou o número
        if número not in lista: #Se o número que o computador sorteou não estiver na lista, add na 'lista'
            lista.append(número) #Coloca o número sorteado dentro da 'lista'
            contador += 1 #Aumenta o contador para atingir os 6 números sorteados.
        if contador >= 6: #Quando atingir os 6 números sorteados, termina o programa.
            break
    lista.sort() #Organiza em ordem crescente
    jogos.append(lista[:]) #Faz uma cópia de todas as listas com os 6 números dentro de uma maior chamada 'jogos'.
    lista.clear() #Limpa a lista para não repetir
    total +=1 #Aumenta o contador para atingir o valor que o usuário solicitou
print(f'-=' * 3, "SORTEANDO {quantidade} JOGOS",'-=' * 3)
for índice, linha in enumerate (jogos): #Cria um índice com a ferramenta enumerate. Irá mostrar em cada linha , os jogos.
    print(f'Jogo {índice+1}: {linha}') #Enumera as linhas, e mostra cada lista em 'jogos'
    sleep(1)
print('-=' * 5, "< BOA SORTE >", '-=' * 5)