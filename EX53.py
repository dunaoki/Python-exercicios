frase = str(input('digite uma frase')).strip()
palavra = frase.split()
junto = ''.join(palavra)
inv = junto[::-1]
print(f'o inverso de {junto} é {inv}')
if junto == inv:
    print('a palavra e palindromo')
else:
    print('a palavra nao e palindromo')

