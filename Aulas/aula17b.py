num = [2, 5, 9, 1]
num[2] = 3 #altera a posição 2 pelo número 3
num.append(7) # adiciona o número 7 na lista
num.sort() # ordem crescente
num.sort(reverse=True) #Ordem Decrescente
num.insert(2, 0) #Na posição 2 insira '0'
num.pop() #Deleta o último
num.remove(2) #Deleta o primeiro elemento encontrado com o valor '2'. Não elimina todos.
print(num)
print(f'Essa lista tem {len(num)} elementos.') #Mostra a quantidade de itens na lista