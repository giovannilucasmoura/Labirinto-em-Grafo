class Aresta:
    def __init__(self, destino):
        self.destino = destino

    def __repr__(self):
        return 'Aresta para %s' % (self.destino)

    def getDestino(self):
        return self.destino

    def setDestino(self, novoDestino):
        self.destino = novoDestino
