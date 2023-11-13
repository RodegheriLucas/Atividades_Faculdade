def rmv(x):
    fltr = []
    for i in x:
        if i[0] == 'A' or i[0] == 'a':
            pass
        else:
            fltr.append(i)
    return fltr

plvr =  ['fita', 'Adenilton',
'armario', 'gaveta', 'Bruna', 'adentro', 'folga',
'impressora']
print(rmv(plvr))
