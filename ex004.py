a = input('digite algo:')
print('o tipo primitivo desse valor e ', type(a))
print('tem espaco?', a.isspace())
print('e um numero:', a.isnumeric())
print('e alfabetico:', a.isalpha())
print('e alfanumerico', a.isalnum())
print('esta em maiusculas', a.upper())
print('esta em minusculas:', a.islower())
print('esta capitalizada', a.istitle())