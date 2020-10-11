from Grafo import *
from Vertice import Vertice

matriz = converterCSVemMatriz('labirintos/lab1.csv')

x =  Grafo(converterLabirintoEmGrafo(matriz))
rato = x.encontrarVerticePorPosicao(10, 5)
queijo = x.encontrarVerticePorPosicao(1, 0)
printMatriz(x.converterEmMatriz(rato, queijo))
