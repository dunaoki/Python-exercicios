num = (int(input('digite um valor: ')),int(input('digite um valor: ')),
       int(input('digite um valor: ')),int(input('digite um valor: ')))
print(f'vc digitou os valores {num}')
print(f'vc digitou o numero 9 {num.count(9)} , vezes')
if 3 in num:
    print(f'o valor 3 apareceu na posicao {num.index(3)+1}')
else:
    print('o numero tres nao foi digitado em nunhuma posicao')
print('o numero pares digitados foi: ')
for n in num:
    if n %2 ==0:
        print(n)
