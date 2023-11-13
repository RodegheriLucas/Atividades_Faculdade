'''João quer montar um painel de leds contendo diversos números. Ele não
possui muitos leds, e não tem certeza se conseguirá montar o número
desejado. Considerando a configuração dos leds dos números abaixo, faça
um algoritmo que ajude João a descobrir a quantidade de leds necessário
para montar o valor.
'''

nums = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
lst = []
led = 0
qnt = input('Qual numero deseja mostrar?: ')
for i in range(len(qnt)):
    lst.append(int(qnt[i]))
    led += nums[lst[i]]
print(f'{led} leds')