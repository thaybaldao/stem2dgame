from Configuracoes import *
from Tela import *
import pygame
import os


class TelaDeEscolhaDePersonagem(Tela):
    def __init__(self, nomeImagemDeFundo):
        super().__init__(nomeImagemDeFundo)

    def imprimirDescricaoDosPersonagens(self, game, event):
        pass

    def desenharPersonagens(self, game, event):
        pass

    def comportamentoBotaoEscolhaPesonagemA(self, game, event):
        # atualizar a string game.tipoJogador com 'A' caso o usuario selecione este personagem
        pass

    def comportamentoBotaoEscolhaPesonagemB(self, game, event):
        # atualizar a string game.tipoJogador com 'B' caso o usuario selecione este personagem
        pass

    def comportamentoBotaoEscolhaPesonagemC(self, game, event):
        # atualizar a string game.tipoJogador com 'C' caso o usuario selecione este personagem
        pass

    def comportamentoBotaoEscolhaPesonagemD(self, game, event):
        # atualizar a string game.tipoJogador com 'D' caso o usuario selecione este personagem
        pass

    def run(self, game):
        pass

    def desenhar(self, game):
        self.desenharTelaBasica()
        self.desenharPersonagens()
        self.imprimirDescricaoDosPersonagens()

        # desenhar o que faltar

        pygame.display.flip()