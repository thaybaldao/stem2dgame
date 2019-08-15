from TelaDeInicio import *
from TelaDeInstrucoes import *
from TelaDeJogo import *
from TelaDePerguntas import *
from TelaResultadoDaPergunta import *
from TelaDeFim import *
from Configuracoes import *
from AdministradorDeAudio import *
from Jogador import *
import pygame
import random

class AdministradorDoJogo:
    def __init__(self):
        # inicializando pygame
        pygame.init()

        # criando a janela do jogo
        self.janela = pygame.display.set_mode((LARGURA_DA_TELA, ALTURA_DA_TELA))
        pygame.display.set_caption(TITULO)

        # criando o relogio do jogo
        self.clock = pygame.time.Clock()
        self.fps = FPS

        # inicializando constantes do jogo
        self.telaAtual = 'Tela de Inicio'
        self.ultimaTela = 'Tela de Inicio'
        self.tela = 0
        self.usuarioSaiu = False
        self.comAudio = True
        self.melhorPontuacao = 0

        self.administradorDeAudio = AdministradorDeAudio()

        self.obstaculos = []
        self.inimigos = []
        self.vidas = []
        self.impulsionadores = []
        self.tiros = []
        self.tirosInimigo = []

        self.perguntas = []
        self.alternativaA = []
        self.alternativaB = []
        self.alternativaC = []
        self.alternativaD = []
        self.respostas = []
        self.i = 0

        self.inserirPerguntas()

        self.novoJogo()

    # metodo para declarar todas as perguntas do jogo
    def inserirPerguntas(self):
        # pergunta 1
        self.perguntas.append("Quem foi Ada Lovelace?")
        self.alternativaA.append("Engenheira")
        self.alternativaB.append("Primeira programadora do mundo")
        self.alternativaC.append("Matematica")
        self.alternativaD.append("Descobridora do DNA")
        self.respostas.append('B')

        # pergunta 2
        self.perguntas.append("Quem foi Marie Curie?")
        self.alternativaA.append("Engenheira da NASA")
        self.alternativaB.append("Primeira matematica do mundo")
        self.alternativaC.append("Descobridora do Radio")
        self.alternativaD.append("Fundadora do ITA")
        self.respostas.append('C')

        # pergunta 3
        self.perguntas.append("Qual a maior contribuicao cientifica de Rosalind Franklin?")
        self.alternativaA.append("Descobriu o Radio")
        self.alternativaB.append("Descoberta do DNA")
        self.alternativaC.append("Engenheira chefe da NASA")
        self.alternativaD.append("Inventou o numero pi")
        self.respostas.append('B')

        # pergunta 4
        self.perguntas.append("Qual o maior feito de Margareth Hamilton?")
        self.alternativaA.append("Descobridora do Radio")
        self.alternativaB.append("Descoberta do DNA")
        self.alternativaC.append("Liderou o projeto Apollo 11")
        self.alternativaD.append("Inventou o numero pi")
        self.respostas.append('C')

    def retirarPergunta(self):
        self.perguntas.pop(self.i)
        self.alternativaA.pop(self.i)
        self.alternativaB.pop(self.i)
        self.alternativaC.pop(self.i)
        self.alternativaD.pop(self.i)
        self.respostas.pop(self.i)

        if len(self.perguntas) == 0:
            self.inserirPerguntas()

    # esse metodo inicializa as constantes do jogo a cada novo jogo
    def novoJogo(self):
        self.pontuacao = 0
        self.aparecimentoElementos = 50
        self.vidasExtras = 3
        self.ehInvencivel = False
        self.respostaCorreta = 0
        self.respostaUsuario = 0
        self.tempoDeInvencibilidade = 15
        self.dvel = 0
        self.jogador = Jogador(self)
        self.obstaculos.clear()
        self.inimigos.clear()
        self.vidas.clear()
        self.impulsionadores.clear()
        self.tiros.clear()
        self.tirosInimigo.clear()

    # metodo que executa o jogo, alternando entre as telas do jogo, de acordo com os comandos do usuario
    def run(self):
        while not self.usuarioSaiu:
            if self.telaAtual == 'Tela de Inicio':
                self.tela = TelaDeInicio(self)
            elif self.telaAtual == 'Tela de Instrucoes':
                self.tela = TelaDeInstrucoes()
            elif self.telaAtual == 'Tela de Jogo':
                self.tela = TelaDeJogo(self)
            elif self.telaAtual == 'Tela de Perguntas':
                self.tela = TelaDePerguntas(self)
            elif self.telaAtual == 'Tela Resultado da Pergunta':
                self.tela = TelaResultadoDaPergunta()
            else:
                self.tela = TelaDeFim(self)

            self.tela.run(self)

        pygame.quit()


game = AdministradorDoJogo()
game.run()