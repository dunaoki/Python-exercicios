palavras = ('arroz','feijao','linguagem','python',
            'curso','gratis', 'estudar','praticar',
            'futuro','trabalhar','mercado')
for p in palavras:
    print(f'\na palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end='')