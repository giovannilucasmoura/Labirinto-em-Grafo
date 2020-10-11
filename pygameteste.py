from Grafo import *
from Vertice import Vertice
import pygame

matriz = converterCSVemMatriz('labirintos/lab4.csv')
grafo = Grafo(converterLabirintoEmGrafo(matriz))
rato = grafo.encontrarVerticePorPosicao(0, 0)
queijo = grafo.encontrarVerticePorPosicao(6, 0)
caminho = grafo.buscaEmLargura(rato, queijo)
caminhoDesenhar = []
delayAnimacao = 250
tamanhoCubo = 32
pygame.init()

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)
AMARELO = (255, 255, 0)
VERMELHO = (255, 140, 140)
CINZA = (150, 150, 150)

loop = True
size = (len(matriz[0]) * tamanhoCubo + (tamanhoCubo * 2), len(matriz) * tamanhoCubo + (tamanhoCubo * 2))
tela = pygame.display.set_mode(size)
pygame.display.set_caption("TESTE LABIRINTO")

clock = pygame.time.Clock()
tickAtual = pygame.time.get_ticks()
tickTroca = tickAtual + delayAnimacao
iAnimacao = 1
loop = True

while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              loop = False

    tela.fill(BRANCO)
    for y in range(len(matriz)):
        for x in range(len(matriz[0])):
            if matriz[y][x] == -1:
                pygame.draw.rect(tela, PRETO, [tamanhoCubo + (x * tamanhoCubo), tamanhoCubo + (y * tamanhoCubo), tamanhoCubo, tamanhoCubo], 0)
            else:
                pygame.draw.rect(tela, BRANCO, [tamanhoCubo + (x * tamanhoCubo), tamanhoCubo + (y * tamanhoCubo), tamanhoCubo, tamanhoCubo], 0)

    for i in range(len(caminhoDesenhar)):
        posCaminho = caminhoDesenhar[i].getPosXY()
        pygame.draw.rect(tela, VERMELHO, [tamanhoCubo + (posCaminho[0] * tamanhoCubo), tamanhoCubo + (posCaminho[1] * tamanhoCubo), tamanhoCubo, tamanhoCubo], 0)

    tickAtual = pygame.time.get_ticks()
    if tickAtual > tickTroca:
        print(iAnimacao)
        tickTroca = tickAtual + delayAnimacao
        caminhoDesenhar.append(caminho[iAnimacao])
        iAnimacao += 1
        if iAnimacao == len(caminho):
            iAnimacao = 1
            caminhoDesenhar = []

    pygame.draw.rect(tela, VERDE, [tamanhoCubo + (rato.getPosXY()[0] * tamanhoCubo), tamanhoCubo + (rato.getPosXY()[1] * tamanhoCubo), tamanhoCubo, tamanhoCubo], 0)
    pygame.draw.rect(tela, AMARELO, [tamanhoCubo + (queijo.getPosXY()[0] * tamanhoCubo), tamanhoCubo + (queijo.getPosXY()[1] * tamanhoCubo), tamanhoCubo, tamanhoCubo], 0)

    for i in range(0, len(matriz[0]) + 1):
        pygame.draw.line(tela, CINZA, [(i * tamanhoCubo) + tamanhoCubo, tamanhoCubo], [(i * tamanhoCubo) + tamanhoCubo, (len(matriz) + 1) * tamanhoCubo], 1)

    for i in range(0, len(matriz) + 1):
        pygame.draw.line(tela, CINZA, [tamanhoCubo, (i * tamanhoCubo) + tamanhoCubo], [(len(matriz[0]) + 1) * tamanhoCubo, (i * tamanhoCubo) + tamanhoCubo], 1)
    pygame.display.flip()


    clock.tick(60)
