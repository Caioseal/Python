ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    média = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], média])
    resposta = str(input('Quer continuar? [S/N] '))
    if resposta in 'Nn':
        break
print('-='*30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for índice, aluno in enumerate(ficha): 
#Esse comando cria um índice e é possível separar cada elemento dentro da lista. A lista está criada com [Nome, Nota1 Nota2, Média]
#Ao selecionar aluno[0] ele irá mostrar o elemento 0 de todas as linhas, ou seja, o nome
    print(f'{índice:<4}{aluno[0]:<10}{aluno[2]:>8}')
while True:
    print('-' * 35)
    opção = int(input('Mostrar as notas de qual aluno? (999 para interromper) ' ))
    if opção == 999:
        print('FINALIZANDO...')
        break
    if opção <= len(ficha) - 1:
        print(f'As notas de {ficha[opção][0]} são {ficha[opção][1]}') #Opção é o número do aluno. 
#O primeiro aluno cadastrado é o zero e assim por diante. Quando digitar a opção, irá buscar na ordem de cadastro
#Zero é o primeiro elemento da lista, que é o nome. Um é o segundo elemento da lista, que são as notas
print('Volte sempre')