import moeda

p = float(input('digite seu preco R$: '))
print(f'a metade de {p} e {moeda.metade(p)}')
print(f'o dobro de {p} e {moeda.dobro(p)}')
print(f'o aumento de 10% {moeda.aumentar(p, 10)}')