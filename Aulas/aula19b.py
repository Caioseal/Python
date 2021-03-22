pessoas = {'nome': 'Caio', 'sexo': 'M', 'idade': 27}
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
#print(pessoas.items())
del pessoas['sexo']
pessoas['nome'] = 'Pedro'
pessoas['peso'] = 69
for key in pessoas.keys():
    print(key)
print()
for values in pessoas.values():
    print(values)
print()
for key, value in pessoas.items(): #No dicionário, o items substitui o enumerate
    print(f'{key} = {value}')