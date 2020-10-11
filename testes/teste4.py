from Grafo import *
from Vertice import Vertice

matriz = [[0, 0, 0, -1, -1, -1, -1],
          [0, -1, 0, -1, -1, -1, -1],
          [0, -1, 0, -1, -1, -1, -1],
          [0, -1, 0, -1, -1, -1, -1],
          [0, -1, 0, 0, 0, 0, 0],
          [0, -1, -1, -1, -1, -1, 0],
          [0, -1, -1, -1, -1, -1, 0]]


x =  Grafo(converterLabirintoEmGrafo(matriz))
rato = x.encontrarVerticePorPosicao(0, 0)
queijo = x.encontrarVerticePorPosicao(6, 6)
x.converterEmMatriz(rato, queijo)
