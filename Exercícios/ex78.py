lista = []
maior = menor = 0
for posição in (range(0,5)): #Posição é o contador, que vai até o número definido no intervalo
    lista.append(int(input(f'Digite um valor para a posição {posição}: '))) #Comando para adicionar valores digitados pelo usuário em uma lista
    if posição == 0: #Quando for o primeiro número digitado, o maior e o menor são iguais
        maior = menor = lista[posição]
    else: #Quando não for o primeiro número digitado
        if lista[posição] > maior:
            maior = lista[posição]
        if lista[posição] < menor:
            menor = lista[posição]
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi o {maior} nas posições ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...',end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ',end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...',end='')
print()