'''
Nome ao contrário em maiúsculas. Faça um programa que
permita ao usuário digitar o seu nome e em seguida mostre o
nome do usuário de trás para frente utilizando somente
letras maiúsculas. Dica: lembre se que ao informar o nome o
usuário pode digitar letras maiúsculas ou minúsculas.
'''

name = input('Qual o seu nome?: ').upper().split(' ')
fnl = []
cont = 0
for i in name:
    inv = name[cont]
    cont += 1
    fnl.append(inv[::-1])
print(' '.join(fnl))