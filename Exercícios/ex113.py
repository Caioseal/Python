def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'Por favor, digite um número inteiro válido.')
            continue #Joga pro while de novo.
        except (KeyboardInterrupt):
            return 0
        else: #Se tudo der certo
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(f'Por favor, digite um número válido.')
            continue
        except (KeyboardInterrupt):
            return 0
        else:
            return n

n1 = leiaInt('Digite um valor: ')
n2 = leiaFloat('Digite um valor:')
print(f'O valor digitado foi {n1} e {n2}.')