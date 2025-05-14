km = int(input('qual a a distancia em km:'))
if km <= 200:
    print(f' o valor da passagem sera de {km * 0.05}')
else:
    print(f'o valor da passagem sera de {km * 0.45}')