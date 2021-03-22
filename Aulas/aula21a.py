#Interactive Help
#função: help()
#print(input.__doc__)
#help(print)

#DocStrings
def contador(i, f, p):
    """-> Faz uma contagem e mostra na tela.
    i = inicio da contagem
    f = final da contagem
    p = passo da contagem
    return = sem retorno"""
     c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM')

help(contador)