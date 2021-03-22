números = list()
while True:
    n = int(input("Digite um valor: "))
    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('Número duplicado')
    r = str(input('Quer contiuar? [S/N] '))
    if r in 'Nn':
        break
    if r not in 'Ss':
        print('Opção inválida')
números.sort()
print(f'Você adicionou os números: {números}')