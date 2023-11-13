class Rect:
    def __init__(self, lenght, height):
        self.lenght = lenght
        self.height = height
    
    def changeSides(self):
        if change := input('Which size do you wanna change?: ').lower() == 'lenght':
            self.lenght = float(input('Type the new length: '))
        else:
            self.height = float(input('Type the new height: '))
            
    def showSizes(self):
        return print(f'The lenght is: {self.lenght}\nThe height is: {self.height}\nThe area is: {self.lenght*self.height}\nThe perimeter is: {self.lenght+self.height}')
    
rect = Rect(float(input("What's the lenght?: ")), float(input("What's the height?: ")))

if opt := input('Wanna change any side?: ').lower() == 'y':
    rect.changeSides()
else:
    pass

rect.showSizes()