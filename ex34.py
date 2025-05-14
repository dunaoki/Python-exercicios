s = float(input('qual o seu salario:'))
if s > 1250:
    print(f'seu novo salario sera de {(s * 0.1) + s }')
if s < 1250:
    print(f' seu novo salario sera de {(s * 0.15) + s}')
