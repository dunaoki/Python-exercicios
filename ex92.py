from datetime import datetime
dados = dict()
dados['nome'] = str(input('nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('carteira de trabalho (0nao tem): '))
if dados['ctps'] != 0:
    dados['contratacao']= int(input('Ano de contratacao: '))
    dados['salario']= int(input('Salario:R$ '))
    dados['aposenta']= dados['idade'] + ((dados['contratacao'] + 35 ) - datetime.now().year)
print('==='*30)
for k ,i in dados.items():
    print(f'   -{k} tem o valor {i}')