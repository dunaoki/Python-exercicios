nome = str(input('qual o seu nome:')).strip()
print(f'Seu nome em letra maiusculas e{nome.upper()}')
print(f'Seu nome em letra minuscula e {nome.lower()}')
print(f'Seu nome tem ao todo de letras {len(nome) - nome.count(' ')}')
print(f'seu primeiro nome tem {nome.find(' ')}')
