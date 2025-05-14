numeros = list()
while True:
    n = int(input('digite um numero: '))
    if n not in numeros:
        numeros.append(n)
    else:
        print('Valor duplicado, tente outro numero...')
    r = str(input('quer continuar[S/N]: '))
    if r in 'Nn':
        break
numeros.sort()
print(f'Voce digitou os valores {numeros}')
print('Fim')