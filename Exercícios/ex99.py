def maior(*número):
    contagem = maior = 0
    print(f'Analisando os valores...')
    for valor in número:
        print(f'{valor} ', end='')
        if contagem == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        contagem += 1
    print(f'\nForam informados {contagem} valores ao todo.')
    print(f'O maior número é {maior}')
maior(1,2,3,4,5,6,7,8,9)
maior(7892, 4, 7, 243, 6, 75)
maior()
maior(6)