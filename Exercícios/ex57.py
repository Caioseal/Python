genero = str(input('Informe o seu sexo [M/F]: ')).strip().upper()[0]
while genero not in 'MmFf':
    genero = str(input('Dados inválidos. Escolha uma opção válida: ')).strip().upper()[0]
print(f'Sexo {genero} registrado com sucesso.')