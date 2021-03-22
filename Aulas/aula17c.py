valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores: #Cria um laço onde irá mostrar todos os itens da lista, de acordo com formatação que mandar.
    print(f'{v}...',)

for c, v in enumerate(valores): #Cria duas variáveis, a primeira com a posição e a segunda com os valores
    print(f'Na posição {c} encontrei o valor {v}!')

lista = []
for contagem in range(0,5): #Contagem é a variável que irá contar. Os números solicitados serão guardados na lista
    lista.append(int(input('Digite um valor: ')))