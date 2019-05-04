from Configuracoes import *
from Tela import *
import pygame
import os


class TelaDeMudancaDeNivel(Tela):
    def __init__(self, game, nomeImagemDeFundo):
        super().__init__(game, nomeImagemDeFundo)

    def comportamentoBotaoProximoNivel(self, game, event):
        pass

    def imprimirMensagemDeCongratulacao(self, game):
        pass

    def run(self):
        pass

    def desenhar(self, game):
        self.desenharTelaBasica(game)
        self.imprimirMensagemDeCongratulacao()

        # desenhar o que faltar

        pygame.display.flip()