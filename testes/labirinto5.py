from Grafo import *
from Vertice import Vertice

matriz = converterCSVemMatriz('labirintos/lab5.csv')

x =  Grafo(converterLabirintoEmGrafo(matriz))
rato = x.encontrarVerticePorPosicao(0, 0)
queijo = x.encontrarVerticePorPosicao(12, 4)
printMatriz(x.converterEmMatriz(rato, queijo))
