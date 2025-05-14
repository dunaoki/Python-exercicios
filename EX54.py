totmaior =0
totmenor = 0
for c in range (1,5):
    idade=int(input(f' em que ano a {c}ª nasceu'))
    if idade < 2006:
        totmaior += 1
    else:
        totmenor = totmenor + 1
print(f' ao todo tivemos {totmaior} maior de idade ')
print(f' e tambem tivemos {totmenor} menor de idade ')













"""from datetime import date
totmaior = 0
totmenor = 0
for n in range(1, 4):
    n = int(input('em que ano essa a pessoa nasceu'))
    if n < 2006:
        totmaior = totmaior + 1
    else:
        totmenor = totmenor + 1
print(f'temos {totmenor} de menor idade')
print(f'temos {totmaior} de maior idade')"""


