class Bola:
    def __init__(self, cor, circunf, mat):
        self.cor, self.circunf, self.mat = cor, circunf, mat

    def trocaCor(self, cor):
        self.cor = cor

    def mostraCor(self):
        print(f'A cor da bola é {self.cor}')
        print(f'A circunferência da bola é {self.circunf}')
        print(f'O material da bola é {self.mat}')

bola = Bola(input('Qual a cor?: '), float(input('Qual a circunferência da bola?: ')), input('Qual o material?: '))

if opt := input('Deseja trocar a cor da bola?: ').lower() == 's':
    bola.trocaCor(input('Qual a cor?: '))
else:
    pass

bola.mostraCor()