n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
média = (n1 + n2) / 2
print(f'Tirando {n1:.1f} e {n2:.1f}, a média do aluno é {média:.1f}')
if média < 5.0:
    print('REPROVADO')
elif média >= 5.0 and média <= 6.9:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')