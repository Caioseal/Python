lista = []
pares = []
ímpares = []
while True: #Enquanto for verdade, faça o comando abaixo
    lista.append(int(input('Digite um número: '))) #Peça um número para o usuário e insira na 'lista'
    print('Número adicionado com sucesso.')
    resposta = str(input('Quer continuar? [S/N] ')) #Pergunte se o usuário quer continuar
    if resposta in 'Nn': #Se a resposta for não, vai quebrar o laço While
        break
    if 'Ss' not in resposta: #Se a resposta NÃO for 'S ou s' informe que a opção é inválida
        print('Opção Inválida. Tente novamente.')
for índice, valor in enumerate(lista): #Faz uma varredura na lista e aplica a função abaixo.
    if valor % 2 == 0: #Descobre se o número é par
        pares.append(valor)  #Insere na lista
    else:
        ímpares.append(valor) #Se não for par, insere na lista ímpar.
print('-=' * 30)
print(f'Os números adicionados foram: {lista}')
print(f'Os números pares são {pares}')
print(f'Os números ímpares são {ímpares}')