dados = dict()
partida = list()
dados['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Qtas partidas {dados["nome"]} jogou? '))
for c in range(0,tot):
    partida.append(int(input(f'Quantos gol na partida {c}: ')))
dados['gols'] = partida[:]
dados['total'] = sum(partida)
print(dados)
print('==='*30)
for k, v in dados.items():
    print(f'o campo {k} tem valor {v}')
print('==='*30)
print(f'o jogador {dados["nome"]} jogou {len(dados["gols"])} partidas')
for i, v in enumerate(dados["gols"]):
    print(f'a partida {i} fez {v} gols')
print(f'foi um total de {dados["total"]} de gols')