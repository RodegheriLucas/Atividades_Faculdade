loop = True
prest = []

def valorPagamento(vlr, days):
    if days>0:
        multa = vlr+(vlr*3/100)+(vlr*(days*0.1/100))
        print(f'Você pagou R${multa:.2f} por conta do atraso.')
        return multa
    else:
        print(f'Você pagou R${vlr} de prestação.')
        return vlr

while loop:
    valor = int(input('Qual o valor da prestação?: '))
    if valor>0:
        atrs = int(input('Quantos dias de atraso?: '))
        prest.append(valorPagamento(valor, atrs))
        loop = True
    else:
        loop = False

print(f'Você pagou um valor total de R${sum(prest)}\nSeu relatório de prestações foi esse: ')
for i in range(len(prest)):
    print(f'{i+1}ª prestação = R${prest[i]}')
