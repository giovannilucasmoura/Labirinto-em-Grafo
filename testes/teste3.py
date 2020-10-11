from Grafo import *
from Vertice import Vertice

matriz = [[0, -1, 0, 0, 0, -1, 0],
          [0, -1, 0, -1, 0, -1, 0],
          [0, 0, 0, -1, 0, 0, 0]]

x =  Grafo(converterLabirintoEmGrafo(matriz))
rato = x.encontrarVerticePorPosicao(0, 0)
queijo = x.encontrarVerticePorPosicao(6, 0)
x.converterEmMatriz(rato, queijo)

#print(x.buscaEmLargura(x.acharVerticesPorPosicao(0, 0), x.acharVerticesPorPosicao(6, 0)))
