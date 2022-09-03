# Lista de produtos e valores de FRETE

produtos = [
    {'Frete': 0.90, 'Produto': 'MILHO',   'Origem': 'MT', 'Destino': 'SP', 'Peso_kg': 5500.0},
    {'Produto': 'SOJA',   'Frete': 0.55, 'Peso_kg': 4300.0, 'Origem': 'MS', 'Destino': 'SP'},
    {'Produto': 'ALGODÃO','Frete': 0.13, 'Peso_kg': 3000.0, 'Origem': 'GO', 'Destino': 'MT'},
    {'Produto': 'MILHO',  'Frete': 0.49, 'Peso_kg': 8000.0, 'Origem': 'MS', 'Destino': 'MT'},
    {'Produto': 'MILHO',  'Frete': 0.22, 'Peso_kg': 5000.0, 'Origem': 'MS', 'Destino': 'MT'},
    {'Produto': 'ADUBO',  'Frete': 0.79, 'Peso_kg': 4500.0, 'Origem': 'SP', 'Destino': 'MS'},
    {'Produto': 'SOJA',   'Frete': 0.31, 'Peso_kg': 8000.0, 'Origem': 'GO', 'Destino': 'SP'},
    {'Produto': 'RAÇÃO',  'Frete': 0.27, 'Peso_kg': 1500.0, 'Origem': 'SP', 'Destino': 'MS'},
    {'Produto': 'ARROZ',  'Frete': 1.90, 'Peso_kg': 5300.0, 'Origem': 'RS', 'Destino': 'PR'},
]
print (produtos)
#1 Colocar em order de peso_kg
produtos.sort(key= lambda elemento: elemento['Peso_kg'])
print(f'Produtos ordernados por peso: {produtos}')

#2 Vamos extrais somente a lista de preço
precos = list(map(lambda  elemento: elemento['Frete'] ,produtos))
print(precos)

#3 Devido ao combustivel, reajustar em 10% o frete
precos = list(map(lambda elemento: round(elemento + 1.10,2), precos))
print(precos)

# Atualizar a LISTA ORIGINAL de Preço
produtos = list(map(lambda elemento: {**elemento, 'Frete': round(elemento['Frete'] + 1.10,2) }, produtos))
print(f'Produtos ordernados novo Fretes: {produtos}')