n = soma = cont = 0
while True:
    n = int(input('digite um numero:'))
    if n == 999:
        break
    soma += n
    cont += 1
print(f' foram digitado {cont} e a soma foi de {soma}')
