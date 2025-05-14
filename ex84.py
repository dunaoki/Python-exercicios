temp =[]
princ =[]
mai= men = 0
while True:
    temp.append(str(input('nome: ')))
    temp.append(float(input('peso: ')))

    if len(princ)==0:
        mai =men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]

        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('quer continuar: [S/N]'))
    if resp in 'Nn':
        break

print(f'Foram cadastrada {len(princ)} pessoas ')
print(f'A pessoa mais pesada e {mai}')
print(f'A pessoa mais leve e {men}')