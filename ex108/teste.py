from ex108 import moeda

p = float(input('digite seu preco R$: '))
print(f'a metade de {moeda.moeda(p)} e {moeda.moeda(moeda.metade(p))}')
print(f'o dobro de {moeda.moeda(p)} e {moeda.moeda(moeda.dobro(p))}')
print(f'o aumento de 10% {moeda.moeda(moeda.aumentar(p, 10))}')