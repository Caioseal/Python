'''n1 = float(input('Comprimento do cateto oposto: '))
n2 = float(input('Comprimento do cateto adjacente: '))
n3 = (n1 ** 2 + n2 ** 2) ** (1/2)
print(f'A hipotenusa vai medir {n3:.2f}')'''

import math
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
hi = math.hypot(co, ca)
print(f'A hipotenusa é: {hi:.2f}')