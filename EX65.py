resp = 'S'
cont = soma = media = maior = menor =0
while resp in 'Ss':
    n = int(input('digite outro numero'))
    cont += 1
    soma += n
    media = soma / cont
    if cont == 1:
        maior = menor = n
    else:
        if maior < n:
            maior = n
        if menor > n:
            menor = n
    resp = str(input('quer digitar outro numero [S/N]')).upper().strip()[0]
print(f'media do valores foram {media} e o maior numero {maior} e o menor {menor}')