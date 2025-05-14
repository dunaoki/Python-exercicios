def ficha(jog='<desconhecido>', gols=0):
    print(f'o {jog} fez {gols} gols no campeonato')


n=str(input('qual o seu nome: '))
g=str(input('quantos gols vc fez: '))
if g.isnumeric():
    g = int(g)
else:
    g=0
if n.strip()== '':
    ficha(gols=g)
else:
    ficha(n,g)