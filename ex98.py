from time import sleep
def contador (i, f, p):
    if p < 0:
        p *= -1
    if p ==0:
        p = 1
    print(f'conta de {i} ate {f} pulando de {p} em {p}')
    sleep(2)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont += p
        print('fim')
    else:
        cont =i
        while cont >= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont -= p
        print('fim')


contador (1, 10, 1)
contador (10, 1, 2)
print('agora e sua vez de personalizar seu programa: ')
ing= int(input('inicio: '))
fim = int(input('fim:   '))
pas=int(input('passo:   '))
contador(ing, fim, pas)