from Configuracoes import *
from Tela import *
import pygame
import os


class TelaDePerguntas(Tela):
    def __init__(self, nomeImagemDeFundo):
        super().__init__(nomeImagemDeFundo)

    def imprimirPergunta(self, game):
        pass

    def imprimirAlternativas(self, game):
        pass

    def comportamentoBotaoAlternativaA(self, game, event):
        pass

    def comportamentoBotaoAlternativaB(self, game, event):
        pass

    def comportamentoBotaoAlternativaC(self, game, event):
        pass

    def comportamentoBotaoAlternativaD(self, game, event):
        pass

    def run(self):
        pass

    def desenhar(self, game):
        self.desenharTelaBasica()
        self.imprimirPergunta()
        self.imprimirAlternativas()

        # desenhar o que faltar

        pygame.display.flip()