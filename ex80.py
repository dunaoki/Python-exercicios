valores=[]
for cont in range(0,5):
    n=(int(input('digite o valor: ')))
    if cont == 0 or n > valores[-1]:
        valores.append(n)
        print('Adicionado no final da lista ...')
    else:
        pos =0
        while pos < (len(valores)):
            if n <= valores[pos]:
                valores.insert(pos,n)
                print(f'Foi add na posicao {pos}da lista')
                break
            pos += 1
print(f'os valores da lista foi {valores}')