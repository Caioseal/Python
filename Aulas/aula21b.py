#Parâmetros operacionais
#Precisa colocar a variável igual a 0 pra que ela seja opcional.
def soma(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}.')

soma(10,5)