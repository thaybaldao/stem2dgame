import pygame
import os
from Configuracoes import *

# um objeto desta classe eh criado em todas as telas, de forma que para chamar os metodos dessa classe basta chamar dentro de uma tela: administradorDeAudio.nomeDoMetodo
class AdministradorDeAudio():
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.set_num_channels(2)


    def tocarMusicaDeFundo(self, musica, game):
        # lembrar de checar se o jogo esta com audio ou nao
        # usar 1 channel para a musica de fundo e outro para os efeitos sonoros
        pygame.mixer.Channel(0).play(pygame.mixer.Sound(musica), -1, fade_ms=200)


    def tocarEfeitoSonoro(self, efeito, game):
        # lembrar de checar se o jogo esta com audio ou nao
        # usar 1 channel para a musica de fundo e outro para os efeitos sonoros
        pygame.mixer.Channel(0).set_volume(0.3)
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(efeito), 0)
        pygame.mixer.Channel(0).set_volume(1)