class ContaBancaria:
    def __init__(self, id, titular, saldo):
        self.id = id
        self.titular = titular
        self.saldo = saldo
        print(f'A conta {self.id} criada com sucesso. saldo R${self.saldo:,.2f}')

    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem o saldo de R${self.saldo:,.2f}"    

    def depositar(self, valor):
        self.saldo += valor
        print(f'{valor} depositado com sucesso na conta {self.id}')

    def sacar(self, valor):
        if valor > self.saldo:
            print(f'Saque de R${valor:,.2f} NEGADO! Na conta {self.id} o saldo é de R${self.saldo:,.2f}')
        else:
            self.saldo -= valor
            print(f'Saque de R${valor:,.2f} concluído com SUCESSO!')           

c1 = ContaBancaria(12365, "Guilherme", 3000)
c1.depositar(500)
c1.sacar(1000)
print(c1)      


c2 = ContaBancaria(6598, "Ione", 9000)
c2.sacar(15000)
print(c2)