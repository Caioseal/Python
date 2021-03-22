import ex107b

preço = float(input('Digite o preço: R$'))
print(f'A metade de R${ex107b.moeda(preço)} é {ex107b.metade(preço, True):}.')
print(f'O dobro de R${ex107b.moeda(preço)} é {ex107b.dobro(preço, True)}.')
print(f'Aumentando em 10%, temos {ex107b.aumentar(preço, True):}.')
print(f'Reduzindo em 13%, temos {ex107b.diminuir(preço, True)}.')