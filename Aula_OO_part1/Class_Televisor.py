

class Televisor:
    def __init__(self, fabricante, modelo, canal, volume):
        self.fabricante = fabricante
        self.modelo = modelo
        self.canal = canal
        self.volume = volume
        self.listaCanal = []

    # Metodos (Funcionalidades)

    def aumentarVolume(self, valor):
        if (self.volume + valor) > 100:
            print(f'Volume MAXIMO 100')
            self.volume = 100
        else:
            self.volume = self.volume + valor

    def diminuirVolume(self, valor):
        self.volume = self.volume - valor

    def status(self):
        print(f'TV: {self.modelo} - Canal Atual: {self.canal} - Volume: {self.volume}')

    def sintonizarCanal(self, canal):
        if canal not in self.listaCanal:
            self.listaCanal.append(canal)

    def trocarCanal(self,novoCanal):
        if novoCanal in self.listaCanal:
            self.canal = novoCanal
        else:
            print(f'Canal INVALIDO {novoCanal}')


# Usando o Televisor com controle Remoto

salaTV = Televisor('LG','smartTV',500,10)

print(salaTV.__dict__)
salaTV.aumentarVolume(5)
print(salaTV.volume)
print(salaTV.__dict__)
salaTV.diminuirVolume(3)
salaTV.status()

# validando o controle do Volume
salaTV.aumentarVolume(50)
salaTV.status()
salaTV.aumentarVolume(50)
salaTV.status()
salaTV.aumentarVolume(10)
salaTV.status()

# Controlando os Canais
salaTV.sintonizarCanal(500)
salaTV.sintonizarCanal(600)
salaTV.trocarCanal(100)
print(salaTV.__dict__)
salaTV.trocarCanal(600)
print(salaTV.__dict__)

#Resolvendo problema de mesmo canal
salaTV.sintonizarCanal(500)
salaTV.sintonizarCanal(500)
salaTV.sintonizarCanal(500)
print(salaTV.__dict__)

