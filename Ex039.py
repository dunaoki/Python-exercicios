# nasc = int(input('Em qual ano voce nasceu :'))
# idade = 2024 - nasc
# if idade < 18:
#     print(f' voce ainda vai se alistar  e falta {18 - idade} anos')
# elif idade == 18:
#     print('esta na hora de alistar')
# else:
#     print(f'ja passou {idade - 18} da anos de alistar')















nasc = int(input('qual o ano de nascimento: '))
idade = 2025 - nasc
if idade > 18:
    print(f'Ja deveria ter alistado {idade - 18  }anos')
elif idade == 18:
    print('deve se alistar IMEDIATAMENTE')
else:
    print(f'ainda falta {18 - idade} anos para se alistar')