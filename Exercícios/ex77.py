lista = ('aprender', 'programar', 'linguaguem', 'python', 'curso', 'grátis', 'estudar', 'praticar', 'trabalhar',
        'mercado', 'programador', 'futuro')
for palavra in lista: #Para cada 'palavra' na lista, mostra o print abaixo
    print(f'\nNa palavra {palavra.upper():^11} temos as vogais:', end=' ')
    for letra in palavra: #Para cada letra na variável palavra, mostra o print abaixo procurando vogal.
        if letra.lower() in 'aãáàeéèiíìou': #Comando para buscar as vogais dentro de cada linha da lista
            print(letra, end=' ')