def área(a, b):
    area = a * b
    print(f'A área de um terreno é {a} x {b} é de {area}m²')

print('Controle de Terrenos')
print('-' * 20)
a = float(input('LARGURA (m): '))
b = float(input('COMPRIMENTO (m): '))
área(a, b)