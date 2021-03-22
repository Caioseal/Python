salário = float(input('Digite o salário do funcionário: R$ '))
if salário >= 1250.00:
    aumento = (salário * 0.10) + salário
else:
    aumento = (salário * 0.15) + salário
print(f'Quem ganhava R${salário:.2f} passa a ganhar R${aumento:.2f} agora')