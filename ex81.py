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
numeros.sort(reverse=True)
print(f'vc digitou {len(numeros)} elementos')
print(f'Voce digitou na ordem decrescente os valores {numeros}')
if 5 in numeros:
    print('o valor 5 foi encontrado na lista ')
else:
    print('o valor 5 nao foi encontrado na lista')

print('Fim')