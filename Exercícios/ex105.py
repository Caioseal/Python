def notas(*n, situação=False): # Asterisco serve para receber várias entradas
    dic = {}
    dic['total'] = len(n)
    dic['maximo'] = max(n)
    dic['mínimo'] = min(n)
    dic['média'] = sum(n) / len(n)
    if situação:
        if dic['média'] >= 7:
            dic['situação'] = 'BOA'
        elif dic['média'] >=5:
            dic['situação'] = 'RAZOÁVEL'
        else:
            dic['situação'] = "RUIM"
    return dic

respostas = notas(2.5, 5, 6.5, situação=True)
print(respostas)