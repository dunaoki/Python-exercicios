from random import randint
computador = randint(0, 10)
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('qual o seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('mais para cima ...')
        elif jogador > computador:
            print('mais para baixo')
print(f'Parabens vc acertou em {palpite} tentativas  ')