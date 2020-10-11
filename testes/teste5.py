from Grafo import *
from Vertice import Vertice

matriz = converterCSVemMatriz('lab1.csv')

x =  Grafo(converterLabirintoEmGrafo(matriz))
rato = x.encontrarVerticePorPosicao(0, 0)
queijo = x.encontrarVerticePorPosicao(3, 3)
x.converterEmMatriz(rato, queijo)
