from Grafo import *
from Vertice import Vertice

matriz = converterCSVemMatriz('labirintos/lab2.csv')

x =  Grafo(converterLabirintoEmGrafo(matriz))
rato = x.encontrarVerticePorPosicao(0, 0)
queijo = x.encontrarVerticePorPosicao(3, 3)
printMatriz(x.converterEmMatriz(rato, queijo))
