from Cores import Cor
from Aresta import Aresta

class Vertice:
    def __init__(self, nome):
        self.nome = nome
        self.tipo = None
        self.distancia = None
        self.vizinhos = []
        self.pai = None
        self.cor = Cor.BRANCO

    def __repr__(self):
        return "Vertice %s" % (self.nome)

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getTipo(self):
        return self.tipo

    def setTipo(self, tipo):
        self.tipo = tipo

    def getVizinhos(self):
        return self.vizinhos

    def setVizinhos(self, listaVizinhos):
        self.vizinhos = listaVizinhos

    def getPai(self):
        return self.pai

    def setPai(self, novoPai):
        self.pai = novoPai

    def adicionarAresta(self, destino):
        novaAresta = Aresta(destino)

        self.vizinhos.append(novaAresta)

    def getCor(self):
        return self.cor

    def setCor(self, novaCor):
        self.cor = novaCor

    def getPosXY(self):
        posX = [int(pos) for pos in self.nome.split() if pos.isdigit()][0]
        posY = [int(pos) for pos in self.nome.split() if pos.isdigit()][1]

        return posX, posY
