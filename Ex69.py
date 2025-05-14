print('---'*15)
print('cadastre um pessoa')
print('---'*15)
total = tots = toti =0
while True:
    idade = int(input('Idade: '))
    sexo= ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if idade >= 18:
            total += 1
        if sexo == 'M':
            tots += 1
        if sexo == 'F' and idade < 20:
                toti += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]')).upper().strip()
    if resp == 'N':
            break
print(f'total de pessoa acima de 18 anos e de {total} pessoa')
print(f'foram cadastrado do sexo masculino {tots} pessoa')
print(f'o total de mulheres menor do que 20 anos e {toti} mulher')
