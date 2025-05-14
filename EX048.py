# soma = 0
# cont= 0
# for c in range(1, 500, 2):
#     if c % 3 ==0:
#         soma= soma + c
#         cont = cont + 1
# print(f'a soma dos {cont} numeros impares e de {soma}')



#
# soma = 0
# cont= 0
#
# for i in range(1, 501, 2):
#     if i % 3== 0:
#         soma +=i
#         cont +=  1
# print(f'a contagem dos numero {cont} e a soma e {soma}')












"""soma = 0
cont = 0
for n in range (1, 501, 2):
    if n % 3 == 0:
        cont = cont + 1
        soma = soma + n
print(f'a soma de todos {cont} e a soma dos valores sao {soma}')"""





print("""
[1] SOMA
[2] SUBTRACAO
[3] MULTIPLICACAO
[4] DIVISAO
""")
num= (int(input("escolha um numero para operacao matematica: ")))

n1 =(int(input("Digite 1 numero: ")))
n2 =(int(input("Digite 2 numero: ")))

if num == 1:
    print(n1+n2)
elif num ==2:
    print(n1 - n2)
elif num == 3:
    print(n1*n2)
elif num == 4:
    if n1>n2:
        print(n1/n2)
    else:
        print("o numero dois precisa ser menos  que o primeiro numero")










