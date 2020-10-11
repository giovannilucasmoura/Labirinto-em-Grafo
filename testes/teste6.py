from Grafo import *
from Vertice import Vertice

matriz = converterCSVemMatriz('lab2.csv')

x =  Grafo(converterLabirintoEmGrafo(matriz))
rato = x.encontrarVerticePorPosicao(0, 0)
queijo = x.encontrarVerticePorPosicao(5, 0)
x.converterEmMatriz(rato, queijo)
