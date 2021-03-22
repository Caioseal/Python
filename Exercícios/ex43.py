peso = float(input('Peso (Kg): '))
alt = float(input('Altura (m): '))
imc = peso / (alt ** 2)
print(f'O seu IMC é de {imc:.1f}!')
if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')