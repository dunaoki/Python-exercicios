galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome']= str(input('nome: '))
    while True:
        pessoa['sexo']= str(input('sexo: [M/F]')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! digite apenas M ou F ')
    pessoa['idade'] = int(input('idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('quer continuar [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO, responda so com S ou N')
    if resp == 'N':
        break
print(galera)
print(f'ao todo temos {len(galera)} cadastradas ')
media = soma / len(galera)
print(f'a media da idade e {media:5.2f} anos ')
print('as mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'fF':
        print(f'{p["nome"]}', end='')
print()
print('lista das pessoas que estao acima da media: ')
for p in galera:
    if p['idade']>= media :
        print('     ',end='')
        for k , v in p.items():
            print(f'{k} = {v}', end='')
        print()
