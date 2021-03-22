a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
#Verificando qual é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Verificando qual é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > a:
    maior = c
print(f'O menor valor é {menor}')
print(f'O maior valor é {maior}')