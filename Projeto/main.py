from TelaDeInicio import *
from TelaDeInstrucoes import *
from TelaDeJogo import *
from TelaDePerguntas import *
from TelaResultadoDaPergunta import *
from TelaDeFim import *
from Configuracoes import *
import pygame

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
        pygame.time.set_timer(USEREVENT + 1, 500)


        # initializing constantes do jogo
        self.telaAtual = 'Tela de Inicio'
        self.usuarioSaiu = False
        self.comAudio = True


        # inicializando telas
        self.telaDeInicio = TelaDeInicio()
        self.telaDeInstrucoes = TelaDeInstrucoes()
        self.telaDeJogo = TelaDeJogo(self)
        self.telaDePerguntas = TelaDePerguntas()
        self.telaResultadoDaPergunta = TelaResultadoDaPergunta()
        self.telaDeFim = TelaDeFim()


    def run(self):

        while not self.usuarioSaiu:
            if self.telaAtual == 'Tela de Inicio':
                self.telaDeInicio.run(self)
            elif self.telaAtual == 'Tela de Instrucoes':
                self.telaDeInstrucoes.run(self)
            elif self.telaAtual == 'Tela de Jogo':
                self.telaDeJogo.run(self)
            elif self.telaAtual == 'Tela de Perguntas':
                self.telaDePerguntas.run(self)
            elif self.telaAtual == 'Tela Resultado da Pergunta':
                self.telaResultadoDaPergunta.run(self)
            else:
                self.telaDeFim.run(self)

        pygame.quit()


game = AdministradorDoJogo()
game.run()