'''Faça um programa que leia algo pelo teclado e mostre na tela o
seu tipo primitivo e informações como: se o valor é um número,
se a variável começa com a primeira letra maiúsculas.
'''

print(f'{type(plvr := input(": "))}\nA primeira letra é maiúscula? = {plvr[0].isupper()}\nÉ um numero? = {plvr.isnumeric()}\nÉ uma letra? = {plvr.isalpha()}')