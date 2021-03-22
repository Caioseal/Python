def fatorial (n, show=False):
    """
    Calcula o fatorial de um número
    n = número a ser calculado
    show = (opcinal) mostrar o cálculo 
    return = retorna o fatorial de n
    """
    f = 1
    for c in range (n, 0, -1):
        if show:
            if c > 1:
                print(f'{c} x ', end='')
            else:
                print(f'{c} = ', end='')
        f *= c
    return f

print(fatorial (10, show=True))
