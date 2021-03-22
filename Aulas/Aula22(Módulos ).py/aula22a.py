import uteis
#from uteis import fatorial, dobro, triplo

num = int(input('Digite um valor: '))
fat = uteis.fatorial(num)
dob = uteis.dobro(num)
trip = uteis.triplo(num)
print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {dob}.')
print(f'O triplo de {num} é {trip}.')

#Vantagens da modularização:
# - Organização do código
# - Facilidade na manutenção
# - Ocultação de código detalhado
# - Reutilizar em outros projetos

# Os pacotes são conjuntos de módulos, que por sua vez, são conjuntos de funções