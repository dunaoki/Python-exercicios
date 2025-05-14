from random import randint
while True:
    jogador = int(input('jogue um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('par ou impar: ')).upper().strip()[0]
    print(f'voce jogou {jogador} e o computador jogou {computador} e o total deu {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print(' você venceu!!')
        else:
            print('voce perdeu')
            break
    if tipo == 'I':
        if total % 2 == 1:
            print('você venceu!!')
        else:
            print('você perdeu!!')
            break
    print('vamos jogar novamente....')
print('GAMER OVER')