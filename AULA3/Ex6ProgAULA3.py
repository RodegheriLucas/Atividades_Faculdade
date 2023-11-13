'''Data por extenso. Faça um programa que solicite a data de
nascimento (dd/mm/aaaa) do usuário e imprima a data com o
nome do mês por extenso.
'''
birth = input('Digite sua data de nascimento: ').split('/')
mnth = {1:'Janeiro', 2:'Fevereiro', 3:'Março', 
4:'Abril', 5:'Maio', 6:'Junho', 7:'Julho', 
8:'Agosto', 9:'Setembro', 10:'Outubro', 
11:'Novembro', 12:'Dezembro'}
i = mnth.get(int(birth[1]))
print(f'Dia {birth[0]} de {i} de {birth[2]}')