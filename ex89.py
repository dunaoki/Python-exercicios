ficha = list()
while True:
    nome=str(input('Nome: '))
    nota1 = float(input('nota1: '))
    nota2 = float(input('nota2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome,[nota1,nota2], media])
    resp = str(input('Quer continar: [S/N]'))
    if resp in 'Nn':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
print('-='*30)
while True:
    opc = int(input('Mostrar nota de qual aluno? (999 interrompe): '))
    if opc == 999:
        break
    if opc <= len(ficha)-1 :
        print(f'notas de {ficha[opc][0]} sao {ficha[opc][1]}')
