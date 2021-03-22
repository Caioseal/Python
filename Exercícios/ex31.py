distância = int(input('Digite a distância da viagem em km: '))
if distância <= 200:
    preço = distância * 0.5
else:
    preço = distância * 0.45
print(f'O preço da viagem é R${preço:.2f}')