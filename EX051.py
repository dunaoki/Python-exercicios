print('-=' * 11)
print('10 TERMOS DE UMA PA')
print('-='*11)
t= int(input('primeiro termo'))
r = int(input('Razao'))
decimo = t +(10 - 1) * r
for c in range(t, decimo, r):
    print(f'{c}', end = '->')
