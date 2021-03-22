lista = [0, 0 , 0], [0, 0, 0], [0, 0, 0] #Define 3 listas com 3 números cada
somapar = maior = somacoluna = 0
for linha in range (0, 3):
    #A intenção de criar 'linha e 'coluna' é para alterar entre as listas. Depois de preencher a primeira lista, muda para a próxima.
    for coluna in range (0, 3):
        lista[linha][coluna] = int(input(f'Digite um número para a posiçao [{linha}], [{coluna}]: '))
for linha in range(0, 3):
    for coluna in range (0, 3):
        print(f'[{lista[linha][coluna]:^5}]',end='') #O MAIS IMPORTANTE É a configuração lista[linha][coluna]
        if lista[linha][coluna] % 2 == 0:
            somapar += lista[linha][coluna]
    print()
print('-='*30)
print(f'A soma de todos os valores PARES digitados são: {somapar}')
for linha in range (0, 3):
    somacoluna += lista[linha][2] #Linha fixa, coluna variável
print(f'A soma dos valores da terceira coluna é {somacoluna}')
for coluna in range(0, 3):
    if coluna == 0:
        maior = lista[1][coluna]
    elif lista[1][coluna] > maior:
        maior = lista[1][coluna]
print(f'O maior número da segunda linha é {maior}')