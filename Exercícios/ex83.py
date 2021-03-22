expressão = str(input('Digite a expressão: '))
lista = []
for símbolo in expressão: #Para cada símbolo na expressão, executar comando abaixo
    if símbolo == "(": #Se na variável símbolo houver um sinal de '('. Aqui você escolhe o que fazer com cada caracter da lista
        lista.append('(') #Adiciona na lista
    elif símbolo == ")": #Se na variável símbolo tem um sinal de ')'
        if len(lista) > 0: #Se a lista for maior que 0, ou seja, se houver mais de um '('
            lista.pop() #Elimina o último '(' da lista
        else:
            lista.append(')') #Se houver mais ')' do que '(', a expressão está errada
            break
if len(lista) == 0: #Se a lista estiver zerada, significa que a quantidade de ( que abriu, também fechou
    print('Sua expressão é válida.')
else:
    print('Sua expressão está errada.')
