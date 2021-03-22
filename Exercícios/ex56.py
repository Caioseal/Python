somaidade = 0
médiaidade = 0
maioridadeh = 0
nomevelho = ''
totalmulher20 = 0
for p in range (1 , 5):
    print(f'---- {p} PESSOA ----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadeh = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadeh:
        maioridadeh = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totalmulher20 += 1
médiaidade = somaidade/4
print(f'A média de idade do grupo é {médiaidade} anos.')
print(f'O homem mais velho se chama {nomevelho}.')
print(f'Ao todo são {totalmulher20} mulheres com menos de 20 anos.')