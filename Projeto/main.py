from TelaDeInicio import *
from TelaDeInstrucoes import *
from TelaDeEscolhaDePersonagem import *
from TelaDeJogo import *
from TelaDePerguntas import *
from TelaResultadoDaPergunta import *
from TelaDeFim import *
from TelaDeMudancaDeNivel import *
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
        self.fps = 100
        pygame.time.set_timer(USEREVENT + 1, 500)

        # initializing constantes do jogo
        self.telaAtual = 'Tela de Jogo' # mudar para tela de inicio quando ela existir
        self.usuarioSaiu = False
        self.comSom = True
        self.tipoJogador = 'N'
        self.nivel = 1

        # inicializando telas
        self.telaDeInicio = TelaDeInicio(self, 'Tela_De_Jogo')
        self.telaDeInstrucoes = TelaDeInstrucoes(self, 'Tela_De_Jogo')
        self.telaDeEscolhaDePersonagem = TelaDeEscolhaDePersonagem(self, 'Tela_De_Jogo')
        self.telaDeJogo = TelaDeJogo(self, 'Tela_De_Jogo')
        self.telaDePerguntas = TelaDePerguntas(self, 'Tela_De_Jogo')
        self.telaResultadoDaPergunta = TelaResultadoDaPergunta(self, 'Tela_De_Jogo')
        self.telaDeFim = TelaDeFim(self, 'Tela_De_Jogo')
        self.telaDeMudancaDeNivel = TelaDeMudancaDeNivel(self, 'Tela_De_Jogo')

    def run(self):
        while not self.usuarioSaiu:
            if self.telaAtual == 'Tela de Inicio':
                self.telaDeInicio.run(self)
            elif self.telaAtual == 'Tela de Intrucoes':
                self.telaDeInstrucoes.run(self)
            elif self.telaAtual == 'Tela de Escolha de Personagens':
                self.telaDeEscolhaDePersonagem.run(self)
            elif self.telaAtual == 'Tela de Jogo':
                self.telaDeJogo.run(self)
            elif self.telaAtual == 'Tela de Perguntas':
                self.telaDePerguntas.run(self)
            elif self.telaAtual == 'Tela Resultado da Pergunta':
                self.telaResultadoDaPergunta.run(self)
            elif self.telaAtual == 'Tela de Fim':
                self.telaDeFim.run(self)
            else:
                self.telaDeMudancaDeNivel.run(self)

        pygame.quit()

game = AdministradorDoJogo()
game.run()

