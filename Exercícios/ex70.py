total = caro = menor = cont = barato =  0
while True:
    produto = str(input('Produto: '))
    preço = float(input('Preço: '))
    total += preço
    cont += 1
    if preço > 1000:
        caro += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'O total das compras foi R${total}. ')
print(f'Há {caro} produto(s) custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
