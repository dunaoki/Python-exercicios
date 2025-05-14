

n1 = int(input(' digite o primeiro numero: '))
n2 = int(input(' digite o segundo numero: '))
opcao = 0
while opcao != 5:
    print('''   [1] somar'
      '[2] multiplicar'
      '[3] maior'
      '[4] novos numeros'
      '[5] finalizar''', )
    opcao = int(input(' qual opcao voce gostaria: '))
    if opcao ==1:
        soma = n1 + n2
        print(f'a soma de {n1} mais {n2} e de {soma}')
    elif opcao == 2:
        multiplicacao = n1 * n2
        print(f'a multiplicacao e de {multiplicacao}')
    elif opcao == 3:
           if n1 > n2:
               maior = n1
           else:
               maior = n2
           print(f'o maior e {maior}')
    elif opcao == 4:
        print('digite novos numeros: ')
        n1 = int(input('qual o primeiro numero: '))
        n2 = int(input('qual o segundo numero: '))
print('FIM')













"""n1 = int(input('digite o primeiro valor: '))
n2 = int(input('digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print('[1] somar')
    print('[2] multiplicar')
    print('[3] maior')
    print('[4] novos numeros')
    print('[5] sair do programa')
    opcao = int(input(' \033[44m Quais das opcoes voce quer? \033[m'))
    if opcao == 1:
       soma = n1 + n2
       print(f'a soma de {n1} e {n2} e de {soma}')
    elif opcao == 2:
        multiplicacao = n1 * n2
        print(f'multiplicacao de {n1} e {n2} deu {multiplicacao}')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'o maior numero e o {maior}')
    elif opcao == 4:
        print('informe um numero novamente')
        n1 = int(input('qual o primeiro numero'))
        n2 = int(input('qual o segundo numero'))

    elif opcao == 5:
        print('finalizado ')

print('fim do programa')"""