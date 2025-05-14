time = list()
jogador = dict()
partida = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Qtas partidas {jogador["nome"]} jogou? '))
    partida.clear()
    for c in range(0,tot):
        partida.append(int(input(f'Quantos gol na partida {c}: ')))
    jogador['gols'] = partida[:]
    jogador['total'] = sum(partida)
    time.append(jogador.copy())
    while True:
        resp = str(input('quer continuar [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO, responda so com S ou N')
    if resp == 'N':
        break
print('==='*30)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print('===' * 30)
for k,v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('===' * 30)
while True:
    busca = int(input('mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO, nao existe jogador com codigo {busca}')
    else:
        print(f'--- LEVANTAMENTO DO JOGADOR  {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    no jogo {i+1} fez {g} gols')
print('<<< VOLTE SEMPRE>>>')