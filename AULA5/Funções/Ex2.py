'''Fazer uma função que receba como parâmetro um numero
inteiro e retorne o fatorial desse numero (não usar
recursividade).'''

def fact(x):
    nums = []
    nums.append(x)
    rslt = 1
    while x != 1:
        x -= 1
        nums.append(x)
    for i in nums:
        rslt = rslt * i
    return rslt

num = int(input(': '))
print(fact(num))