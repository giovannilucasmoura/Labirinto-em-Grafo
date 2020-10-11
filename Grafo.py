from Vertice import *
from Cores import Cor
import sys
import csv

class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices

    def getVertices(self):
        return self.vertices

    def adicionarVertice(self, novoVertice):
        self.vertices.append(novoVertice)

    def encontrarVerticePorPosicao(self, x, y):
        for vertice in self.vertices:
            if vertice.getPosXY()[0] == x and vertice.getPosXY()[1] == y:
                return vertice

    def buscaEmLargura(self, inicio, destino):
        for vertice in self.vertices:
            vertice.cor = Cor.BRANCO
            vertice.distancia = sys.maxsize
            vertice.pai = None

        inicio.cor = Cor.CINZA
        inicio.distancia = 0
        inicio.pai = None

        fronteira = []
        fronteira.append(inicio)

        caminho = []
        while len(fronteira) != 0:
            u = fronteira.pop(0)
            for aresta in u.vizinhos:
                if aresta.destino.getCor() == Cor.BRANCO:
                    aresta.destino.cor = Cor.CINZA
                    aresta.destino.distancia = u.distancia + 1
                    aresta.destino.pai = u
                    fronteira.append(aresta.destino)
                if aresta.destino == destino:
                    verticeAtual = aresta.destino
                    while verticeAtual.pai != None:
                        caminho.append(verticeAtual)
                        verticeAtual = verticeAtual.pai
                    caminho.append(verticeAtual)
                    fronteira = []
                    break
            u.cor = Cor.PRETO

        return caminho[::-1]

    def converterEmMatriz(self, inicio, destino):
        posicoesX = []
        posicoesY = []
        for vert in self.vertices:
            posicoesX.append(vert.getPosXY()[0])
            posicoesY.append(vert.getPosXY()[1])

        xMax = max(posicoesX)
        yMax = max(posicoesY)

        matriz = []
        for i in range(yMax + 1):
            matriz.append([0])
            for x in range(xMax):
                matriz[i].append(0)

        for vert in self.vertices:
            vertPos = vert.getPosXY()
            matriz[vertPos[1]][vertPos[0]] = vert.tipo

        caminho = self.buscaEmLargura(inicio, destino)
        inicio = caminho.pop(len(caminho) - 1)
        destino = caminho.pop(0)

        inicioPos = inicio.getPosXY()
        destinoPos = destino.getPosXY()

        matriz[inicioPos[1]][inicioPos[0]] = 1
        matriz[destinoPos[1]][destinoPos[0]] = 2

        for vert in caminho:
            vertPos = vert.getPosXY()
            matriz[vertPos[1]][vertPos[0]] = 'X'

        return matriz
        
def converterLabirintoEmGrafo(matriz):
    tamanhoY = len(matriz)
    tamanhoX = len(matriz[0])
    vertices = []
    j = 0
    i = 0

    for j in range(tamanhoY):
        for i in range(tamanhoX):
            verticeAux = Vertice("X " + str(i) + " Y " + str(j))
            verticeAux.tipo = matriz[j][i]
            vertices.append(verticeAux)

    for vert in vertices:
        vertX = vert.getPosXY()[0]
        vertY = vert.getPosXY()[1]

        if vert.tipo != -1:
            for viz in vertices:    #viz = Vizinho
                vizX = viz.getPosXY()[0]
                vizY = viz.getPosXY()[1]

                if vertX - 1 == vizX and vertY == vizY and viz.tipo == 0:
                    vert.adicionarAresta(viz)
                elif vertX + 1 == vizX and vertY == vizY and viz.tipo == 0:
                    vert.adicionarAresta(viz)
                elif vertX == vizX and vertY - 1 == vizY and viz.tipo == 0:
                    vert.adicionarAresta(viz)
                elif vertX == vizX and vertY + 1 == vizY and viz.tipo == 0:
                    vert.adicionarAresta(viz)

    return vertices

def converterCSVemMatriz(nomeArquivo):
    matriz = []
    elementos = []
    with open(nomeArquivo) as arquivo:
        leitor = csv.reader(arquivo, delimiter=',')
        for linha in leitor:
            elementos = []
            for elemento in linha:
                elementos.append(int(elemento))
            matriz.append(elementos)

    return matriz

#Função Descontinuada
def printMatriz(matriz):
    print("% ", end = '')
    for i in range(len(matriz[0])):
        print('% ', end = '')
    print('%')

    for linha in matriz:
        print("% ", end = '')
        for vertice in linha:
            if vertice == 'X':
                print("# ", end = '')
            elif vertice == 1:
                print("R ", end = '')
            elif vertice == 2:
                print("Q ", end = '')
            elif vertice == 0:
                print("- ", end = '')
            elif vertice == -1:
                print("x ", end = '')
        print("%")

    print("% ", end = '')
    for i in range(len(matriz[0])):
        print('% ', end = '')
    print('%')

#Função Descontinuada
def ptmtz(matriz):
    for x in matriz:
        print(x)
