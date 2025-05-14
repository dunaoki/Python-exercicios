n = str(input('digite seu nome:')).strip()
nome = n.split()
print(f'seu primeiro nome {nome[0]}')
print(f'seu ultimo nome {nome[len(nome)-1]}')
