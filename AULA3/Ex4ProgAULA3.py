'''Nome na vertical em escada. Modifique o programa anterior
de forma a mostrar o nome em formato de escada.'''

name = input('Digite o seu nome: ').upper()
cont = 0
stair = ''
for i in name:
    stair += name[cont]
    print(stair)
    cont += 1