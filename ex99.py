from time import sleep
def maior (*num):
    cont = maior = 0
    print('Analisando o valores passados :')
    for valor in num:
        print(f'{valor}', end=' ')
        sleep(0.2)
        if cont == 0:
            maior = valor
        else:
            if valor > maior :
                maior = valor
        cont += 1
    print(f' Foram informado {cont} valores ao todo')
    print(f'e o maior valor foi {maior}')


maior(1, 2, 4, 6,8, 9)
#maior(1, 4, 6)
#maior(2, 4)
#maior(6)
#maior()