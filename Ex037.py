num = int(input('Escreva um numero inteiro?:'))
escolha = int(input('''
[1] para binario
[2] para octal
[3] para hexadeciamal:--> '''))
if escolha == 1:
    print(f'o binario e {bin(num)}')
elif escolha == 2:
    print(f'ooctal e {oct(num)} ')
else:
    print(f'o hexadecimal e {hex(num)}')