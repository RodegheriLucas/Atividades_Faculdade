'''Crie uma aplicação que leia dois números e imprima a soma
entre eles é.…'''

loop = True
while loop:
    print(int(input('Primeiro Numero: '))+int(input('Segundo Numero: ')))
    loop = False
    if  rpt := input('Deseja repetir?: ').lower() == 's':
        loop = True
    else:
        loop = False
