sis = {'Windows':0, 'Unix':0, 'Linux':0, 'Netware':0, 'MacOS':0, 'outros':0}
for i in sis:
    vote = int(input(f'Quantos votos o sistema {i} teve?: '))
    sis[i] += vote
ttl = sum(sis.values())
print(f'Sistema Operacional Votos  %\n{"-"*19} {"-"*5} {"-"*3}')
for i in sis:
    bigv = max(sis.values())
    tmnh = 19-len(i)
    tmnh2 = tmnh - 3
    print(f'{i}:{" "*tmnh}{sis[i]}{" "*tmnh2}{round(sis[i]*100//ttl)}%')
print(f'{"-"*19} {"-"*5} {"-"*3}\nTotal {ttl}\nO Sistema Operacional mais votado foi o {max(sis, key=sis.get)}, com {bigv} votos, correspondendo a {round(bigv*100//ttl)}% dos votos.')