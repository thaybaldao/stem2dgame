from Configuracoes import *
from Tela import *
import pygame
import os


class TelaResultadoDaPergunta(Tela):
    def __init__(self, nomeImagemDeFundo):
        super().__init__(nomeImagemDeFundo)

    def imprimirResultadoPergunta(self, game):
        pass

    def run(self):
        # fazer a tela rodar por um intervalo de tempo suficiente para se poder ler o resultado
        pass

    def desenhar(self, game):
        self.desenharTelaBasica()
        self.imprimirResultadoPergunta()
        pygame.display.flip()