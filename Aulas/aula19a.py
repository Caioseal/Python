#DICIONÁRIOS
#Tuplas = ()
#Listas = [] ou dados = list()
#Dicionários {} ou dados = dict()
#dados = {'nome':'Pedro','idade':25}
#print(dados['nome']): Pedro
#print(dados['idade]): 25
#dados['sexo'] = 'M'
#del dados['idade'] - Elimina o elemento idade

#filme = {'título': 'Star Wars', 
#'ano': 1977,
#'diretor':'George Lucas'}
#print(filme.values()) - Mostra todos os valores: Star Wars, 1977, George Lucas
#print(filme.keys()) - Mostra as chaves: Título, Ano, Diretor
#print(filme.items()) - Mostra tudo
#for key, value in filme.items(): #Leia para cada chave e valor no filme.items, vai fazer um print.
#   print(f'O {key} é {value}') #- O título é Star Wars. O ano é 1977. O diretor é George Lucas
#LOCADORA:
#Zero = Título: Star Wars, Ano: 1977, Diretor: George Lucas
#Um = Título: Avengers, Ano: 2012, Diretor: Joss Whedon
#Dois = Título: Matrix, Ano: 1999, Diretor: Wachowski
#print(locadora[0]['ano']) - Vai mostrar o ano do item 0, que é o filme Star Wars
#print(locadora[2][título]) - Matrix