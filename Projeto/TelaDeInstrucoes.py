from Configuracoes import *
from Tela import *
import pygame
import os


class TelaDeInstrucoes(Tela):
    def __init__(self, nomeImagemDeFundo):
        super().__init__(nomeImagemDeFundo)

    def comportamentoBotaoPlay(self, game, event):
        pass

    def comportamentoBotaoVoltarTelaInicio(self, game):
        pass

    def imprimirInstrucoes(self, game):
        pass

    def desenhar(self, game):
        self.desenharTelaBasica()
        self.imprimirInstrucoes()

        # desenhar o que faltar

        pygame.display.flip()
