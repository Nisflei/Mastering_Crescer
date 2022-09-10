# carregando dados do Excel...!!!

import pandas as pd
print('>> Carregando o Excell')

tabela_excel = pd.read_excel('janeiro.xlsx')

print(tabela_excel)