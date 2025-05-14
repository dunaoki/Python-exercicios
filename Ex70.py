print('----'*15)
print(                      '                       SUPER BARATAO')
print('----'*15)
total = maior = cont = menor = 0
barato =' '
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço:R$ '))
    cont += 1
    total += preco
    if preco >= 1000:
        maior += 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto

    resp =' '
    while resp not in 'NS':
        resp = str(input('Quer continur? [S/N]')).strip().upper()
    if resp == 'N':
        break
print(f'o total gasto na compra foi de {total}')
print(f'existe {maior} produtos maior do que mil reais')
print(f'o produto mais barato foi {barato} e o preco dele foi de {menor}')
print('FIM')

