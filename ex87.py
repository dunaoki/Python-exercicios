matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somar = scol= mai =0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'digite um valor para [{l}, {c}]: '))

for l in range (0,3):
    for c in range (0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
        if matriz[l][c] %2 == 0:
            somar += matriz[l][c]
    print()
print(f'a soma dos valores pares e {somar}')
for l in range(0,3):
    scol += matriz [l][2]
print(f'a soma da terceira coluna e {scol}')
for c in range (0,3):
    if c == 0:
        mai = matriz [1][c]
    elif matriz[1][c] > mai:
        mai = matriz [1][c]
print(f'o maior numero da linha dois e {mai}')


