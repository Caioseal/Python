def voto(ano):
    from datetime import date #Importar o módulo somente dentro da função.Economiza memória
    atual = date.today().year #Recebe o ano atual
    idade = atual - ano #Calcula a idade
    if idade < 16:
        return f'Com {idade} anos: NÃO É PERMITIDO VOTAR' #Essa função pode retornar string, True, False ou valores.
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO"

nascimento = int(input('Em que ano você nasceu? '))
print(voto(nascimento)) #Ativando a função.