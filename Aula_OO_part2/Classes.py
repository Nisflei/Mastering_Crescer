
class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.contato = None

class Email:
    def __init__(self,email):
        self.email = email

    def ver(self):
        print(f'Contato: {self.email}')

class Fone:
    def __init__(self,fone):
        self.fone = fone

    def ver(self):
        print(f'Contato: {self.fone}')

Noclass ContaBancaria:
    def __init__(self,numero, digito, agencia, saldo, cliente ):
        self.numero =  numero
        self.digito = digito
        self.agencia = agencia
        self.saldo = saldo
        self.cliente = cliente

    def verificarSaldo(self):
        return self.saldo

    def depositar(self,valor):
        self.saldo = self.saldo  + valor

    def sacar(self,valor):
        if (self.saldo  - valor) > 0:
            self.saldo = self.saldo - valor
        else:
            print('Saldo insuficiente..!!!')

    def info(self):
        print('Dados da Conta:')
        print(f'- cliente: {self.cliente.nome}')
        print(f'- contato:{self.cliente.contato.ver()}')
        print(f'- num: {self.numero}')
        print(f'- saldo: {self.saldo}')

class Poupanca(ContaBancaria):
    def __init__(self,numero, digito, agencia, saldo, cliente ,rendimento):
        ContaBancaria.__init__(self,numero, digito, agencia, saldo, cliente)
        self.rendimento = rendimento

    def creditarRendimento(self):
        self.saldo = self.rendimento + self.saldo


