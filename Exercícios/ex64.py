soma = cont = n = 0
while n != 999:
    n = int(input('Digite um número: [999 para parar] '))
    if n != 999:
        soma += n
        cont += 1
print(f'A quantidade de números digitados foi {cont} e a soma foi: {soma}.')
print('Acabou')