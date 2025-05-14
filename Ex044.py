preco = float(input('qual o preco do produto:'))
print('''Qual a forma de pagamento:
[1] a vista dinheiro/cheque:
[2] a vista cartao:
[3] 2X no cartao:
[4] 3X ou mais no cartao:''')
pagamento = int(input('qual opcao?'))
if pagamento == 1:
    print(f'o valor do produto sera de R${preco -(preco * 0.10)} ')
elif pagamento == 2:
    print(f'o valor do produto sera de R$ {preco- (preco * 0.05)}')
elif pagamento == 3:
    print(f'o preco do produto sera R${preco}')
elif pagamento == 4:
    print(f'o preco do produto tera um acrescimo de R${preco + (preco*0.2)}')