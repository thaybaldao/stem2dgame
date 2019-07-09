from Configuracoes import *
from AdministradorDeAudio import *
import pygame
import os

class Tela:
    def __init__(self, game, nomeImagemDeFundo):
        self.imagemDeFundo = pygame.image.load(os.path.join('Imagens', nomeImagemDeFundo + '.png'))
        self.administradorDeAudio = AdministradorDeAudio() # sempre que uma tela precisar utilizar algum som, basta chamar este objeto e algum metodo de sua classe


    # metodo para lidar com interacoes com o botao de audio
    # pode ser utilizado em qualquer tela
    def comportamentoBotaoDeAudio(self, game, evento, pos):
        if evento.type == pygame.MOUSEBUTTONDOWN and pos[0] > 740 and pos[0] < 785 and pos[1] > 450 and pos[1] < 495 or pygame.key.get_pressed()[pygame.K_m]:
            if game.comAudio:
                game.comAudio = False
            else:
                game.comAudio = True

    # metodo para lidar com interacoes com o botao de sair
    # pode ser utilizado em qualquer tela
    def comportamentoBotaoDeSair(self, game, evento):
        if evento.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            game.usuarioSaiu = True


    # desenha os elementos comuns a toda a tela, isto eh, o background e o botao de audio
    def desenharTelaBasica(self, game):
        # carrega o background da tela
        game.janela.blit(self.imagemDeFundo, (0, 0))

        # carrega a imagem do botao de audio de acordo com o status de audio do jogo
        if game.comAudio:
            self.botaoSom = pygame.image.load(os.path.join('Imagens', 'audio_ligado.png'))
        else:
            self.botaoSom = pygame.image.load(os.path.join('Imagens', 'audio_desligado.png'))
        game.janela.blit(self.botaoSom, (740, 450))



