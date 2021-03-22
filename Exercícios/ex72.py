numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    usuario = int(input('Digite um número entre 0 e 20: '))
    if 0 <= usuario <= 20: # Se o número estiver entre 0 e 20
        break
    print('Tente novamente')
print(f'Você digitou o número {numeros[usuario]}')
        