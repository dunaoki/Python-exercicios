from random import randint

def sorteia (lista):
    print('Sorteando 5 numeros: ', end=' ')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ')
    print(' << PRONTO')

def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 ==0:
            soma += valor
    print(f'a soma dos valores pares da lista {lista} e de {soma}')


numeros = list()
sorteia(numeros)
somapar(numeros)
