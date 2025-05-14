soma =0
cont=0

for c in range (1, 7):
    n = int(input('digite um valor:'))
    if n % 2 == 0:
        soma = soma + n
        cont += 1
print(f'existe {cont} numeros pares e a soma e de {soma}')





""" soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('digite o primeiro numero'))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
print(f'vc informou {cont} numeros e a soma foi {soma}')"""

