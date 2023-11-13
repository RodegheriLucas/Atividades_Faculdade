'''Conta espaços e vogais. Dado uma string com uma frase
informada pelo usuário (incluindo espaços em branco),
conte:'''

vowels = ['a','e','i','o','u']
word = input('Digite algo: ')
cont = 0
space = word.split(' ')
for i in range(len(word)):
    if word[i] in vowels:
        cont += 1
    else:
        pass
if len(space) == 2:
    print(f'{cont} vogais e {len(space)-1} espaço')
else:
    print(f'{cont} vogais e {len(space)-1} espaços')