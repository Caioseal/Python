resp = 'S'
média = soma = cont = maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um número: '))
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    soma += n
    cont += 1
    média = soma / cont
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print(f'Você digitou {cont} números e a média é: {média:.2f}.\nO maior valor foi {maior} e o menor {menor}.\nACABOU')