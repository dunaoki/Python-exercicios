def aumentar (preco=0, taxa=0, formato = False):
    r = preco + (preco * taxa/100)
    return r if formato is False else moeda(r)

def diminuir (preco=0, taxa=0, formato = False):
    r = preco - (preco * taxa/100)
    return r if not formato else moeda(r)

def dobro (preco=0, formato = False):
    r = preco * 2
    return r if not formato else moeda(r)


def metade (preco=0, formato = False):
    r = preco / 2
    return r if not formato else moeda(r)


def moeda (preco = 0, moeda ='R$'):
    return f'{moeda}{preco}'.replace('.',',')


def resumo (preco =0, taxaa=10, taxar=5):
    print('-'*30 )
    print(f'Preco analisado: {moeda(preco)}')
    print(f'Dobro do preco: {dobro(preco,True )}')
    print(f'Metade do preco: {metade(preco,True)}')
    print(f'com {taxaa} % de aumento:{aumentar(preco,taxaa,True)}')
    print(f'com {taxar}% de reducao:{diminuir(preco,taxar,True)}')