cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco','seis' , 'sete', 'oito',
        'nove','dez', 'onze', 'doze')
while True:
    num = int(input('digite de 0 a 20: '))
    if 0<= num <=20:
        break
    print('tente novamente...', end='')
print(f'o numero digitado foi {cont[num]}')

