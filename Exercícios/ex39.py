from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}.')
if idade == 18:
    print('Você tem que se alistar nesse ano!')
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print(f'Você ainda não tem 18 anos. Ainda faltam {saldo} anos para o alistamento.')
    print(f'Você deveria ter se alistado em {ano}')
else:
    saldo = idade - 18
    ano = atual - saldo
    print(f'Você deveria ter se alistado há {saldo} anos.')
    print(f'Você deverá se alistar em {ano}')