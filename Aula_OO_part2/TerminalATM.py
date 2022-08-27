from Classes import Cliente, Fone, Email, ContaBancaria, Poupanca

# Terminal do USUARIO

# Abrindo uma Conta Bancaria

print('Bem vindo..! ')
print('Informe seus dados para Abrir uma Conta :)')

# fazendo a leitura por teclado

cli1 = Cliente(input('Digite o Nome:'),
               input('Digite CPF:'))

print("Preciso de seus dados de contato (Email ou Fone):")
email = Email(input('Digite email(opcional):'))
fone = Fone(input('Digite fone(opcional):'))

if email.email == '':
    cli1.contato = fone
else:
    cli1.contato = email

print(f'Dados de contato Cliente {cli1.nome}:')
cli1.contato.ver()

# Vamos para criar a conta Bancaria

print('')
print(f'----- Apresentando dados da ContaBancaria-----')

conta1 = ContaBancaria(1010,1,101010,0,cli1)

print(conta1.numero)
print(conta1.cliente)
print(conta1.cliente.nome)
print(conta1.cliente.contato)
print(conta1.cliente.contato.ver())

conta1.info()

#Usando Poupança

poupanca1 = Poupanca(1010,500,101010,5000,cli1,50)
poupanca1.info()
poupanca1.creditarRendimento()
poupanca1.info()



#cli1 = Cliente('Fausto','12346')
#objEmail = Email('email@fiap.com.edu')
#objFone = Fone('999888555')

#cli1.contato = objFone
#print(cli1.__dict__)


