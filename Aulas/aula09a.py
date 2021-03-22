frase = 'Curso em Vídeo Python'
print(frase[9])
#Mostra o 9 carácter, que é V
print(frase[9:14])
#Motra do 9 carácter até o 13
print(frase[9:21:2])
#Mostra do 9 até o último carácter(20 no caso), pulando de 2 em 2
print(frase[:5])
#Mostra do primeiro carácter até o 5
print(frase[15:])
#Mostra do 15 até o último
print(frase[9::3])
#Mostra do 9 até o último, pulando de 3 em 3
print(len(frase))
#Mostra a quantidade de carácter da 'frase
print(frase.count('o'))
#Conta a quantidade de 'o'
print(frase.count('o',0,13))
#Mostra a quantidade de 'o' entre o 1 carácter e o 12
print(frase.find('deo'))
#Mostra em qual carácter começa o texto 'deo'
print(frase.find('Android'))
#Retorna o valor -1 pois não consta na frase.
print('Curso' in frase)
#Retorna True ou False para saber se existe a palavra Curso na frase
frase.replace('Python', 'Android')
#Substitui Python por Android. Precisa salvar em uma nova variável
frase.upper()
#TUDO MAIÚSCULO
frase.lower()
#tudo minúsculo
frase.capitalize()
#Primeiro carácter maiúsculo e demais minúsculos
frase.title()
#A primeira letra de cada palavra com maiúsculo
frase.strip()
#Remove espaços do início e final
frase.rstrip()
#Remove espaços do final. R = right
frase.lstrip()
#Remove espaços do início. L = left
frase.split()
#Onde tiver espaço, vai dividir
'-'.join(frase)
#Insere um '-' entre as palavras que estão divididas.
print(len(frase.strip()))
#Calcula o comprimento, tirando espaços do começo e final.