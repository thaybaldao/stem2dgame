import pygame
from Configuracoes import *

# um objeto desta classe, denominado administradorDeAudio, esta disponivel em todas as telas, de modo que para chamar
# os metodos dessa classe basta chamar dentro de uma tela: administradorDeAudio.nomeDoMetodo
class AdministradorDeAudio():
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.set_num_channels(2)

    def tocarMusicaDeFundo(self, musica, game):
        # lembrar de checar se o jogo esta com audio ou nao
        # usar 1 canal para a musica de fundo e outro para os efeitos sonoros
        pass

    def tocarEfeitoSonoro(self, efeito, game):
        # lembrar de checar se o jogo esta com audio ou nao
        # usar 1 canal para a musica de fundo e outro para os efeitos sonoros
        pass

    # deixar o som mudo
    def deixarSomMudo(self, game):
        pass

    # deixar o som tocando
    def deixarSomTocar(self, game):
        pass

