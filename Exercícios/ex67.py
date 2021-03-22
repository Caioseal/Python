while True:
    n = int(input('Digite um número para ver sua tabuada: ')) 
    for c in range (1,11):
        print(f' {n} x {c:2} = {n*c}')
        c += 1
    if n < 0:
        break
print("PROGRAMA DE TABUADA ENCERRADO")