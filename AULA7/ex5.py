class Cc:
    def __init__(self, conta, nome, saldo=0):
        self.conta, self.nome, self.saldo = conta, nome, saldo
    
    def trocaNome(self):
        self.name = input('Qual o novo nome?: ')

    def transf(self):
        if opt := input('Deseja fazer um saque ou depósito?: ').lower() == 'saque':
            saque = float(input('Quanto deseja retirar?: '))
            if self.saldo<saque:
                print('Saldo insuficiente!')
                self.transf()
            else:
                self.saldo -= saque
        else:
            self.saldo += float(input('Qual é o valor do deposito?: '))
    
    def showCc(self):
        return f'Aqui está sua conta {self.nome}\nConta: {self.conta}\nSaldo: {self.saldo}'


prsn = Cc(input('Qual o número da sua conta corrente?: '), input('Qual é o seu nome?: '), float(input('Ta com quanto de saldo meu ludmillo?: ')))

if dcs := input('Deseja alterar o nome da conta?: ').lower() == 's':
    prsn.trocaNome()

prsn.transf()
print(prsn.showCc())