#for c in range (0, 6) - Conta de 0 até 5, no 6 ele para.
#for c in range (6, 0, -1) - Conta subtraindo
# for c in range (0, 6, 2) - Conta de 2 em 2

#n = int(input('Digite um número: '))
#for c in range(0, n+1):
#    print(c)
#print('FIM')

#i = int(input('Início: '))
#f = int(input('Fim: '))
#p = int(input('Paso: '))
#for c in range (i, f+1, p):
#    print(c)
#print('FIM')

s = 0
for c in range (0, 5):
    n = int(input('Digite um valor: '))
    s += n
print(f'A somados números é: {s}')