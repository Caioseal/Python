from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for pessoas in range (1, 8):
    nasc = int(input('Em que ano a pessoa nasceu? '))
    idade = atual - nasc
    print(f'A pessoa tem {idade} anos.')
    if idade >=18:
        print('Essa pessoa é maior de idade')
        totalmaior += 1
    else:
        print('Essa pessoa é menor')
        totalmenor += 1
print(f'Ao todo tivemos {totalmaior} pessoas maiores de idade e\n {totalmenor} pessoas menores de idade.')