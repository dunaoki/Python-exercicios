# valor = float(input('qual e o valor da casa:'))
# sal = float(input('qual e o seu salario:'))
# ano = int(input('quantos anos vc vai pagar:'))
# prest = valor / ano
# print(f'o valor da prestacao da casa em {ano} sera de {prest:.2f}')
# if prest > (sal*0.3):
#     print('vc \033[41m NAO \033[m  podera financiar este imovel ')
# else:
#     print('seu emprestimo sera \033[44m concedido \033[m')

















valor = float(input('Qual e o valor do imovel? '))
sal = float(input('qual éo seu salario?:'))
ano = int(input('quantos anos vai pagar?: '))

prest = valor / ano
if prest > (sal *0.3):
    print('seu emprestimo sera negado ')
else:
    print('emprestimo concedido ')



