vlrs = {'2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0, '1':0}
loop = True
while loop:
    venda = int(input('Quanto o funcionario vendeu?: '))*0.09+200
    cont = str(venda)
    if venda<=999:
        vlrs[cont[0]] += 1
    else:
        vlrs['1'] += 1
    dnv = input('Repetir?(S/N): ').lower()
    if dnv == 's':
        loop = True
    else:
        loop = False
        print(f'De R$200 a R$299: {vlrs["2"]}\nDe R$300 a R$399: {vlrs["3"]}\nDe R$400 a R$499: {vlrs["4"]}\nDe R$500 a R$599: {vlrs["5"]}\nDe R$600 a R$699: {vlrs["6"]}\nDe R$700 a R$799: {vlrs["7"]}\nDe R$800 a R$899: {vlrs["8"]}\nDe R$900 a R$999: {vlrs["9"]}\nDe R$1000 em diante: {vlrs["1"]}')