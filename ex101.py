"""def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'com {idade} anos : NAO VOTA'
    elif 16 <= idade <18 or idade > 65:
        return f'com {idade} anos : E OPCIONAL'
    else:
        return f'com {idade} ano: E OBRIGATORIO'


nasc = int(input('Em que ano voce nasceu: '))
print(voto(nasc))"""


def multiplicar(a, b):
    return a * b


resultado = multiplicar(5, 3) + multiplicar(2, 4)
print(resultado)
