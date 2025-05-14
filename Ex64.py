cont = soma = n = 0
n = int(input(' digite um numero'))
while n != 999:
    cont += 1
    soma += n
    n = int(input(' digite um numero'))
print(f'vc digitou {cont} e a soma foi de {soma}')

