titulo = 'BANCO S.A'
print('=' * 30)
print(titulo.center(30))
print('=' * 30)
saque = int(input('Quanto deseja sacar: R$'))
cédula = 100
contadorcédula = 0
total = saque
while True:
    if total >= cédula:
        total -= cédula
        contadorcédula += 1
    else:
        if contadorcédula > 0:
            print(f'Total de {contadorcédula} notas de R${cédula}.')
        if cédula == 100:
            cédula = 50
        elif cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 5
        elif cédula == 5:
            cédula = 2
        contadorcédula = 0
        if total == 0:
            break
