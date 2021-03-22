frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.' .format(frase.count('A')))
print('A letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A letra A aparece na última vez na posição {}' .format(frase. rfind('A')+1))
# +1 para que o programa comece a contar a partir do 1, ao invés do 0