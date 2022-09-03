
print('Aula Lambda:')

print('1o. Calculando informações de Imposto ICMS:')

def calculo_ICMS(valor):
    return valor * 0.18

print(f'Para o valor de R$ 100.00 - Imposto ICMS: {calculo_ICMS(100.00)}')

#solução usando LAMBDA ( sem precisar criar uma função "def")
calculo_ICMS2 = lambda valor: valor * 0.18
print(f'Para o valor de R$ 100.00 - Imposto ICMS2: {calculo_ICMS2(100.00)}')

#exemplo: LAMBDA + função
def calcular_imposto(imposto):
    return lambda valor: valor * imposto

icms_SP = calcular_imposto(0.18)
icms_RJ = calcular_imposto(0.12)

print(f'Para o valor de R$ 100.00 - Imposto ICMS-SP: {icms_SP(100.00)}')
print(f'Para o valor de R$ 100.00 - Imposto ICMS-SP: {icms_RJ(100.00)}')

#FASE 2 -  Trabalhando com DADOS

lista = [
    ['Prod1', 100],
    ['Prod5', 500],
    ['Prod4', 400],
    ['Prod3', 300]
]
print(lista)
print('-- Colocando em ORDEM com função')
def func_ordenar(linha):
    return linha[1]

lista.sort(key = func_ordenar)
print(lista)

print('-- Colocando em ORDEM com LAMBDA')
lista2 = [
    ['Prod1', 100],
    ['Prod5', 500],
    ['Prod4', 400],
    ['Prod3', 300]
]
lista2.sort(key = lambda elemento: elemento[1])
print(lista2)

# FASE 3 - Trabalhando com MAP
print('-- Usando MAP')
lista_valores = [100,
                 200,
                 500,
                 400]
novosValores = list(map(lambda elemento: elemento * 2 , lista_valores))
print(novosValores)
animais = ['cao',
           'gato',
           'coelho',
           'passarinho']
animais2 = list(map(lambda elemento: str.upper(elemento) , animais))
print(animais2)

# FASE 4 - Trabalhando com FILTER (filtrar/separar os elementos)
print('-- Usando FILTER:')
lista = [
    ['Prod1', 100],
    ['Prod5', 500],
    ['Prod4', 400],
    ['Prod3', 300]
]
listaMaior300 = list(filter(lambda elemento: elemento[1] > 300, lista))
print(listaMaior300)

# FASE 5 - Trabalhando com REDUCE ( é apenas executar totalização)
from functools import reduce
print('-- Usando REDUCE')
listaValores=[
    200,
    500,
    200,
    300
]
valorTotal = reduce(lambda acumulador, elemento: elemento + acumulador, listaValores )
print(f'Aplicando o REDUCE: {listaValores} - Total Somatorio: {valorTotal}')
