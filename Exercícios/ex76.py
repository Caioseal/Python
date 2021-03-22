lista = ('Lápis', 1.75,
        'Borracha', 2,
        'Caderno', 15.90,
        'Estojo', 25,
        'Transferidor', 4.20,
        'Compasso', 9.99,
        'Mochila', 120.32,
        'Canetas', 22.30,
        'Livro', 34.90 )
print('=' * 39)
print(f'{"LISTA DE PREÇOS":^39}') #Nesse caso precisa ser aspas duplas no meio, para não confundir. Formatado centralizado
print('=' * 39)
for posição in range(0, len(lista)): #Para cada linha da lista faça o comando abaixo. '0, len(lista)') - Significa que vai começar no zero e vai até o final da lista
    if posição % 2 == 0: # Cada posição pode ser par ou ímpar, para as posições pares, mostrar a formatação abaixo
        print(f'{lista[posição]:.<30}', end='')
    else: # Para cada linha ímpar, mostrar a formatação abaixo
        print(f'R${lista[posição]:>7.2f}')
print('-' * 39)