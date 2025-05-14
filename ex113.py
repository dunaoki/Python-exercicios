def leiaint(msg):
    while True:
        try:
            n=int(input(msg))
        except (ValueError, TypeError):
            print('ERRO, digite uma valor valido:')
            continue
        else:
            return n

def leiafloat(msg):
    while True:
        try:
            n=float(input(msg))
        except (ValueError, TypeError):
            print('ERRO, digite uma valor valido:')
            continue
        else:
            return n


n =leiaint('digite um valor: ')
f = leiafloat('digite um num real: ')
print(f'o numero digitado inteiro foi  {n} e o real {f}')