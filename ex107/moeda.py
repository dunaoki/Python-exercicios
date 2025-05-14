
def aumentar (preco, taxa):
    r = preco + (preco * taxa/100)
    return r

def diminuir (preco, taxa):
    r = preco - (preco * taxa/100)
    return r

def dobro (preco):
    return preco *2


def metade (preco):
    return preco / 2