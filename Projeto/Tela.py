from Configuracoes import *
from AdministradorDeAudio import *
import pygame
import os

class Tela:
    def __init__(self, game, nomeImagemDeFundo):
        self.imagemDeFundo = pygame.image.load(os.path.join('Imagens', nomeImagemDeFundo + '.png'))
        self.administradorDeAudio = AdministradorDeAudio()


    def comportamentoBotaoDeAudio(self, game, evento, pos):
        if evento.type == pygame.MOUSEBUTTONDOWN and pos[0] > 740 and pos[0] < 785 and pos[1] > 450 and pos[1] < 495 or pygame.key.get_pressed()[pygame.K_m]:
            if game.comAudio:
                game.comAudio = False
            else:
                game.comAudio = True


    def comportamentoBotaoDeSair(self, game, evento):
        if evento.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            game.usuarioSaiu = True


    def desenharTelaBasica(self, game):
        game.janela.blit(self.imagemDeFundo, (0, 0))

        # carrega a imagem do botao de audio de acordo com o status de audio do jogo
        if game.comAudio:
            self.botaoSom = pygame.image.load(os.path.join('Imagens', 'Com_Som.png'))
        else:
            self.botaoSom = pygame.image.load(os.path.join('Imagens', 'Sem_Som.png'))
        game.janela.blit(self.botaoSom, (740, 450))



