def inteiro(mensagem):
    valor = 0
    ok = False #O OK é necessário para terminar a função.
    while True:
        numero = str(input(mensagem)) #Leia como um string
        if numero.isnumeric(): #Valida se é numérico
            valor = int(numero) #Caso positivo, utiliza o número como um inteiro na variável valor
            ok = True
        else:
            print('Erro! Digite um número inteiro')
        if ok: #Se estiver ok, termina
            break
    return valor #Retorna o valor salvo na variável.

n = inteiro('Digite um número inteiro: ') #Ativando a função
print(f'Você acabou de digitar o número {n}')