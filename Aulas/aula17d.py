a = [2, 3, 4, 7]
b = a[:]#Com esse comando, cria-se uma cópia de A dentro de B. Não há uma ligação
b[2] = 8 #Python cria ligação, as duas listas serão alteradas.
print(f'A lista A: {a}')
print(f'A lista B: {b}')