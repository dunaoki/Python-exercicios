frase = str(input('digite uma frase:')).strip().lower()
print(frase.count('a'))
print(f'a primeira letra A aparece na posicao {frase.find('a')}')
print(f'a ultima letra A aparece na posica {frase.rfind('a')}')