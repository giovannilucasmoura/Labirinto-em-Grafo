from Grafo import *
from Vertice import Vertice

matriz = [[0, 0, 0],
          [0, -1, 0],
          [0, -1, 0]]

x =  Grafo(converterLabirintoEmGrafo(matriz))
rato = x.encontrarVerticePorPosicao(0, 2)
queijo = x.encontrarVerticePorPosicao(2, 2)
x.converterEmMatriz(rato, queijo)
#verts = converterLabirintoEmGrafo(matriz)

#exVerts = []
#for vert in verts:
#    vertX = vert.getPosXY()[0]
#    vertY = vert.getPosXY()[1]
#
#    print("X" + str(vertX) + " | Y" + str(vertY) + " | " + str(vert.vizinhos))

#print(x.acharVerticesPorPosicao(2, 0).vizinhos)
#print(x.buscaEmLargura(x.acharVerticesPorPosicao(0, 2), x.acharVerticesPorPosicao(2, 2)))
