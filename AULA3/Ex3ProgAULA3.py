''' Nome na vertical. Faça um programa que solicite o nome do
usuário e imprima-o na vertical.'''

name = input('Digite o seu nome: ').upper()
cont = 0
for i in name:
    print(name[cont])
    cont += 1