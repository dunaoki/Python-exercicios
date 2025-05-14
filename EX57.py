sexo = str(input('qual o seu sexo [M/F]: '))
while sexo not in 'MF':
    sexo = str(input('dados incorreto, qual o seu sexo? ')).upper().strip()
print(f' seu sexo e {sexo} registrado com sucesso'.upper())
















"""sexo = str(input('qual o seu sexo [m/f]')).upper()
while sexo not in 'mMFf':
    sexo = str(input('Dados invalido. Por favor informe seu sexo: '))
print(f'Sexo {sexo} registrado com sucesso!'.upper())"""
