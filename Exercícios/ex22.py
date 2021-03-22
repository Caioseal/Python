nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print(f'Seu nome com letras maiúsculas é {nome.upper()}.')
print(f'Seu nome com letras minúsculas é {nome.lower()}.')
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
#[0] especifica que é só a primeira palavra