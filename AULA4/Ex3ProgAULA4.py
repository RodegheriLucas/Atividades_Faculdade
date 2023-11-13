enqt = {}
loop = True
while loop:
    vote = input('Qual o numero do jogador?(Caso não haja mais votos digite 0): ')
    if vote.isalpha() == True:
        print('Valor inválido')
        loop = True
    else:
        if vote in enqt and 0<int(vote):
            enqt[vote] += 1
        elif 0<int(vote)<=23:
            enqt[vote] = 1
        else:
            loop = False
            sorted(enqt, reverse = True)
cont = 0
print(f'Foram computados {sum(enqt.values())} votos')
print(f'Jogador   votos   %')
for i in enqt:
    cont += 1
    print(f'{i}{" "*9}{enqt[i]}{" "*7}{enqt[i]*100//sum(enqt.values())}%')
    if cont == 3:
        break
print(f'O melhor jogador foi o camisa {max(enqt, key=enqt.get)} com {max(enqt.values())} votos, correspondente à {max(enqt.values())*100//sum(enqt.values())}% dos votos.')