from Configuracoes import *
from Tela import *
import pygame
import os

class TelaDeInicio(Tela):
    def __init__(self, game, nomeImagemDeFundo):
        super().__init__(game, nomeImagemDeFundo)

    def comportamentoBotaoDeInstrucoes(self, game):
        pass

    def comportamentoBotaoDeJogar(self, game):
        pass

    def compotamentoBotaoDeEscolherPersonagem(self, game):
        pass

    def run(self, game):
        pass

    def desenhar(self, game):
        self.desenharTelaBasica(game)

        # desenhar o que faltar

        pygame.display.flip()



