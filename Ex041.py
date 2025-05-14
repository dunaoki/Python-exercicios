ano = int(input('Qual seiu ano de nascimento?'))
idade = 2024 - ano
if idade <= 9:
    print('seu categoria e \033[33m Mirim\033[m')
elif idade <= 14:
    print('Sua categoria e \033[33m Infantil \033[m')
elif idade <= 19:
    print(' Sua categoria e \033[33m Junior \033[m')
elif idade <= 25:
    print('Sua categotia e \033[33m Senior \033[m')
else:
    print('Sua categoria e \033[33m Master \033[m')
