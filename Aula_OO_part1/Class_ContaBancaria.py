
class ContaBancaria:
    def __init__(self,numero, digito, agencia, saldo ):
        self.numero =  numero
        self.digito = digito
        self.agencia = agencia
        self.saldo = saldo

    def verificarSaldo(self):
        return self.saldo

    def depositar(self,valor):
        self.saldo = self.saldo  + valor

    def sacar(self,valor):
        if (self.saldo  - valor) > 0:
            self.saldo = self.saldo - valor
        else:
            print('Saldo insuficiente..!!!')


# Terminal ATM (caixa eletronico)

conta1 = ContaBancaria(1010,1,'A1010', 5000)
conta2 = ContaBancaria(2020,2,'A1010', 100)

print(conta1.__dict__)
print(conta2.__dict__)

print(f'Seu saldo é {conta1.verificarSaldo()}')

print('Fazendo deposito de R$ 10.00')
conta1.depositar(10)
print(f'Seu saldo é {conta1.verificarSaldo()}')

print('Fazendo saque de R$ 10.000')
conta1.sacar(10000)
print(f'Seu saldo é {conta1.verificarSaldo()}')
