from ex110 import moeda

p = float(input('digite seu preco R$: '))
print(f'a metade de {moeda.moeda(p)} e {moeda.metade(p, True)}')
print(f'o dobro de {moeda.moeda(p)} e {moeda.dobro(p, True)}')
print(f'o aumento de 10% {moeda.aumentar(p, 10)}')