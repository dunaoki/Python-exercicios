listagem = ('lapis', 1.75,
            'borracha', 2.00,
            'caderno', 3.50,
            'mochila', 15.00,
            'tesoura', 4.50,
            'compasso', 6.00)
print('='*40)
print(F'{"LISTAGEM DE PRECO":^40}')
print('='*40)
for pos in range (0, len(listagem)):
    if pos % 2 ==0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('='*40)
