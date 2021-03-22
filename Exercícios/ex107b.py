def aumentar(n=0, formato=False):  
    n += (n * 0.10)
    return n if format is False else moeda(n)

def diminuir(n=0, formato=False):
    n -= (n * 0.13)
    return n if format is False else moeda(n)

def dobro(n=0, formato=False):
    n *= 2
    return n if formato is False else moeda(n)

def metade(n= 0, formato=False):
    n *= 0.5
    return n if formato is False else moeda(n)

def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')

def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'ERRO! {entrada} é um preço inválido.')
        else:
            válido = True
            return float(entrada)