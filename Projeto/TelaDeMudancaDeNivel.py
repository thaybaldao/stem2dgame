from Configuracoes import *
from Tela import *
import pygame
import os


class TelaDeMudancaDeNivel(Tela):
    def __init__(self, nomeImagemDeFundo):
        super().__init__(nomeImagemDeFundo)

    def comportamentoBotaoProximoNivel(self, game, event):
        pass

    def imprimirMensagemDeCongratulacao(self, game):
        pass

    def run(self):
        pass

    def desenhar(self, game):
        self.desenharTelaBasica()
        self.imprimirMensagemDeCongratulacao()

        # desenhar o que faltar

        pygame.display.flip()