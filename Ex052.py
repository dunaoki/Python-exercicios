n = int(input('digite um numero'))
tot = 0
for c in range (1, n +1):
    if n % c == 0:
       print ('\033[33m', end=" ")
       tot = tot + 1
    else:
        print('\033[34m', end=" ")
    print(c, end=" ")

print(f' o {n} e foi divisivel {tot} vezes')
if tot == 2:
    print(f' o {n} é  um numero primo')
else:
    print(f'o {n} nao é um numero primo')
























"""
n = int(input('digite um numero'))
tot = 0
for c in range (1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        tot += +1
    else:
        print('\033[m', end='')
    print(f'{c} ',end='' )

print(f'\033[m o numero {n} foi divisivel {tot}')
if tot == 2 :
    print(f'o numeor {n} é primo')
"""

