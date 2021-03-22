n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma é {s}.')
# O acento circunflexo significa centralizar. Ex: {n:^20}. Vai centralizar a variável n em 20 caracteres.