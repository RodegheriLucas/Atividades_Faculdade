class Person:
    def __init__(self, name, age, weight, height):
        self.name, self.age, self.weight, self.height = name, age, weight, height
    
    def getOld(self, years):
        self.age += years

    def toGrow(self,years):
        if self.age<=21:
            self.height += 0.05*years
        else:
            grow = float(input('Quanto vc cresceu?: '))
            self.height += grow

    def getWeight(self, fat):
        self.weight += fat

    def showPerson(self):
        return f'Seu nome é {self.name}\nSua idade será {self.age}\nSeu peso será {self.weight}\nSua altura será {self.height}'
    
prsn = Person(input('Qual o seu nome?: '), int(input('Qual a sua idade?: ')), float(input('Qual o seu peso?: ')), float(input('Qual a sua altura?: ')))

prsn.getOld(idade := int(input('Quantos anos se passaram?: ')))

prsn.toGrow(idade)

if opt := input('Você engordou ou emagreceu?: ').lower() == 'emagreci':
    wght = float(input('Quanto vc emagreceu?: '))
    prsn.getWeight(-1*wght)
else:
    wght = float(input('Quanto vc engordou?: '))
    prsn.getWeight(wght)

print(prsn.showPerson())
