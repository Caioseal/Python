dicionário = {}
dicionário['Nome'] = str(input('Nome: '))
dicionário['Média'] = float(input(f'Média de {dicionário["Nome"]}: '))
print('-='*30)
if dicionário['Média'] >= 7:
    dicionário['Situação'] = 'Aprovado'
elif 5 <= dicionário['Média'] < 7:
    dicionário['Situação'] = 'Recuperação'
else:
    dicionário['Situação'] = 'Reprovado'
print('-=' * 30)
for key, value in dicionário.items():
    print(f'{key} é igual a {value}')