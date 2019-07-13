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
        self.tela = 0
        self.usuarioSaiu = False
        self.comAudio = True


    def run(self):

        while not self.usuarioSaiu:
            if self.telaAtual == 'Tela de Inicio':
                self.tela = TelaDeInicio()
            elif self.telaAtual == 'Tela de Instrucoes':
                self.tela = TelaDeInstrucoes()
            elif self.telaAtual == 'Tela de Jogo':
                self.tela = TelaDeJogo(self)
            elif self.telaAtual == 'Tela de Perguntas':
                self.tela = TelaDePerguntas()
            elif self.telaAtual == 'Tela Resultado da Pergunta':
                self.tela = TelaResultadoDaPergunta()
            else:
                self.tela = TelaDeFim()

            self.tela.run(self)

        pygame.quit()


game = AdministradorDoJogo()
game.run()