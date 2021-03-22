def contador(*num): #Asterisco é o simbolo de 'desempacotar'. Todos os valores estão dentro de núm.
    tamanho = len(num)
    print(f'Recebi os valores {num} e são ao todo {tamanho} números.')
contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2)