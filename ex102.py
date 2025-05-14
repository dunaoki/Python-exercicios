def fatorial (n, show=False):
    """
    -> Calcula o fatorial de um numero
    :param n: o numero para ser calculado
    :param show: mostra ou nao a conta
    :return: o valor do fatorial
    """
    f =1
    for c in range(n,0,-1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f' {f} '



print(fatorial (5, show=True))