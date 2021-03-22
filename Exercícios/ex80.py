lista = []
for contador in range (0,5):
    número = int(input('Digite um valor: '))
    if contador == 0 or número > lista [-1]: #Se for o número digitado foi o primeiro ou maior que o último da lista, add.
        lista.append(número)
        print('Adicionado do final da lista')
    else:
        posição = 0
        while posição < len(lista): #Esse comando faz uma varredura na lista
            if número <= lista[posição]: #Número digitado maior que a o contador que está varrendo a lista
                lista.insert(posição, número) # Inserir quando o número for menor do que o próximo
                print(f'Adicionado na posição {posição} da lista')
                break
            posição += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')