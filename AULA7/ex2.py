class Square:
    def __init__(self, side):
        self.side = side

    def changeSize(self):
        self.side = float(input('Qual o novo tamanho do lado?: '))
    
    def showSide(self):
        print(f'\nO lado do quadrado é igual a {self.side}\n')
    
    def area(self):
        return f'A área é igual a {self.side**2}'

sqr = Square(float(input('Qual o tamanho do lado do quadrado?: ')))
if opt := input('Deseja alterar o tamanho?: ').lower() == 's':
    sqr.changeSize()
else:
    pass

sqr.showSide()

print(sqr.area())