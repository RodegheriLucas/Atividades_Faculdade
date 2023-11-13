contg = ['primeiro', 'segundo', 'terceiro', 'quarto', 'quinto']
dist = []
nome = input('Qual o nome do atleta?: ')
if len(nome) <= 1:
    exit()
for i in contg:
    valor = float(input(f'Qual foi a distância do {i} salto?: '))
    dist.append(valor)
print(f'Nome: {nome}')
for i in range(len(dist)):
    print(f'{contg[i]} salto: {dist[i]}')
print(f'Média: {sum(dist)/5}')