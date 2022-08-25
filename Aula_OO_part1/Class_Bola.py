

class Bola:
    def __init__(self, material, formato, tamanho, cor):
        self.material = material
        self.formato = formato
        self.tamanho = tamanho
        self.cor = cor

# Criar um objeto a partir da Classe

futebol = Bola('couro','redonda','40 cm','malhada')
print(futebol.__dict__)
print(futebol.material)

bolaDenteLeite = Bola('borracha','oval','50 cm','colorida')
print(bolaDenteLeite.__dict__)
print(bolaDenteLeite.cor)








