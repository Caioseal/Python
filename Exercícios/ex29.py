velocidade = float(input('Digite a velocidade do carro: '))
if velocidade <= 80:
    print('Você está dentro do limite de velocidade')
else:
    multa = velocidade - 80
    valor = multa * 7
    print(f'Você ultrapassou {multa}km/h do limite, e terá que pagar R${valor:.2f} de multa')