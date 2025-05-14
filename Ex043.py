peso=float(input('qual o seu peso:'))
altura = float(input('qual sua altura:'))
imc = peso / (altura ** 2)
print(f'seu imc é {imc:.1f}')
if imc <18.5:
    print('abaixo do peso ')
elif 18.5 <= imc < 25:
    print('peso ideal')
elif 25 <= imc < 30:
    print('sobrepeso')
elif 30<= imc < 40:
    print('obesidade')
elif imc > 40:
    print('obesidade morbida')