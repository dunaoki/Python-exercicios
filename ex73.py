time =('corintians','palmeiras', 'santos', 'gremio',
       'cruzeiro', 'lamengo', 'vasco', 'chapecoense',
       'atletico', 'botafogo', 'atle-pr', 'bahia',
       'sp', 'flumi', 'sport recife', 'ec vito',
       'coritiba', 'avai', 'ponte preta','tle-go')
print('====='*15)
print(f'Lista de times do brasileirao{time}')
print('====='*15)
print(f'Os 5 primeiro do brasileirao {time[0:5]}')
print('====='*15)
print(f'os 4 ultimos do brasileirao {time[-4:]}')
print('====='*15)
print(f'Time em ordem alfabetica {sorted(time)}')
print('====='*15)
print(f'o chapeco esta na {time.index("chapecoense")+1} posicao')