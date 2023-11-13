'''Fazer uma função que recebe um argumento inteiro. A
função retorna o valor de caractere 'P', se seu
argumento for positivo, e 'N', se seu argumento for
zero ou negativo.'''

def posneg(x):
    if x>0:
        return 'P'
    else:
        return 'N'
    
num = int(input(': '))
print(posneg(num))