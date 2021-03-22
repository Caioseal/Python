dias = int(input('Digite a quantidade de diárias: '))
km = int(input('Digite a quilometragem rodada: '))
valordias = dias * 60 + (km * 0.15)
print(f'O total a pagar é de R${valordias:.2f}.')