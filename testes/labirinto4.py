from Grafo import *
from Vertice import Vertice

matriz = converterCSVemMatriz('labirintos/lab4.csv')

x =  Grafo(converterLabirintoEmGrafo(matriz))
rato = x.encontrarVerticePorPosicao(0, 0)
queijo = x.encontrarVerticePorPosicao(6, 0)
printMatriz(x.converterEmMatriz(rato, queijo))
