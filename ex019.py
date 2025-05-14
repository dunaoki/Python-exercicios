#uma lista para escolher o nome de uma pessoa aleatoria


import random

n1 = str(input('digite um nome:'))
n2 = str(input('digite o segundo nome:'))
n3 = str(input('digite o terceiro nome'))
n4 = str(input('digite o quarto nome'))
list = [n1, n2, n3, n4]
nome = random.choice(list)
print(f'o nome escolhido e {nome}')
