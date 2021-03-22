tot18 = h = m20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        h += 1
    if sexo == 'F' and idade <20:
        m20 += 1
    decisão = ' '
    while decisão not in 'SN':
        decisão = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if decisão == 'N':
        break
print(f'Foram cadastradas {tot18} pessoas com menos de 18 anos.\n {h} homens e {m20} mulheres com menos de 20 anos.')
