from Configuracoes import *
from AdministradorDeAudio import *
import pygame
import os

class Tela:
    def __init__(self, nomeImagemDeFundo):
        self.botaoSom = pygame.image.load(os.path.join('Imagens', 'Sound.png'))
        self.imagemDeFundo = pygame.image.load(os.path.join('Imagens', nomeImagemDeFundo + '.png'))
        self.administradorDeAudio = AdministradorDeAudio()


    def comportamentoBotaoDeAudio(self, game, event):
        pass

    def comportamentoBotaoDeSair(self, game, event):
        pass


    def desenharTelaBasica(self, game):
        game.screen.blit(self.imagemDeFundo, (0, 0))

        # carrega a imagem do botao de audio de acordo com o status de audio do jogo
        if self.comAudio:
            self.botaoSom = pygame.image.load(os.path.join('Imagens', 'Com_Som.png'))
        else:
            self.botaoSom = pygame.image.load(os.path.join('Imagens', 'Sem_Som.png'))
        game.screen.blit(self.botaoSom, (740, 450))



