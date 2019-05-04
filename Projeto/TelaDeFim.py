from Configuracoes import *
from Tela import *
import pygame
import os


class TelaDeFim(Tela):
    def __init__(self, nomeImagemDeFundo):
        super().__init__(nomeImagemDeFundo)

    def comportamentoBotaoDeReplay(self, game, event):
        pass

    def imprimirScore(self, game):
        pass

    def imprimirMaiorScore(self, game):
        pass

    def run(self, game):
        pass

    def desenhar(self, game):
        self.desenharTelaBasica(game)
        self.imprimirScore(game)
        self.imprimirMaiorScore(game)

        # desenhar o que faltar

        pygame.display.flip()



