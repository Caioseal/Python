def dobra(lista):
    posição = 0
    while posição < len(lista):
        lista[posição]*=2
        posição += 1
valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)

def soma(* valores):
    s = 0
    for número in valores:
        s += número
    print(f'Somando os valores {valores} temos {s}.')

soma(5, 2)
soma(2, 9, 4)