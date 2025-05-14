a =int(input('digite o\033[4m primeiro \033[m valor:'))
b =int(input('digite o\033[4m segundo \033[m valor:'))
c =int(input('digite o\033[4m terceiro \033[m valor:'))
if a+b>c and a+c>b and b+c>a:
    print(f'o numero {a, b, c} formam um triangulo')
    if a==b==c:
        print('o tringulo é \033[46m equilatero \033[m')
    if a!=b!=c!=a:
        print('o triangulo e \033[46mescaleno\033[m')
    else:
        print('o triangulo e \033[46misosceles\033[m')
else:
    print('esse numero \033[46m NAO \033[m pode formar um triangulo')