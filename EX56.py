mulher = 0
totidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for c in range (1, 4):
    print(f'====  {c} pessoa  ====')
    n1 = str(input('nome:'))
    idade = int(input('idade:'))
    sexo = str(input('sexo [M/F]:'))
    totidade = totidade + idade
    if c and sexo in 'Mm'== 1:
        maioridadehomem = idade
        nomevelho = n1
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = n1
    if sexo in 'Ff' and idade > 20:
        totmulher20 = totmulher20 + 1


print(f'A media do grupo e de {totidade / 3}')
print(f'a idade do mais velho e {maioridadehomem} e nome dele e {nomevelho}')
print(f'o total de mulher maior de 20 anos e {totmulher20}')
