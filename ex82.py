numeros = list()
pares = list()
impares = list()
while True:
    n = int(input('digite um numero: '))
    if n not in numeros:
        numeros.append(n)
    else:
        print('Valor duplicado, tente outro numero...')
    r = str(input('quer continuar[S/N]: '))
    if r in 'Nn':
        break


for i, v in enumerate(numeros):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'a lista de numeros pares e {pares}')
print(f'a lista de numeros impares e {impares}')
print(f'vc digitou {len(numeros)} elementos')
print(f'Voce digitou na ordem decrescente os valores {numeros}')