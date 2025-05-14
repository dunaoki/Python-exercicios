
n = int(input(' calcular seu fatorial'))
c = n
f = 1
while c > 0:
    print(c, end='')
    print('x' if c > 1 else '=', end='')
    f = f * c
    c = c -1

print(f'o fatoria de {n}! e {f}')
