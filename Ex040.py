n1 = float(input('qual sua primeira nota:'))
n2 = float(input('qual sua segunda nota:'))
media = (n1 + n2 ) / 2
if media < 5.0:
    print(' vc esta \033[4m REPROVADO \033[m')
elif 7 > media >= 5 :
    print('o aluno esta \033[4m RECUPERACAO \033[m')
else:
    print('o aluno esta \033[4m APROVADO \033[m')