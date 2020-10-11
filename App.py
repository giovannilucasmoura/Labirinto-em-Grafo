from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from tkinter import messagebox
from Grafo import *
import pygame

class App:
    labirintoMatriz = []
    posRato = []
    posQueijo = []

    def __init__(self, master):
        frame = Frame(master)
        frame.grid(row = 0, column = 0, sticky = (N, W, E, S))

        self.grupoBotoes = LabelFrame(master, text = "Controle", labelanchor = N)
        self.grupoBotoes.grid(row = 0, column = 0, sticky = (N, S))

        botaoCarregarLabirinto = Button(self.grupoBotoes, text = "Carregar Labirinto", width = 18, command = self.carregarLabirinto)
        botaoCarregarLabirinto.grid(row = 0, column = 0)

        self.botaoInserirPosicoes = Button(self.grupoBotoes, text = "Inserir Posições", width = 18, command = self.janelaPosicoes, state = DISABLED)
        self.botaoInserirPosicoes.grid(row = 1, column = 0)

        self.botaoMostrarCaminho = Button(self.grupoBotoes, text = "Mostrar Caminho", width = 18, command = self.mostrarCaminho, state = DISABLED)
        self.botaoMostrarCaminho.grid(row = 2, column = 0)

        grupoInformacoes = LabelFrame(master, text = "Informações", labelanchor = N)
        grupoInformacoes.grid(row = 0, column = 1, sticky = (N, S))

        self.labirintoCarregado = StringVar()
        textoLabirintoCarregado = Label(grupoInformacoes, textvariable = self.labirintoCarregado, width = 25)
        textoLabirintoCarregado.grid(row = 0, column = 0, sticky = (N, S))
        self.labirintoCarregado.set("Labirinto - Não Carregado")

        self.labirintoTamanho = StringVar()
        textoLabirintoTamanho = Label(grupoInformacoes, textvariable = self.labirintoTamanho, width = 25)
        textoLabirintoTamanho.grid(row = 1, column = 0, sticky = (N, S))

        self.stringPosicaoRato = StringVar()
        self.stringPosicaoRato.set("Posição do Rato: N/A")
        self.textoPosicaoRato = Label(grupoInformacoes, textvariable = self.stringPosicaoRato, width = 25)
        self.textoPosicaoRato.grid(row = 2, column = 0, sticky = (N, S))

        self.stringPosicaoQueijo = StringVar()
        self.stringPosicaoQueijo.set("Posição do Queijo: N/A")
        self.textoPosicaoQueijo = Label(grupoInformacoes, textvariable = self.stringPosicaoQueijo, width = 25)
        self.textoPosicaoQueijo.grid(row = 3, column = 0, sticky = (N, S))

    def carregarLabirinto(self):
        arquivo = filedialog.askopenfilename(title = "Selecione um arquivo:", defaultextension = ".csv")

        matriz = converterCSVemMatriz(arquivo)
        erro = 0

        tamanhoX = len(matriz[0])
        for x in matriz:
            if len(x) != tamanhoX:
                erro = 1

        for linha in matriz:
            for valor in linha:
                if valor != 0 and valor != -1:
                    erro = 2

        if erro == 0:
            self.labirintoMatriz = matriz
        elif erro == 1:
            messagebox.showinfo("Erro", "Todas as linhas do labirinto devem ter o mesmo tamanho.")
        elif erro == 2:
            messagebox.showinfo("Erro", "Os valores do labirinto tem que ser 0 ou -1.")
        self.posRato = []
        self.posQueijo = []
        self.atualizarInformacoes()


    def janelaPosicoes(self):
        if len(self.labirintoMatriz) == 0:
            messagebox.showinfo("Erro", "Labirinto Inválido, carregue outro.")
        else:
            janela = Toplevel(None)
            janela.title("Inserção")

            textoInfo = Message(janela, text = "Insira as posições X e Y: ", width = 150)
            textoInfo.grid(row = 0, column = 0, columnspan = 3, sticky = (E, W))

            textoInfo2 = Message(janela, text = "OBS: X e Y começam de (1, 1) no canto superior esquerdo do labirinto.", width = 150)
            textoInfo2.grid(row = 1, column = 0, columnspan = 3, sticky = (E, W))

            textoInfo2 = Message(janela, text = "X            Y")
            textoInfo2.grid(row = 2, column = 1, columnspan = 2, sticky = (E, W))

            textoRato = Message(janela, text = "Rato: ")
            textoRato.grid(row = 3, column = 0, sticky = (E, W))

            entradaRatoX = Entry(janela, width = 5)
            entradaRatoX.grid(row = 3, column = 1, sticky = (E, W))
            entradaRatoY = Entry(janela, width = 5)
            entradaRatoY.grid(row = 3, column = 2, sticky = (E, W))

            textoQueijo = Message(janela, text = "Queijo: ")
            textoQueijo.grid(row = 4, column = 0, sticky = (E, W))

            entradaQueijoX = Entry(janela, width = 5)
            entradaQueijoX.grid(row = 4, column = 1, sticky = (E, W))
            entradaQueijoY = Entry(janela, width = 5)
            entradaQueijoY.grid(row = 4, column = 2, sticky = (E, W))

            botaoInserir = Button(janela, text = "Inserir", command = lambda: self.inserirPosicoes(entradaRatoX.get(), entradaRatoY.get(), entradaQueijoX.get(), entradaQueijoY.get()))

            botaoInserir.grid(row = 5, column = 0, columnspan = 3, sticky = (E, W))


    def inserirPosicoes(self, ratoX, ratoY, queijoX, queijoY):
        erro = 0

        try:
            ratoX = int(ratoX)
            ratoY = int(ratoY)
            queijoX = int(queijoX)
            queijoY = int(queijoY)

            if ratoX > len(self.labirintoMatriz[0]) or ratoY > len(self.labirintoMatriz):
                erro = 1
            elif queijoX > len(self.labirintoMatriz[0]) or queijoY > len(self.labirintoMatriz):
                erro = 1
            elif ratoX < 1 or ratoY < 1 or queijoX < 1 or queijoY < 1:
                erro = 1
            elif self.labirintoMatriz[ratoY - 1][ratoX - 1] == -1:
                erro = 2
            elif self.labirintoMatriz[queijoY - 1][queijoX - 1] == -1:
                erro = 3
            elif ratoX == queijoX and ratoY == queijoY:
                erro = 4

            if erro == 0:
                messagebox.showinfo("Sucesso!", "Valores inseridos com sucesso.")
                self.posRato = [ratoX - 1, ratoY - 1]
                self.posQueijo = [queijoX - 1, queijoY - 1]
            elif erro == 1:
                messagebox.showinfo("Erro", "Um ou mais dos valores é inválido.")
            elif erro == 2:
                messagebox.showinfo("Erro", "O rato está dentro de uma parede.")
            elif erro == 3:
                messagebox.showinfo("Erro", "O queijo está dentro de uma parede.")
            elif erro == 4:
                messagebox.showinfo("Erro", "O rato e o queijo estão na mesma posição.")
            else:
                messagebox.showinfo("Erro")
            self.atualizarInformacoes()
        except:
            messagebox.showinfo("Erro", "Um ou mais dos valores é inválido.")

    def mostrarCaminho(self):
        grafo = Grafo(converterLabirintoEmGrafo(self.labirintoMatriz))
        rato = grafo.encontrarVerticePorPosicao(self.posRato[0], self.posRato[1])
        queijo = grafo.encontrarVerticePorPosicao(self.posQueijo[0], self.posQueijo[1])
        caminho = grafo.buscaEmLargura(rato, queijo)
        if len(caminho) == 0:
            messagebox.showinfo("Erro", "O rato não tem como chegar no queijo.")
        else:
            caminhoDesenhar = []
            delayAnimacao = 250
            tamanhoCubo = 32
            pygame.init()

            PAREDE    =  (0, 0, 0)
            FUNDO    =  (255, 255, 255)
            RATO     =  (185, 125, 50)
            QUEIJO   =  (255, 255, 0)
            CAMINHO  =  (150, 150, 150)
            LINHA    =  (150, 150, 150)

            loop = True
            size = (len(self.labirintoMatriz[0]) * tamanhoCubo + (tamanhoCubo * 2), len(self.labirintoMatriz) * tamanhoCubo + (tamanhoCubo * 2))
            tela = pygame.display.set_mode(size)
            pygame.display.set_caption("Demonstração do Caminho")

            clock = pygame.time.Clock()
            tickAtual = pygame.time.get_ticks()
            tickTroca = tickAtual + delayAnimacao
            iAnimacao = 1
            loop = True

            while loop:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        loop = False

                tela.fill(FUNDO)
                for y in range(len(self.labirintoMatriz)):
                    for x in range(len(self.labirintoMatriz[0])):
                        if self.labirintoMatriz[y][x] == -1:
                            pygame.draw.rect(tela, PAREDE, [tamanhoCubo + (x * tamanhoCubo), tamanhoCubo + (y * tamanhoCubo), tamanhoCubo, tamanhoCubo], 0)
                        else:
                            pygame.draw.rect(tela, FUNDO, [tamanhoCubo + (x * tamanhoCubo), tamanhoCubo + (y * tamanhoCubo), tamanhoCubo, tamanhoCubo], 0)

                for i in range(len(caminhoDesenhar)):
                    posCaminho = caminhoDesenhar[i].getPosXY()
                    pygame.draw.rect(tela, LINHA, [tamanhoCubo + (posCaminho[0] * tamanhoCubo), tamanhoCubo + (posCaminho[1] * tamanhoCubo), tamanhoCubo, tamanhoCubo], 0)

                tickAtual = pygame.time.get_ticks()
                if tickAtual > tickTroca:
                    tickTroca = tickAtual + delayAnimacao
                    caminhoDesenhar.append(caminho[iAnimacao])
                    iAnimacao += 1
                    if iAnimacao == len(caminho):
                        iAnimacao = 1
                        caminhoDesenhar = []

                pygame.draw.rect(tela, RATO, [tamanhoCubo + (rato.getPosXY()[0] * tamanhoCubo), tamanhoCubo + (rato.getPosXY()[1] * tamanhoCubo), tamanhoCubo, tamanhoCubo], 0)
                pygame.draw.rect(tela, QUEIJO, [tamanhoCubo + (queijo.getPosXY()[0] * tamanhoCubo), tamanhoCubo + (queijo.getPosXY()[1] * tamanhoCubo), tamanhoCubo, tamanhoCubo], 0)

                for i in range(0, len(self.labirintoMatriz[0]) + 1):
                    pygame.draw.line(tela, LINHA, [(i * tamanhoCubo) + tamanhoCubo, tamanhoCubo], [(i * tamanhoCubo) + tamanhoCubo, (len(self.labirintoMatriz) + 1) * tamanhoCubo], 1)

                for i in range(0, len(self.labirintoMatriz) + 1):
                    pygame.draw.line(tela, LINHA, [tamanhoCubo, (i * tamanhoCubo) + tamanhoCubo], [(len(self.labirintoMatriz[0]) + 1) * tamanhoCubo, (i * tamanhoCubo) + tamanhoCubo], 1)
                pygame.display.flip()

                clock.tick(60)
            pygame.quit()

    def atualizarInformacoes(self):
        if len(self.labirintoMatriz) > 0:
            self.botaoInserirPosicoes.config(state = NORMAL)
            if self.posRato != [] and self.posQueijo != []:
                self.botaoMostrarCaminho.config(state = NORMAL)
            self.labirintoCarregado.set("Labirinto - Carregado")
            self.labirintoTamanho.set("Tamanho - "+ str(len(self.labirintoMatriz[0])) + " por " + str(len(self.labirintoMatriz)))

        if len(self.posRato) > 0 and len(self.posQueijo) > 0:
            self.stringPosicaoRato.set("Posição do Rato: ("+ str(self.posRato[0] + 1) + ", " + str(self.posRato[1] + 1) + ")")
            self.stringPosicaoQueijo.set("Posição do Queijo: ("+ str(self.posQueijo[0] + 1) + ", " + str(self.posQueijo[1] + 1) + ")")
