from Configuracoes import *
import pygame
import os

class TelaDeInicio(Tela):
    def __init__(self, nomeImagemDeFundo):
        super().__init__(nomeImagemDeFundo)

    def comportamentoBotaoDeInstrucoes(self, game):
        pass

    def comportamentoBotaoDeJogar(self, game):
        pass

    def compotamentoBotaoDeEscolherPersonagem(self, game):
        pass

    def run(self, game):
        pass

    def desenhar(self, game):
        self.desenharTelaBasica()

        # desenhar o que faltar

        pygame.display.flip()



