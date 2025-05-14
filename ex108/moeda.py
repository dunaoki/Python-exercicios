
def aumentar (preco=0, taxa=0):
    r = preco + (preco * taxa/100)
    return r

def diminuir (preco=0, taxa=0):
    r = preco - (preco * taxa/100)
    return r

def dobro (preco=0):
    return preco *2


def metade (preco=0):
    return preco / 2

def moeda (preco = 0, moeda ='R$'):
    return f'{moeda}{preco}'.replace('.',',')