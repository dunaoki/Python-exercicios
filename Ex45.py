# from random import randint
# itens = ('pedra', 'papel', 'tesoura')
# comp = randint(0,2)
#
# print('''escolha sua jogada :
# [0]Pedra
# [1]Papel
# [2]Tesoura''')
# jogada = int(input('qual sua jogada :'))
# print('=-'*11)
# print(f'o computador escolheu {itens[comp]}')
# print(f'o jogador escolheu {itens[jogada]}')
# print('=-'*11)
#
# if comp == 0: # computador jogar pedra
#     if jogada == 0:
#         print('empate')
#     elif jogada == 1:
#         print(' jogador ganha')
#     elif jogada == 2:
#         print('computador ganha')
# if comp == 1: # computador jogar papel
#     if jogada == 0:
#         print('computador ganha')
#     elif jogada == 1:
#         print('empate')
#     elif jogada == 2:
#         print('jogador ganha')
# if comp == 2: # computador jogar tesoura
#     if jogada ==0:
#         print('jogador ganha')
#     elif jogada == 1:
#         print('computador ganha')
#     elif jogada == 2:
#         print('empate')


from random import randint

itens=("pedra","papel",'tesoura')
comp=randint(0,2)
print('''
[1] pedra
[2] papel
[3] tesoura 
''')
jogador =int(input('Escolha um numero para jogar?'))
print(f'o computador escolheu {itens[comp]}')
print(f'o jogador escolheu {itens[jogador]}')

if comp == 0: #comp jogo pedra
    if jogador == 0:
        print('empatou')
    elif jogador == 1:
        print('o jogador ganhou ')
    elif jogador == 2:
        print('o comp ganhou')


