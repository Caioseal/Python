teste = []
teste.append('Gustavo')
teste.append(40)
galera = []
galera.append(teste[:]) #Cópia
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)