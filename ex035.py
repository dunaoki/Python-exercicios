a = int(input('digite uma reta:'))
b = int(input('digite a segunda reta:'))
c = int(input('digite a terceira reta:'))
equilatero = a == b == c
isosceles = a==b or a==c or b==c
escaleno = a != b or a!=c or b!=c
if a+b>c and a+c>b and b+c>a:
    print(f'o numero {a, b, c} formam um triangulo')
else:
    print(f'o numero {a, b, c} NAO formam um triangulo')