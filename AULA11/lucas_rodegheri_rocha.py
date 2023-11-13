def media(notas):
    for i in notas:
        ttl = 0
        ttl += int(i)
    return ttl/len(notas)

notas = {}
file = open('notas_estudantes.txt', 'r+')
lines = file.readlines()


for i in lines:
    espc = i.split('\n')
    for x in espc:
        if x == '':
            espc.remove('')
        else:
            aluno = x.split(' ')
            for y in aluno:
                if y.isalpha() == True:
                    pass
                else:
                    int(y)
                    notas[aluno[0]] = aluno[1::]


for b in notas:
    if len(notas[b])>6:
        print(f'O aluno com mais de 6 notas é {b}\n')
    else:
        pass
for a in notas:
    print(f'A média de {a} é igual à {media(notas[a])}\n')
h = 0
for c in notas.values():
    for d in notas:
        print(f'{d}:\nA nota mínima é = {min(c)}\nA nota maxima é = {max(c)}\n')
    h += 1
    if h == 1:
        break

