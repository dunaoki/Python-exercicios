valores=[]
for cont in range(0,5):
    valores.append(int(input('digite o valor: ')))
    maior = max(valores)
    menor = min(valores)
print(f'Voce digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} na posicao ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}..', end='')
print()
print(f'O menor valor digitado foi {menor} na posicao ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...',end='')


