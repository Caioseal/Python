casa = float(input('Qual o valor da casa que você quer financiar? '))
salário = float(input('Qual o seu salário? '))
tempo = int(input('Em quantos anos você quer pagar? '))

prestação = casa / (tempo * 12)
máximo = salário * 0.30
print(f'Para pagar uma casa de R${casa:.2f} em {tempo} anos, a prestação será de R${prestação:.2f}')
if prestação > máximo:
    print('Desculpa, mas você não atende os requisitos para conseguir o empréstimo!')
else:
    print(f'E o seu empréstimo foi aprovado!')