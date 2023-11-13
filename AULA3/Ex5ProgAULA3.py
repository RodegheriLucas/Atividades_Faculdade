'''Nome na vertical em escada invertida. Altere o programa
anterior de modo que a escada seja invertida.'''

name = input('Digite o seu nome: ').upper()
cont = len(name)
for i in name:
    print(name[:cont:])
    cont -= 1