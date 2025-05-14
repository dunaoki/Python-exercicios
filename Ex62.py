primeiro = int(input('qual o primeiro termo: '))
razao = int(input('Qual a razao: '))
cont =1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{primeiro} ->', end='')
        primeiro += razao
        cont += 1
    mais = int(input(' quantos termos mais vc quer contar: '))
print(f'o tatal de termo fora de {total}')
