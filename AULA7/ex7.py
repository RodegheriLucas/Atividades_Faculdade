class Tamaguchi:
    def __init__(self, name, hungry=10, health='Boa', age=1):
        self.name, self.hungry, self.health, self.age = name, hungry, health, age
    
    def changeName(self):
        self.name = input('Digite um novo nome: ').capitalize()
    
    def toFeed(self):
        for i in range(self.hungry):
            self.hungry -= 2
            if self.hungry<0:
                self.hungry = 0
            if 0<=self.hungry<=5:
                self.health = 'Ruim'
                print('O tamagushi precisa se alimentar.')
            elif 5<self.hungry<=7:
                self.health = 'Mediana'
            elif 7<=self.hungry<=10:
                self.health = 'Boa'
            else: 
                pass
            if opt := input('Deseja alimentar o tmaagushi?: ').lower() == 's':
                self.hungry += 10
            else:
                pass
    
    def toGrow(self):
        self.age += 1

    def showTamagushi(self):
        return f'O tamagushi {self.name} tem {self.age} anos, e está com a saúde {self.health}'       

pet = Tamaguchi(input('Digite o nome do seu pet: ')) 

if opt := input('Deseja trocar o nome do seu pet?: ').lower() == 's':
    pet.changeName()
else:
    pass

pet.toFeed()

pet.toGrow()

print(pet.showTamagushi())