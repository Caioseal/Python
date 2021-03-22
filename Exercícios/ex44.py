preço = float(input('Preço da compra: '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Escolha a opção: '))
if opção == 1:
    total = preço - (preço * 0.10)
elif opção == 2:
    total = preço - (preço * 0.05)
elif opção == 3:
    total = preço
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} ')
elif opção == 4:
    total = preço + (preço * 0.20)
    totalparc = int(input('Quantas parcelas: '))
    parcela = total / totalparc
    print(f'Sua compra será parcelada em {totalparc}x de R${parcela:.2f} COM JUROS.')
else:
    total = preço
    print('Opção Inválida. Tente novamente')
print(f'Sua compra de R${preço:.2f} vai custar R${total:.2f} no final.')