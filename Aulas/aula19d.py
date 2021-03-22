estado = dict() #Cria um dicionário
brasil = list() #Cria uma lista
for c in range (0,3): #Cria um contador para perguntar 3x
    estado['uf'] = str(input('Estado: ')) #Cria uma variável 'uf' dentro do dicionário 'estado' e pede p usuário
    estado['sigla'] = str(input('Sigla: ')) #Cria uma variável 'sigla'dentro do dicionário 'estado' e pede p usuário
    brasil.append(estado.copy()) #Insere o dicionário dentro da lista.
#print(brasil)
print()
for estado in brasil:#Mostra todos os itens de todas as linhas
    print(estado)
print()
for estado in brasil: #Separa por linha
    for key, value in estado.items(): #Separa por elemento.
        print(f'O campo {key} tem valor {value}.') #Irá mostrar o estado e seu valor, depois a sigla e valor, de todas as linhas
print()
for estado in brasil:
    for value in estado.values(): 
        print(value, end=' ') #Mostra somente o resultado, sem a categorização
    print()
