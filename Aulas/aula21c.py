#Escopo de variáveis

def teste(): # X vai funcionar somente a função, e não no programa principal.
    x = 8
    print(f'Na função teste, n vale {n}.')
    print(f'Na função teste, x vale {x}')


#Programa Principal
n = 2
print(f'No programa principal, n vale {n}.')
teste()