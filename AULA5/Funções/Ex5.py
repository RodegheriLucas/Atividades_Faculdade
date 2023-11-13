'''Escreva um script que pergunta ao usuário se ele
deseja converter uma temperatura de grau Celsius para
Farenheit ou vice-versa. Para cada opção, crie uma
função. Crie uma terceira, que é um menu para o
usuário escolher a opção desejada, onde esse menu
chama a função de conversão correta.'''

def menu(opt):
    if opt == 'a':
        temp = float(input('Qual a temperatura em Farenheit para converter?: '))
        return str(celsius(temp))+'°C'
    else:
        temp = float(input('Qual a temperatura em Celsuis para converter?: '))
        return str(farh(temp))+'°F'

def celsius(fah):
    return (fah*5 - 160)//9
def farh(cels):
    return (cels*9 + 160)//5

opt = input('a - Farenheit -> Celsius\nb - Celsius -> Farenheit\nQual você deseja usar?: ').lower()
print(menu(opt))